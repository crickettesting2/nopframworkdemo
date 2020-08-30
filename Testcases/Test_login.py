import pytest
from selenium import webdriver
from pageObjects.Loginpage import login
from utilities.readProperties import readconfig
from utilities.customLogger import loggen

class Test_01_Login:
    baseURL=readconfig.getapplicationURL()
    username=readconfig.getUsername()
    password=readconfig.getpassword()
    logger=loggen.log()  # calling log method from customLogger

    @pytest.mark.regression

    def test_hompage_title(self,setup):
        self.logger.info("*******Test_01_Login**************")
        self.logger.info("*******verifying home page**************")
        self.driver= setup
        self.driver.get(self.baseURL)
        #self.driver.maximize_window()
        title=self.driver.title

        if title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*******verifying home page passed**************")
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_hompage_title.png')
            self.driver.close()
            self.logger.info("*******verifying home pag Failede**************")
            assert False

    @pytest.mark.sanity

    def test_login(self,setup):
        self.logger.info("*******verifying login test**************")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        title=self.driver.title
        if title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******Login test is passes**************")
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_login.png') # here instead of giving complete path add . (dot) current project\\folder name
            self.logger.error("*******Login test is failed**************")
            self.driver.close()
            assert False