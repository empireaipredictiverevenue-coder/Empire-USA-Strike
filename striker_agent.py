import requests
from bs4 import BeautifulSoup
import logging
import time

# 1. THE COCKPIT RADAR (Live Logging)
# This shows you exactly what the agent is doing in real time.
logging.basicConfig(level=logging.INFO, format='[AGENT 001] %(asctime)s : %(message)s')

class StrikerAgent:
    def __init__(self, target_url, threat_keywords):
        self.target_url = target_url
        self.threat_keywords = threat_keywords

    def scan(self):
        logging.info("Initiating Satellite Scan for USA Strike Zones...")
        # 2. THE SAFETY NET (Error Handling)
        try:
            # We give the server 10 seconds to respond. If it fails, we do not crash.
            response = requests.get(self.target_url, timeout=10)
            response.raise_for_status()
            self._parse_and_strike(response.content)
        except requests.exceptions.RequestException as error:
            logging.error(f"Radar jammed. Retrying on next loop. Error: {error}")

    def _parse_and_strike(self, xml_data):
        soup = BeautifulSoup(xml_data, 'xml')
        alerts = soup.find_all('entry')
        found_threat = False

        for alert in alerts:
            title = alert.title.text.upper()
            # 3. THE MULTI-THREAT DETECTOR
            if any(threat in title for threat in self.threat_keywords):
                location = alert.find('cap:areaDesc').text if alert.find('cap:areaDesc') else "Unknown Zone"
                logging.warning(f"TARGET ACQUIRED: {title} in {location}")
                self.trigger_commander(location)
                found_threat = True

        if not found_threat:
            logging.info("Clear skies. Maintaining radar lock.")

    def trigger_commander(self, location):
        logging.info(f"OVERDRIVE ENGAGED: Forging 80-Second Page for {location}...")
        
        # 4. THE COMMANDER PAYLOAD
        payload = {
            "zone": location,
            "template": "COCKPIT_V1",
            "lead_magnet": "STORM_IMPACT_CALCULATOR",
            "affiliate_payout": "50%"
        }
        
        logging.info("Strike Page LIVE. Agent 005 notified.")

# ---------------------------------------------------------
# THE IGNITION SWITCH
# ---------------------------------------------------------
if __name__ == "__main__":
    # Target: Wisconsin Live Feed
    WI_URL = "https://alerts.weather.gov/cap/wi.php?x=0"
    
    # Target: Triple Threat Logic
    THREATS = ["TORNADO WARNING", "SEVERE THUNDERSTORM", "FLASH FLOOD WARNING"]

    # Build the Agent
    agent_001 = StrikerAgent(WI_URL, THREATS)

    # The Continuous Loop (Runs every 60 seconds)
    while True:
        agent_001.scan()
        logging.info("Sleeping for 60 seconds...")
        time.sleep(60)
