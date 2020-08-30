from selenium import webdriver

class login:
    textbox_email_id='Email'   # id for email field is 'Email'
    textbox_password_id ='Password' # id for password field is 'Password'
    button_login_xpath="//input[@class='button-1 login-button']"  # login button, taken xpath
    link_logiu_linktext='Logout'  # logout is a link text

    def __init__(self,driver): # create a constructor and this driver will pass from actual test case,and this driver will initate local driver
        self.driver=driver

    #Action methods
    def setUserName(self,username): # username will pass from actual test case
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self. button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self. link_logiu_linktext).click()
