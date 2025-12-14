#!/usr/bin/env python3
"""
🏴‍☠️ Captain Jackhood's Maritime Log Analyzer 
==============================================

A legendary tool forged by Captain Jackhood himself for detecting suspicious
activities and potential treasure leaks across the digital seas.

Author: Captain Jackhood
Ship: HMS Digital Revenge
Port: SERVER_IP:9999
Last Updated: September 4, 2025
"""

import sys
import re
import json
from datetime import datetime
from utils.filters import detect_suspicious_patterns, analyze_port_activity

# Captain's signature banner
CAPTAIN_BANNER = """
🏴‍☠️ =============================================== 🏴‍☠️
   CAPTAIN JACKHOOD'S MARITIME LOG ANALYZER
   "In Code We Trust, In Security We Sail"
🏴‍☠️ =============================================== 🏴‍☠️
"""

class MaritimeLogAnalyzer:
    def __init__(self):
        self.captain_name = "Captain Jackhood"
        self.ship_name = "HMS Digital Revenge"
        self.home_port = "SERVER_IP:9999"
        self.threats_detected = 0
        self.treasures_secured = 0
    
    def print_captain_header(self):
        """Display the Captain's signature banner"""
        print(CAPTAIN_BANNER)
        print(f"⚓ Ship: {self.ship_name}")
        print(f"🏠 Home Port: {self.home_port}")
        print(f"👨‍✈️ Captain: {self.captain_name}")
        print(f"📅 Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
    
    def analyze_log(self, file_path):
        """Main analysis function with Captain's maritime expertise"""
        print(f"🔍 Analyzing log file: {file_path}")
        print("🚢 Setting sail for analysis...")
        
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            print(f"📊 Log entries found: {len(lines)}")
            
            # Detect suspicious patterns using Captain's filters
            suspicious_results = detect_suspicious_patterns(lines)
            
            # Special analysis for port 9999 (Captain's home port)
            port_activity = analyze_port_activity(lines, self.home_port)
            
            # Generate Captain's report
            self.generate_maritime_report(suspicious_results, port_activity)
            
        except FileNotFoundError:
            print(f"❌ Shiver me timbers! Log file not found: {file_path}")
        except Exception as e:
            print(f"💥 Batten down the hatches! Error occurred: {str(e)}")
    
    def generate_maritime_report(self, suspicious_results, port_activity):
        """Generate Captain Jackhood's detailed security report"""
        print("\n" + "🗺️ " + "CAPTAIN'S SECURITY REPORT".center(50) + " 🗺️")
        print("=" * 60)
        
        # Suspicious activity analysis
        if suspicious_results:
            print(f"⚠️  THREATS DETECTED: {len(suspicious_results)}")
            print("🚨 Suspicious activities found:")
            for i, result in enumerate(suspicious_results, 1):
                print(f"   {i}. {result.strip()}")
            self.threats_detected = len(suspicious_results)
        else:
            print("✅ No immediate threats detected - seas are calm")
        
        print("\n" + "-" * 60)
        
        # Port 9999 specific analysis
        if port_activity:
            print(f"🏠 HOME PORT ({self.home_port}) ACTIVITY:")
            for activity in port_activity:
                print(f"   📡 {activity.strip()}")
        else:
            print(f"🏠 No activity detected on home port {self.home_port}")
        
        print("\n" + "-" * 60)
        
        # Captain's recommendations
        self.print_captain_recommendations()
        
        # Final summary
        print(f"\n⚓ Analysis complete. Captain {self.captain_name} signing off.")
        print(f"🏴‍☠️ Fair winds and following seas! 🏴‍☠️")
    
    def print_captain_recommendations(self):
        """Captain Jackhood's expert security recommendations"""
        print("🧭 CAPTAIN'S RECOMMENDATIONS:")
        
        if self.threats_detected > 0:
            print("   🔥 IMMEDIATE ACTION REQUIRED:")
            print("   • Investigate all flagged activities")
            print("   • Check for unauthorized treasure transfers")
            print("   • Review access controls on all ports")
            print("   • Consider raising the security alert level")
        else:
            print("   ✅ Current security posture appears sound")
            print("   • Continue regular monitoring")
            print("   • Maintain vigilance for new threats")
        
        print("   📋 STANDARD SECURITY MEASURES:")
        print(f"   • Keep monitoring port {self.home_port}")
        print("   • Regular log analysis (daily)")
        print("   • Update threat patterns weekly")
        print("   • Backup all treasure regularly")

def main():
    """Main execution function"""
    analyzer = MaritimeLogAnalyzer()
    analyzer.print_captain_header()
    
    if len(sys.argv) != 2:
        print("❌ Usage: python maritime_analyzer.py <logfile>")
        print("🗺️  Example: python maritime_analyzer.py logs/upload-success.log")
        print("⚓ For more help, consult the Captain's manual")
        sys.exit(1)
    
    log_file = sys.argv[1]
    analyzer.analyze_log(log_file)

if __name__ == '__main__':
    main()
