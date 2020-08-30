class Searchcustomer:
    txt_email_id="SearchEmail"
    txt_firstname_id="SearchFirstName"
    txt_lastname_id="SearchLastName"
    btn_search_id="search-customers"

    tble_xpath="//table[@id='customers-grid']"  # inspect from <table class
    tble_Rows_search_path="//table[@id='customers-grid']//tbody/tr"# after <table class, inspect from <tbody xpath and add /tr at the end
    tble_columns_search_path ="//table[@id='customers-grid']//tbody/tr/td"# add/td at the end

    def __init__(self,driver):
        self.driver=driver

    def email(self,email):
        self.driver.find_element_by_id(self.txt_email_id).clear()
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def frisrname(self,firstname):
        self.driver.find_element_by_id(self.txt_firstname_id).clear()
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(firstname)

    def lastname(self,lastname):
        self.driver.find_element_by_id(self.txt_lastname_id).clear()
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lastname)

    def search(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def getNoofRows(self):
        return len(self.driver.find_elements_by_xpath(self.tble_Rows_search_path))

    def getNoofcolumns(self):
        return len(self.driver.find_elements_by_xpath(self.tble_columns_search_path))

    def searchCustomerByemail(self,email):
        flag=False
        for r in  range(1,self.getNoofRows()+1):
            table=self.driver.find_element_by_xpath(self.tble_xpath)
            emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerbyname(self,Name):
        flag=False
        for r in  range(1,self.getNoofRows()+1):
            table=self.driver.find_element_by_xpath(self.tble_xpath)
            name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==Name:
                flag=True
                break
        return flag


