"""
Compliance Engine - Monitors and validates compliance requirements
"""
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List
import config

class ComplianceEngine:
    """Engine for monitoring compliance with various standards"""
    
    def __init__(self):
        self.standards = config.COMPLIANCE_STANDARDS
        self.check_categories = [
            "Data Privacy",
            "Access Controls",
            "Audit Logging",
            "Encryption",
            "Data Retention",
            "User Consent",
            "Data Minimization",
            "Security Measures"
        ]
    
    def get_compliance_score(self, standard: str = None) -> float:
        """Get overall compliance score"""
        if standard:
            return round(random.uniform(75, 98), 1)
        # Overall compliance
        return round(random.uniform(82, 96), 1)
    
    def get_compliance_status(self) -> Dict:
        """Get compliance status for all standards"""
        status = {}
        for standard in self.standards:
            score = self.get_compliance_score(standard)
            status[standard] = {
                'score': score,
                'status': 'compliant' if score >= 80 else 'at_risk',
                'last_audit': datetime.now() - timedelta(days=random.randint(1, 30)),
                'violations': random.randint(0, 5) if score < 90 else 0
            }
        return status
    
    def detect_violations(self) -> List[Dict]:
        """Detect compliance violations"""
        violations = []
        severity_levels = ['critical', 'high', 'medium', 'low']
        
        num_violations = random.randint(2, 8)
        for i in range(num_violations):
            severity = random.choice(severity_levels)
            violations.append({
                'id': f"VIO-{random.randint(10000, 99999)}",
                'standard': random.choice(self.standards),
                'category': random.choice(self.check_categories),
                'severity': severity,
                'description': f"Compliance check failed: {random.choice(['missing documentation', 'insufficient controls', 'policy violation', 'unauthorized access'])}",
                'detected': datetime.now() - timedelta(hours=random.randint(1, 72)),
                'status': random.choice(['open', 'investigating', 'resolved']),
                'affected_systems': random.randint(1, 10)
            })
        
        # Sort by severity
        severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        violations.sort(key=lambda x: severity_order[x['severity']])
        
        return violations
    
    def get_compliance_trends(self, days: int = 30) -> pd.DataFrame:
        """Get compliance score trends"""
        dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
        
        # Simulate improving compliance trend
        base_score = 85
        improvement = np.linspace(0, 10, days)
        noise = np.random.normal(0, 2, days)
        scores = base_score + improvement + noise
        scores = np.clip(scores, 70, 100)
        
        data = {
            'date': dates,
            'overall_score': scores,
            'gdpr_score': np.random.uniform(80, 98, days),
            'soc2_score': np.random.uniform(85, 98, days),
            'iso27001_score': np.random.uniform(82, 96, days),
            'violations': np.random.poisson(2, days)
        }
        
        return pd.DataFrame(data)
    
    def get_audit_summary(self) -> Dict:
        """Get audit summary metrics"""
        return {
            'total_checks': random.randint(500, 1000),
            'passed': random.randint(450, 950),
            'failed': random.randint(10, 50),
            'in_progress': random.randint(5, 20),
            'compliance_rate': round(random.uniform(90, 98), 1),
            'last_audit': datetime.now() - timedelta(days=random.randint(1, 14)),
            'next_audit': datetime.now() + timedelta(days=random.randint(15, 45))
        }
    
    def get_policy_coverage(self) -> Dict[str, float]:
        """Get policy coverage by category"""
        coverage = {}
        for category in self.check_categories:
            coverage[category] = round(random.uniform(75, 100), 1)
        return coverage
    
    def get_remediation_timeline(self) -> List[Dict]:
        """Get timeline for remediation of violations"""
        timeline = []
        for i in range(5):
            timeline.append({
                'violation_id': f"VIO-{random.randint(10000, 99999)}",
                'issue': random.choice(['Data retention', 'Access control', 'Encryption', 'Logging', 'Consent']),
                'reported': datetime.now() - timedelta(days=random.randint(5, 30)),
                'deadline': datetime.now() + timedelta(days=random.randint(5, 45)),
                'status': random.choice(['not_started', 'in_progress', 'review', 'completed']),
                'progress': random.randint(0, 100)
            })
        return timeline
    
    def generate_compliance_report(self) -> Dict:
        """Generate comprehensive compliance report"""
        return {
            'report_id': f"RPT-{random.randint(100000, 999999)}",
            'generated': datetime.now(),
            'period': '30 days',
            'overall_score': self.get_compliance_score(),
            'standards': self.get_compliance_status(),
            'violations': len(self.detect_violations()),
            'remediation_rate': round(random.uniform(80, 95), 1),
            'audit_findings': random.randint(10, 30),
            'recommendations': random.randint(5, 15)
        }
