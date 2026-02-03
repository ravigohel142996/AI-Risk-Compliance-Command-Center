"""
Risk Engine - Analyzes and scores AI system risks
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import random

class RiskEngine:
    """Engine for calculating and monitoring AI system risks"""
    
    def __init__(self):
        self.risk_factors = [
            "Model Bias",
            "Data Quality",
            "Model Drift",
            "Security Vulnerabilities",
            "Performance Degradation",
            "Privacy Risks",
            "Compliance Gaps",
            "Integration Issues"
        ]
        
    def calculate_risk_score(self, metrics: Dict) -> float:
        """Calculate overall risk score based on various metrics"""
        weights = {
            "model_accuracy": 0.2,
            "data_quality": 0.15,
            "security_score": 0.25,
            "compliance_score": 0.2,
            "performance_score": 0.1,
            "drift_score": 0.1
        }
        
        risk_score = 0
        for metric, weight in weights.items():
            value = metrics.get(metric, 50)
            # Convert to risk (100 - quality_score)
            risk_score += (100 - value) * weight
            
        return min(100, max(0, risk_score))
    
    def get_risk_level(self, score: float) -> str:
        """Determine risk level from score"""
        if score >= 80:
            return "critical"
        elif score >= 60:
            return "high"
        elif score >= 40:
            return "medium"
        elif score >= 20:
            return "low"
        else:
            return "minimal"
    
    def generate_risk_trends(self, days: int = 30) -> pd.DataFrame:
        """Generate simulated risk trend data"""
        dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
        
        # Simulate risk scores with some trends
        base_score = 45
        trend = np.linspace(0, 15, days)  # Gradual increase
        noise = np.random.normal(0, 5, days)
        risk_scores = base_score + trend + noise
        risk_scores = np.clip(risk_scores, 0, 100)
        
        data = {
            'date': dates,
            'risk_score': risk_scores,
            'model_risk': np.random.uniform(30, 70, days),
            'data_risk': np.random.uniform(20, 60, days),
            'security_risk': np.random.uniform(25, 65, days),
            'compliance_risk': np.random.uniform(15, 55, days)
        }
        
        return pd.DataFrame(data)
    
    def get_risk_breakdown(self) -> Dict[str, float]:
        """Get breakdown of risk by category"""
        breakdown = {}
        for factor in self.risk_factors:
            # Simulate risk scores
            breakdown[factor] = round(random.uniform(20, 80), 2)
        return breakdown
    
    def get_risk_heatmap_data(self, models: List[str], timeframes: List[str]) -> pd.DataFrame:
        """Generate risk heatmap data for multiple models"""
        data = []
        for model in models:
            for timeframe in timeframes:
                risk_score = random.uniform(20, 85)
                data.append({
                    'model': model,
                    'timeframe': timeframe,
                    'risk_score': round(risk_score, 1)
                })
        return pd.DataFrame(data)
    
    def detect_risk_anomalies(self, df: pd.DataFrame) -> List[Dict]:
        """Detect anomalies in risk data"""
        anomalies = []
        
        # Simple anomaly detection: scores > mean + 2*std
        mean_risk = df['risk_score'].mean()
        std_risk = df['risk_score'].std()
        threshold = mean_risk + 2 * std_risk
        
        for idx, row in df.iterrows():
            if row['risk_score'] > threshold:
                anomalies.append({
                    'date': row['date'],
                    'risk_score': row['risk_score'],
                    'severity': self.get_risk_level(row['risk_score']),
                    'message': f"Risk spike detected: {row['risk_score']:.1f}"
                })
        
        return anomalies
    
    def get_risk_metrics(self) -> Dict:
        """Get current risk metrics and KPIs"""
        return {
            'overall_risk': round(random.uniform(40, 70), 1),
            'active_risks': random.randint(5, 15),
            'critical_risks': random.randint(0, 3),
            'risk_trend': random.choice(['increasing', 'decreasing', 'stable']),
            'models_monitored': random.randint(15, 30),
            'last_updated': datetime.now()
        }
    
    def get_top_risks(self, limit: int = 5) -> List[Dict]:
        """Get top risks requiring attention"""
        risks = []
        categories = ['Model Performance', 'Data Quality', 'Security', 'Compliance', 'Integration']
        
        for i in range(limit):
            risk_score = random.uniform(60, 95)
            risks.append({
                'id': f"RISK-{random.randint(1000, 9999)}",
                'category': random.choice(categories),
                'description': f"Risk issue in {random.choice(['production', 'staging', 'dev'])} environment",
                'score': round(risk_score, 1),
                'level': self.get_risk_level(risk_score),
                'detected': datetime.now() - timedelta(hours=random.randint(1, 48)),
                'affected_models': random.randint(1, 5)
            })
        
        # Sort by score descending
        risks.sort(key=lambda x: x['score'], reverse=True)
        return risks
