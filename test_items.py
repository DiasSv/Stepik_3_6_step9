import time

link = "http://selenium1py.pythonanywhere.com/catalogue/hacking_182/"


def test_button_add_basket(browser):
    browser.get(link)
    time.sleep(10)  # Установил паузу в 10 сек для того, чтобы проверяющий мог увидеть смену языка

    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")

    assert button, "Кнопка не найдена"
