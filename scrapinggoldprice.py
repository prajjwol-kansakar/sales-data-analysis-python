from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from datetime import datetime
import time

# Folders
data_folder = "data"
screenshot_folder = os.path.join(data_folder, "screenshots")
os.makedirs(data_folder, exist_ok=True)
os.makedirs(screenshot_folder, exist_ok=True)

json_file = os.path.join(data_folder, "bullion.json")
latest_json = os.path.join(data_folder, "latest_screenshot.json")

# Setup Selenium
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # optional if you want browser invisible
options.add_argument("--start-maximized")  # make window large for screenshot
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.sharesansar.com/bullion")
wait = WebDriverWait(driver, 20)

# Wait for table to load
tbody = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "table.table-bordered.table-striped tbody")
))

# Scroll table into view
driver.execute_script("arguments[0].scrollIntoView(true);", tbody)
time.sleep(2)  # wait to ensure fully rendered

# Scrape table
rows = tbody.find_elements(By.TAG_NAME, "tr")
data = []

for row in rows:
    try:
        name = row.find_element(By.TAG_NAME, "h3").text.strip()
        price = row.find_element(By.TAG_NAME, "h4").text.strip()
        daily_change = row.find_element(By.TAG_NAME, "h5").text.strip()
        data.append({
            "Name": name,
            "Price": price,
            "Daily Change": daily_change
        })
    except:
        continue


with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Take screenshot of the table element
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_file = os.path.join(screenshot_folder, f"bullion_{timestamp}.png")
tbody.screenshot(screenshot_file)  # <- screenshot only the table

# Save latest screenshot info
with open(latest_json, "w") as f:
    json.dump({"latest": os.path.basename(screenshot_file)}, f)

driver.quit()
print(f"Data saved to {json_file} and screenshot saved to {screenshot_file}")
