"""
Alert Engine - Classifies and manages security alerts
"""
import random
from datetime import datetime, timedelta
from typing import Dict, List
import config

class AlertEngine:
    """Engine for security alert classification and management"""
    
    def __init__(self):
        self.alert_types = [
            "Unauthorized Access",
            "Data Breach",
            "Anomalous Behavior",
            "Policy Violation",
            "System Intrusion",
            "DDoS Attack",
            "Malware Detection",
            "Suspicious API Calls",
            "Model Tampering",
            "Data Exfiltration"
        ]
        
        self.alert_sources = [
            "WAF",
            "IDS/IPS",
            "SIEM",
            "ML Model Monitor",
            "API Gateway",
            "Database Monitor",
            "Cloud Security",
            "Endpoint Protection"
        ]
    
    def classify_alert_severity(self, alert_data: Dict) -> str:
        """Classify alert severity using ML-like logic"""
        # Simple scoring based on various factors
        score = 0
        
        # Factor in threat level
        threat_keywords = ['breach', 'intrusion', 'unauthorized', 'critical']
        if any(kw in alert_data.get('description', '').lower() for kw in threat_keywords):
            score += 30
        
        # Factor in impact
        if alert_data.get('affected_systems', 0) > 10:
            score += 20
        if alert_data.get('affected_users', 0) > 100:
            score += 20
        
        # Factor in data sensitivity
        if alert_data.get('data_sensitivity') == 'high':
            score += 30
        
        # Classify based on score
        if score >= 70:
            return 'critical'
        elif score >= 50:
            return 'high'
        elif score >= 30:
            return 'medium'
        else:
            return 'low'
    
    def get_active_alerts(self) -> List[Dict]:
        """Get currently active security alerts"""
        alerts = []
        num_alerts = random.randint(5, 15)
        
        for i in range(num_alerts):
            severity = random.choice(['critical', 'high', 'medium', 'low'])
            alert = {
                'id': f"ALT-{random.randint(100000, 999999)}",
                'type': random.choice(self.alert_types),
                'severity': severity,
                'source': random.choice(self.alert_sources),
                'timestamp': datetime.now() - timedelta(minutes=random.randint(1, 1440)),
                'status': random.choice(['new', 'investigating', 'contained', 'resolved']),
                'affected_systems': random.randint(1, 20),
                'description': f"Security event detected in {random.choice(['production', 'staging'])} environment",
                'assigned_to': random.choice(['Security Team', 'DevOps', 'ML Team', 'Unassigned'])
            }
            alerts.append(alert)
        
        # Sort by severity and timestamp
        severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        alerts.sort(key=lambda x: (severity_order[x['severity']], x['timestamp']), reverse=True)
        
        return alerts
    
    def get_alert_statistics(self) -> Dict:
        """Get alert statistics and metrics"""
        return {
            'total_alerts': random.randint(100, 500),
            'critical': random.randint(5, 20),
            'high': random.randint(15, 50),
            'medium': random.randint(30, 100),
            'low': random.randint(50, 330),
            'resolved_24h': random.randint(40, 150),
            'avg_resolution_time': f"{random.randint(15, 120)} minutes",
            'false_positives': random.randint(10, 40),
            'true_positives': random.randint(60, 200)
        }
    
    def get_alert_trends(self, days: int = 7) -> Dict:
        """Get alert trends over time"""
        dates = []
        critical = []
        high = []
        medium = []
        low = []
        
        for i in range(days):
            date = datetime.now() - timedelta(days=days-i-1)
            dates.append(date.strftime('%Y-%m-%d'))
            critical.append(random.randint(0, 10))
            high.append(random.randint(5, 25))
            medium.append(random.randint(10, 40))
            low.append(random.randint(20, 60))
        
        return {
            'dates': dates,
            'critical': critical,
            'high': high,
            'medium': medium,
            'low': low
        }
    
    def get_alert_by_source(self) -> Dict[str, int]:
        """Get alert count by source"""
        source_counts = {}
        for source in self.alert_sources:
            source_counts[source] = random.randint(5, 50)
        return source_counts
    
    def get_mttr_by_severity(self) -> Dict[str, int]:
        """Get Mean Time To Resolution by severity"""
        return {
            'critical': random.randint(15, 45),  # minutes
            'high': random.randint(45, 120),
            'medium': random.randint(120, 360),
            'low': random.randint(360, 1440)
        }
    
    def get_recent_incidents(self, limit: int = 10) -> List[Dict]:
        """Get recent security incidents"""
        incidents = []
        for i in range(limit):
            severity = random.choice(['critical', 'high', 'medium'])
            incidents.append({
                'id': f"INC-{random.randint(1000, 9999)}",
                'title': f"{random.choice(self.alert_types)} Incident",
                'severity': severity,
                'timestamp': datetime.now() - timedelta(hours=random.randint(1, 168)),
                'duration': f"{random.randint(10, 180)} minutes",
                'impact': random.choice(['High', 'Medium', 'Low']),
                'status': random.choice(['Resolved', 'Investigating', 'Contained']),
                'root_cause': random.choice(['Configuration Error', 'Software Bug', 'External Attack', 'Human Error'])
            })
        return incidents
    
    def detect_cost_anomaly(self, current_cost: float, baseline_cost: float) -> Dict:
        """Detect cost anomalies"""
        percent_change = ((current_cost - baseline_cost) / baseline_cost) * 100
        
        is_anomaly = abs(percent_change) > config.COST_THRESHOLD_PERCENT
        
        return {
            'is_anomaly': is_anomaly,
            'current_cost': current_cost,
            'baseline_cost': baseline_cost,
            'percent_change': round(percent_change, 2),
            'severity': 'high' if abs(percent_change) > 50 else 'medium' if abs(percent_change) > 30 else 'low',
            'timestamp': datetime.now()
        }
    
    def get_cost_metrics(self) -> Dict:
        """Get cost tracking metrics"""
        current = random.uniform(5000, 15000)
        baseline = random.uniform(4000, 12000)
        
        return {
            'current_cost': round(current, 2),
            'baseline_cost': round(baseline, 2),
            'monthly_projection': round(current * 30, 2),
            'cost_trend': 'increasing' if current > baseline else 'decreasing',
            'top_cost_driver': random.choice(['Model Training', 'Inference API', 'Data Storage', 'Compute Resources']),
            'cost_by_service': {
                'Model Training': round(random.uniform(1000, 5000), 2),
                'Inference': round(random.uniform(2000, 6000), 2),
                'Storage': round(random.uniform(500, 2000), 2),
                'Networking': round(random.uniform(300, 1500), 2),
                'Monitoring': round(random.uniform(200, 1000), 2)
            }
        }
