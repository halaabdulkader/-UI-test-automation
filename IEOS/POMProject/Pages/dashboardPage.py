from IEOS.POMProject.Locators.locators import Locators
class DashBoardPage():

	def __init__(self, driver):

		self.driver = driver

		self.navigate_dropdown_xpath = Locators.navigate_dropdown_xpath
		self.logout_link_linkText = Locators.logout_link_linkText

	def click_navigate(self):
		self.driver.find_element_by_xpath(self.navigate_dropdown_xpath).click()

	def click_logout(self):
		self.driver.find_element_by_link_text(self.logout_link_linkText).click()


