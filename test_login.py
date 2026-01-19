from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):

    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # Enter username
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click Login
    driver.find_element(By.ID, "login-button").click()

    # Checkpoint 1: URL contains inventory
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url

    # Checkpoint 2: inventory container is visible
    inventory = wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))
    assert inventory.is_displayed()
