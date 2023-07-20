---
title: Basic Selenium Setup
date: 2023-07-19 02:00:00 -700
categories: [Selenium]
tags: [selenium,python]
---

## Basic Selenium Setup Guide
Selenium is an open-source, widely used software testing framework primarily used for automating web browsers. It allows testers and developers to write automation on the frontend for QA testing and more.

### Install and Setup
1. Install selenium with pip3.
```
pip3 install selenium
```

2. Check Chrome version, open browser and type:
```
chrome://version/
```

3. Install the driver that matches your Chrome's version.
```
https://chromedriver.storage.googleapis.com/index.html
```

4. Now you can start using selenium. Try the following code to use Selenium to log into Tradingview.
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
service = Service(r'/Users/nicehost/Documents/Local_Files/Browser_Drivers/chromedriver')
chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-deb-shm-usage')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
#
longInfo = ["my-user-name", "my-pass-word"]
driver.get("https://www.tradingview.com/#signin")
wait=WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Email']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='username']"))).send_keys(longInfo[0])
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='password']"))).send_keys(longInfo[1])
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(., 'Sign in')]]"))).click()
```