import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os



try:
    # Set up the webdriver to connect to the remote Selenium server
    options = webdriver.ChromeOptions()

    # Configure Chrome preferences to allow downloads
    prefs = {
        "download.default_directory": "/home/seluser/Downloads",
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
        "safebrowsing.disable_download_protection": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Disable headless mode to show the Chrome UI
    # options.add_argument('--headless=false')

    options.add_argument("--allow-running-insecure-content")  # Allow insecure content
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://192.168.70.147:4000")
    # Remote WebDriver URL (provided by the selenium/standalone-chrome service)
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    # Open the browser and go to the URL
    driver.get('http://192.168.70.147:4000')

    # time.sleep(120)


    # Wait for the "File" button to be clickable and click it
    basic_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'menu-button') and .//span[text()='File']]"))
    )
    basic_button.click()

    # Wait for the dropdown menu to be visible
    dropdown_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@role='menu' and @aria-label='File']"))
    )

    # Wait for the "Open" menu item to be clickable and click it
    open_menu_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@role='menu' and @aria-label='File']//li[text()='Open']"))
    )
    open_menu_item.click()

    # Wait for the file input element to be present in the dialog
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )

    # Use pyautogui to handle the file upload dialog
    time.sleep(2)  # Wait for the file dialog to appear
    pyautogui.write('/home/seluser/Demo_Autoparking_ROS2_1.vc3')
    pyautogui.press('enter')

    time.sleep(2)

        # Wait for the "File" button to be clickable and click it
    basic_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'menu-button') and .//span[text()='File']]"))
    )
    basic_button.click()

    # Wait for the dropdown menu to be visible
    dropdown_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@role='menu' and @aria-label='File']"))
    )

    # Wait for the "Open" menu item to be clickable and click it
    open_menu_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@role='menu' and @aria-label='File']//li[text()='Build and Download']"))
    )
    open_menu_item.click()


    
    time.sleep(20)
    
    download_directory = "/home/seluser/Downloads"
    zip_files = [f for f in os.listdir(download_directory) if f.endswith('.zip')]

    if zip_files:
        print("Test Passed: .zip file downloaded successfully.")
        sys.exit(0)  # Exit with code 0 for success
    else:
        print("Test Failed: No .zip file found.")
        sys.exit(1)  # Exit with code 1 for failure



finally:
    # Close the browser
    if driver:
        driver.quit()
