#!/usr/bin/env python3
"""
🏴‍☠️ Captain Jackhood's Treasure Scanner
======================================

Advanced treasure leak detection system developed by the legendary
Captain Jackhood. This tool specializes in identifying valuable
data that might be at risk of theft by digital pirates.

"No treasure shall be lost on my watch!" - Captain Jackhood
"""

import os
import sys
import re
import json
from datetime import datetime
from utils.filters import scan_for_treasure_leaks, generate_security_score

class TreasureScanner:
    def __init__(self):
        self.captain = "Captain Jackhood"
        self.ship = "HMS Digital Revenge"
        self.treasures_found = 0
        self.security_threats = 0
        
    def scan_directory(self, directory_path):
        """Scan entire directory for treasure leaks"""
        print(f"🏴‍☠️ {self.captain}'s Treasure Scanner")
        print(f"⚓ Scanning directory: {directory_path}")
        print("=" * 50)
        
        treasure_reports = []
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.log'):
                    file_path = os.path.join(root, file)
                    report = self.scan_single_file(file_path)
                    if report:
                        treasure_reports.append(report)
        
        self.generate_treasure_map(treasure_reports)
    
    def scan_single_file(self, file_path):
        """Scan individual log file for treasures"""
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            treasures = scan_for_treasure_leaks(lines)
            security_score = generate_security_score(lines)
            
            if treasures or security_score < 80:
                return {
                    'file': file_path,
                    'treasures': treasures,
                    'security_score': security_score,
                    'total_lines': len(lines)
                }
            
        except Exception as e:
            print(f"⚠️ Error scanning {file_path}: {e}")
        
        return None
    
    def generate_treasure_map(self, reports):
        """Generate comprehensive treasure security report"""
        print("\n🗺️ CAPTAIN JACKHOOD'S TREASURE MAP")
        print("=" * 50)
        
        if not reports:
            print("✅ No treasures at risk detected!")
            print("🏴‍☠️ All cargo appears secure, Captain!")
            return
        
        for report in reports:
            print(f"\n📁 File: {report['file']}")
            print(f"🛡️  Security Score: {report['security_score']}/100")
            
            if report['treasures']:
                print("💎 TREASURES AT RISK:")
                for treasure in report['treasures']:
                    print(f"   {treasure}")
                    self.treasures_found += 1
            
            if report['security_score'] < 50:
                print("🚨 CRITICAL: Immediate attention required!")
            elif report['security_score'] < 80:
                print("⚠️ WARNING: Enhanced monitoring recommended")
        
        print(f"\n⚓ SUMMARY:")
        print(f"   💎 Total treasures at risk: {self.treasures_found}")
        print(f"   📊 Files analyzed: {len(reports)}")
        print(f"   👨‍✈️ Analysis by: {self.captain}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python treasure_scanner.py <directory>")
        print("Example: python treasure_scanner.py logs/")
        sys.exit(1)
    
    scanner = TreasureScanner()
    scanner.scan_directory(sys.argv[1])
