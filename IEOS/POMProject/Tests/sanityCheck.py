from IEOS.POMProject.Tests.login import LoginLogoutTest
from selenium import webdriver
import time
import unittest


class SanityCheckTest1(unittest.TestCase):
	@classmethod
	def test(self):
		login = LoginLogoutTest()
		login.setUpClass()
		login.test_login_logout_valid()
		login.tearDown()
