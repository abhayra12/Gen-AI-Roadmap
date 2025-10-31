"""
ML Agent - Machine Learning Predictions for Manufacturing
Provides predictive maintenance, anomaly detection, and quality forecasting
"""

import logging
import numpy as np
import pandas as pd
from typing import Dict, Any, List
from pathlib import Path
import joblib
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from ml_models.predictive_maintenance.train_model import PredictiveMaintenanceModel

logger = logging.getLogger(__name__)


class MLAgent:
    """
    ML Agent for predictive analytics in manufacturing
    Uses trained ML models for failure prediction, anomaly detection, quality forecasting
    """
    
    def __init__(self, models_dir: str = "./ml_models"):
        """Initialize ML Agent with trained models"""
        self.models_dir = Path(models_dir)
        self.predictive_maintenance_model = None
        self.anomaly_detection_model = None
        self.quality_prediction_model = None
        
        # Load models
        self._load_models()
        
        logger.info("ML Agent initialized successfully")
    
    def _load_models(self):
        """Load all trained ML models"""
        try:
            # Load Predictive Maintenance Model
            pm_model_path = self.models_dir / "predictive_maintenance"
            if pm_model_path.exists():
                self.predictive_maintenance_model = PredictiveMaintenanceModel.load_model(
                    str(pm_model_path)
                )
                logger.info("✅ Predictive Maintenance model loaded")
            else:
                logger.warning(f"⚠️  Predictive Maintenance model not found at {pm_model_path}")
                logger.info("   Run: python ml_models/predictive_maintenance/train_model.py")
            
            # TODO: Load other models when implemented
            # self.anomaly_detection_model = AnomalyDetectionModel.load_model(...)
            # self.quality_prediction_model = QualityPredictionModel.load_model(...)
            
        except Exception as e:
            logger.error(f"Error loading ML models: {e}")
            raise
    
    async def predict_failure(
        self,
        equipment_id: str,
        sensor_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Predict equipment failure probability
        
        Args:
            equipment_id: Equipment identifier
            sensor_data: Recent sensor readings and equipment metadata
            
        Returns:
            Dictionary with failure prediction and recommendations
        """
        try:
            logger.info(f"Predicting failure risk for {equipment_id}")
            
            # If model not loaded, return mock prediction
            if self.predictive_maintenance_model is None:
                return self._mock_failure_prediction(equipment_id, sensor_data)
            
            # Prepare features from sensor data
            features_df = self._prepare_features_for_prediction(sensor_data)
            
            # Make prediction
            prediction = self.predictive_maintenance_model.predict(features_df)
            
            failure_prob = prediction['probabilities'][0]
            risk_level = prediction['risk_levels'][0]
            
            # Generate explanation and recommendations
            explanation = self._generate_failure_explanation(sensor_data, failure_prob)
            recommendations = self._generate_maintenance_recommendations(risk_level, sensor_data)
            
            result = {
                "equipment_id": equipment_id,
                "prediction_type": "failure_risk",
                "failure_probability": failure_prob,
                "risk_level": risk_level,
                "time_horizon": "7_days",
                "contributing_factors": explanation,
                "recommendations": recommendations,
                "confidence": 0.85,
                "model_used": "Random Forest (Predictive Maintenance)"
            }
            
            logger.info(f"Failure prediction complete: {risk_level} risk ({failure_prob:.2%})")
            return result
            
        except Exception as e:
            logger.error(f"Error in failure prediction: {e}")
            return {
                "equipment_id": equipment_id,
                "error": str(e),
                "prediction_type": "failure_risk",
                "failure_probability": 0.0,
                "risk_level": "Unknown"
            }
    
    def _prepare_features_for_prediction(self, sensor_data: Dict[str, Any]) -> pd.DataFrame:
        """Prepare features from sensor data for model input"""
        
        # Extract sensor readings (assuming recent averages are provided)
        features = {
            'temperature_avg': sensor_data.get('temperature_avg', 65.0),
            'temperature_std': sensor_data.get('temperature_std', 2.0),
            'temperature_max': sensor_data.get('temperature_max', 70.0),
            
            'vibration_avg': sensor_data.get('vibration_avg', 2.5),
            'vibration_std': sensor_data.get('vibration_std', 0.3),
            'vibration_max': sensor_data.get('vibration_max', 3.0),
            
            'pressure_avg': sensor_data.get('pressure_avg', 45.0),
            'pressure_std': sensor_data.get('pressure_std', 1.5),
            'pressure_min': sensor_data.get('pressure_min', 42.0),
            
            'hours_since_maintenance': sensor_data.get('hours_since_maintenance', 168.0),
            'equipment_age_months': sensor_data.get('equipment_age_months', 24),
            'cycles_completed': sensor_data.get('cycles_completed', 1000),
            
            'hour_of_day': sensor_data.get('hour_of_day', 12),
            'day_of_week': sensor_data.get('day_of_week', 3),
            
            'load_factor': sensor_data.get('load_factor', 0.8),
            'ambient_temperature': sensor_data.get('ambient_temperature', 25.0),
            'humidity': sensor_data.get('humidity', 50.0),
        }
        
        # Engineer features (same as training)
        features['temp_vibration_interaction'] = features['temperature_avg'] * features['vibration_avg']
        features['high_temp_low_pressure'] = int(
            features['temperature_avg'] > 70 and features['pressure_avg'] < 40
        )
        features['maintenance_overdue'] = int(features['hours_since_maintenance'] > 360)
        features['high_temperature_flag'] = int(features['temperature_avg'] > 75)
        features['high_vibration_flag'] = int(features['vibration_avg'] > 4.0)
        
        return pd.DataFrame([features])
    
    def _generate_failure_explanation(
        self,
        sensor_data: Dict[str, Any],
        failure_prob: float
    ) -> List[str]:
        """Generate human-readable explanation for failure prediction"""
        
        factors = []
        
        # Check temperature
        temp = sensor_data.get('temperature_avg', 65.0)
        if temp > 75:
            deviation = ((temp - 65) / 65) * 100
            factors.append(f"Elevated temperature ({temp:.1f}°C, {deviation:.0f}% above normal)")
        
        # Check vibration
        vibration = sensor_data.get('vibration_avg', 2.5)
        if vibration > 3.5:
            deviation = ((vibration - 2.5) / 2.5) * 100
            factors.append(f"High vibration levels ({vibration:.2f} mm/s, {deviation:.0f}% above normal)")
        
        # Check pressure
        pressure = sensor_data.get('pressure_avg', 45.0)
        if pressure < 35:
            deviation = ((45 - pressure) / 45) * 100
            factors.append(f"Low pressure readings ({pressure:.1f} PSI, {deviation:.0f}% below normal)")
        
        # Check maintenance schedule
        hours_since_maint = sensor_data.get('hours_since_maintenance', 168)
        if hours_since_maint > 360:
            days = hours_since_maint / 24
            factors.append(f"Maintenance overdue ({days:.0f} days since last maintenance)")
        
        # Check equipment age
        age_months = sensor_data.get('equipment_age_months', 24)
        if age_months > 60:
            years = age_months / 12
            factors.append(f"Equipment age ({years:.1f} years, increased wear expected)")
        
        # If no specific factors but high probability, add generic warning
        if not factors and failure_prob > 0.5:
            factors.append("Multiple sensor readings trending toward failure patterns")
        
        if not factors:
            factors.append("All parameters within normal operating range")
        
        return factors
    
    def _generate_maintenance_recommendations(
        self,
        risk_level: str,
        sensor_data: Dict[str, Any]
    ) -> List[str]:
        """Generate maintenance recommendations based on risk level"""
        
        recommendations = []
        
        if risk_level == 'Critical':
            recommendations.append("🔴 URGENT: Schedule immediate inspection within 24 hours")
            recommendations.append("Consider stopping equipment if safety is at risk")
            recommendations.append("Prepare replacement parts and backup equipment")
            
        elif risk_level == 'High':
            recommendations.append("🟠 Schedule maintenance within 3 days")
            recommendations.append("Increase monitoring frequency (hourly checks)")
            recommendations.append("Review recent operational logs for anomalies")
            
        elif risk_level == 'Medium':
            recommendations.append("🟡 Plan preventive maintenance within 7 days")
            recommendations.append("Continue standard monitoring")
            recommendations.append("Document current readings for trend analysis")
            
        else:  # Low
            recommendations.append("🟢 Equipment operating normally")
            recommendations.append("Continue routine maintenance schedule")
            recommendations.append("Monitor as per standard operating procedures")
        
        # Add specific recommendations based on sensors
        temp = sensor_data.get('temperature_avg', 65.0)
        if temp > 75:
            recommendations.append("Check cooling system: inspect coolant levels and filters")
        
        vibration = sensor_data.get('vibration_avg', 2.5)
        if vibration > 3.5:
            recommendations.append("Inspect bearings and mounting bolts for wear/looseness")
        
        pressure = sensor_data.get('pressure_avg', 45.0)
        if pressure < 35:
            recommendations.append("Check hydraulic/pneumatic lines for leaks or blockages")
        
        return recommendations
    
    def _mock_failure_prediction(
        self,
        equipment_id: str,
        sensor_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate mock prediction when model is not loaded"""
        
        logger.warning("Using mock prediction (model not loaded)")
        
        # Calculate simple risk score based on sensor data
        temp = sensor_data.get('temperature_avg', 65.0)
        vibration = sensor_data.get('vibration_avg', 2.5)
        pressure = sensor_data.get('pressure_avg', 45.0)
        
        risk_score = (
            ((temp - 65) / 20) * 0.4 +
            ((vibration - 2.5) / 2.0) * 0.4 +
            ((45 - pressure) / 15) * 0.2
        )
        risk_score = max(0, min(1, risk_score))  # Clip to [0, 1]
        
        if risk_score > 0.7:
            risk_level = 'Critical'
        elif risk_score > 0.4:
            risk_level = 'High'
        elif risk_score > 0.2:
            risk_level = 'Medium'
        else:
            risk_level = 'Low'
        
        return {
            "equipment_id": equipment_id,
            "prediction_type": "failure_risk",
            "failure_probability": risk_score,
            "risk_level": risk_level,
            "time_horizon": "7_days",
            "contributing_factors": self._generate_failure_explanation(sensor_data, risk_score),
            "recommendations": self._generate_maintenance_recommendations(risk_level, sensor_data),
            "confidence": 0.60,
            "model_used": "Mock Model (Rule-based)",
            "note": "Using simplified rule-based prediction. Train ML model for better accuracy."
        }
    
    async def detect_anomaly(
        self,
        equipment_id: str,
        sensor_reading: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Detect anomalies in real-time sensor data
        
        Args:
            equipment_id: Equipment identifier
            sensor_reading: Current sensor reading
            
        Returns:
            Dictionary with anomaly detection results
        """
        # Placeholder for anomaly detection
        # TODO: Implement with Isolation Forest or Autoencoder
        
        logger.info(f"Detecting anomalies for {equipment_id}")
        
        # Simple threshold-based anomaly detection for now
        anomalies = []
        
        temp = sensor_reading.get('temperature', 65.0)
        if temp > 80 or temp < 40:
            anomalies.append({
                'sensor': 'temperature',
                'value': temp,
                'threshold': '40-80°C',
                'severity': 'High' if temp > 85 else 'Medium'
            })
        
        vibration = sensor_reading.get('vibration', 2.5)
        if vibration > 4.5:
            anomalies.append({
                'sensor': 'vibration',
                'value': vibration,
                'threshold': '<4.5 mm/s',
                'severity': 'High'
            })
        
        pressure = sensor_reading.get('pressure', 45.0)
        if pressure < 25 or pressure > 65:
            anomalies.append({
                'sensor': 'pressure',
                'value': pressure,
                'threshold': '25-65 PSI',
                'severity': 'Medium'
            })
        
        return {
            "equipment_id": equipment_id,
            "anomaly_detected": len(anomalies) > 0,
            "anomaly_score": len(anomalies) / 3.0,  # Normalized
            "anomalies": anomalies,
            "timestamp": sensor_reading.get('timestamp'),
            "model_used": "Threshold-based (Placeholder)"
        }


# ============================================================================
# Node function for LangGraph integration
# ============================================================================

ml_agent = MLAgent()


def ml_agent_node(state: dict) -> dict:
    """LangGraph node for ML Agent"""
    import asyncio
    
    logger.info("Executing ML Agent node")
    
    try:
        # Extract sensor data from state
        sensor_data = {
            'temperature_avg': state.get('temperature_avg', 67.0),
            'vibration_avg': state.get('vibration_avg', 2.8),
            'pressure_avg': state.get('pressure_avg', 45.0),
            'hours_since_maintenance': state.get('hours_since_maintenance', 240),
            'equipment_age_months': state.get('equipment_age_months', 36)
        }
        
        # Run async function in sync context
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                ml_result = pool.submit(
                    asyncio.run,
                    ml_agent.predict_failure(state['equipment_id'], sensor_data)
                ).result()
        else:
            ml_result = loop.run_until_complete(
                ml_agent.predict_failure(state['equipment_id'], sensor_data)
            )
        
        state['ml_prediction'] = ml_result
        
    except Exception as e:
        logger.error(f"ML Agent node error: {e}")
        state.setdefault('errors', []).append(f"ML Agent: {str(e)}")
        state['ml_prediction'] = {"error": str(e)}
    
    return state


if __name__ == '__main__':
    # Test ML Agent
    import asyncio
    
    logging.basicConfig(level=logging.INFO)
    
    agent = MLAgent()
    
    # Test prediction
    test_sensor_data = {
        'temperature_avg': 78.5,
        'vibration_avg': 3.8,
        'pressure_avg': 38.0,
        'hours_since_maintenance': 400,
        'equipment_age_months': 48
    }
    
    result = asyncio.run(agent.predict_failure('CNC-A-102', test_sensor_data))
    
    print(f"\n🤖 ML Agent Test Result:")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Failure Probability: {result['failure_probability']:.2%}")
    print(f"\nContributing Factors:")
    for factor in result['contributing_factors']:
        print(f"  • {factor}")
    print(f"\nRecommendations:")
    for rec in result['recommendations']:
        print(f"  {rec}")
