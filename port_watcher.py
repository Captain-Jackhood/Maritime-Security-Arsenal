#!/usr/bin/env python3
"""
🏴‍☠️ Captain Jackhood's Port Watcher
===================================

Advanced port monitoring system designed by Captain Jackhood
to keep a keen eye on all maritime traffic, especially on
the legendary SERVER_IP:9999 port.

"A good captain always knows what's happening at every port!" - Captain Jackhood
"""

import re
import sys
import time
from datetime import datetime
from utils.filters import analyze_port_activity, determine_activity_type

class JackhoodPortWatcher:
    def __init__(self, target_port="SERVER_IP:9999"):
        self.captain = "Captain Jackhood"
        self.target_port = target_port
        self.ship = "HMS Digital Revenge"
        self.alerts_triggered = 0
        self.activities_monitored = 0
        
    def monitor_log_file(self, log_file):
        """Monitor specific log file for port activities"""
        print(f"🏴‍☠️ {self.captain}'s Port Watcher")
        print(f"⚓ Monitoring port: {self.target_port}")
        print(f"📄 Log file: {log_file}")
        print(f"🚢 Ship: {self.ship}")
        print("=" * 60)
        
        try:
            with open(log_file, 'r') as f:
                lines = f.readlines()
            
            port_activities = analyze_port_activity(lines, self.target_port)
            self.process_port_activities(port_activities)
            
        except FileNotFoundError:
            print(f"❌ Log file not found: {log_file}")
        except Exception as e:
            print(f"💥 Error monitoring port: {e}")
    
    def process_port_activities(self, activities):
        """Process and analyze port activities"""
        if not activities:
            print(f"📊 No activity detected on port {self.target_port}")
            print("🌊 Seas are calm around this port, Captain!")
            return
        
        print(f"📡 PORT {self.target_port} ACTIVITY DETECTED:")
        print("-" * 60)
        
        for activity in activities:
            self.activities_monitored += 1
            threat_level = self.assess_threat_level(activity)
            
            if threat_level == "HIGH":
                print(f"🚨 HIGH THREAT: {activity}")
                self.alerts_triggered += 1
            elif threat_level == "MEDIUM":
                print(f"⚠️  MEDIUM THREAT: {activity}")
            else:
                print(f"ℹ️  INFO: {activity}")
        
        self.generate_port_report()
    
    def assess_threat_level(self, activity):
        """Assess threat level of port activity using Captain's expertise"""
        activity_lower = activity.lower()
        
        # High threat indicators
        high_threat_patterns = [
            'unauthorized', 'failed', 'breach', 'attack',
            'malicious', 'suspicious', 'hack', 'exploit'
        ]
        
        # Medium threat indicators  
        medium_threat_patterns = [
            'curl', 'upload', 'download', 'transfer',
            'dump', 'backup', 'export'
        ]
        
        for pattern in high_threat_patterns:
            if pattern in activity_lower:
                return "HIGH"
        
        for pattern in medium_threat_patterns:
            if pattern in activity_lower:
                return "MEDIUM"
        
        return "LOW"
    
    def generate_port_report(self):
        """Generate Captain Jackhood's port monitoring report"""
        print("\n" + "🗺️ PORT MONITORING REPORT".center(60))
        print("=" * 60)
        print(f"👨‍✈️ Monitoring Officer: {self.captain}")
        print(f"⚓ Target Port: {self.target_port}")
        print(f"🚢 Command Ship: {self.ship}")
        print(f"📅 Report Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        print(f"📊 Total Activities: {self.activities_monitored}")
        print(f"🚨 Alerts Triggered: {self.alerts_triggered}")
        
        if self.alerts_triggered > 0:
            print(f"⚠️  RECOMMENDATION: Investigate {self.alerts_triggered} flagged activities")
            print("🔍 Suggested Actions:")
            print("   • Review access logs for unauthorized attempts")
            print("   • Check firewall rules and access controls")
            print("   • Consider temporary port restrictions")
            print("   • Alert security team of suspicious patterns")
        else:
            print("✅ ASSESSMENT: Port appears secure")
            print("🛡️  Continue regular monitoring")
        
        print(f"\n⚓ {self.captain} - End of Report")

def main():
    if len(sys.argv) < 2:
        print("🏴‍☠️ Captain Jackhood's Port Watcher")
        print("Usage: python port_watcher.py <log_file> [port]")
        print("Example: python port_watcher.py logs/upload-success.log")
        print("Example: python port_watcher.py logs/access.log SERVER_IP:8080")
        sys.exit(1)
    
    log_file = sys.argv[1]
    target_port = sys.argv[2] if len(sys.argv) > 2 else "SERVER_IP:9999"
    
    watcher = JackhoodPortWatcher(target_port)
    watcher.monitor_log_file(log_file)

if __name__ == "__main__":
    main()
