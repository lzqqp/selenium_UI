from selenium import webdriver
def login(driver,username,password):
    driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[1]/div[2]/input').clear()
    driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[1]/div[2]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[2]/input').clear()
    driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[2]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="yunkeSubmit"]/div[4]/input').submit()


