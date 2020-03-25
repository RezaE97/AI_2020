from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image


def fetch_nastaliq(text='شکستنی'):

    driver = webdriver.Chrome()
    driver.get('http://nastaliqonline.ir/')

    selectSize = Select(driver.find_element_by_id('xcolor1'))
    selectSize.select_by_visible_text('50')
    selectFont = Select(driver.find_element_by_name('coli'))
    selectFont.select_by_value('0')  # 0 is Regular Nastaliq
    driver.find_element_by_name('shadow').click()

    inputElement = driver.find_element_by_id('matn')
    inputElement.send_keys(Keys.CONTROL, 'a')
    inputElement.send_keys(Keys.DELETE)
    inputElement.send_keys(text)

    driver.find_element_by_id('generateit').click()

    imageName = 'temp.png'
    driver.save_screenshot(imageName)
    driver.close()
    image = Image.open(imageName)

    return image

fetch_nastaliq()