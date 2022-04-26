from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get('https://canvas.donga.edu.vn')

driver.implicitly_wait(4)



input_Username = driver.find_element(By.CSS_SELECTOR, '#identifierId')
input_Username.send_keys('vinh48181@donga.edu.vn')
input_Username = driver.find_element(By.CSS_SELECTOR, '#identifierNext > div > button').click()
#

driver.implicitly_wait(2)


input_Username = driver.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
input_Username.send_keys('abc.12345')
input_Username = driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button').click()


# driver.implicitly_wait(2)


driver.find_element(By.CSS_SELECTOR, '#global_nav_profile_link').click()
AfterLogin_username = driver.find_element(By.CSS_SELECTOR, '#nav-tray-portal > span > span > div > div > div > div > div > span > div > h2').text
print("Tên người dùng: ", AfterLogin_username)
driver.implicitly_wait(6)


BangDieuKhien = driver.find_element(By.CSS_SELECTOR, '#dashboard_header_container > div > h1 > span').text
print(BangDieuKhien)

driver.implicitly_wait(6)

testXpath = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/div')
for testXpaths in testXpath:
    try:
        Tieu_De = testXpaths.find_element(By.XPATH, 'div/a/div/h3/span').text
        Tieu_De_phu = testXpaths.find_element(By.XPATH, "div/a/div/div[1]").text
        print(Tieu_De)
        print(Tieu_De_phu)
        print('----------------------')
    except NoSuchElementException:
        pass


driver.close()
# driver.quit()