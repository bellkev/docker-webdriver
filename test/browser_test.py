from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
    desired_capabilities=DesiredCapabilities.CHROME,
    command_executor="http://localhost:4444"
)
driver.get('http://nginx:8000')
print driver.page_source
assert 'Hello' in driver.page_source
driver.quit()
