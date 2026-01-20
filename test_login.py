from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver, logger):

    wait = WebDriverWait(driver, 10)

    logger.info("Test Start: test_login")
    logger.info("Step 1: Open login page")
    driver.get("https://www.saucedemo.com/")

    # Enter username
    logger.info("Step 2: Enter username")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")


    # Enter password
    logger.info("Step 3: Enter Password")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click Login
    logger.info("Step 4: Click Login")
    driver.find_element(By.ID, "login-button").click()

    # Checkpoint: URL contains inventory
    logger.info("Checkpoint: Verify inventory page is opened")
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url
