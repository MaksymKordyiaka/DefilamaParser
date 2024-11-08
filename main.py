import time
import json
import re
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    filename="scraping_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

with open("config.json", "r") as config_file:
    config = json.load(config_file)

scrape_interval_seconds = config["scrape_interval_minutes"] * 60
proxy = config.get("proxy")

chrome_options = Options()
if proxy:
    chrome_options.add_argument(f'--proxy-server={proxy}')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
url = 'https://defillama.com/chains'


def scrape_data():
    try:
        logging.info("Starting to scrape data...")
        driver.get(url)
        time.sleep(5)

        rows = driver.find_elements(By.CSS_SELECTOR, "div[data-chainpage='true'].sc-af4250f5-0.fYBVwr")

        if not rows:
            logging.error("No data found on the page.")
            return

        count = 0
        data = []

        for i in range(0, len(rows), 14):
            if count >= 12:
                break

            if i == 0:
                continue

            try:
                raw_name = rows[i].text
                if not raw_name:
                    raise ValueError("Missing Name data")
                name = re.sub(r'^\d+\s+', '', raw_name)

                protocols = rows[i + 1].text
                if not protocols:
                    raise ValueError("Missing Protocols data")

                tvl = rows[i + 6].text
                if not tvl:
                    raise ValueError("Missing TVL data")

                blockchain_data = {
                    "Name": name,
                    "Protocols": protocols,
                    "TVL": tvl
                }
                data.append(blockchain_data)

                count += 1

            except ValueError as ve:
                logging.warning(f"Data Error: {ve}. Skipping this entry.")
                continue

            except Exception as e:
                logging.error(f"Unexpected error while scraping row {i}: {e}")

        if data:
            with open("blockchain_data.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            logging.info(f"Successfully scraped and saved {len(data)} records.")
        else:
            logging.warning("No valid data found to save.")

    except TimeoutException as te:
        logging.error(f"Timeout Error: {te}. Retrying...")
        time.sleep(5)
        scrape_data()

    except WebDriverException as we:
        logging.error(f"WebDriver Error: {we}. Retrying...")
        time.sleep(5)
        scrape_data()

    except ConnectionAbortedError as cae:
        logging.error(f"Connection Error: {cae}. An established connection was aborted. Retrying...")
        time.sleep(5)
        scrape_data()

    except Exception as e:
        logging.error(f"Error during scraping: {e}")


while True:
    scrape_data()
    logging.info(f"Waiting for {scrape_interval_seconds / 60} minutes...")
    logging.info("-" * 50)
    time.sleep(scrape_interval_seconds)
