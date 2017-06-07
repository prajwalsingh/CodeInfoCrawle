from bs4 import BeautifulSoup
from selenium import webdriver
import os

class CodeChef:
	
	path = "@codeChef_"
	userName = ""

	def setPath(self,dirPath,userName):

		self.userName = userName

		self.path = os.path.join(dirPath,self.path)

		self.path = self.path+userName
		
		if not os.path.exists(self.path):
			os.mkdir(self.path)


	def accessUserProfile(self,driver):

		driver.get('https://www.codechef.com/users/'+self.userName)
		
		driver.save_screenshot(os.path.join(self.path,'profile.png') )

		self.soup = BeautifulSoup( driver.page_source , 'lxml')

	def problemData(self):
		self.problemDetails = ['solutions_partially_accepted','compile_error','runtime_error','time_limit_exceeded','wrong_answers','solutions_accepted']
		self.problemStatus = []
		findG = self.soup.find('div',{'id':'submissions-graph'})
		for item in findG.find_all('g'):
			if item != None:
				for childItem in item.findChildren():
					if childItem.string != None and len(self.problemStatus)<6 and (childItem.string not in self.problemStatus) :
						self.problemStatus.append(childItem.string)


	def psCount(self):
		return int(self.problemStatus[0])+int(self.problemStatus[5])

	def ssCount(self):
		sum = 0
		for i in self.problemStatus:
			sum += int(i)
		return sum	

	def saCount(self):
		return int(self.problemStatus[5])
		
	def waCount(self):
		return int(self.problemStatus[4])				

	def ceCount(self):
		return int(self.problemStatus[1])
	
	def reCount(self):
		return int(self.problemStatus[2])		

	def tleCount(self):
		return int(self.problemStatus[3])	

		
	def problemStatus(self):
		return self.problemStatus


	def getCodeCPath(self):
		return self.path