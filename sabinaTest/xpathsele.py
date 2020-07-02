import sys,pyautogui
from BrowserSeleninumUtils import WebSeleniumUtils
from time import sleep

class CharmHealth():
	"""Cunstractor for xpath"""
	def __init__(self):
		self.login_xapth ='//span[@class="sign-button"]'
		self.username = 'Dev+7@deepscribe.ai'
		self.passwrd = 'vgS9Y3RDhq2tnhE'
		self.input_xapth = '//input[@id="lid"]'
		self.input_pwd = '//input[@id="pwd"]'
		self.signin_submit = '//div[@id="signin_submit"]'
		self.chartnot = '//span[@id="MEMBER_TAB_COUNT_ID_2"]'
		self.close_aler = '//i[@id="NEW_DIALOG_CLOSE_MARK"]'
		self.encounter = '//div[@class="v1-action-btn v1-action-btn-bg v1-cmcur"]'
		self.enc_serach = '//input[@class="v1-search-field"]'
		self.dummytext = '//div[@class="DUMMYTEXT"]'
		self.visit_type = '//select[@id="VISIT_TYPE"]/option[text()=" New Patient Visit"]'
		self.create_btn = '//button[@class="v1-pmy-btn v1-pmy-btn-bg v1-cmcur"]'
		self.text_oly  =  "//div[@class='v1-rw-text']"
		self.histroy = "//div[@id='encounterTab_2']"
		self.template = "//div[text()='Templates']"

	def checking_for_login(self,url,seleobj):
		""" checking for login"""
		res = seleobj.loadUrl(url)
		seleobj.click_By_XPath(self.login_xapth)
		seleobj.sendKeys_Xpath(self.input_xapth,self.username)
		sleep(2)
		seleobj.sendKeys_Xpath(self.input_pwd,self.passwrd)
		res = seleobj.click_By_XPath(self.signin_submit)
		return res

	def click_on_chartnote(self,seleniumobj):
		try:

			seleniumobj.click_By_XPath(self.close_aler)
			sleep(3)
			charnot = seleniumobj.click_By_XPath(self.chartnot)
			return charnot
		except Exception as er:
			print(er)

	def click_on_history(self,seleniumobj):
		try:

			seleniumobj.click_By_XPath(self.histroy)
			sleep(3)
			res = seleniumobj.click_By_XPath(self.template)
			return res
		except Exception as er:
			print(er)

	def click_on_encounter(self,seleniumobj,name):
		try:
			seleniumobj.click_By_XPath(self.encounter)
			seleniumobj.sendKeys_Xpath(self.enc_serach,name)
			seleniumobj.click_By_XPath(self.text_oly)
			sleep(3)
			seleniumobj.click_By_XPath(self.dummytext)
			seleniumobj.felement_by_xpath(self.visit_type).click()
			sleep(2)
			seleniumobj.click_By_XPath(self.create_btn)
		except Exception as er:
			print(er)


