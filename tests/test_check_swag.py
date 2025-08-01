from pages.base_page import BasePage
from pages.swag_labs import SwagLabs

# i. перейти на страницу https://www.saucedemo.com/
# ii. проверить наличие иконки
def test_checking_for_a_icon(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.exist_icon(), 'Иконка не найдена :('


# i. перейти на страницу https://www.saucedemo.com/
# ii. проверить наличие поля имени
def test_checking_for_a_name_field(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.find_element(locator='[data-test="username"]'), 'Поле имени не найдено :('



# i. перейти на страницу https://www.saucedemo.com/
# ii. проверить наличие поля пароля
def test_checking_for_a_password_field(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    assert swag_labs.find_element(locator='[data-test="password"]'), 'Поле для ввода пароля не найдено :('