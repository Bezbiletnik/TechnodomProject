from selenium import webdriver # type: ignore
from time import sleep

PATH = "/home/bezbiletnik/chromedriver/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get(r"https://site.evrika.com/catalog/smartfony/c234")
driver.find_element_by_xpath(r'/html/body/div[4]/div/div[3]/button[1]').click()
sleep(5)
driver.quit()
