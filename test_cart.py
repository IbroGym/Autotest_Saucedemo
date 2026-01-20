from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def login(driver, wait):
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url


def test_cart(driver, logger):

    wait = WebDriverWait(driver, 10)
    
    # Step 1: Login
    logger.info("Test Start: test_cart")
    logger.info("Step 1: Login to application")
    login(driver, wait)

    # Step 2: Click "Add to Cart" for Sauce Labs Backpack
    logger.info("Step 2: Click 'Add to Cart' for Sauce Labs Backpack")
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_btn.click()

    # Step 3: quantity input should appear
    logger.info("Step 3: Verify quantity input is displayed")
    try:
        quantity_input = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quantity"))
        )
        logger.info("Checkpoint Passed: Quantity input is visible")
    except TimeoutException:
        logger.error("Checkpoint Failed")
        logger.error("Expected: Quantity input field should appear")
        logger.error("Actual: Quantity input field did not appear")
        assert False, (
            "EXPECTED: Quantity input field should appear after clicking 'Add to Cart'. "
            "ACTUAL: Quantity input field did not appear (timeout)."
        )

    # Input quantity and check the product existence in cart page
    logger.info("Step 4: Input quantity of the product")
    quantity_input.clear()
    quantity_input.send_keys("3")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkpoint: product is displayed in cart page
    logger.info("Step 5: Verify the product in cart page")
    cart_item = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

    logger.info("Test End: test_cart")
    assert cart_item.text.strip() == "Sauce Labs Backpack", (
    "Product is not displayed in the cart page")
