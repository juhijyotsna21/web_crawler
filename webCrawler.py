import requests
from bs4 import BeautifulSoup
class webcrawler:
	def __init__(self,base_url,depth):
		self.base_url=base_url
		self.depth=depth
		self.html_data=None
		self.image_dict={}
		self.link_list=[]

	def url_fetch(self):
		data=requests.get(self.base_url)
		if data.status_code==200:
			return data.content
		else:
			return False

	def parsing_data(self):
		self.html_data=BeautifulSoup(self.url_fetch(),'html.parser')
		for url in self.html_data.find_all('a'):
			# print url.get('href')
			self.link_list.append(url.get('href'))
		self.image_dict[self.base_url]=[]
		for img in self.html_data.find_all('img'):
			print img
			self.image_dict[self.base_url].append(img.get('src'))

	def bfs_fetch(self):
		if self.url_fetch() != False:
			self.parsing_data()
		if len(self.link_list)!=0:
			for link in range(self.depth):
				self.base_url=self.base_url+self.link_list[0]
				self.parsing_data()
			return self.image_dict
		else:
			return "No Links Available"

ob=webcrawler(r'https://yourstory.com/',4)
print ob.bfs_fetch()

		
