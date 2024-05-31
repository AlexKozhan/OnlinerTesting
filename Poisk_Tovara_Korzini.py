"""Поиск товара, добавление его в корзину и проверка корректности добавления"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера браузера
driver = webdriver.Chrome()

# Открытие главной страницы сайта
driver.get("https://www.onliner.by/")

# Поиск поля ввода для поиска и ввод запроса
search_box = driver.find_element_by_css_selector("input.fast-search__input")
search_box.send_keys("iPhone")
search_box.submit()

# Ожидание загрузки результатов поиска и выбор первого товара
first_result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.product__title"))
)
first_result.click()

# Добавление товара в корзину
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.buy-button"))
)
add_to_cart_button.click()

# Переход в корзину
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.b-top-profile__cart"))
)
cart_button.click()

# Проверка наличия товара в корзине
cart_item_title = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cart-product__title"))
).text

expected_title = "iPhone"
if expected_title in cart_item_title:
    print("Тест успешно пройден: товар успешно добавлен в корзину.")
else:
    print("Тест не пройден: товар не найден в корзине.")

# Закрытие браузера
driver.quit()
