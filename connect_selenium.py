'''
Required installations:
    - selenium (pip install selenium)
    - chromedriver (https://sites.google.com/a/chromium.org/chromedriver/)
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import config

# browser init
options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome('C:\Python34\Lib\site-packages\selenium\webdriver\chromedriver.exe', chrome_options=options)

browser.get('http://facebook.com')
time.sleep(2)

# user credentials
user = browser.find_element_by_css_selector('#email')
user.send_keys(config.SITE_USERNAME)
password = browser.find_element_by_css_selector('#pass')
password.send_keys(config.SITE_PASSWORD)

# log in
login = browser.find_element_by_id("loginbutton").click()

# pokes page
browser.get('http://facebook.com/pokes')

while(1):
    try:
        browser.find_element_by_link_text("Poke back").click()
        # time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        browser.close()
        break
    except Exception:
        pass
