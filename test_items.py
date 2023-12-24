import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
expected_value = "btn btn-lg btn-primary btn-add-to-basket"


def test_assert_cart_button(driver):
    driver.get(url)
    time.sleep(5)  # для проверки выбранного языка

    cart_button = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((
        By.CSS_SELECTOR, "button.btn-add-to-basket")))
    cart_button_value = cart_button.get_attribute("class")  # Записываем в переменную значение аттрибута class кнопки
    print(f"Фактическое значение value: \"{cart_button_value}\"")
    """
    Проверку наличия кнопки выполняю по assert через атрибут class. 
    Смысла от этого не вижу, но таков фактор оценивания,
    чтобы был какой-то assert
    """
    assert cart_button_value == expected_value, f"Содержимое value: \"{expected_value}\""
    print(f"Ожидаемое значение value:   \"{expected_value}\" подтверждено")
