from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

class AddCustomer:
    lnk_customer_main_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    lnk_Customer_submenu_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    btn_add_new_xpath="//a[@class='btn bg-blue']"

    txt_email_xpath="//input[@id='Email']"
    txt_password_xpath="//input[@id='Password']"
    txt_firstname_xpath="//input[@id='FirstName']"
    txt_lastname_xpath="//input[@id='LastName']"

    btn_male_xpath="//input[@id='Gender_Male']"
    btn_female_xpath="//input[@id='Gender_Female']"

    txt_DOB_xpath="//input[@id='DateOfBirth']"
    txt_companyname_xpath="//input[@id='Company']"

    chk_taxexempt_xpath="//input[@id='IsTaxExempt']"

    txt_newsletter_xpath='//*[@id="customer-info"]/div[2]/div[1]/div[9]/div[2]/div/div[1]/div'
    lst_storename_xpath="//li[contains(text(),'Your store name')]"
    lst_teststore_xpath="//li[contains(text(),'Test store 2')]"

    txt_customers_roles_xpath="//div[10]//div[2]//div[1]//div[1]//div[1]"
    lst_admin_xpath="//li[contains(text(),'Administrators')]"
    lst_forum_moderators_xpath="//li[contains(text(),'Forum Moderators')]"
    lst_guest_xpath="//li[contains(text(),'Guests')]"
    lst_registered_xpath="//li[contains(text(),'Registered')]"
    lst_vendors_xpath="//li[contains(text(),'Vendors')]"

    drp_managerof_vendor_xpath="//select[@id='VendorId']"

    chk_active_xpath="//input[@id='Active']"
    txt_admin_comment_xpath="//textarea[@id='AdminComment']"

    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickoncustomersmain(self):
        self.driver.find_element_by_xpath(self.lnk_customer_main_xpath).click()

    def clickoncustomersub(self):
        self.driver.find_element_by_xpath(self.lnk_Customer_submenu_xpath).click()

    def addnew(self):
        self.driver.find_element_by_xpath(self.btn_add_new_xpath).click()
        
    def email(self,email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def password(self,password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def firstname(self,firstname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(firstname)

    def lastname(self,lastname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lastname)

    def genderset(self,gender):
        if gender=="male":
            self.driver.find_element_by_xpath(self.btn_male_xpath).click()
        elif gender=="female":
            self.driver.find_element_by_xpath(self.btn_female_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.btn_male_xpath).click()

    def DOB(self,dob):
        self.driver.find_element_by_xpath(self.txt_DOB_xpath).send_keys(dob)

    def companyname(self,compname):
        self.driver.find_element_by_xpath(self.txt_companyname_xpath).send_keys(compname)

    def tax_exempt(self):
        self.driver.find_element_by_xpath(self.chk_taxexempt_xpath).click()

    def news_letter(self,value):
        self.driver.find_element_by_xpath(self.txt_newsletter_xpath).click()
        if value=="Your store name":
            self.driver.find_element_by_xpath(self.lst_storename_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.lst_teststore_xpath).click()


# while creating a user under customer roles by default Registered will be selected, so we need to remove registered first
# Also The customer cannot be in both 'Guests' and 'Registered' customer roles

    def customerroles(self,role):
        self.driver.find_element_by_xpath(self.txt_customers_roles_xpath).click()

        if role=="Registered":
            self.list_item=self.driver.find_element_by_xpath(self.lst_registered_xpath)

        elif role=="Administrator":
            self.list_item=self.driver.find_element_by_xpath(self.lst_admin_xpath)

        elif role=="moderators":
            self.list_item=self.driver.find_element_by_xpath(self.lst_forum_moderators_xpath)

        elif role == "Vendors":
            self.list_item=self.driver.find_element_by_xpath(self.lst_vendors_xpath)

        elif role == "Guests":
            self.driver.find_element_by_xpath("//li[@class='k-button']//span[@class='k-select']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath(self.txt_customers_roles_xpath).click()
            self.list_item=self.driver.find_element_by_xpath(self.lst_guest_xpath)

        else:
            self.list_item=self.driver.find_element_by_xpath(self.lst_guest_xpath)
            time.sleep(3)
        self.list_item.click()#this click won't work here, and in some cases click won't work .so we use java script

        #self.driver.execute_script("arguements[0].click();", self.list_item)

    def manage_vendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drp_managerof_vendor_xpath))
        drp.select_by_visible_text(value)

    def check_active(self):
        self.driver.find_element_by_xpath(self.chk_active_xpath).click()

    def admin_comment(self,value):
        self.driver.find_element_by_xpath(self.txt_admin_comment_xpath).send_keys(value)

    def save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
