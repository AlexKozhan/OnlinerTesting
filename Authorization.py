"""Авторизация пользователя и проверка доступа к личному кабинету"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера браузера
driver = webdriver.Chrome()

# Открытие страницы входа
driver.get("https://www.onliner.by/")

# Поиск и нажатие кнопки "Войти"
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.b-top-profile__auth"))
)
login_button.click()

# Ввод логина и пароля
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input.auth-form__input[type='text']"))
)
username_input.send_keys("your_username")

password_input = driver.find_element_by_css_selector("input.auth-form__input[type='password']")
password_input.send_keys("your_password")

# Отправка формы
login_button = driver.find_element_by_css_selector("button.auth-button")
login_button.click()

# Проверка успешного входа
user_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.b-top-profile__preview"))
)

if user_menu:
    print("Тест успешно пройден: успешный вход в личный кабинет.")
else:
    print("Тест не пройден: вход в личный кабинет не выполнен.")

# Закрытие браузера
driver.quit()
