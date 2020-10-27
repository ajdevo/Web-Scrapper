from selenium import webdriver
import time
import requests
import urllib
from bs4 import BeautifulSoup
import datetime


driver = webdriver.Firefox()
url="https://www.youtube.com/c/mensxp/community"
# url = "https://www.youtube.com/channel/UCnaOzPCUym-vNapCjV2p9Pg/community"   #GateAcademy
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
results = soup.find(id="post")


localtime = time.asctime( time.localtime(time.time()) )

post_elem = results.find('yt-img-shadow', class_="style-scope ytd-backstage-image-renderer no-transition")

image_elem = post_elem.find('img', class_='style-scope yt-img-shadow')
link = image_elem['src']
urllib.urlretrieve(link,"{}.jpg".format(localtime))

driver.quit()
