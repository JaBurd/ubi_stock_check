from slack_sdk.webhook import WebhookClient
from bs4 import BeautifulSoup
import time
import requests
import json
import os

TARGET_URL = "https://store.ui.com/us/en/products/" + os.environ.get('UBI_PRODUCT')

def notify(product, url):
    webhook = WebhookClient(os.environ.get('SLACK_WEBHOOK_URL'))

    response = webhook.send(text="The " + product + " is available! URL: " + url)
    assert response.status_code == 200
    assert response.body == "ok"
    print("Notified!")
def scrape():
    page = requests.get(TARGET_URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # time.sleep(60)

    product_json = soup.find(id="product-jsonld")
    
    product_data = json.loads(product_json.contents[0])

    if product_data['offers']['availability'] == "https://schema.org/InStock":
        print("The",product_data['name'],"is available! URL:",product_data['url'])
        notify(product_data['name'], product_data['url'])
    else:
        print("The",product_data['name'],"is NOT available! URL:",product_data['url'])

if __name__ == "__main__":
    scrape()