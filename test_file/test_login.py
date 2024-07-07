import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PycharmProjects.pythonProject.automation_project.pages import login_page

class Test_drive:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
        print("Test Successfully Completed")
    def test_booting(self,driver):
        self.driver.get(self.url)
        assert self.driver.title=="OrangeHRM"
        print("login successfully")
    def pass_reset(self,driver):
        driver.get(self.url)
        self.driver.find_element(by=By.XPATH,value=login_page.Selectors.forget_password_xpath).click()
        self.driver.find_element(by=By.XPATH,value=login_page.Selectors.user_path).send_keys(login_page.Pabitha_data.username_1).submit()
        print("Password Reset successfully")
    def login_page(self,driver):
        driver.get(self.url)
        self.driver.find_element(by=By.XPATH,value=login_page.Selectors.username_path).send_keys(login_page.Pabitha_data.username)
        self.driver.find_element(by=By.XPATH,value=login_page.Selectors.password_path).send_keys(login_page.Pabitha_data.password)
        self.driver.find_element(by=By.XPATH,value=login_page.Selectors.login_button_path).click()
        print("Admin login successfully")
    def validate_options_in_admin_page(self,driver):
        driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_page.Selectors.username_path).send_keys(login_page.Pabitha_data.username)
        self.driver.find_element(by=By.XPATH, value=login_page.Selectors.password_path).send_keys(login_page.Pabitha_data.password)
        self.driver.find_element(by=By.XPATH, value=login_page.Selectors.login_button_path).click()
        self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Admin_path).click()
        expected_options={self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Organization),
                          self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Qualifications),
                          self.driver.find_element(by=By.XPATH,value=login_page.Selectors.user_management),
                          self.driver.find_element(by=By.XPATH,value=login_page.Selectors.job),
                          self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Nationalities),
                          self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Corporate_Banking),
                          self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Configuration)}
        missing_options=[]
        for option,xpath in expected_options.items():
            try:
                self.driver.find_element(by=By.XPATH,value=xpath)
                print(f"Option '{option}' is present.")
            except Exception as e:
                (missing_options.append(option))
                print(f"Option '{option}' is missing. Error: {e}")
            assert not missing_options, f"Missing options: {', '.join(missing_options)}"
        print("Validation of options in Admin page completed successfully")
    def validate_menu_options(self,driver):
        driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_page.Selectors.username_path).send_keys(login_page.Pabitha_data.username)
        self.driver.find_element(by=By.XPATH, value=login_page.Selectors.password_path).send_keys(login_page.Pabitha_data.password)
        self.driver.find_element(by=By.XPATH, value=login_page.Selectors.login_button_path).click()
        expected_menu={self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Admin),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.PIM),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Leave),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Time),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Recruitment),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.My_Info),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Performance),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Dashboard),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Directory),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Maintanence),
                       self.driver.find_element(by=By.XPATH,value=login_page.Selectors.Buzz)}
        missing_options = []
        for option, xpath in expected_menu.items():
            try:
                self.driver.find_element(by=By.XPATH, value=xpath)
                print(f"Option '{option}' is present.")
            except Exception as e:
                (missing_options.append(option))
                print(f"Option '{option}' is missing. Error: {e}")
            assert not missing_options, f"Missing options: {', '.join(missing_options)}"
        print("Validation of menu completed successfully")




