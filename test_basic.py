#import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test1():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    try:
      driver.quit()
    except Exception as e:
       print(e)

    assert True