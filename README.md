# PwFinalProject
Port of the SelFinalProject study project (Selenium) to Playwright + pytest.

## Installation
```
pip install -r requirements.txt
playwright install chromium firefox
```

## Running
The tests that register a user need the password of the test user in the `TEST_USER_PASSWORD` environment variable
(in CI - the `TEST_USER_PASSWORD` repository secret):
```
export TEST_USER_PASSWORD='...'      # PowerShell: $env:TEST_USER_PASSWORD = '...'
```

```
pytest                               # chromium, en, headless
pytest --browser firefox             # firefox
pytest --headed                      # with a browser window
pytest --language ru                 # browser language
pytest -m login_test                 # only the tests for going to the login page
```

## Logging
Uses [loguru](https://github.com/Delgan/loguru) (`from loguru import logger`), configured in `conftest.py`:
- live console log (INFO and above) - loguru is propagated to `logging`, which pytest displays;
- full log (DEBUG) - in `var/logs/run_tests_log_<id>.log` (a new file for every run; settings in `configs/config.yml`).

```
pytest --log-cli-level=DEBUG         # verbose log in the console
pytest -o log_cli=false              # no log in the console
```
