from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

class TestingFramework():
    def test(self):
        def timeNow(time = datetime.now(), timeFormat = "%m-%d-%y %H:%M:%S"):
            return(str(datetime.strftime(time, timeFormat)))
        startTime = timeNow()

        objectLibrary = {}

        def printM(message):
            print(timeNow() + " " + message)

        def isSelected(element):
            print(timeNow() + " Element selected? : " + str(element.is_selected()))

        print("Testing start at: " + startTime)

        URL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")

        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.ID, "hondaradio")
        objectLibrary["bmwRadioBtn"] = bmwRadioBtn
        objectLibrary["bmwRadioBtn"].click()
        print("BMW button has been clicked")
        time.sleep(2)
        print(objectLibrary)

        benzRdBtn = driver.find_element(By.ID, "benzradio")
        benzRdBtn.click()
        printM("benzRdBtn was clicked.")
        isSelected(benzRdBtn)

        hondaCheckB = driver.find_element(By.ID, "hondacheck")
        hondaCheckB.click()
        isSelected(hondaCheckB)

        inputF = driver.find_element(By.ID, "name")
        inputF.send_keys("Konstantin")
        printM("Name Konstantin was input.")

        confirmBtn = driver.find_element(By.ID, "confirmbtn")
        confirmBtn.click()
        time.sleep(1)
        alertMsg = driver.switch_to.alert
        alertMsg.dismiss()
        time.sleep(1)
        printM("Alert box was dismissed.")

        time.sleep(2)

        inputF = driver.find_element(By.ID, "name")
        inputF.send_keys("Konstantin")
        printM("Name Konstantin was input.")

        alertBtn = driver.find_element(By.ID, "alertbtn")
        alertBtn.click()
        printM("Alert Button was clicked.")

        time.sleep(2)

        alertDialogBox = driver.switch_to.alert
        alertDialogBox.accept()
        printM("Alert dialog box was dismissed.")

        time.sleep(2)

        print(timeNow() + " Preparing to quit.")
        driver.quit()

Test = TestingFramework()
Test.test()


