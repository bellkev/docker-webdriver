from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.alert import Alert


driver = webdriver.Remote(
    desired_capabilities=DesiredCapabilities.CHROME,
    command_executor="http://localhost:4444"
)
driver.get('http://nginx:8000')
alert = Alert(driver)
print alert.text
assert 'Hello' in alert.text
alert.accept()
driver.get_screenshot_as_file('screenshot.png')
driver.quit()
