# https://sites.google.com/a/chromium.org/chromedriver/getting-started
from selenium import webdriver

driver = webdriver.Chrome('/Users/moonmayor/Third/bin/chromedriver')
driver.get('http://5tephen.com')
links = driver.find_elements_by_tag_name('a')
links[1].click()

driver.quit()
