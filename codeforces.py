from bs4 import BeautifulSoup
from selenium import webdriver
import os

class CodeForces:
	
	path = "@codeForces_"
	userName = ""

	def setPath(self,dirPath,userName):

		self.userName = userName

		self.path = os.path.join(dirPath,self.path)

		self.path = self.path+userName
		
		if not os.path.exists(self.path):
			os.mkdir(self.path)


	def accessUserProfile(self,driver):

		driver.get('http://codeforces.com/profile/'+self.userName)
		
		driver.save_screenshot(os.path.join(self.path,'profile.png') )

	def getCodeFPath(self):
		return self.path