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


def test_cart(driver):

    wait = WebDriverWait(driver, 10)

    # Preconditions: user logged in and on inventory page
    login(driver, wait)

    # Step 1: Click "Add to Cart" for Sauce Labs Backpack
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_btn.click()

    # Step 2: quantity input should appear
    try:
        quantity_input = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "quantity"))
        )
    except TimeoutException:
        assert False, (
            "EXPECTED: Quantity input field should appear after clicking 'Add to Cart'. "
            "ACTUAL: Quantity input field did not appear (timeout)."
        )

    # Input quantity and check the product existence in cart page
    quantity_input.clear()
    quantity_input.send_keys("3")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkpoint: product is displayed in cart page
    cart_item = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

    assert cart_item.text.strip() == "Sauce Labs Backpack", (
    "Product is not displayed in the cart page")
