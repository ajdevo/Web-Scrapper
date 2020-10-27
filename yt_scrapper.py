from selenium import webdriver   #Used to open browser 
import time
import requests
import urllib
from bs4 import BeautifulSoup
import datetime


#Open the YT community page to get DOM of that page.

driver = webdriver.Firefox()                     
url="https://www.youtube.com/c/mensxp/community"

driver.maximize_window()
driver.get(url)

time.sleep(5)

#Using beutifulSoup module creating HTML to DOM
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
results = soup.find(id="post")

#Creat time variable only to name the image using it.
localtime = time.asctime( time.localtime(time.time()) )

#Finds our desired post in DOM
post_elem = results.find('yt-img-shadow', class_="style-scope ytd-backstage-image-renderer no-transition")
image_elem = post_elem.find('img', class_='style-scope yt-img-shadow')

#Getting post's image source url 
link = image_elem['src']

#Downloading the image
urllib.urlretrieve(link,"{}.jpg".format(localtime))

driver.quit()
