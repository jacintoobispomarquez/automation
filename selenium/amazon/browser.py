from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj= Service("../geckodriver/geckodriver")
#driver = webdriver.Firefox(service=service_obj)

#service_obj= Service("../edge/msedgedriver")
#driver = webdriver.Edge(service=service_obj)

service_obj= Service("../chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.amazon.es/")
print(driver.title)
print(driver.current_url)
driver.close()
