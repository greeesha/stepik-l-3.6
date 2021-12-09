import time

def test_add_item_to_basket_button_lang(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    assert "Añadir al carrito" == browser.find_element_by_class_name("btn-add-to-basket").text
