# Конвертер 

### Pet-проект: приложение для конвертации даты в день недели.  

Приложение развёрнуто на [Amvera Cloud](https://amvera.ru) — облаке для хостинга ботов, сайтов и других IT-приложений.

#### Приложение: 

https://converter-project-vofka.amvera.io

#### Swagger: 

https://converter-project-vofka.amvera.io/swagger  
**⚠️ Примечание:** *Из-за особенностей обработки сертификата может отобразиться ошибка «Подключение не защищено. Возможно, злоумышленники пытаются похитить вашу информацию...». В этом случае можно перейти на страницу https://converter-project-vofka.amvera.io, а затем допечатать "swagger"*.

#### Kaiten:

https://projectsdesk.kaiten.ru/p/d4f3fa93-290f-4a6c-9665-2c8fae9b3e46 

#### Документация (чек-листы, тест-кейсы, баг-репорты, вопросы/предложения): 

https://docs.google.com/spreadsheets/d/1nbOnGE4f6kM6eiIE-QPPEszQCJDUO2Jvz7EkFdKYpoY/edit?usp=sharing

Для проверки приложения был спроектирован чек-лист, на основе которого были спроектированы тест-кейсы для функциональных проверок. Остальные проверки (UI/UX) оставлены в чек-листе. 

#### Отчет о тестировании:

https://docs.google.com/document/d/1SZhydd8rQ6LXUyPuJxZICe8V2Rjl7SW8u9P_017VhDQ/edit?usp=sharing 

#### Структура проекта: 

```
Converter-Project/
│
├── app.py                  # Основной файл приложения (Flask)
├── README.md               # Описание проекта
├── requirements.txt        # Зависимости Python
├── Product_Requirements.md # Требования
├── amvera.yml              # Конфигурационный файл для запуска на Amvera
│
├── templates/
│ └── index.html            # Фронтенд (HTML/CSS/JS)
│
├── Autotests_API/
│ ├── config.py                 # Конфигурация тестов (URL, эндпоинты)
│ ├── data.py                   # Тестовые данные
│ ├── receive_data.py           # Отправка запросов к API
│ ├── test_check_health.py      # Тесты /health
│ ├── test_get_day_positive.py  # Позитивные тесты /get_day
│ └── test_get_day_negative.py  # Негативные тесты /get_day
│
├── Autotests_GUI/
│ ├── data.py                   # Селекторы и тестовые данные
│ ├── test_01_positive.py       # Позитивные UI-тесты
│ └── test_02_negative.py       # Негативные UI-тесты
│
├── Autotests_GUI_API_Cucumber/         # BDD-тесты (Cucumber/Behave)
│   ├── data.py                         # Тестовые данные
│   └── features/
│       ├── environment.py              # Настройки окружения (before_all, after_all)
        ├── receive_data.py             # API-запросы и ответы
│       ├── API/                        # API-тесты в Gherkin
│       │   ├── get_day.feature
│       │   └── health_check.feature
│       ├── GUI/                        # GUI-тесты в Gherkin
│       │   ├── positive_scen_converter.feature
│       │   └── negative_scen_converter.feature
│       └── steps/
│           └── ui_steps.py             # Шаги для GUI-тестов
|
├── Screenshots/                        # Скриншоты состояний приложения
│ ├── Скриншоты состояний приложения с учётом светлой/тёмной темы
│ 
├── Converter-Project.postman_collection.json   # Коллекция автотестов Postman
└── CHARLES_Map_Local_Mock_Error_Response.txt   # Мок-файл для эмуляции ошибки сети
```

#### Установка и Запуск

Проверить наличие Python (требуется версия 3.11 или выше):

```bash
python --version
```

Установить Python:  
**https://www.python.org/downloads/**

Установить зависимости: 

```bash
pip install -r requirements.txt
```

Установить браузер для Playwright:
```bash
playwright install
```

Запустить автотесты API:
```bash
pytest test_check_health.py test_get_day_positive.py test_get_day_negative.py
```

Запустить автотесты GUI:
```bash
pytest test_01_positive.py test_02_negative.py
```

Установка зависимостей для BDD-тестов (Cucumber/Behave):
```bash
pip install behave playwright
```
```bash
playwright install chromium
```  

Запуск GUI-автотестов BDD (Cucumber/Behave):
```bash
behave features/GUI/
```

Запуск API-автотестов BDD (Cucumber/Behave):
```bash
behave features/API/
```

#### Технологии

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (без фреймворков)
- **API-документация:** Swagger (Flasgger)
- **Деплой:** Amvera
- **Таск-трекер:** Kaiten
- **Тестирование:** Postman, Charles, DevTools
- **Автотесты API:** Python + pytest
- **Автотесты GUI:** Python + Playwright + pytest
- **Автотесты BDD:** Cucumber + Behave + Playwright
- **Репозиторий:** GitHub и GitFlic 
