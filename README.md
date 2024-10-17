# Blockchain Security Monitor

This Python script provides a monitoring solution for blockchain networks, focusing on detecting and logging anomalies in transactions. It can help enhance the security of your blockchain applications by alerting you to suspicious activities.

## Features

- **Fetch Latest Block**: Retrieves the latest block from the blockchain.
- **Transaction Analysis**: Analyzes transactions for anomalous patterns.
- **Anomaly Logging**: Logs detected anomalies for future review.
- **Alerts**: Sends alerts if the number of anomalies exceeds a specified threshold.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/blockchain_security_monitor.git
    cd blockchain_security_monitor
    ```

2. **Install required packages**:

    ```bash
    pip install requests
    ```

3. **Run the monitor**:

    ```bash
    python blockchain_security_monitor.py
    ```

## Configuration

- Update the `blockchain_url` variable in `blockchain_security_monitor.py` to point to your blockchain node's API endpoint. For example:

    ```python
    blockchain_url = "http://localhost:5000"  # URL of your blockchain node
    ```

- The script currently considers a transaction anomalous if its amount exceeds `1000`. You can modify this threshold in the `is_anomalous` method according to your requirements.

## Log File

- Anomalies detected during monitoring are logged in `blockchain_security.log`. Check this file for detailed records of any suspicious transactions.

## Alerts

- The script will print an alert message in the console if the number of detected anomalies exceeds the threshold specified in the constructor (`alert_threshold`). You can customize the alerting mechanism (e.g., email notifications) by modifying the `send_alert` method.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for discussion.
