"""
Helper functions for the application
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Any
from datetime import datetime


def calculate_risk_score(data: Dict[str, Any]) -> float:
    """
    Calculate risk score based on input data
    
    Args:
        data: Dictionary containing risk factors
        
    Returns:
        Risk score between 0 and 1
    """
    # Simplified risk calculation
    factors = []
    
    if "compliance_score" in data:
        factors.append(1 - data["compliance_score"])
    if "incident_count" in data:
        factors.append(min(data["incident_count"] / 10, 1.0))
    if "audit_failures" in data:
        factors.append(min(data["audit_failures"] / 5, 1.0))
        
    return np.mean(factors) if factors else 0.0


def get_risk_level(score: float) -> str:
    """
    Get risk level based on score
    
    Args:
        score: Risk score between 0 and 1
        
    Returns:
        Risk level string
    """
    if score >= 0.95:
        return "Critical"
    elif score >= 0.8:
        return "High"
    elif score >= 0.6:
        return "Medium"
    elif score >= 0.3:
        return "Low"
    else:
        return "Minimal"


def format_timestamp(timestamp: datetime = None) -> str:
    """
    Format timestamp for display
    
    Args:
        timestamp: Datetime object (defaults to now)
        
    Returns:
        Formatted timestamp string
    """
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def generate_sample_data(n_samples: int = 100) -> pd.DataFrame:
    """
    Generate sample risk assessment data for demo
    
    Args:
        n_samples: Number of samples to generate
        
    Returns:
        DataFrame with sample data
    """
    np.random.seed(42)
    
    data = {
        "entity_id": [f"ENT-{i:05d}" for i in range(n_samples)],
        "compliance_score": np.random.uniform(0.5, 1.0, n_samples),
        "incident_count": np.random.poisson(2, n_samples),
        "audit_failures": np.random.poisson(1, n_samples),
        "last_audit_date": pd.date_range(end=datetime.now(), periods=n_samples, freq="D"),
    }
    
    df = pd.DataFrame(data)
    df["risk_score"] = df.apply(
        lambda row: calculate_risk_score(row.to_dict()), axis=1
    )
    df["risk_level"] = df["risk_score"].apply(get_risk_level)
    
    return df
