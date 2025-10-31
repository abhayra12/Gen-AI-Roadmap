"""
Kafka Consumer for Manufacturing IoT Sensor Data
Consumes data from Kafka topics and stores to storage (GCS/Local files)
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from confluent_kafka import Consumer, KafkaError
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ManufacturingDataConsumer:
    """Consumes manufacturing sensor data from Kafka and stores it"""
    
    def __init__(
        self,
        bootstrap_servers: str = "localhost:9092",
        group_id: str = "manufacturing-consumer-group",
        output_dir: str = "./data_lake/raw"
    ):
        """Initialize Kafka consumer"""
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest',  # Start from beginning if no offset
            'enable.auto.commit': True,
        }
        self.consumer = Consumer(self.config)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Subscribe to topics
        self.topics = ['equipment-sensors', 'equipment-status', 'quality-metrics']
        self.consumer.subscribe(self.topics)
        
        logger.info(f"Consumer initialized. Subscribed to: {self.topics}")
        logger.info(f"Output directory: {self.output_dir}")
        
        # Buffers for batch writing
        self.buffers = {
            'equipment-sensors': [],
            'equipment-status': [],
            'quality-metrics': []
        }
        self.batch_size = 100  # Write to file every 100 messages
        
    def process_message(self, msg) -> Optional[Dict[str, Any]]:
        """Process a Kafka message"""
        try:
            # Decode message
            data = json.loads(msg.value().decode('utf-8'))
            
            # Add metadata
            data['kafka_topic'] = msg.topic()
            data['kafka_partition'] = msg.partition()
            data['kafka_offset'] = msg.offset()
            data['consumed_at'] = datetime.utcnow().isoformat()
            
            return data
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return None
    
    def write_to_storage(self, topic: str, data_list: list):
        """Write data to local storage (simulating data lake)"""
        if not data_list:
            return
        
        try:
            # Create DataFrame
            df = pd.DataFrame(data_list)
            
            # Generate filename with timestamp
            timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            filename = f"{topic}_{timestamp}.parquet"
            filepath = self.output_dir / topic / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # Write to Parquet (efficient columnar format)
            df.to_parquet(filepath, engine='pyarrow', compression='snappy')
            
            logger.info(f"Wrote {len(data_list)} records to {filepath}")
            
        except Exception as e:
            logger.error(f"Error writing to storage: {e}")
    
    def consume(self, max_messages: Optional[int] = None):
        """
        Consume messages from Kafka
        
        Args:
            max_messages: Maximum number of messages to consume (None = infinite)
        """
        logger.info("Starting consumption...")
        
        message_count = 0
        
        try:
            while True:
                # Poll for messages (timeout 1 second)
                msg = self.consumer.poll(timeout=1.0)
                
                if msg is None:
                    continue
                
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition
                        logger.debug(f'Reached end of partition {msg.partition()}')
                    else:
                        logger.error(f'Consumer error: {msg.error()}')
                    continue
                
                # Process message
                data = self.process_message(msg)
                if data:
                    topic = msg.topic()
                    self.buffers[topic].append(data)
                    message_count += 1
                    
                    # Log progress
                    if message_count % 10 == 0:
                        logger.info(f"Consumed {message_count} messages")
                    
                    # Write batch if buffer is full
                    if len(self.buffers[topic]) >= self.batch_size:
                        self.write_to_storage(topic, self.buffers[topic])
                        self.buffers[topic] = []  # Clear buffer
                
                # Check if max messages reached
                if max_messages and message_count >= max_messages:
                    logger.info(f"Reached max messages: {max_messages}")
                    break
                    
        except KeyboardInterrupt:
            logger.info("Shutting down consumer...")
        finally:
            # Write remaining buffered data
            for topic, data_list in self.buffers.items():
                if data_list:
                    self.write_to_storage(topic, data_list)
            
            self.consumer.close()
            logger.info("Consumer shut down complete")


class RealTimeAnalyzer:
    """Performs real-time analysis on streaming data"""
    
    def __init__(self, alert_threshold: Dict[str, float]):
        """
        Initialize real-time analyzer
        
        Args:
            alert_threshold: Dictionary of thresholds for alerts
                Example: {'temperature': 80.0, 'vibration': 5.0, 'pressure': 30.0}
        """
        self.alert_threshold = alert_threshold
        self.stats = {
            'total_messages': 0,
            'anomalies_detected': 0,
            'alerts_triggered': 0
        }
    
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze sensor data and generate alerts"""
        self.stats['total_messages'] += 1
        
        alerts = []
        
        # Check if marked as anomaly by producer
        if data.get('is_anomaly'):
            self.stats['anomalies_detected'] += 1
        
        # Check thresholds
        if 'temperature' in data and data['temperature'] > self.alert_threshold.get('temperature', 100):
            alerts.append({
                'type': 'HIGH_TEMPERATURE',
                'equipment_id': data['equipment_id'],
                'value': data['temperature'],
                'threshold': self.alert_threshold['temperature'],
                'timestamp': data['timestamp']
            })
        
        if 'vibration' in data and data['vibration'] > self.alert_threshold.get('vibration', 10):
            alerts.append({
                'type': 'HIGH_VIBRATION',
                'equipment_id': data['equipment_id'],
                'value': data['vibration'],
                'threshold': self.alert_threshold['vibration'],
                'timestamp': data['timestamp']
            })
        
        if 'pressure' in data and data['pressure'] < self.alert_threshold.get('pressure', 20):
            alerts.append({
                'type': 'LOW_PRESSURE',
                'equipment_id': data['equipment_id'],
                'value': data['pressure'],
                'threshold': self.alert_threshold['pressure'],
                'timestamp': data['timestamp']
            })
        
        if alerts:
            self.stats['alerts_triggered'] += len(alerts)
            for alert in alerts:
                logger.warning(f"⚠️  ALERT: {alert['type']} on {alert['equipment_id']} - "
                             f"Value: {alert['value']}, Threshold: {alert['threshold']}")
        
        return {
            'has_alerts': len(alerts) > 0,
            'alerts': alerts,
            'stats': self.stats.copy()
        }


class ManufacturingConsumerWithAnalytics(ManufacturingDataConsumer):
    """Consumer with real-time analytics capabilities"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Initialize real-time analyzer
        self.analyzer = RealTimeAnalyzer(alert_threshold={
            'temperature': 80.0,
            'vibration': 4.0,
            'pressure': 25.0
        })
    
    def process_message(self, msg) -> Optional[Dict[str, Any]]:
        """Process message with real-time analytics"""
        data = super().process_message(msg)
        
        if data and msg.topic() == 'equipment-sensors':
            # Perform real-time analysis
            analysis_result = self.analyzer.analyze(data)
            data['analysis_result'] = analysis_result
            
            # Log stats periodically
            if self.analyzer.stats['total_messages'] % 50 == 0:
                logger.info(f"📊 Stats: {self.analyzer.stats}")
        
        return data


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Manufacturing Kafka Consumer')
    parser.add_argument('--bootstrap-servers', default='localhost:9092',
                       help='Kafka bootstrap servers')
    parser.add_argument('--group-id', default='manufacturing-consumer-group',
                       help='Consumer group ID')
    parser.add_argument('--output-dir', default='./data_lake/raw',
                       help='Output directory for consumed data')
    parser.add_argument('--max-messages', type=int, default=None,
                       help='Maximum messages to consume (default: infinite)')
    parser.add_argument('--with-analytics', action='store_true',
                       help='Enable real-time analytics')
    
    args = parser.parse_args()
    
    if args.with_analytics:
        consumer = ManufacturingConsumerWithAnalytics(
            bootstrap_servers=args.bootstrap_servers,
            group_id=args.group_id,
            output_dir=args.output_dir
        )
    else:
        consumer = ManufacturingDataConsumer(
            bootstrap_servers=args.bootstrap_servers,
            group_id=args.group_id,
            output_dir=args.output_dir
        )
    
    consumer.consume(max_messages=args.max_messages)


if __name__ == '__main__':
    main()
