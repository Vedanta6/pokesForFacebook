To launch the program you need to have/install: 

    - Python 3
    - selenium (pip install selenium)
    - chromedriver (https://sites.google.com/a/chromium.org/chromedriver/)
    - Google Chrome

Preparations:
1. Enter your own login and password of your facebook account in config.py:

          SITE_USERNAME = '[enter your email]'
          SITE_PASSWORD = '[enter your password]'
          
2. Replace the path to chromedriver.exe in line 15 connect_selenium.py:

          browser = webdriver.Chrome('[enter your path]\chromedriver.exe', chrome_options=options)
    
Enjoy the process ;)
