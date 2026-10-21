from datetime import datetime

import allure
import pytest
from loguru import logger

from common.logger import ConfigurateLogger
from configs.config import Config


@pytest.fixture(scope="session")
def project_config():
    return Config()


@pytest.fixture(autouse=True, scope="session")
def log(project_config):
    ConfigurateLogger(project_config)


# The browser is chosen with the standard pytest-playwright option: --browser chromium|firefox|webkit (chromium by default),
# the browser window with --headed (headless by default). We only add the language.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


# Browser language (analog of intl.accept_languages) - set through the context locale
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    return {
        **browser_context_args,
        "locale": pytestconfig.getoption("language"),
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Screenshot on failure in setup or in the test body (as in android-graypart-autotests)
    if rep.when in ("setup", "call") and rep.failed:
        logger.error(f"[{item.nodeid}] {rep.when} failed:\n{rep.longreprtext}")
        page = item.funcargs.get("page")
        if page is not None:
            take_screenshot(page, item.nodeid)


# screenshot named with the test, date and time - attached to the allure report
def take_screenshot(page, node_id):
    screenshot_name = f'{node_id}_{datetime.today().strftime("%Y-%m-%d_%H-%M")}.png'
    logger.error(f"Screenshot name - {screenshot_name}")
    try:
        screenshot_png = page.screenshot()
    except Exception as e:
        logger.warning(f"Failed to take screenshot for {node_id}: {e}")
        return

    allure.attach(
        screenshot_png,
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG,
    )
