from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj= Service("../geckodriver/geckodriver")
#driver = webdriver.Firefox(service=service_obj)

#service_obj= Service("../edge/msedgedriver")
#driver = webdriver.Edge(service=service_obj)

service_obj = Service("../chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://www.amazon.es/")

#Search guitars
driver.find_element(By.ID, "sp-cc-accept").click()
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Gibson SG")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

# above 500 Euros
driver.find_element(By.XPATH, "//li[@id='p_36/2493687031']//a[@class='a-link-normal s-navigation-item']").click()

# find prices
prices = driver.find_elements(By.CSS_SELECTOR, ".a-price-whole")

elements = 0
correct_prices = True
for price in prices:
    elements = elements + 1
    if(int(float(price.text.replace(",", ".")))*1.1) < 500:
        correct_prices=False
    print(price.text)

assert elements > 0
assert correct_prices

#driver.close()
