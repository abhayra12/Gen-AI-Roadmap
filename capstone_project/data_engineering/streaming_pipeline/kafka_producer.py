"""
Kafka Producer for Manufacturing IoT Sensor Data
Simulates real-time sensor data from manufacturing equipment
"""

import json
import time
import random
from datetime import datetime, timezone
from typing import Dict, Any
import logging
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ManufacturingDataProducer:
    """Produces simulated manufacturing sensor data to Kafka"""
    
    def __init__(self, bootstrap_servers: str = "localhost:9092"):
        """Initialize Kafka producer"""
        self.config = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': 'manufacturing-sensor-producer'
        }
        self.producer = Producer(self.config)
        self.equipment_list = self._initialize_equipment()
        
        # Create topics if they don't exist
        self._create_topics()
        
    def _create_topics(self):
        """Create Kafka topics if they don't exist"""
        admin_client = AdminClient({'bootstrap.servers': self.config['bootstrap.servers']})
        
        topics = [
            NewTopic('equipment-sensors', num_partitions=3, replication_factor=1),
            NewTopic('equipment-status', num_partitions=2, replication_factor=1),
            NewTopic('quality-metrics', num_partitions=2, replication_factor=1),
        ]
        
        # Create topics
        fs = admin_client.create_topics(topics)
        
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                logger.info(f"Topic {topic} created")
            except Exception as e:
                if 'already exists' in str(e).lower():
                    logger.info(f"Topic {topic} already exists")
                else:
                    logger.error(f"Failed to create topic {topic}: {e}")
    
    def _initialize_equipment(self) -> list:
        """Initialize list of equipment to simulate"""
        return [
            {
                'equipment_id': 'CNC-A-101',
                'equipment_type': 'CNC',
                'plant_id': 'PUNE-IN',
                'normal_temp': 65.0,
                'normal_vibration': 2.5,
                'normal_pressure': 45.0
            },
            {
                'equipment_id': 'CNC-A-102',
                'equipment_type': 'CNC',
                'plant_id': 'PUNE-IN',
                'normal_temp': 67.0,
                'normal_vibration': 2.8,
                'normal_pressure': 47.0
            },
            {
                'equipment_id': 'WELD-B-201',
                'equipment_type': 'WELDING',
                'plant_id': 'PUNE-IN',
                'normal_temp': 85.0,
                'normal_vibration': 1.5,
                'normal_pressure': 55.0
            },
            {
                'equipment_id': 'ASM-C-301',
                'equipment_type': 'ASSEMBLY',
                'plant_id': 'DELHI-IN',
                'normal_temp': 35.0,
                'normal_vibration': 0.8,
                'normal_pressure': 30.0
            },
            {
                'equipment_id': 'COAT-D-401',
                'equipment_type': 'COATING',
                'plant_id': 'DELHI-IN',
                'normal_temp': 45.0,
                'normal_vibration': 1.2,
                'normal_pressure': 40.0
            }
        ]
    
    def generate_sensor_data(self, equipment: Dict[str, Any]) -> Dict[str, Any]:
        """Generate realistic sensor data with occasional anomalies"""
        
        # 95% of time: normal operation with small variations
        # 5% of time: inject anomalies
        is_anomaly = random.random() < 0.05
        
        if is_anomaly:
            # Simulate various anomaly patterns
            anomaly_type = random.choice(['high_temp', 'high_vibration', 'pressure_drop'])
            
            if anomaly_type == 'high_temp':
                temp_multiplier = random.uniform(1.15, 1.30)  # 15-30% higher
                vibration_multiplier = random.uniform(1.05, 1.15)
                pressure_multiplier = random.uniform(0.95, 1.05)
            elif anomaly_type == 'high_vibration':
                temp_multiplier = random.uniform(1.05, 1.15)
                vibration_multiplier = random.uniform(1.30, 1.50)  # 30-50% higher
                pressure_multiplier = random.uniform(0.95, 1.05)
            else:  # pressure_drop
                temp_multiplier = random.uniform(1.05, 1.15)
                vibration_multiplier = random.uniform(1.05, 1.15)
                pressure_multiplier = random.uniform(0.70, 0.85)  # 15-30% lower
        else:
            # Normal variation: ±5%
            temp_multiplier = random.uniform(0.95, 1.05)
            vibration_multiplier = random.uniform(0.95, 1.05)
            pressure_multiplier = random.uniform(0.95, 1.05)
        
        sensor_data = {
            'equipment_id': equipment['equipment_id'],
            'equipment_type': equipment['equipment_type'],
            'plant_id': equipment['plant_id'],
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'temperature': round(equipment['normal_temp'] * temp_multiplier, 2),
            'vibration': round(equipment['normal_vibration'] * vibration_multiplier, 2),
            'pressure': round(equipment['normal_pressure'] * pressure_multiplier, 2),
            'humidity': round(random.uniform(40, 60), 1),
            'power_consumption': round(random.uniform(10, 50), 2),
            'is_anomaly': is_anomaly
        }
        
        return sensor_data
    
    def generate_status_event(self, equipment: Dict[str, Any]) -> Dict[str, Any]:
        """Generate equipment status event"""
        
        # Status distribution: 85% running, 10% idle, 5% error
        status_value = random.random()
        if status_value < 0.85:
            status = 'RUNNING'
            error_code = None
        elif status_value < 0.95:
            status = 'IDLE'
            error_code = None
        else:
            status = 'ERROR'
            error_code = random.choice(['E001', 'E002', 'E003', 'E004'])
        
        status_event = {
            'equipment_id': equipment['equipment_id'],
            'equipment_type': equipment['equipment_type'],
            'plant_id': equipment['plant_id'],
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'status': status,
            'error_code': error_code,
            'uptime_hours': round(random.uniform(0, 168), 2),  # Up to 1 week
            'cycles_completed': random.randint(0, 1000)
        }
        
        return status_event
    
    def generate_quality_metric(self, equipment: Dict[str, Any]) -> Dict[str, Any]:
        """Generate quality inspection metrics"""
        
        # Quality distribution: 80% good, 15% minor defect, 5% major defect
        quality_value = random.random()
        if quality_value < 0.80:
            quality_status = 'GOOD'
            defect_count = 0
        elif quality_value < 0.95:
            quality_status = 'MINOR_DEFECT'
            defect_count = random.randint(1, 3)
        else:
            quality_status = 'MAJOR_DEFECT'
            defect_count = random.randint(4, 10)
        
        quality_metric = {
            'equipment_id': equipment['equipment_id'],
            'equipment_type': equipment['equipment_type'],
            'plant_id': equipment['plant_id'],
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'quality_status': quality_status,
            'defect_count': defect_count,
            'inspection_passed': quality_status == 'GOOD',
            'throughput': random.randint(50, 200),
            'batch_id': f"BATCH-{random.randint(1000, 9999)}"
        }
        
        return quality_metric
    
    def delivery_report(self, err, msg):
        """Callback for message delivery reports"""
        if err is not None:
            logger.error(f'Message delivery failed: {err}')
        else:
            logger.debug(f'Message delivered to {msg.topic()} [{msg.partition()}] @ {msg.offset()}')
    
    def produce_sensor_data(self, interval_seconds: int = 5):
        """Continuously produce sensor data"""
        logger.info(f"Starting sensor data production (interval: {interval_seconds}s)")
        logger.info(f"Monitoring {len(self.equipment_list)} equipment units")
        
        try:
            while True:
                for equipment in self.equipment_list:
                    # Send sensor data
                    sensor_data = self.generate_sensor_data(equipment)
                    self.producer.produce(
                        'equipment-sensors',
                        key=equipment['equipment_id'],
                        value=json.dumps(sensor_data),
                        callback=self.delivery_report
                    )
                    
                    # Send status event (less frequent)
                    if random.random() < 0.3:  # 30% chance
                        status_event = self.generate_status_event(equipment)
                        self.producer.produce(
                            'equipment-status',
                            key=equipment['equipment_id'],
                            value=json.dumps(status_event),
                            callback=self.delivery_report
                        )
                    
                    # Send quality metric (even less frequent)
                    if random.random() < 0.1:  # 10% chance
                        quality_metric = self.generate_quality_metric(equipment)
                        self.producer.produce(
                            'quality-metrics',
                            key=equipment['equipment_id'],
                            value=json.dumps(quality_metric),
                            callback=self.delivery_report
                        )
                
                # Flush to ensure delivery
                self.producer.flush()
                
                logger.info(f"Produced data for {len(self.equipment_list)} equipment units")
                time.sleep(interval_seconds)
                
        except KeyboardInterrupt:
            logger.info("Shutting down producer...")
        finally:
            self.producer.flush()
            logger.info("Producer shut down complete")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Manufacturing Kafka Producer')
    parser.add_argument('--bootstrap-servers', default='localhost:9092',
                       help='Kafka bootstrap servers')
    parser.add_argument('--interval', type=int, default=5,
                       help='Data production interval in seconds')
    
    args = parser.parse_args()
    
    producer = ManufacturingDataProducer(bootstrap_servers=args.bootstrap_servers)
    producer.produce_sensor_data(interval_seconds=args.interval)


if __name__ == '__main__':
    main()
