"""
Predictive Maintenance ML Model
Predicts equipment failure within next 7 days using sensor data
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler
import joblib
import logging
from pathlib import Path
from typing import Tuple, Dict, Any
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PredictiveMaintenanceModel:
    """Predictive Maintenance Model for Equipment Failure Prediction"""
    
    def __init__(self, model_type: str = 'random_forest'):
        """
        Initialize the model
        
        Args:
            model_type: 'random_forest' or 'gradient_boosting'
        """
        self.model_type = model_type
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = None
        self.model_metadata = {}
        
        if model_type == 'random_forest':
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=42,
                n_jobs=-1
            )
        elif model_type == 'gradient_boosting':
            self.model = GradientBoostingClassifier(
                n_estimators=100,
                learning_rate=0.1,
                max_depth=5,
                random_state=42
            )
        else:
            raise ValueError(f"Unknown model type: {model_type}")
    
    def generate_synthetic_data(self, n_samples: int = 10000) -> pd.DataFrame:
        """
        Generate synthetic training data
        
        In production, replace this with real historical data from BigQuery
        """
        logger.info(f"Generating {n_samples} synthetic training samples...")
        
        np.random.seed(42)
        
        data = {
            # Sensor readings (last 24 hours average)
            'temperature_avg': np.random.normal(65, 10, n_samples),
            'temperature_std': np.random.exponential(3, n_samples),
            'temperature_max': np.random.normal(70, 12, n_samples),
            
            'vibration_avg': np.random.normal(2.5, 1.0, n_samples),
            'vibration_std': np.random.exponential(0.5, n_samples),
            'vibration_max': np.random.normal(3.5, 1.5, n_samples),
            
            'pressure_avg': np.random.normal(45, 8, n_samples),
            'pressure_std': np.random.exponential(2, n_samples),
            'pressure_min': np.random.normal(40, 10, n_samples),
            
            # Equipment metadata
            'hours_since_maintenance': np.random.uniform(0, 720, n_samples),  # Up to 30 days
            'equipment_age_months': np.random.randint(1, 120, n_samples),
            'cycles_completed': np.random.randint(0, 10000, n_samples),
            
            # Time-based features
            'hour_of_day': np.random.randint(0, 24, n_samples),
            'day_of_week': np.random.randint(0, 7, n_samples),
            
            # Operating conditions
            'load_factor': np.random.uniform(0.3, 1.0, n_samples),
            'ambient_temperature': np.random.normal(25, 5, n_samples),
            'humidity': np.random.uniform(30, 70, n_samples),
        }
        
        df = pd.DataFrame(data)
        
        # Generate target variable (failure_within_7_days)
        # Equipment is more likely to fail if:
        # - High temperature
        # - High vibration
        # - Low pressure
        # - Long time since maintenance
        # - High equipment age
        
        failure_score = (
            (df['temperature_avg'] - 65) / 10 * 0.3 +
            (df['vibration_avg'] - 2.5) / 1.0 * 0.3 +
            (45 - df['pressure_avg']) / 8 * 0.2 +
            (df['hours_since_maintenance'] / 720) * 0.15 +
            (df['equipment_age_months'] / 120) * 0.05
        )
        
        # Add noise
        failure_score += np.random.normal(0, 0.1, n_samples)
        
        # Convert to binary labels (failure if score > threshold)
        df['failure_within_7_days'] = (failure_score > 0.6).astype(int)
        
        # Create some imbalance (realistic scenario: ~10% failure rate)
        failure_rate = df['failure_within_7_days'].mean()
        if failure_rate > 0.15:
            # Downsample failures
            failure_indices = df[df['failure_within_7_days'] == 1].sample(
                frac=0.15/failure_rate, random_state=42
            ).index
            non_failure_indices = df[df['failure_within_7_days'] == 0].index
            df = df.loc[list(failure_indices) + list(non_failure_indices)]
        
        logger.info(f"Generated data shape: {df.shape}")
        logger.info(f"Failure rate: {df['failure_within_7_days'].mean():.2%}")
        
        return df
    
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Additional feature engineering"""
        
        # Create interaction features
        df['temp_vibration_interaction'] = df['temperature_avg'] * df['vibration_avg']
        df['high_temp_low_pressure'] = (df['temperature_avg'] > 70) & (df['pressure_avg'] < 40)
        
        # Create risk indicators
        df['maintenance_overdue'] = (df['hours_since_maintenance'] > 360).astype(int)
        df['high_temperature_flag'] = (df['temperature_avg'] > 75).astype(int)
        df['high_vibration_flag'] = (df['vibration_avg'] > 4.0).astype(int)
        
        return df
    
    def train(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Train the predictive maintenance model
        
        Args:
            df: DataFrame with features and target
            
        Returns:
            Dictionary with training metrics
        """
        logger.info("Starting model training...")
        
        # Feature engineering
        df = self.engineer_features(df)
        
        # Separate features and target
        target_col = 'failure_within_7_days'
        feature_cols = [col for col in df.columns if col != target_col]
        
        X = df[feature_cols]
        y = df[target_col]
        
        self.feature_names = feature_cols
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        logger.info(f"Training set: {X_train.shape}, Test set: {X_test.shape}")
        logger.info(f"Training failure rate: {y_train.mean():.2%}")
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        logger.info(f"Training {self.model_type} model...")
        self.model.fit(X_train_scaled, y_train)
        
        # Predictions
        y_pred = self.model.predict(X_test_scaled)
        y_pred_proba = self.model.predict_proba(X_test_scaled)[:, 1]
        
        # Evaluate
        metrics = {
            'accuracy': (y_pred == y_test).mean(),
            'roc_auc': roc_auc_score(y_test, y_pred_proba),
            'classification_report': classification_report(y_test, y_pred, output_dict=True),
            'confusion_matrix': confusion_matrix(y_test, y_pred).tolist()
        }
        
        # Cross-validation
        cv_scores = cross_val_score(self.model, X_train_scaled, y_train, cv=5, scoring='roc_auc')
        metrics['cv_roc_auc_mean'] = cv_scores.mean()
        metrics['cv_roc_auc_std'] = cv_scores.std()
        
        # Feature importance
        if hasattr(self.model, 'feature_importances_'):
            feature_importance = pd.DataFrame({
                'feature': feature_cols,
                'importance': self.model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            metrics['top_features'] = feature_importance.head(10).to_dict('records')
            
            logger.info("\n🔝 Top 10 Important Features:")
            for idx, row in feature_importance.head(10).iterrows():
                logger.info(f"  {row['feature']}: {row['importance']:.4f}")
        
        # Log metrics
        logger.info(f"\n📊 Model Performance:")
        logger.info(f"  Accuracy: {metrics['accuracy']:.4f}")
        logger.info(f"  ROC-AUC: {metrics['roc_auc']:.4f}")
        logger.info(f"  CV ROC-AUC: {metrics['cv_roc_auc_mean']:.4f} ± {metrics['cv_roc_auc_std']:.4f}")
        
        report = metrics['classification_report']
        logger.info(f"\n  Precision (Failure): {report['1']['precision']:.4f}")
        logger.info(f"  Recall (Failure): {report['1']['recall']:.4f}")
        logger.info(f"  F1-Score (Failure): {report['1']['f1-score']:.4f}")
        
        # Store metadata
        self.model_metadata = {
            'model_type': self.model_type,
            'n_features': len(feature_cols),
            'feature_names': feature_cols,
            'training_samples': len(X_train),
            'test_samples': len(X_test),
            'metrics': metrics
        }
        
        return metrics
    
    def predict(self, features: pd.DataFrame) -> Dict[str, Any]:
        """
        Make predictions on new data
        
        Args:
            features: DataFrame with feature values
            
        Returns:
            Dictionary with predictions and probabilities
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train() first.")
        
        # Ensure all features are present
        missing_features = set(self.feature_names) - set(features.columns)
        if missing_features:
            raise ValueError(f"Missing features: {missing_features}")
        
        # Select and order features
        X = features[self.feature_names]
        
        # Scale
        X_scaled = self.scaler.transform(X)
        
        # Predict
        predictions = self.model.predict(X_scaled)
        probabilities = self.model.predict_proba(X_scaled)[:, 1]
        
        # Determine risk level
        risk_levels = []
        for prob in probabilities:
            if prob >= 0.7:
                risk_levels.append('Critical')
            elif prob >= 0.4:
                risk_levels.append('High')
            elif prob >= 0.2:
                risk_levels.append('Medium')
            else:
                risk_levels.append('Low')
        
        return {
            'predictions': predictions.tolist(),
            'probabilities': probabilities.tolist(),
            'risk_levels': risk_levels
        }
    
    def save_model(self, output_dir: str = './ml_models/predictive_maintenance'):
        """Save trained model and metadata"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save model
        model_file = output_path / 'model.joblib'
        joblib.dump(self.model, model_file)
        logger.info(f"Model saved to {model_file}")
        
        # Save scaler
        scaler_file = output_path / 'scaler.joblib'
        joblib.dump(self.scaler, scaler_file)
        logger.info(f"Scaler saved to {scaler_file}")
        
        # Save metadata
        metadata_file = output_path / 'metadata.json'
        with open(metadata_file, 'w') as f:
            json.dump(self.model_metadata, f, indent=2, default=str)
        logger.info(f"Metadata saved to {metadata_file}")
    
    @classmethod
    def load_model(cls, model_dir: str = './ml_models/predictive_maintenance'):
        """Load trained model"""
        model_path = Path(model_dir)
        
        # Load metadata
        with open(model_path / 'metadata.json', 'r') as f:
            metadata = json.load(f)
        
        # Create instance
        instance = cls(model_type=metadata['model_type'])
        
        # Load model and scaler
        instance.model = joblib.load(model_path / 'model.joblib')
        instance.scaler = joblib.load(model_path / 'scaler.joblib')
        instance.feature_names = metadata['feature_names']
        instance.model_metadata = metadata
        
        logger.info(f"Model loaded from {model_dir}")
        return instance


def main():
    """Main training pipeline"""
    logger.info("🚀 Starting Predictive Maintenance Model Training Pipeline")
    
    # Initialize model
    model = PredictiveMaintenanceModel(model_type='random_forest')
    
    # Generate synthetic data (in production, load from BigQuery)
    df = model.generate_synthetic_data(n_samples=10000)
    
    # Train model
    metrics = model.train(df)
    
    # Save model
    model.save_model()
    
    logger.info("\n✅ Training complete!")
    logger.info(f"Model saved and ready for deployment")
    
    # Test loading
    logger.info("\n🔄 Testing model loading...")
    loaded_model = PredictiveMaintenanceModel.load_model()
    logger.info("✅ Model loaded successfully!")
    
    # Test prediction
    logger.info("\n🧪 Testing prediction on sample data...")
    test_sample = df.iloc[:5][loaded_model.feature_names]
    predictions = loaded_model.predict(test_sample)
    
    logger.info(f"\nSample Predictions:")
    for i, (prob, risk) in enumerate(zip(predictions['probabilities'], predictions['risk_levels'])):
        logger.info(f"  Sample {i+1}: Failure Probability = {prob:.2%}, Risk = {risk}")


if __name__ == '__main__':
    main()
