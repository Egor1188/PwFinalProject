# PwFinalProject
Порт учебного проекта SelFinalProject (Selenium) на Playwright + pytest.

## Установка
```
pip install -r requirements.txt
playwright install chromium firefox
```

## Запуск
```
pytest                               # chromium, en, headless
pytest --browser firefox             # firefox
pytest --headed                      # с окном браузера
pytest --language ru                 # язык браузера
pytest -m login_test                 # только тесты перехода на логин
```
