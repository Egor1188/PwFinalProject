import pytest


# Браузер выбирается штатным параметром pytest-playwright: --browser chromium|firefox|webkit (по умолчанию chromium),
# окно браузера — --headed (по умолчанию headless). Добавляем только язык.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


# Язык браузера (аналог intl.accept_languages) — задаём через locale контекста
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, pytestconfig):
    return {
        **browser_context_args,
        "locale": pytestconfig.getoption("language"),
        "viewport": {"width": 1920, "height": 1080},
    }
