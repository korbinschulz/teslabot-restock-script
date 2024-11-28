import requests
import json
import time

# Configuration
url = "https://shop.tesla.com/inventory.json"
headers = {
    "Host": "shop.tesla.com",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": '"macOS"',
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "Origin": "https://shop.tesla.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://shop.tesla.com/product/tesla-bot-action-figure?sku=2080682-00-A&web=true",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
}

discord_webhook_url = 'put-your-discord-webhook-here'
data = '["2080682-00-A"]'

def check_inventory():
    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        inventory = response.json()

        # Check the purchasable key in the response
        for item in inventory:
            if item.get("purchasable", False):
                print("Item is now purchasable!")
                print("Details:", json.dumps(item, indent=4))
                send_discord_notification(discord_webhook_url)
                return True
        print("Item is not purchasable yet.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def send_discord_notification(webhook_url):
    """
    Sends a notification to a Discord webhook when the product is in stock.

    :param webhook_url: Discord webhook URL
    """
    tesla_bot_link = 'https://shop.tesla.com/product/tesla-bot-action-figure?sku=2080682-00-A&web=true'
    message = {
        "content": f"🚨 **TESLA BOT RESTOCKED!** 🚨\n"
                   f"**Link:** {tesla_bot_link}\n",
        "username": "Tesla Inventory Bot"
    }

    try:
        response = requests.post(webhook_url, json=message)
        response.raise_for_status()
        print("Notification sent successfully to Discord!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")


def main():
    while True:
        is_purchasable = check_inventory()
        if is_purchasable:
            print("Exiting the script since the item is purchasable.")
            break
        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    main()
