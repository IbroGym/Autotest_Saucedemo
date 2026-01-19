import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from logging_config import setup_logger
from datetime import datetime

@pytest.fixture
def logger():
    return setup_logger()

@pytest.fixture
def driver(logger):
    logger.info("=== Browser session START ===")

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("prefs", {
        
    # отключает всплывашки паролей
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,

    # отключает "password leak detection" / password check
    "profile.password_manager_leak_detection": False,

    # иногда помогает убрать разные подсказки/инфобары
    "autofill.profile_enabled": False,
    "autofill.credit_card_enabled": False,
})

    options.add_argument("--window-size=1400,900")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(0)

    yield driver

    logger.info("=== Browser session END ===")
    driver.quit()

# Hook pytest: catching FAIL and logging
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        logger = item.funcargs.get("logger", None)
        driver = item.funcargs.get("driver", None)

        if logger:
            logger.error(f"TEST FAILED: {item.name}")
            if call.excinfo:
                logger.error(f"EXCEPTION: {call.excinfo.value}")

        # Screenshot on failure
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{ts}.png"
            path = os.path.join("screenshots", filename)
            driver.save_screenshot(path)

            if logger:
                logger.error(f"SCREENSHOT SAVED: {path}")

            # Attach screenshot to pytest-html report if plugin is enabled
            extra = getattr(report, "extra", [])
            try:
                import pytest_html  # type: ignore
                extra.append(pytest_html.extras.png(path))
                report.extra = extra
            except Exception:
                pass