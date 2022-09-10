from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image, ImageOps
import io
import time

time_string = time.strftime("%Y%m%d-%H%M%S")
stock_ticker = "WEAT"
file_name = f"StockChart_{stock_ticker}_{time_string}.png"

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)
browser.get("https://stockcharts.com/")
browser.find_element(By.CSS_SELECTOR, "#nav-chartSearch-input").send_keys(stock_ticker + Keys.ENTER)
time.sleep(2)
Select(browser.find_element(By.CSS_SELECTOR, "#overType_0")).select_by_value("BB")
browser.find_element(By.CSS_SELECTOR, "#overArgs_0").clear()
browser.find_element(By.CSS_SELECTOR, "#overArgs_0").send_keys("20,1")
Select(browser.find_element(By.CSS_SELECTOR, "#overType_1")).select_by_value("BB")
Select(browser.find_element(By.CSS_SELECTOR, "#overType_2")).select_by_value("SAR")

Select(browser.find_element(By.CSS_SELECTOR, "#indType_0")).select_by_value("RSI")
Select(browser.find_element(By.CSS_SELECTOR, "#indType_1")).select_by_value("MACD")
Select(browser.find_element(By.CSS_SELECTOR, "#indType_2")).select_by_value("CCI")

browser.execute_script("submitIt();")

time.sleep(2)

stock_chart = ImageOps.invert(Image.open(io.BytesIO(browser.find_element(By.CSS_SELECTOR, "#chartImg").screenshot_as_png)).convert("RGB"))

browser.close()

stock_chart.show()