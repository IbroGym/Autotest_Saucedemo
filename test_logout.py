from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, wait):
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory.html"))


def test_logout(driver):
    
    wait = WebDriverWait(driver, 10)

    # Preconditions: user is logged in
    login(driver, wait)

    # Step 1: Open burger menu
    menu_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_btn.click()

    # Step 2: Click Logout
    logout_link = wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    # Checkpoint 1: URL is login page
    wait.until(EC.url_to_be("https://www.saucedemo.com/"))
    assert driver.current_url == "https://www.saucedemo.com/"

    # Checkpoint 2: Login button is visible
    login_button = wait.until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert login_button.is_displayed()
