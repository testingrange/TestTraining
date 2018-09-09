from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "name":
            return By.TAG_NAME
        else:
            print("Locator type is not supported")
            return False

    def iPrint(self, message, timeFormat = "%m-%d-%y %H:%M:%S"):
        print(str(datetime.strftime(datetime.now(), timeFormat)) + " " + message)

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.iPrint("Element Found (getElement)")
        except:
            self.iPrint("Element not found")
        return element

    def isElementPresent(self, locator, byType="id"):
        element = None
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                self.iPrint("Element Found (isElementPresent)" + element.get_attribute("style"))
                return True
            else:
                return False
        except:
            self.iPrint("Element not found" + element.get_attribute("style"))
            return False

    def elementPresenceCheck(self, locator, byType="id"):
        """
        Takes all elements with the same locators and returns first one that is present.
        """
        element = None
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                self.iPrint("There " + str(len(elementsList)) + " elements in the list.")
                for element in elementsList:
                    if element.is_displayed():
                        self.iPrint("Element displayed.")
                        return True
                    else:
                        return False
            else:
                self.iPrint("No elements have been detected.")
        except:
            self.iPrint("Elements are not displayed.")
            return False

    def takeScrShot(self, destination):
        filename = str(datetime.strftime(datetime.now(), "{0}%H%M%S{1}%m%d%y").format('t.', '_d.'))
        self.iPrint("filename format is - " + filename)
        destinationFileName = destination + filename + ".png"
        self.iPrint("destinationFileName is - " + destinationFileName)
        try:
            self.driver.save_screenshot(destinationFileName)
            self.iPrint("Screenshot has been saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            self.iPrint("Not a directory error")


