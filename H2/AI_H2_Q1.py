from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image
import numpy
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
	x=int(imRGB.size/imRGB[0].size)
	y=int(imRGB[0].size/imRGB[0][0].size)
	print(x)
	print(y)
	print(imRGB[99][99])
	for i in range(0,x):
		for j in range(0,y):
			pixel=imRGB[i][j]
			pixel=numpy.array(pixel)
			if abs(pixel[0]-pixel[1])<30 and abs(pixel[1]-pixel[2])<30 and abs(pixel[0]-pixel[2])<30:
				pass
			else:
				imRGB[i][j]=(255,255,255)
	outputImage = Image.fromarray(imRGB)
	return outputImage

taggedImage=fetchNastaliq()
image=remove_tag(taggedImage)
image.show()