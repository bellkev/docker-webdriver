from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.alert import Alert


driver = webdriver.Remote(
    desired_capabilities=DesiredCapabilities.CHROME,
    command_executor="http://localhost:4444"
)
driver.get('http://nginx:8000')
alert_text = Alert(driver).text
print alert_text
assert 'Hello' in alert_text
driver.quit()
