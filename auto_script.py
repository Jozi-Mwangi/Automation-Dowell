from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# wait.until(EC.visibility_of_element_located((By.XPATH, "//div/div/div/h3" )))

def start_server():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(options=options)

    driver.get('https://100093.pythonanywhere.com/')
    print("Driver Running")

    title = driver.find_element(by=By.XPATH, value="//div/div/div/h3").text
    print(title)

    naving_to_team_management(driver)
    driver.quit()

# driver.implicitly_wait(5)

def naving_to_team_management (driver):
    wait =  WebDriverWait(driver=driver, timeout=2)
    wait.until(EC.presence_of_element_located((By.ID, "selectorg")))

    dropdown_element = driver.find_element(By.ID, "selectorg")
    select = Select(dropdown_element)
    # select.select_by_value("HR_DOWELL Research (HR_DOWELL Research)")
    select.select_by_index(1)

    wait.until(EC.presence_of_element_located((By.ID, "productbtn")))
    product_button = driver.find_element(By.ID, "productbtn")
    product_button_text = driver.find_element(By.ID, "productbtn").text
    print(product_button_text)
    product_button.click()

start_server()
