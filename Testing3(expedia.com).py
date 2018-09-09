from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from functions.handyWrappers import HandyWrappers
from datetime import datetime
import time
import random
from functions.explicit_wait import ExplicitWaitType


class TestCase1():
    def testSuite(self):
        driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")
        URL = "https://www.expedia.com/"
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(URL)
        wait = ExplicitWaitType(driver)
        hw = HandyWrappers(driver)
        ## generic method to select dates from calendar

        destinationForScreenshots = "C:\\Users\S4etovodov\Desktop\Selenium_screenshots\\"

        flightsBtn = hw.getElement("tab-flight-tab-hp")
        flightsBtn.click()

        advancedOptions = hw.getElement("flight-advanced-options-hp-flight")
        advancedOptions.click()

        time.sleep(2)

        nonstopCheckBox = hw.getElement("advanced-flight-nonstop-hp-flight")
        nonstopCheckBox.click()

        time.sleep(2)

        preferredAirlineDrDwn = hw.getElement("flight-advanced-preferred-airline-hp-flight")
        sel = Select(preferredAirlineDrDwn)
        sel.select_by_value("SU")

        time.sleep(2)

        classDrpDwn = hw.getElement("flight-advanced-preferred-class-hp-flight")
        sel1 = Select(classDrpDwn)
        sel1.select_by_value("business")

        OriginField = hw.getElement("flight-origin-hp-flight")
        OriginField.send_keys("new")
        time.sleep(2)
        OriginItem = hw.getElement("// ul[ @ id = 'typeaheadDataPlain'] // li/a[contains(@data-value,'New York (NYC-All Airports)')]", "xpath")
        OriginItemText = OriginItem.text
        print(OriginItemText)
        OriginItem.click()
        time.sleep(2)

        flyingToField = hw.getElement("flight-destination-hp-flight")
        flyingToField.send_keys("mos")
        time.sleep(2)
        flyingToFieldItem = hw.getElement("//ul[@id='typeaheadDataPlain']//li/a[contains(@data-value, 'Moscow, Russia (MOW-All Airports)')]","xpath")
        flyingToFieldItem.click()

        time.sleep(2)

        oneWayBtn = hw.getElement("flight-type-one-way-label-hp-flight")
        oneWayBtn.click()

        time.sleep(2)
        departingField = hw.getElement("//input[@id='flight-departing-single-hp-flight']", "xpath")
        departingField.click()


        monthsSel = {
            "january": '0',
            "february": '1',
            "september": '8'
        }


        depDateMonth = "september"
        depDateDay = "18"
        depDateYear = "2018"

        print(monthsSel[depDateMonth])

        depDXpath = "//div[@id='flight-departing-wrapper-single-hp-flight']//button[contains(@data-year, '{0}') and contains(@data-month, '{1}') and contains(@data-day, '{2}')]"
        depDateXpath = depDXpath.format(depDateYear, monthsSel[depDateMonth], depDateDay)
        print(depDateXpath)
        departureDate = hw.getElement(depDateXpath, "xpath")
        departureDate.click()
        #//div[ @ id = 'flight-departing-wrapper-single-hp-flight'] //  button[contains( @ data - year, '2018') and contains( @ data - month, '8') and contains( @ data - day, '18')]
        #driver.find_element(By.XPATH, "//div[@id='flight-departing-wrapper-single-hp-flight']//button[contains (@data-year, '2018') and contains (@data-month, '8') and contains (@data-day, '18')]").click()
        #el = wait.waitForElement("//div[@id='flight-departing-wrapper-single-hp-flight']//button[contains(@data-year,'2018') and contains( @data-month, '8') and contains(@data-day, '18')]", "xpath", 25).click()

        hw.takeScrShot(destinationForScreenshots)


        element = wait.waitForElement("//form[@id='gcw-flights-form-hp-flight']/div[8]/label/button", "xpath", 10)
        element.click()
        time.sleep(2)

        hw.takeScrShot(destinationForScreenshots)

        driver.quit()

TestExecution1 = TestCase1()
TestExecution1.testSuite()

