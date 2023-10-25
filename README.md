# Allure Results Publisher

Утилита для публикации результатов тестирования в [Allure Report Service](https://github.com/Gwinkamp/allure-report-service)

## Установка

```bash
pip install \
    --index-url https://registry.astralnalog.ru/repository/pypi-edo/simple/ \
    --extra-index-url https://pypi.org/simple \
    allure-publisher
```

## Запуск

Справка:
```bash
python -m allure_publisher --help
```

Пример запуска:
```bash
python -m allure_publisher http://localhost:1155 path/to/results 
```
