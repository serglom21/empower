def test_checkout(ios_sim_driver):
    ios_sim_driver.find_element_by_accessibility_id("Empower Plant").click()

    cart_btn = ios_sim_driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="Add to Cart"])[1]')
    cart_btn.click()
    cart_btn.click()
    cart_btn.click()
    cart_btn.click()

    ios_sim_driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Cart"]').click()
    ios_sim_driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Checkout"]').click()

    ios_sim_driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="email"])[3]/XCUIElementTypeTextField').click()
    ios_sim_driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="Place your order"])[2]').click()

