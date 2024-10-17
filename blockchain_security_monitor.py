import time
import json
import requests
import logging
from datetime import datetime, timedelta

# Setting up logging
logging.basicConfig(filename='blockchain_security.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BlockchainSecurityMonitor:
    def __init__(self, blockchain_url, alert_threshold=5):
        self.blockchain_url = blockchain_url
        self.alert_threshold = alert_threshold
        self.transaction_log = []
        self.anomaly_count = 0

    def fetch_latest_block(self):
        """Fetch the latest block from the blockchain."""
        response = requests.get(f"{self.blockchain_url}/latest_block")
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch latest block: {response.status_code}")
            return None

    def analyze_transactions(self, block):
        """Analyze transactions in the block for anomalies."""
        for transaction in block['transactions']:
            if self.is_anomalous(transaction):
                self.anomaly_count += 1
                self.log_anomaly(transaction)

    def is_anomalous(self, transaction):
        """Define criteria for anomalies. This can be customized."""
        # Example: detecting anomalous transaction amounts
        if transaction['amount'] > 1000:  # Anomaly threshold
            return True
        return False

    def log_anomaly(self, transaction):
        """Log an anomaly for review."""
        logging.warning(f"Anomaly detected: {transaction}")
        self.send_alert(transaction)

    def send_alert(self, transaction):
        """Send an alert if anomalies exceed the threshold."""
        if self.anomaly_count >= self.alert_threshold:
            # You can configure alerting (e.g., via email or webhooks)
            alert_message = f"Alert: {self.anomaly_count} anomalies detected!"
            logging.info(alert_message)
            print(alert_message)

    def run(self):
        """Main loop for monitoring."""
        while True:
            block = self.fetch_latest_block()
            if block:
                self.analyze_transactions(block)
            time.sleep(10)  # Polling interval (10 seconds)

if __name__ == "__main__":
    blockchain_url = "http://localhost:5000"  # Your blockchain network URL
    monitor = BlockchainSecurityMonitor(blockchain_url)
    monitor.run()
