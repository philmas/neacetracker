import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading


def track_neace_score():
    print("Currently tracking wins...")
    threading.Timer(1200.0, track_neace_score).start()  # called every minute
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://fortnitestats.net/stats/n-e-a-c-e")
    solo_wins = driver.find_element_by_class_name("panel-main").text.splitlines()[0]

    with open(ROOT_DIR + "/wins.txt", "w") as text_file:
        text_file.write(solo_wins)


track_neace_score()
