#!/usr/bin/env python3
"""
🏴‍☠️ Captain Jackhood's Maritime Security Filters 
================================================

Advanced pattern detection algorithms developed by Captain Jackhood
during his legendary voyages across the digital seas.

These filters have been battle-tested against the most notorious
digital pirates and treasure thieves.
"""

import re
from datetime import datetime

def detect_suspicious_patterns(lines):
    """
    Captain Jackhood's legendary pattern detection algorithm.
    Identifies potential treasure theft and unauthorized activities.
    """
    # The Captain's carefully crafted suspicious patterns
    threat_patterns = [
        'upload', 'sftp', 'wget', 'curl', 'scp', 'rsync',
        'exfil', 'dump', 'leak', 'steal', 'hack', 'breach',
        'unauthorized', 'suspicious', 'anomaly', 'threat'
    ]
    
    # Captain's special attention to data transfer activities
    treasure_theft_patterns = [
        r'curl.*-F.*data=@',  # File upload via curl
        r'wget.*-O.*dump',    # Suspicious downloads
        r'scp.*@.*:',         # Secure copy operations
        r'SERVER_IP:9999',    # Activities on Captain's home port
    ]
    
    suspicious_activities = []
    
    for line_num, line in enumerate(lines, 1):
        line_lower = line.lower().strip()
        
        # Check for basic suspicious patterns
        for pattern in threat_patterns:
            if pattern in line_lower:
                suspicious_activities.append(
                    f"⚠️  Line {line_num}: Threat pattern '{pattern}' detected - {line.strip()}"
                )
                break
        
        # Check for advanced treasure theft patterns
        for pattern in treasure_theft_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                suspicious_activities.append(
                    f"🚨 Line {line_num}: CRITICAL - Potential treasure theft pattern detected - {line.strip()}"
                )
    
    return suspicious_activities

def analyze_port_activity(lines, target_port="SERVER_IP:9999"):
    """
    Captain Jackhood's specialized port monitoring function.
    Focuses on activities involving the specified port.
    """
    port_activities = []
    
    for line_num, line in enumerate(lines, 1):
        if target_port in line:
            timestamp = extract_timestamp(line)
            activity_type = determine_activity_type(line)
            
            port_activities.append(
                f"Line {line_num} [{timestamp}] {activity_type}: {line.strip()}"
            )
    
    return port_activities

def extract_timestamp(line):
    """Extract timestamp from log line using Captain's regex patterns"""
    # Common timestamp patterns the Captain has encountered
    timestamp_patterns = [
        r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]',
        r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})',
        r'(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})'
    ]
    
    for pattern in timestamp_patterns:
        match = re.search(pattern, line)
        if match:
            return match.group(1)
    
    return "Unknown time"

def determine_activity_type(line):
    """Classify the type of activity based on Captain's experience"""
    line_lower = line.lower()
    
    if 'curl' in line_lower:
        return "🌊 CURL Operation"
    elif 'upload' in line_lower:
        return "📤 Upload Activity"
    elif 'download' in line_lower:
        return "📥 Download Activity"
    elif 'connection' in line_lower:
        return "🔌 Connection Event"
    elif 'success' in line_lower:
        return "✅ Successful Operation"
    elif 'failed' in line_lower or 'error' in line_lower:
        return "❌ Failed Operation"
    else:
        return "❓ Unknown Activity"

def scan_for_treasure_leaks(lines):
    """
    Captain Jackhood's advanced treasure leak detection.
    Looks for patterns indicating valuable data being transferred.
    """
    treasure_patterns = [
        r'dump\.txt',           # Database dumps
        r'backup\.sql',         # SQL backups
        r'config\.json',        # Configuration files
        r'\.env',               # Environment files
        r'secret',              # Secret files
        r'password',            # Password files
        r'token',               # Token files
        r'key\.pem',            # Private keys
    ]
    
    treasure_alerts = []
    
    for line_num, line in enumerate(lines, 1):
        for pattern in treasure_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                treasure_alerts.append(
                    f"💎 TREASURE ALERT Line {line_num}: Potential valuable data - {line.strip()}"
                )
    
    return treasure_alerts

def detect_captain_adversaries(lines):
    """
    Detect known adversaries and threats that Captain Jackhood has encountered.
    """
    known_adversaries = [
        'blackbeard', 'redbeard', 'ghostfleet', 'kraken',
        'malware', 'botnet', 'backdoor', 'trojan'
    ]
    
    adversary_alerts = []
    
    for line_num, line in enumerate(lines, 1):
        line_lower = line.lower()
        for adversary in known_adversaries:
            if adversary in line_lower:
                adversary_alerts.append(
                    f"☠️  ADVERSARY DETECTED Line {line_num}: '{adversary}' activity - {line.strip()}"
                )
    
    return adversary_alerts

def generate_security_score(lines):
    """
    Captain Jackhood's proprietary security scoring algorithm.
    Returns a score from 0 (total chaos) to 100 (smooth sailing).
    """
    total_lines = len(lines)
    if total_lines == 0:
        return 100
    
    suspicious_count = len(detect_suspicious_patterns(lines))
    treasure_leaks = len(scan_for_treasure_leaks(lines))
    adversary_count = len(detect_captain_adversaries(lines))
    
    # Captain's scoring formula
    threat_ratio = (suspicious_count + treasure_leaks * 2 + adversary_count * 3) / total_lines
    security_score = max(0, 100 - (threat_ratio * 100))
    
    return round(security_score, 2)
