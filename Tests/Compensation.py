from selenium import webdriver
from selenium.webdriver.common.by import By

# Тест по компенсациям

driver = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
driver.implicitly_wait(5)

driver.get("http://dev.leadbit.com/")
# Пока не работает
# driver.minimize_window()

# Пока не работает
user_logo = driver.find_element(By.CSS_SELECTOR, '.icon--profile')
user_logo.click()

driver.quit()
