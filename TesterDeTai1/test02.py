from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By             #TV2


driver = webdriver.Chrome()

driver.get("https://vnexpress.net")


# driver.implicitly_wait(1.5) #chờ ngầm định đề phòng mạng chậm load không nổi

testXpath = driver.find_elements(By.XPATH, '/html/body/section[5]/div/div[1]/article')
for testXpaths in testXpath:
    try:
        Tieu_De = testXpaths.find_element(By.TAG_NAME, 'h3').text
        Mieu_Ta = testXpaths.find_element(By.TAG_NAME, "p").text
        Link_BaiViet = testXpaths.find_element(By.XPATH, 'h3/a').get_attribute('href')
        print(Tieu_De)
        print(Mieu_Ta)
        print(Link_BaiViet)
        print('=======================')
    except NoSuchElementException:
        print('Error ko hiện thông tin')
        pass




#lấy title
# print(driver.title)

#lấy page soure
# print(driver.page_source)








#sau khi thực hiện xong thì tắt hẳn những thứ liên quan
# driver.quit()

#sau khi thực hiện xong thì chỉ tắt trình duyệt
# driver.close()