#!/usr/bin/env python3
"""
🏴‍☠️ CAPTAIN JACKHOOD'S MARITIME SECURITY DASHBOARD
==================================================
Real-time security monitoring and threat visualization
for the legendary Captain's digital fleet

Author: Captain Jackhood
Ship: HMS Digital Revenge
Port: SERVER_IP:9999
"""

import os
import sys
import time
import json
import yaml
import logging
import threading
from datetime import datetime, timedelta
from collections import defaultdict, deque
import subprocess
import re
import hashlib
from pathlib import Path

# ASCII Art Banner
CAPTAIN_BANNER = """
╔══════════════════════════════════════════════════════════════╗
║          🏴‍☠️ CAPTAIN JACKHOOD'S SECURITY DASHBOARD 🏴‍☠️          ║
║                                                              ║
║  "In the digital seas, vigilance is the wind in our sails"  ║
║                     - Captain Jackhood                      ║
║                                                              ║
║  Ship: HMS Digital Revenge    ⚓ Port: SERVER_IP:9999       ║
╚══════════════════════════════════════════════════════════════╝
"""

class MaritimeDashboard:
    """Captain Jackhood's legendary security dashboard"""
    
    def __init__(self, config_path="captain_config.yaml"):
        self.config = self.load_config(config_path)
        self.captain_info = self.config.get('captain_info', {})
        self.monitoring_config = self.config.get('monitoring', {})
        self.running = False
        
        # Initialize logging
        self.setup_logging()
        
        # Data storage for real-time metrics
        self.metrics = {
            'threats_detected': 0,
            'ports_scanned': 0,
            'treasure_alerts': 0,
            'security_score': 100,
            'uptime_start': datetime.now(),
            'last_scan': None
        }
        
        # Recent activity queues (last 100 events)
        self.recent_threats = deque(maxlen=100)
        self.recent_port_activity = deque(maxlen=100)
        self.recent_alerts = deque(maxlen=100)
        
        # Threat patterns from config
        self.threat_patterns = self.config.get('threat_detection', {})
        
        self.logger.info("🏴‍☠️ Captain Jackhood's Dashboard initialized successfully!")
        self.logger.info(f"⚓ Monitoring home port: {self.captain_info.get('home_port', 'SERVER_IP:9999')}")
    
    def load_config(self, config_path):
        """Load Captain's configuration file"""
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return yaml.safe_load(f)
            else:
                return self.get_default_config()
        except Exception as e:
            print(f"⚠️  Warning: Could not load config: {e}")
            return self.get_default_config()
    
    def get_default_config(self):
        """Fallback configuration if config file missing"""
        return {
            'captain_info': {
                'name': 'Captain Jackhood',
                'ship': 'HMS Digital Revenge',
                'home_port': 'SERVER_IP:9999'
            },
            'monitoring': {
                'critical_ports': ['SERVER_IP:9999', 'SERVER_IP:8080'],
                'scan_interval': 60
            },
            'logging': {
                'log_directory': './logs'
            }
        }
    
    def setup_logging(self):
        """Initialize the Captain's logging system"""
        log_dir = self.config.get('logging', {}).get('log_directory', './logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - [CAPTAIN] - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'{log_dir}/captain_dashboard.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_uptime(self):
        """Calculate dashboard uptime"""
        uptime = datetime.now() - self.metrics['uptime_start']
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if days > 0:
            return f"{days}d {hours}h {minutes}m"
        elif hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        else:
            return f"{minutes}m {seconds}s"
    
    def calculate_security_score(self):
        """Calculate current security score based on threats and activity"""
        base_score = 100
        
        # Deduct points for recent threats
        recent_threats_count = len([t for t in self.recent_threats 
                                  if t['timestamp'] > datetime.now() - timedelta(hours=1)])
        base_score -= min(recent_threats_count * 5, 50)
        
        # Deduct points for treasure alerts
        base_score -= min(self.metrics['treasure_alerts'] * 2, 30)
        
        # Bonus points for long uptime
        uptime_hours = (datetime.now() - self.metrics['uptime_start']).total_seconds() / 3600
        if uptime_hours > 24:
            base_score += min(int(uptime_hours / 24), 10)
        
        self.metrics['security_score'] = max(0, min(100, base_score))
        return self.metrics['security_score']
    
    def get_threat_level_color(self, score):
        """Get color code for threat level"""
        if score >= 90:
            return "\033[92m"  # Green
        elif score >= 70:
            return "\033[93m"  # Yellow
        elif score >= 50:
            return "\033[91m"  # Red
        else:
            return "\033[95m"  # Magenta (Critical)
    
    def scan_ports(self):
        """Scan critical ports for activity"""
        critical_ports = self.monitoring_config.get('critical_ports', ['SERVER_IP:9999'])
        
        for port_spec in critical_ports:
            try:
                # Extract port from SERVER_IP:PORT format
                if ':' in port_spec:
                    host, port = port_spec.split(':')
                    port = int(port)
                else:
                    continue
                
                # Simulate port scanning (in real implementation, use socket)
                import random
                is_open = random.choice([True, False])
                
                activity = {
                    'timestamp': datetime.now(),
                    'port': port_spec,
                    'status': 'OPEN' if is_open else 'CLOSED',
                    'response_time': round(random.uniform(0.1, 5.0), 2)
                }
                
                self.recent_port_activity.append(activity)
                self.metrics['ports_scanned'] += 1
                
                if port_spec == 'SERVER_IP:9999' and not is_open:
                    # Critical alert - home port is down!
                    alert = {
                        'timestamp': datetime.now(),
                        'level': 'CRITICAL',
                        'message': '🚨 HOME PORT SERVER_IP:9999 IS DOWN! 🚨',
                        'source': 'Port Monitor'
                    }
                    self.recent_alerts.append(alert)
                    self.logger.critical(alert['message'])
                
            except Exception as e:
                self.logger.warning(f"⚠️  Port scan error for {port_spec}: {e}")
    
    def detect_threats(self):
        """Detect threats in log files and system"""
        log_dir = self.config.get('logging', {}).get('log_directory', './logs')
        
        # Check for suspicious files
        treasure_patterns = self.threat_patterns.get('treasure_patterns', [])
        
        for pattern in treasure_patterns:
            # Simulate threat detection
            import random
            if random.random() < 0.1:  # 10% chance of detecting threat
                threat = {
                    'timestamp': datetime.now(),
                    'type': 'File Threat',
                    'pattern': pattern,
                    'severity': random.choice(['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']),
                    'location': f"./suspicious/{pattern.replace('*', 'leaked_data')}"
                }
                
                self.recent_threats.append(threat)
                self.metrics['threats_detected'] += 1
                
                if 'treasure' in pattern or threat['severity'] in ['HIGH', 'CRITICAL']:
                    self.metrics['treasure_alerts'] += 1
                    
                    alert = {
                        'timestamp': datetime.now(),
                        'level': threat['severity'],
                        'message': f"💰 TREASURE THREAT: {threat['pattern']} detected at {threat['location']}",
                        'source': 'Threat Detector'
                    }
                    self.recent_alerts.append(alert)
                    self.logger.warning(alert['message'])
    
    def display_header(self):
        """Display the dashboard header"""
        print(CAPTAIN_BANNER)
        print(f"📅 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏰ Uptime: {self.get_uptime()}")
        print(f"👑 Captain: {self.captain_info.get('name', 'Captain Jackhood')}")
        print(f"🚢 Ship: {self.captain_info.get('ship', 'HMS Digital Revenge')}")
        print(f"⚓ Home Port: {self.captain_info.get('home_port', 'SERVER_IP:9999')}")
        print("═" * 70)
    
    def display_metrics(self):
        """Display current security metrics"""
        security_score = self.calculate_security_score()
        color = self.get_threat_level_color(security_score)
        reset = "\033[0m"
        
        print("\n📊 SECURITY METRICS:")
        print(f"   Security Score: {color}{security_score}/100{reset}")
        print(f"   Threats Detected: {self.metrics['threats_detected']}")
        print(f"   Ports Scanned: {self.metrics['ports_scanned']}")
        print(f"   Treasure Alerts: 💰 {self.metrics['treasure_alerts']}")
        print(f"   Last Scan: {self.metrics['last_scan'].strftime('%H:%M:%S') if self.metrics['last_scan'] else 'Never'}")
    
    def display_recent_activity(self):
        """Display recent security activity"""
        print("\n🔍 RECENT THREATS (Last 5):")
        recent_threats = list(self.recent_threats)[-5:]
        if recent_threats:
            for threat in recent_threats:
                timestamp = threat['timestamp'].strftime('%H:%M:%S')
                print(f"   [{timestamp}] {threat['severity']:8} | {threat['type']} | {threat['pattern']}")
        else:
            print("   No recent threats detected 🎉")
        
        print("\n⚓ PORT ACTIVITY (Last 5):")
        recent_ports = list(self.recent_port_activity)[-5:]
        if recent_ports:
            for activity in recent_ports:
                timestamp = activity['timestamp'].strftime('%H:%M:%S')
                status_icon = "🟢" if activity['status'] == 'OPEN' else "🔴"
                print(f"   [{timestamp}] {status_icon} {activity['port']:20} | {activity['status']:6} | {activity['response_time']}ms")
        else:
            print("   No recent port activity")
        
        print("\n🚨 RECENT ALERTS (Last 3):")
        recent_alerts = list(self.recent_alerts)[-3:]
        if recent_alerts:
            for alert in recent_alerts:
                timestamp = alert['timestamp'].strftime('%H:%M:%S')
                level_icon = {"LOW": "🟡", "MEDIUM": "🟠", "HIGH": "🔴", "CRITICAL": "💀"}.get(alert['level'], "⚪")
                print(f"   [{timestamp}] {level_icon} {alert['level']:8} | {alert['message'][:50]}...")
        else:
            print("   All quiet on the digital seas 🌊")
    
    def display_status_bar(self):
        """Display bottom status bar"""
        print("\n" + "═" * 70)
        status = "🟢 MONITORING" if self.running else "🔴 STOPPED"
        print(f"Status: {status} | Press Ctrl+C to stop | Scan Interval: {self.monitoring_config.get('scan_interval', 60)}s")
        print("═" * 70)
    
    def monitoring_loop(self):
        """Main monitoring loop"""
        scan_interval = self.monitoring_config.get('scan_interval', 60)
        
        while self.running:
            try:
                # Update last scan time
                self.metrics['last_scan'] = datetime.now()
                
                # Perform security scans
                self.scan_ports()
                self.detect_threats()
                
                # Update display
                self.clear_screen()
                self.display_header()
                self.display_metrics()
                self.display_recent_activity()
                self.display_status_bar()
                
                # Wait for next scan
                time.sleep(scan_interval)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"❌ Monitoring loop error: {e}")
                time.sleep(5)  # Brief pause before retry
    
    def start(self):
        """Start the dashboard monitoring"""
        print(CAPTAIN_BANNER)
        print("\n🚀 Initializing Captain Jackhood's Security Dashboard...")
        print(f"⚓ Monitoring home port: {self.captain_info.get('home_port', 'SERVER_IP:9999')}")
        print("🔍 Starting security scans...")
        
        self.running = True
        
        try:
            # Start monitoring in a separate thread
            monitor_thread = threading.Thread(target=self.monitoring_loop)
            monitor_thread.daemon = True
            monitor_thread.start()
            
            # Keep main thread alive
            monitor_thread.join()
            
        except KeyboardInterrupt:
            print("\n\n🏴‍☠️ Captain Jackhood's Dashboard shutting down...")
            print("Fair winds and following seas! ⛵")
        finally:
            self.running = False
            self.logger.info("🏴‍☠️ Dashboard stopped by Captain's orders")
    
    def generate_report(self, output_format='text'):
        """Generate security report"""
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'captain': self.captain_info.get('name', 'Captain Jackhood'),
            'ship': self.captain_info.get('ship', 'HMS Digital Revenge'),
            'home_port': self.captain_info.get('home_port', 'SERVER_IP:9999'),
            'uptime': self.get_uptime(),
            'metrics': self.metrics.copy(),
            'security_score': self.calculate_security_score(),
            'recent_threats': [dict(t) for t in list(self.recent_threats)[-10:]],
            'recent_alerts': [dict(a) for a in list(self.recent_alerts)[-10:]],
            'recent_port_activity': [dict(p) for p in list(self.recent_port_activity)[-10:]]
        }
        
        if output_format == 'json':
            return json.dumps(report_data, indent=2, default=str)
        elif output_format == 'html':
            return self.generate_html_report(report_data)
        else:
            return self.generate_text_report(report_data)
    
    def generate_text_report(self, data):
        """Generate text format report"""
        report = f"""
🏴‍☠️ CAPTAIN JACKHOOD'S SECURITY REPORT 🏴‍☠️
════════════════════════════════════════════

Report Generated: {data['timestamp']}
Captain: {data['captain']}
Ship: {data['ship']}
Home Port: {data['home_port']}
Dashboard Uptime: {data['uptime']}

SECURITY OVERVIEW:
─────────────────
Security Score: {data['security_score']}/100
Threats Detected: {data['metrics']['threats_detected']}
Treasure Alerts: {data['metrics']['treasure_alerts']}
Ports Scanned: {data['metrics']['ports_scanned']}

RECENT THREATS:
──────────────
"""
        
        for threat in data['recent_threats']:
            report += f"• [{threat['timestamp']}] {threat['severity']} - {threat['type']}: {threat['pattern']}\n"
        
        report += f"\nRECENT ALERTS:\n──────────────\n"
        for alert in data['recent_alerts']:
            report += f"• [{alert['timestamp']}] {alert['level']} - {alert['message']}\n"
        
        report += f"\n⚓ End of Report - Fair winds and following seas!\n"
        report += f"   - Captain {data['captain']}\n"
        
        return report
    
    def generate_html_report(self, data):
        """Generate HTML format report"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Captain Jackhood's Security Report</title>
    <style>
        body {{ font-family: 'Courier New', monospace; background: #1a1a1a; color: #ffd700; margin: 20px; }}
        .header {{ text-align: center; border: 2px solid #ffd700; padding: 20px; margin-bottom: 20px; }}
        .metric {{ background: #2a2a2a; padding: 10px; margin: 5px 0; border-left: 4px solid #ffd700; }}
        .threat {{ background: #3a1a1a; padding: 8px; margin: 3px 0; border-left: 3px solid #ff6b6b; }}
        .alert {{ background: #1a3a1a; padding: 8px; margin: 3px 0; border-left: 3px solid #ffd700; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🏴‍☠️ CAPTAIN JACKHOOD'S SECURITY REPORT 🏴‍☠️</h1>
        <p>Ship: {data['ship']} | Home Port: {data['home_port']}</p>
        <p>Report Generated: {data['timestamp']}</p>
    </div>
    
    <h2>Security Overview</h2>
    <div class="metric">Security Score: {data['security_score']}/100</div>
    <div class="metric">Threats Detected: {data['metrics']['threats_detected']}</div>
    <div class="metric">Treasure Alerts: {data['metrics']['treasure_alerts']}</div>
    <div class="metric">Dashboard Uptime: {data['uptime']}</div>
    
    <h2>Recent Threats</h2>
"""
        
        for threat in data['recent_threats']:
            html += f'<div class="threat">[{threat["timestamp"]}] {threat["severity"]} - {threat["type"]}: {threat["pattern"]}</div>\n'
        
        html += "<h2>Recent Alerts</h2>\n"
        for alert in data['recent_alerts']:
            html += f'<div class="alert">[{alert["timestamp"]}] {alert["level"]} - {alert["message"]}</div>\n'
        
        html += """
    <div class="header" style="margin-top: 30px;">
        <p>⚓ Fair winds and following seas!</p>
        <p>- Captain Jackhood, HMS Digital Revenge</p>
    </div>
</body>
</html>
"""
        return html

def main():
    """Main function to run Captain Jackhood's Dashboard"""
    print("🏴‍☠️ Loading Captain Jackhood's Maritime Security Dashboard...")
    
    # Initialize dashboard
    dashboard = MaritimeDashboard()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'report':
            # Generate and display report
            format_type = sys.argv[2] if len(sys.argv) > 2 else 'text'
            report = dashboard.generate_report(format_type)
            print(report)
            
        elif command == 'config':
            # Display current configuration
            print(json.dumps(dashboard.config, indent=2))
            
        elif command == 'status':
            # Display quick status
            print(f"Captain: {dashboard.captain_info.get('name')}")
            print(f"Ship: {dashboard.captain_info.get('ship')}")
            print(f"Home Port: {dashboard.captain_info.get('home_port')}")
            print(f"Security Score: {dashboard.calculate_security_score()}/100")
            
        else:
            print(f"Unknown command: {command}")
            print("Available commands: report, config, status")
    else:
        # Start interactive dashboard
        dashboard.start()

if __name__ == "__main__":
    main()
