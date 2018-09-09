import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testing():
    def test(self):
        URL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")

        def timeNow(timeformat = "%d/%m/%y %H:%M:%S"):
            return(str(datetime.strftime(datetime.now(),timeformat)))

        print(timeNow())

        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)
        title = driver.title
        print(timeNow() + "Title of the page is: " + str(title))


        currentURL = driver.current_url
        print("Current URL is: " + str(currentURL))
        driver.refresh()
        print("page has been refreshed")
        driver.get(driver.current_url)
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")


        title = driver.title
        currentURL = driver.current_url
        print("Title of the page is: " + str(title))
        print("Current URL is: " + str(currentURL))

        driver.back()
        print("One step back")

        driver.forward()
        print("One step forward")
        driver.back()
        print("One step back")

        time.sleep(2)
        title = driver.title
        currentURL = driver.current_url
        print("Title of the page is: " + str(title))
        print("Current URL is: " + str(currentURL))

        interField = driver.find_element(By.ID, "name")
        interField.clear()
        interField.send_keys("Konstantin")
        time.sleep(2)

        submitBtn = driver.find_element(By.ID, "confirmbtn")
        submitBtn.click()
        print(timeNow() + "button has been clicked")
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        benzRad = driver.find_element(By.ID, "benzradio")
        if benzRad is not None:
            benzRad.click()
        else:
            print("Warning, element is not located")
        time.sleep(2)
        print(timeNow() + " System preparing to quit.")

        driver.quit()

        print(timeNow() + "System quits. See you.")


newTest = Testing()
newTest.test()


