"""Взаимодействие с выпадающим списком и выбор опции:"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера браузера
driver = webdriver.Chrome()

# Открытие страницы с товарами
driver.get("https://www.onliner.by/")

# Нажатие на выпадающий список "Выбрать город"
city_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.b-top-profile__region"))
)
city_dropdown.click()

# Выбор города (например, Минск)
minsk_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Минск')]"))
)
minsk_option.click()

# Проверка выбора города
selected_city = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.b-top-profile__region span.b-top-profile__region"))
).text

if selected_city == "Минск":
    print("Тест успешно пройден: город успешно выбран.")
else:
    print("Тест не пройден: город не выбран корректно.")

# Закрытие браузера
driver.quit()
