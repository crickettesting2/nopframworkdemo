from selenium import webdriver
import pytest

@pytest.fixture()  # fixture method
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser=="firefox":
        driver = webdriver.Firefox()
        print("launching firefox browser")
    else:
        driver=webdriver.Ie()  # eventhough no browser is menttioned test case shouldn't fail, setting IE as default
        print("launching IE browser")
    return driver


def pytest_addoption(parser):   # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # this will return the browser value to setup method
    return request.config.getoption("--browser")

# pytest HTML reports ###

# It is hook for adding environment in to html report, also can add multiple details as requirement in report
def pytest_configure(config):
    config._metadata['Project Name']="NOP commerce"
    config._metadata['Module Name']="customers"
    config._metadata['Tester']="Manu"

# It is hook for delete/modify environment in to html report (to remove some unwanted default data from report)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)