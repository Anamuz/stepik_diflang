from selenium.webdriver.common.by import By




def test_cart_button(browser):
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button

