
from selenium import webdriver   #Used to open browser 

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import requests
import urllib.request
from bs4 import BeautifulSoup
import datetime
from PIL import Image

try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain
    
#Installing packages
pipmain(['install','selenium'])
pipmain(['install','webdriver_manager'])
pipmain(['install','b4s'])
pipmain(['install','PIL'])

#import sys
#import subprocess

# implement pip3 as a subprocess:
#subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
#'selenium'])

# process output with an API in the subprocess module:
#reqs = subprocess.check_output([sys.executable, '-m', 'pip3',
#'freeze'])
#installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

#print(installed_packages)

#Open the YT community page to get DOM of that page.
ytcom=input('\n\n\nEnter youtube community name---\n\n')
#driver = webdriver.Chrome('/home/anuj/chromedriver')                     
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://www.youtube.com/c/%s/community"%ytcom

driver.maximize_window()
driver.get(url)

#time.sleep(5)

#Using beutifulSoup module creating HTML to DOM
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
results = soup.find(id="post")
driver.quit()
#Creat time variable only to name the image using it.
localtime = time.asctime( time.localtime(time.time()) )
im_name = "{}.jpg".format(ytcom+' '+localtime)

#Finds our desired post in DOM
post_elem = results.find('yt-img-shadow', class_="style-scope ytd-backstage-image-renderer no-transition")
image_elem = post_elem.find('img', class_='style-scope yt-img-shadow')

#Getting post's image source url 
link = image_elem['src']

#Downloading the image
urllib.request.urlretrieve(link,im_name)

#driver.quit()

image = Image.open(im_name)
image.show()
