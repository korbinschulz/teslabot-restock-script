# Teslabot Restock Script

A Python script that checks Tesla's inventory API to monitor product availability. If a product becomes purchasable, the script sends a notification to a Discord webhook.

---

## Features

- **Monitor Inventory**: Automatically checks Tesla's inventory API every minute.
- **Detect In-Stock Products**: Alerts when a product's `purchasable` status changes to `true`.
- **Discord Notifications**: Sends a notification to a specified Discord webhook with product details.

---

## Requirements

- Python 3.7+
- `requests` library

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/korbinschulz/teslabot-restock-script.git
   cd tesla-inventory-checker


--- 

## Install Dependencies

- pip install requests

---

## Discord

- Be sure to create a discord webhook, and then add that to the code
- After doing that you can run the script using the command `python main.py`
- Feel free to adjust the sleep time as desired, but making it too low could result in you getting rate limited (which is bad)
