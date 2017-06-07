from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from PIL import Image
import hackerearth as hackE
import codechef as codeC
import codeforces as codeF
import hackerrank as hackR
import htmlcopy



class Driver:

        phantomPath = "/usr/bin/bin/phantomjs"

        def __init__(self):
                self.driver = webdriver.PhantomJS(self.phantomPath)



class UserData:
        path                               = ""
        userName                           = ""
        hackerEarthUserName    = ""
        hackerRankUserName     = ""
        codeChefUserName       = ""
        codeForcesUserName     = "" 

        totalProblemSolved     = 0
        totalProblemSubmitted  = 0
        totalWrongAnswer       = 0
        totalTimeLimitExceed   = 0
        totalRuntimeError      = 0
        totalCompilationError  = 0

        def __init__(self):
                print("Enter user name for different platforms (enter * if no user name)\n")
                self.userName = input("Enter user name for folder\t:")
                self.hackerEarthUserName = input("Enter HackerEarth user name\t:")
                self.hackerRankUserName = input("Enter HackerRank user name\t:")
                self.codeChefUserName = input("Enter CodeCehf user name\t:")
                self.codeForcesUserName = input("Enter CodeForces user name\t:")

        def showUserData(self):
                print("\n\n"+"--"*35)
                print("\t\t\t\t\t\tUser Information\n"+"--"*35)
                print("HackerEarth user name : ",self.hackerEarthUserName,"\n")
                print("HackerRank  user name : ",self.hackerRankUserName,"\n")
                print("CodeChef    user name : ",self.codeChefUserName,"\n")
                print("CodeForces  user name : ",self.codeForcesUserName,"\n")

        def userDir(self):
                
                self.path = os.getcwd()

                self.path = os.path.join(self.path,self.userName)

                if not os.path.exists(self.path):
                        os.mkdir(self.path)     

        
        def buildHeadHTML(self,htmlObj):

                htmlObj.p('Hackerearth username :&nbsp;&nbsp;&nbsp;'+self.hackerEarthUserName,'rgb(50,55,84)','WHITE')
                htmlObj.p('Hackerank   username :&nbsp;&nbsp;&nbsp;'+self.hackerRankUserName,'rgb(50,55,84)','WHITE')
                htmlObj.p('Codechef    username :&nbsp;&nbsp;&nbsp;'+self.codeChefUserName,'rgb(50,55,84)','WHITE')
                htmlObj.p('Codeforces  username :&nbsp;&nbsp;&nbsp;'+self.codeForcesUserName,'rgb(50,55,84)','WHITE')
                
                htmlObj.p('<br/><br/>HackerEarth + CodeChef','rgb(50,55,84)','white')
                theadDataList = ['Total Problem Solved','Total Problem Submitted','Total Wrong Answer','Total Time Limit Exceeded','Total Runtime Error','Total Compilation Error']
                tbodyDataList = [[str(self.totalProblemSolved),str(self.totalProblemSubmitted),str(self.totalWrongAnswer),str(self.totalTimeLimitExceed),str(self.totalRuntimeError),str(self.totalCompilationError)]]
                rowCount = 1
                
                # n row count - keep height n * 100 

                htmlObj.table(theadDataList,tbodyDataList,rowCount,'white','rgb(50,55,84)',100)



        def buildHEHTML(self,htmlObj,path,hackerEObj,userName):

                htmlObj.h('hackerearth profile ('+userName+')','WHITE','rgb(50,55,84)')
                htmlObj.img(os.path.join(path,'profile.png'))
                htmlObj.h('hackerearth ratings ('+userName+')','WHITE','rgb(50,55,84)')
                htmlObj.img(os.path.join(path,'rating.png'))
                

        def buildCCHTML(self,htmlObj,path,codeCObj,userName):

                htmlObj.h('codechef profile ('+userName+')','WHITE','rgb(110,57,26)')
                htmlObj.img(os.path.join(path,'profile.png'))           


        def buildCFHTML(self,htmlObj,path,codeFObj,userName):

                htmlObj.h('codeforces profile ('+userName+')','WHITE','rgb(102,124,175)')
                htmlObj.img(os.path.join(path,'profile.png'))           
        

        def buildHRHTML(self,htmlObj,path,hackerRObj,userName):

                htmlObj.h('hackerrank profile ('+userName+')','WHITE','rgb(46,200,102)')
                htmlObj.img(os.path.join(path,'profile.png'))



if __name__ == '__main__':
        
        driverObj    = Driver()
        userDataObj  = UserData() 
        htmlObj      = htmlcopy.HTML()
        hackerEObj = hackE.HackerEarth()
        hackerRObj = hackR.HackerRank()
        codeCObj = codeC.CodeChef()
        codeFObj = codeF.CodeForces()


        userDataObj.userDir()
        htmlObj.setPath(userDataObj.path)


        if userDataObj.hackerEarthUserName != '*':
            print('\n\nParsing Hackerearth.....: Wait')
            hackerEObj.setPath(userDataObj.path,userDataObj.hackerEarthUserName)
            hackerEpath = hackerEObj.getHackEPath()
            hackerEObj.accessUserProfile(driverObj.driver)
            hackerEObj.problemData()
            userDataObj.totalProblemSolved    += hackerEObj.psCount()
            userDataObj.totalProblemSubmitted += hackerEObj.ssCount()
            userDataObj.totalWrongAnswer      += hackerEObj.waCount()
            userDataObj.totalTimeLimitExceed  += hackerEObj.tleCount()
            userDataObj.totalRuntimeError     += hackerEObj.reCount()
            userDataObj.totalCompilationError += hackerEObj.ceCount()
            print('Parsing Hackerearth.....: Done\n')


        if userDataObj.codeChefUserName != '*':
                print('Parsing Codechef.....: Wait')
                codeCObj.setPath(userDataObj.path,userDataObj.codeChefUserName)
                codeCpath = codeCObj.getCodeCPath()
                codeCObj.accessUserProfile(driverObj.driver)
                codeCObj.problemData()
                userDataObj.totalProblemSolved    += codeCObj.psCount()
                userDataObj.totalProblemSubmitted += codeCObj.ssCount()
                userDataObj.totalWrongAnswer      += codeCObj.waCount()
                userDataObj.totalTimeLimitExceed  += codeCObj.tleCount()
                userDataObj.totalRuntimeError     += codeCObj.reCount()
                userDataObj.totalCompilationError += codeCObj.ceCount()
                print('Parsing Codechef.....: Done\n')


        if userDataObj.codeForcesUserName != '*':
                print('Parsing Codeforces.....: Wait')
                codeFObj.setPath(userDataObj.path,userDataObj.codeForcesUserName)
                codeFpath = codeFObj.getCodeFPath()
                codeFObj.accessUserProfile(driverObj.driver)
                print('Parsing Codeforces.....: Done\n')


        if userDataObj.hackerRankUserName != '*':
                print('Parsing Hackerrank.....: Wait')
                hackerRObj.setPath(userDataObj.path,userDataObj.hackerRankUserName)
                hackerRpath = hackerRObj.getHackRPath()
                hackerRObj.accessUserProfile(driverObj.driver)              
                print('Parsing Hackerearth.....: Done\n')

        

        userDataObj.buildHeadHTML(htmlObj)


        if userDataObj.hackerEarthUserName != '*':
              userDataObj.buildHEHTML(htmlObj,hackerEpath,hackerEObj,userDataObj.hackerEarthUserName)

        if userDataObj.codeChefUserName != '*':
              userDataObj.buildCCHTML(htmlObj,codeCpath,codeCObj,userDataObj.codeChefUserName)        

        if userDataObj.codeForcesUserName != '*':
              userDataObj.buildCFHTML(htmlObj,codeFpath,codeFObj,userDataObj.codeForcesUserName)        

        if userDataObj.hackerRankUserName != '*':
              userDataObj.buildHRHTML(htmlObj,hackerRpath,hackerRObj,userDataObj.hackerRankUserName)

        htmlObj.makeFile()

        print("\nOpen "+userDataObj.userName+"/codeinfo.html to see details.")