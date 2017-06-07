from bs4 import BeautifulSoup
from selenium import webdriver
import os

class HackerEarth:
	
	path = "@hackerEarth_"
	userName = ""

	def setPath(self,dirPath,userName):

		self.userName = userName

		self.path = os.path.join(dirPath,self.path)

		self.path = self.path+userName
		
		if not os.path.exists(self.path):
			os.mkdir(self.path)


	def accessUserProfile(self,driver):

		driver.get('https://www.hackerearth.com//@'+self.userName)
		
		driver.save_screenshot(os.path.join(self.path,'profile.png') )
		
		driver.get('https://www.hackerearth.com/@'+self.userName+'/activity/hackerearth/#user-rating-graph')

		driver.save_screenshot(os.path.join(self.path,'rating.png') )

		self.soup = BeautifulSoup( driver.page_source , 'lxml')


	def problemData(self):
		findDiv = self.soup.find('div',{'class':'profile-overview medium-margin'})
		self.problemDetails = [item.string for item in findDiv.thead.tr if item.string!="\n"]
		self.problemStatus  = [item.string for item in findDiv.tbody.tr if item.string!="\n"]


	def psCount(self):
		return int(self.problemStatus[0])

	def ssCount(self):
		return int(self.problemStatus[1])

	def saCount(self):
		return int(self.problemStatus[2])
		
	def waCount(self):
		return int(self.problemStatus[3])				

	def ceCount(self):
		return int(self.problemStatus[4])
	
	def reCount(self):
		return int(self.problemStatus[5])		

	def tleCount(self):
		return int(self.problemStatus[6])	

		
	def problemStatus(self):
		return self.problemStatus


	def getHackEPath(self):
		return self.path