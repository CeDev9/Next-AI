SCROLL_PAUSE_TIME = 2
from selenium import webdriver
# Get scroll height
import time
driver = webdriver.Firefox()
driver.get('https://www.ycombinator.com/companies')
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

posts = driver.find_elements_by_css_selector("a.no-hovercard [href]")
cont = ""
for block in posts:
    print(block.get_attribute('href'))
    cont = cont + block.get_attribute('href') + "\n"
with open("links.txt", "w") as f:
    f.write(cont)
