from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import simpledialog
import time
def login():
    driver=webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)

    mobile_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div[1]/div[2]/div[1]/form/div[1]/input')))
    mobile_no.send_keys("8838651636")

    driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div[2]/div/form/div[3]/button').click()
    
    root=tk.Tk()
    root.withdraw()
    pin = simpledialog.askstring("OTP Verification", "Enter OTP:")

    otp_boxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[maxlength='1']")))

    # type digits one by one
    for box, digit in zip(otp_boxes,pin):
        box.clear()
        box.send_keys(digit)


    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div[2]/div/div/form/button').click()

    print("login successful")
    return driver