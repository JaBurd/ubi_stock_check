from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup
import time
import requests

TARGET_URL = "https://store.ui.com/us/en/category/all-cloud-gateways/collections/cloud-gateway-fiber/products/ucg-fiber"
WEBHOOK_URL = (
    "<Discord Webhook URL>"
)

def notify():
    webhook = DiscordWebhook(url=WEBHOOK_URL, content='@everyone Product is in stock!')
    return webhook.execute()
    print("Notified!")
def scrape():
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    time.sleep(60)
    found = soup.find_all("button", string="Add to Cart")
    print(found)
    if found:
        print("Found availability.")
        # notify()
    else:
        print("Out of stock.")
    scrape()


if __name__ == "__main__":
    scrape()