import time
import urllib.request

from selenium.webdriver.common.by import By
from math import sin, cos, pi 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

t = 0
while(t <= 1):
    a = -0.5 + 1*sin(2*pi*t)
    b = 1*cos(2*pi*t)
    url = 'https://www.wolframalpha.com/input?i2d=true&i=StreamDensityPlot%5C%2891%29%7Bx%5C%2840%29y-' + str(toFixed(a,2)) + '*x%5C%2841%29%2C+y%5C%2840%29' + str(toFixed(b,2)) + '%2Bx%2By%5C%2841%29%7D%5C%2844%29+%7Bx%2C+-3%2C+3%7D%5C%2844%29+%7By%2C+-3%2C+3%7D%5C%2893%29'
    browser.get(url)
    time.sleep(20)
    element = browser.find_element(by=By.TAG_NAME, value="[alt='Result']")
    image_url = element.get_attribute("src")
    urllib.request.urlretrieve(image_url, 'results/'+str(toFixed(t,2))+'.jpg')
    print(t)
    t += 0.01
