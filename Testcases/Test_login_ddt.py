import pytest
from selenium import webdriver
from pageObjects.Loginpage import login
from utilities.readProperties import readconfig
from utilities.customLogger import loggen
from utilities import ExcelUtils  # import excel actions
import time

class Test_02__ddt_Login:       # Add test case id
    baseURL=readconfig.getapplicationURL()
    path=".//TestData/logintestdata.xlsx"   # give excel path
    logger=loggen.log()  # calling log method from customLogger

    @pytest.mark.regression
    @pytest.mark.sanity


    def test_login_ddt(self,setup):
        self.logger.info("*********Test_02__ddt_Login********")
        self.logger.info("*******verifying login ddt test**************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=login(self.driver)

        self.rows=ExcelUtils.getRowcount(self.path,'Sheet1')
        print("Number of rows in the excel", self.rows)

        list_results=[] # empty list

        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readData(self.path,'Sheet1',r,1) # read user name from excel
            self.password=ExcelUtils.readData(self.path,'Sheet1',r,2) # read password  from excel
            self.expected=ExcelUtils.readData(self.path,'Sheet1',r,3) # read expected pass/fail  from excel

            self.lp.setUserName(self.user) # get user name
            self.lp.setPassword(self.password) # get password
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            expect_title="Dashboard / nopCommerce administration"

            if act_title == expect_title:
                if self.expected=='Pass':
                    self.logger.info("*** passed**")
                    self.lp.clicklogout()
                    list_results.append("Pass")
                elif self.expected=="Fail":
                    self.logger.info("*** Failed**")
                    self.lp.clicklogout()
                    list_results.append("Fail")

            elif act_title != expect_title:
                if self.expected == 'Pass':
                    self.logger.info("*** failed**")
                    list_results.append("fail")
                elif self.expected == "Fail":
                    self.logger.info("*** passed**")
                    list_results.append("pass")

        if "fail" not in list_results:
            self.logger.info("Login DDT is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Log  in DDT is failed")
            self.driver.close()
            assert False

        self.logger.info("*******End of Login DDT********* ")
        self.logger.info("********Completed Test_02__ddt_Login*******")
















