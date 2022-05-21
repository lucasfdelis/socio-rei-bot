from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://sociorei.com.br/')

time.sleep(10)

pop_up = driver.find_element_by_xpath(
    '/html/body/app-root/div/fengstlayout-header/header/div/span[2]/span').text

print(pop_up)
