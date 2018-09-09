import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from functions.handyWrappers import HandyWrappers
from functions.explicit_wait import ExplicitWaitType


class Testing():

    def test(self):
        URL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(URL)

        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        hw = HandyWrappers(driver)
        wait = ExplicitWaitType(driver)

        destinationForScreenshots = "C:\\Users\S4etovodov\Desktop\Selenium_screenshots"

        openWindowBtn = hw.getElement("openwindow")
        openWindowBtn.click()

        handles = driver.window_handles

        for handle in handles:
            print("Hanle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                searchBox = hw.getElement("search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        driver.switch_to.window(parentHandle)
        hw.getElement("name").send_keys("Test Successful")


TestCase = Testing()
#TestCase.test()


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        print(self.name)
        print(self.next.name)
        another = self.next.name
        print(Song(another).next.name)
        return None


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())





