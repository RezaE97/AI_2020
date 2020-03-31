from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image
import numpy
import os


def fetchNastaliq(text='شکستنی'):

    driver = webdriver.Firefox()
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

    imageElement=driver.find_element_by_xpath("//img[1]")
    size=imageElement.size
    location = imageElement.location
    driver.save_screenshot("pageImage.png")
    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']
    im = Image.open('pageImage.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    image=im
    driver.close()
    return image


def remove_tag(inputImage):
    imRGB=numpy.array(inputImage.convert('RGB'))
    red, green, blue=imRGB.T
    redArea = (red>= 36) & (green>=3) & (blue>=3)
    imRGB[..., :3][redArea.T] = (255, 255, 255)
    outputImage = Image.fromarray(imRGB)
    return outputImage

currentPath = os.path.dirname(os.path.realpath(__file__))

taggedImage=fetchNastaliq()
image=remove_tag(taggedImage)
image.save(os.path.join(currentPath, "output.png"))
image.show()
