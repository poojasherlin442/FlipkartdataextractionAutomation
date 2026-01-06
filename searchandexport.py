from flipkartlogin import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
import tkinter as tk
from tkinter import simpledialog
import pandas as pd
import time

driver=login()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

root=tk.Tk()
root.withdraw()

query = simpledialog.askstring("Search", "Enter product to search:")
search = wait.until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search.clear()
search.send_keys(query)
search.send_keys(Keys.RETURN)

data=[]
page=1
max_page=2
while page<=max_page:
    cards=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.QSCKDh.dLgFEE")))
    for card in cards:
        singlecard=card.find_elements(By.CSS_SELECTOR,"div.lvJbLV.col-12-12")
        for i in singlecard:
            try:
                name = i.find_element(By.CSS_SELECTOR, "div.RG5Slk").text.strip()
                price = i.find_element(By.CSS_SELECTOR, "div.hZ3P6w").text.replace("₹"," ").strip()
                rating = i.find_element(By.CSS_SELECTOR, "div.MKiFS6").text.strip()
                if name and price:
                    data.append({
                        "Name": name,
                        "Price": price,
                        "Rating": rating
                        })

            except NoSuchElementException:
                continue        
    
    if page == max_page:
        break

    try:
        next_btn = driver.find_element(By.XPATH, "//span[text()='Next']/parent::a")
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(2)
        page += 1
    except NoSuchElementException:
        print("No more pages")
        break


df = pd.DataFrame(data)
df.to_excel(r"C:\Users\Admin\Desktop\Pooja\flipkartresult.xlsx",index=False)
print("Saved to flipkartresult.xlsx")