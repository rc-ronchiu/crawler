import os
import urllib.request as req
import bs4

url = str(input('URL: '))

def getRawData(url):
	request = req.Request(url, headers = {"User-Agent":"Mozilla"})
	with req.urlopen(request) as response:
		rawData = response.read().decode("utf-8")
	return rawData

data = bs4.BeautifulSoup(getRawData(url), "html.parser")
imgs = data.find_all('img')
links = []

for img in imgs:
	link = img.get('src')
	if 'http://' not in link:
		link = url + link
	links.append(link)

print("Number of images: " + str(len(links)))

for i in range(len(links)):
	filename = '{}.png'.format(link[i])
	fullfilename = os.path.join("/home/parallels/Desktop/crawler/", filename)
	req.urlretrieve(links[i], fullfilename)       
