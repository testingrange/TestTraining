from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
from functions.handyWrappers import HandyWrappers
import time



class Testing():
    def test(self):
        print(round(random()*10))
        URL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")

        def timeNow(timeFormat = "%m-%d-%y %H:%M:%S"):
            return(str(datetime.strftime(datetime.now(), timeFormat)))

        def printM(message):
            print(timeNow() + " " + message)

        driver.get(URL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        radioBtns = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        printM("Quantity of elements in the list: " + str(len(radioBtns)))
        for i in radioBtns:
            if not i.is_selected():
                rbname = i.get_attribute("value")
                print(rbname + " is selected? " + str(i.is_selected()))
                i.click()
                time.sleep(2)
                printM("Radion button " + rbname + " was clicked.")

        drdwnElement = driver.find_element(By.ID, "carselect")
        sel = Select(drdwnElement)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index(1)
        printM("Select second item")
        time.sleep(2)

        sel.select_by_visible_text("Honda")
        printM("Select Honda by visible text")
        time.sleep(2)
        print("=================")

        hideBtn = driver.find_element(By.ID, "hide-textbox")
        hideBtn.click()
        printM("hide btn was clicked")
        time.sleep(2)

        inpField = driver.find_element(By.ID, "displayed-text")
        if inpField.is_displayed():
            printM("Inp is displayed")
            inpField.send_keys("New text")
        else:
            printM("Inp Field is not visible")
        time.sleep(2)

        inpNameField = driver.find_element(By.ID, "name")
        inpNameFieldName = inpNameField.get_attribute("placeholder")
        printM("Attribute name is : " + inpNameFieldName)

        hw = HandyWrappers(driver)

        textField = hw.getElement("name")
        textField.send_keys("TestTest")
        time.sleep(2)

        submitBtn = hw.getElement("//input[@id='confirmbtn']", "xpath")
        submitBtn.click()
        time.sleep(2)
        alertBox = driver.switch_to.alert
        alertBox.accept()
        time.sleep(2)

        hw.elementPresenceCheck("//input[contains(@name, 'cars') and contains (@type, 'radio')]", "xpath")

        hw.isElementPresent("displayed-text")

        driver.execute_script()

        driver.quit()



newTest = Testing()
newTest.test()




