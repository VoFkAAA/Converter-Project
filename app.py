from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flasgger import Swagger, swag_from
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

# Swagger конфигурация
app.config["SWAGGER"] = {
    "title": "Date to Weekday Converter API",
    "description": "Конвертирует дату в день недели",
    "version": "1.0.0",
    "termsOfService": "",
    "contact": {"name": "QA Project", "email": "qa@example.com"},
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

swagger = Swagger(app, config=swagger_config)

# Дни недели на русском
WEEKDAYS_RU = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}


def validate_date(date_str):
    """
    Валидация даты (с учётом багов, заложенных в требованиях)
    БАГ №1: можно ввести буквы (но мы их отфильтруем для расчёта)
    БАГ №2: можно ввести день 00 (валидация пропустит)
    """
    # Очищаем от всего, кроме цифр и точек
    cleaned = re.sub(r"[^\d\.]", "", date_str)

    # Проверка формата (баг: буквы могли попасть, но мы их удалили)
    pattern = r"^(\d{2})\.(\d{2})\.(\d{4})$"
    match = re.match(pattern, cleaned)

    if not match:
        return False, None, None, None

    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))

    # БАГ №2: день 00 считается валидным (нарушение требований)
    # Пропускаем 00 без ошибки

    # Год должен быть в диапазоне 1900-2100
    if year < 1900 or year > 2100:
        return False, None, None, None

    # Месяц 1-12
    if month < 1 or month > 12:
        return False, None, None, None

    # Проверка дня с учётом месяца и високосности
    # БАГ №2: день 00 всегда валидный (пропускаем)
    if day == 0:
        return True, day, month, year

    if day < 1 or day > 31:
        return False, None, None, None

    # Дни в месяцах
    days_in_month = [
        31,
        29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]

    if day > days_in_month[month - 1]:
        return False, None, None, None

    return True, day, month, year


@app.route("/")
def index():
    """Главная страница"""
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health_check():
    """
    Проверка работоспособности сервиса
    ---
    responses:
      200:
        description: Сервис работает
        schema:
          type: object
          properties:
            status:
              type: string
              example: ok
    """
    return jsonify({"status": "ok", "message": "Converter is running"})


@app.route("/get_day", methods=["POST"])
def get_day():
    """
    Конвертирует дату в день недели
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            date:
              type: string
              example: "15.03.2024"
    responses:
      200:
        description: Успешная конвертация
        schema:
          type: object
          properties:
            success:
              type: boolean
            weekday:
              type: string
            date:
              type: string
      400:
        description: Ошибка валидации
        schema:
          type: object
          properties:
            success:
              type: boolean
            error:
              type: string
    """
    data = request.get_json()
    if not data or "date" not in data:
        return jsonify({"success": False, "error": "Дата не передана"}), 400

    date_str = data["date"]
    is_valid, day, month, year = validate_date(date_str)

    if not is_valid:
        return jsonify({"success": False, "error": "Некорректная дата"}), 400

    # БАГ №2: для дня 00 возвращаем фиктивный день недели
    if day == 0:
        # Баг: возвращаем "ошибка" при дне 00
        return jsonify({"success": False, "error": "Некорректная дата"}), 400

    try:
        dt = datetime(year, month, day)
        weekday_num = dt.weekday()  # 0 = понедельник
        weekday_ru = WEEKDAYS_RU[weekday_num]

        return jsonify(
            {
                "success": True,
                "weekday": weekday_ru,
                "date": f"{day:02d}.{month:02d}.{year}",
            }
        )
    except ValueError:
        return jsonify({"success": False, "error": "Некорректная дата"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
