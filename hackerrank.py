from bs4 import BeautifulSoup
from selenium import webdriver
import os

class HackerRank:
	
	path = "@hackerRank_"
	userName = ""

	def setPath(self,dirPath,userName):

		self.userName = userName

		self.path = os.path.join(dirPath,self.path)

		self.path = self.path+userName
		
		if not os.path.exists(self.path):
			os.mkdir(self.path)


	def accessUserProfile(self,driver):

		driver.get('https://www.hackerrank.com/'+self.userName)
		
		driver.save_screenshot(os.path.join(self.path,'profile.png') )


	def getHackRPath(self):
		return self.path	