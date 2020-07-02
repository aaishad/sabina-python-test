import subprocess,os
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException,\
	StaleElementReferenceException, ElementNotVisibleException
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
global driver

driver = None

class WebSeleniumUtils:
	def __init__(self,dirct_download=0):
		self.dirct_download = dirct_download
		global driver
		if (driver == None):
			chrome_options = webdriver.ChromeOptions()
			preferences = {"download.default_directory": self.dirct_download,
               "directory_upgrade": True,
               "safebrowsing.enabled": True,
               "download.extensions_to_open": "applications/ica"}
			chrome_options.add_experimental_option("prefs", preferences)
			chrome_options.add_argument('--start-maximized')
			chrome_options.add_argument("--disable-dev-shm-usage")
			driver = webdriver.Chrome(executable_path=r'/home/bremen/sabinaTest/drivers/driverlist/chromedriver_74ver', chrome_options=chrome_options)
		print(driver)
		#return driver

	def loadUrl(self, url):
		try:
			#driver.maximize_window()
			driver.get(url)
			return True
		except TimeoutException as err:
			return err

	def click_By_Id(self, element):
		try:
			myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, element)))
			driver.execute_script('arguments[0].click()', myElem)
			return True
		except TimeoutException:
			err = 'Given element is not displayed: '+element
			print(err)
			return err

	def click_By_Name(self, element):
		try:
			myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, element)))
			driver.execute_script('arguments[0].click()', myElem)
			return True
		except TimeoutException:
			err = 'Given element is not displayed: '+element
			print(err)
			return err

	def click_By_XPath(self, element):
		try:
			myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
			driver.execute_script('arguments[0].click()', myElem)
			return True
		except TimeoutException:
			err = 'Given element is not displayed: '+element
			print(err)
			return err

	def quitDriver(self):
		try:
			global driver
			driver.close()
			driver = None
			return True
		except Exception as err:
			print(err)
			return str(err)

	def getText_ByName(self, element):
		try:
			return driver.find_element_by_name(element).text
		except Exception as err:
			print(err)
			return str(err)

	def getText_By_XPath(self, element):
		try:
			return driver.find_element_by_xpath(element).text
		except Exception as err:
			print(err)
			return str(err)

	def getText_By_Id(self, element):
		try:
			return driver.find_element_by_id(element).text
		except Exception as err:
			print(err)
			return str(err)

	def getTitle(self):
		try:
			return driver.title
		except Exception as err:
			print(err)
			return str(err)

	def getattribute_By_LinkText(self, element, name):
		try:
			return driver.find_element_by_link_text(element).get_attribute(name)
		except Exception as err:
			print(err)
			return str(err)


	def sendKeys_Xpath(self,element,data):
		try:
			myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
			myElem.clear()
			myElem.send_keys(data)
			return True
		except TimeoutException:
			raise Exception('Given element is not displayed: '+element)


	def felement_by_xpath(self, element):
		try:
			return driver.find_element_by_xpath(element)
		except Exception as err:
			print(err)
			return str(err)





if __name__ == "__main__":
	selenium_obj = WebSeleniumUtils()
