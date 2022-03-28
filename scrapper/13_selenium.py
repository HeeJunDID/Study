from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("./chromedriver")
browser.get("https://developers.google.com/maps/documentation/geocoding/overview")
elem = browser.find_element_by_id("query-input")
elem.send_keys