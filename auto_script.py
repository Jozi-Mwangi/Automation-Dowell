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
    second_wait =  WebDriverWait(driver=driver, timeout=20)
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

    wait.until(EC.presence_of_element_located((By.XPATH, "// a [@id='Workflow AI']")))
    # button_el = second_wait.until(EC.element_to_be_clickable((By.ID, 'mySelect')))

    # //button[@name='connect_portfolio']
    second_wait.until(EC.visibility_of_element_located((By.ID, 'mySelect')))
    button_el = second_wait.until(EC.element_to_be_clickable((By.XPATH, "(//a/div/div/div/form/b/button[@name='connect_portfolio'])[1]")))
    # button_el = driver.find_element(By.XPATH, "(//a/div/div/div/form/b/button[@name='connect_portfolio'])[1]")
    # team_mgmnt_link.click()
    button_el.click()
    print("Link Clicked")
    driver.implicitly_wait(10)

    team_management_funcs(driver)

def team_management_funcs(driver):
    wait = WebDriverWait(driver=driver, timeout=15)
    work_log_text = wait.until(EC.presence_of_element_located((By.XPATH, '(// div /div/ h4 )[2]')))
    print(work_log_text)

    add_work_log_element = driver.find_element(By.XPATH, '(// div [@class="Create_Team"])[2]')
    add_work_log_element.click()
    print("Plus Button Clicked")

    wait.until(EC.presence_of_element_located((By.XPATH, '// div /h1 [@class="title__Item"]')))
    name_input = driver.find_element(By.XPATH, '// div /input [@placeholder="Task Assignee"]')
    date_input = driver.find_element(By.XPATH, '// div /input [@placeholder="today time"]')

    name_value = name_input.get_attribute("value")
    date_value = date_input.get_attribute("value")

    print(name_value)
    print(date_value)


start_server()
