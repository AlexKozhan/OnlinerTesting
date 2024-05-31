"""Поиск товара с использованием фильтров и проверка правильности отображения результатов"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера браузера
driver = webdriver.Chrome()

# Открытие страницы с товарами
driver.get("https://www.onliner.by/")

# Нажатие на категорию "Телефоны"
phones_category = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.b-main-navigation__link[data-id='catalog']"))
)
phones_category.click()

# Нажатие на ссылку "Смартфоны"
smartphones_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/catalog/mobile/') and contains(text(), 'Смартфоны')]"))
)
smartphones_link.click()

# Активация фильтров
brand_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Производитель')]"))
)
brand_filter.click()

# Выбор производителя (например, Samsung)
samsung_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Samsung')]/preceding-sibling::input"))
)
samsung_checkbox.click()

# Применение выбранных фильтров
apply_filters_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.button_orange"))
)
apply_filters_button.click()

# Проверка результатов поиска
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.schema-product__title"))
)

if results:
    print("Тест успешно пройден: результаты поиска отображаются корректно.")
else:
    print("Тест не пройден: результаты поиска не отображаются.")

# Закрытие браузера
driver.quit()
