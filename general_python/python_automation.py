import time
from selenium import webdriver
import pyautogui


def move_mouse():
    for i in range(5):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)
        pyautogui.typewrite("It works!!")


def open_youtube_song():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://youtube.com')
    search_box = driver.find_element_by_xpath('//*[@id="search"]')
    search_box.send_keys("further up")
    search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
    search_button.click()
    time.sleep(3)
    search_button = driver.find_element_by_xpath('//*[@id="description-text"]/span[3]')
    search_button.click()

if __name__=="__main__":
    # open_youtube_song()
    move_mouse()
