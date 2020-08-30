import pytest
import time
from selenium import webdriver
from pageObjects.Loginpage import login
from pageObjects.Addcustomer import AddCustomer
from utilities.readProperties import readconfig
from utilities.customLogger import loggen
import string
import random

class Test_03_AddCustomer:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getUsername()
    password = readconfig.getpassword()
    logger = loggen.log()  # calling log method from customLogger

    @pytest.mark.sanity

    def test_addcustomer(self,setup):
        self.logger.info("*******Test_03_Login**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("*******Login successfull**************")

        self.logger.info("*******Starting add customer test**************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickoncustomersmain()
        self.addcust.clickoncustomersub()

        self.addcust.addnew()

        self.logger.info("*******providing customer details**************")

        self.email=random_generator() + "@gmail.com"
        self.addcust.email(self.email)
        self.addcust.password("test123")
        self.addcust.firstname("QA")
        self.addcust.lastname("Tester")
        self.addcust.genderset("male")
        self.addcust.DOB("01/01/1995")
        self.addcust.companyname("TEST")
        self.addcust.tax_exempt()
        self.addcust.news_letter("test")
        self.addcust.customerroles("moderators")
        self.addcust.manage_vendor("Vendor 2")
        self.addcust.admin_comment("this is for testing purpose")
        self.addcust.save()

        self.logger.info("saving customer info")

        self.logger.info("validating customer info")


        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_add_customer.png') # here instead of giving complete path add . (dot) current project\\folder name
            self.logger.info("**Add customer test failed")
            assert True == False

        self.driver.close()
        self.logger.info("****Testing completed")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))




