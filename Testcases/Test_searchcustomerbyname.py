import time
import pytest
from pageObjects.Loginpage import login
from pageObjects.Addcustomer import AddCustomer
from pageObjects.SearchCustomer import Searchcustomer
from utilities.customLogger import loggen
from utilities.readProperties import readconfig


class Test_searchcustomerbyname005:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getUsername()
    password = readconfig.getpassword()
    logger = loggen.log()

    @pytest.mark.regression

    def test_searchcustomerbyname(self, setup):
        self.logger.info("***Test_searchcustomerbyname005 starting*")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("*******Login successfull**************")

        self.logger.info("*******Starting search customer**************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickoncustomersmain()
        self.addcust.clickoncustomersub()

        self.logger.info("*******Searching  customer by name**************")
        searchcust = Searchcustomer(self.driver)
        searchcust.frisrname("John")
        searchcust.lastname("Smith")
        searchcust.search()
        time.sleep(3)
        status = searchcust.searchCustomerbyname("John Smith")
        assert True == status
        self.logger.info("*** Test_searchcustomerbyemail004 finihed*****")

        self.driver.close()

