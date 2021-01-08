from selenium import webdriver
import time
import unittest
from IEOS.POMProject.Pages.loginPage import LoginPage
from IEOS.POMProject.Pages.dashboardPage import DashBoardPage



class LoginLogoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/hostedtoolcache/windows/Python/3.8.6/x64/Lib/site-packages/seleniumbase/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_logout_valid(self):
        driver = self.driver
        driver.get("http://elbtesting.idscan.cloud/idscanapp/#/login")
        login = LoginPage(driver)
        login.enter_username("superadministrator")
        login.enter_password("Password1!")
        login.click_login()
        dashboardpage = DashBoardPage(driver)
        dashboardpage.click_navigate()
        dashboardpage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


