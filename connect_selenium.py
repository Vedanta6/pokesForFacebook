##
# Required installations:
#    - selenium (pip install selenium)
#    - chromedriver (https://sites.google.com/a/chromium.org/chromedriver/)
##

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, ElementNotSelectableException, ElementNotVisibleException, \
    InvalidElementStateException, ElementNotInteractableException, NoSuchElementException, \
    StaleElementReferenceException, TimeoutException
import time
import config

element_exceptions = (WebDriverException, ElementNotSelectableException, ElementNotVisibleException,
                      InvalidElementStateException, ElementNotInteractableException, NoSuchElementException,
                      StaleElementReferenceException, TimeoutException)

# browser init
options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome(config.CHROME_DRIVER, chrome_options=options)

browser.get('https://www.facebook.com')
time.sleep(2)

# user credentials
user = browser.find_element_by_css_selector('#email')
user.send_keys(config.SITE_USERNAME)
password = browser.find_element_by_css_selector('#pass')
password.send_keys(config.SITE_PASSWORD)

# log in
login = browser.find_element_by_id("loginbutton").click()

# pokes page
browser.get('https://www.facebook.com/pokes')

while 1:
        try:
        if browser.current_url == 'https://www.facebook.com/pokes':
            if not browser.find_element_by_link_text("Poke back").is_selected():
                browser.find_element_by_link_text("Poke back").click()
        else:
            browser.get('https://www.facebook.com/pokes')
    except element_exceptions:
        pass
    except (KeyboardInterrupt, SystemExit, WebDriverException):
        break
