from selenium import webdriver
chromeDriverPath = 'D:\DevelopTools\Test\chromedriver_win32for-83.0.4103.39\chromedriver.exe'

driver = webdriver.Chrome(chromeDriverPath)

def login():
    driver.get("http://sys.gapit.cn:8012")
    # username = driver.find_element_by_tag_name("input")
    # username.send_keys("ss")
    # password = driver.find_element_by_tag_name("input")
    # password.send_keys("123123")

    inputs = driver.find_elements_by_tag_name('input')
    # print(inputs)
    inputs[0].send_keys("admin")
    inputs[1].send_keys("123123")

    driver.find_element_by_tag_name('button').click()

login()