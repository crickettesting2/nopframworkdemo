import configparser # defaul package
config=configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini') # object will read in file,\\Configurations\\config.ini path for ini file

class readconfig:
    @staticmethod
    def getapplicationURL():
        url= config.get('Common data','baseURL')
        return url

    @staticmethod
    def getUsername():
        email= config.get('Common data','username')
        return email

    @staticmethod
    def getpassword():
        password= config.get('Common data','password')
        return password