from poium import Page, Element, Elements


class SSIDivingLog(Page):
    more_btn = Element(ios_predicate='label == "More"',
                          describe="more_btn")
    logbook = Element(ios_predicate='label == "Logbook"', describe="logbook")


class Stylish(Page):
    t_shirt_btn = Element(ios_class_chain ='**/XCUIElementTypeButton[`name == "catalog_btn"`]',
                          describe="t_shirt_btn")
    cart = Element(accessibility_id='cart_btn', describe="cart")