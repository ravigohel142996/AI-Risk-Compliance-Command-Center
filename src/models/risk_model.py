"""
Risk assessment model
"""
import numpy as np
from typing import Dict, Any, List
from sklearn.ensemble import RandomForestClassifier
from src.utils.logger import app_logger
from src.utils.helpers import calculate_risk_score, get_risk_level


class RiskAssessmentModel:
    """
    Machine Learning model for risk assessment
    """
    
    def __init__(self):
        self.model = None
        self.is_trained = False
        self.logger = app_logger
        
    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Train the risk assessment model
        
        Args:
            X: Feature matrix
            y: Target labels
        """
        try:
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42
            )
            self.model.fit(X, y)
            self.is_trained = True
            self.logger.info("Risk assessment model trained successfully")
        except Exception as e:
            self.logger.error(f"Error training model: {str(e)}")
            raise
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict risk scores
        
        Args:
            X: Feature matrix
            
        Returns:
            Array of predictions
        """
        if not self.is_trained or self.model is None:
            raise ValueError("Model not trained. Call train() first.")
        
        try:
            predictions = self.model.predict_proba(X)[:, 1]
            self.logger.info(f"Generated {len(predictions)} predictions")
            return predictions
        except Exception as e:
            self.logger.error(f"Error making predictions: {str(e)}")
            raise
    
    def assess_entity(self, entity_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess risk for a single entity
        
        Args:
            entity_data: Dictionary with entity information
            
        Returns:
            Dictionary with risk assessment results
        """
        try:
            risk_score = calculate_risk_score(entity_data)
            risk_level = get_risk_level(risk_score)
            
            assessment = {
                "entity_id": entity_data.get("entity_id", "UNKNOWN"),
                "risk_score": round(risk_score, 3),
                "risk_level": risk_level,
                "compliance_score": entity_data.get("compliance_score", 0.0),
                "incident_count": entity_data.get("incident_count", 0),
                "audit_failures": entity_data.get("audit_failures", 0),
            }
            
            self.logger.info(f"Assessed entity {assessment['entity_id']}: {risk_level}")
            return assessment
            
        except Exception as e:
            self.logger.error(f"Error assessing entity: {str(e)}")
            raise
    
    def batch_assess(self, entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Assess multiple entities
        
        Args:
            entities: List of entity data dictionaries
            
        Returns:
            List of assessment results
        """
        results = []
        for entity in entities:
            try:
                assessment = self.assess_entity(entity)
                results.append(assessment)
            except Exception as e:
                self.logger.error(f"Error in batch assessment: {str(e)}")
                continue
        
        return results
