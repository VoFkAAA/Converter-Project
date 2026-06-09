from behave import when, then
import receive_data

@when('я отправляю GET-запрос на "/health"')
def send_GET_health(context):
    context.response = receive_data.check_service_health()

@when('я отправляю POST-запрос на "/health"')
def send_POST_health(context):
    context.response = receive_data.check_service_health_by_method_POST()

@when('я отправляю POST-запрос с датой "{date_string}"')
def send_post_get_day(context, date_string):
    payload = {"date": date_string}
    context.response = receive_data.check_get_date(payload)

@when('я отправляю GET-запрос с датой "{date_string}"')
def send_get_get_day(context, date_string):
    payload = {"date": date_string}
    context.response = receive_data.check_get_date_by_method_GET(payload)

@when('я отправляю POST-запрос с дублированной датой "{date1}" и "{date2}"')
def send_post_duplicate_date(context, date1, date2):
    # Формируем JSON строку с дублирующимся ключом вручную
    json_string = f'{{"date": "{date1}", "date": "{date2}"}}'
    context.response = receive_data.check_get_date_raw(json_string)

# =============================================================================================

@then('статус-код ответа должен быть {status_code:d}')
def check_status(context, status_code):
    assert context.response.status_code == status_code

@then('тело ответа содержит message = "{expected_message}"')
def check_message(context, expected_message):
    body = context.response.json()
    assert body["message"] == expected_message

@then('тело ответа содержит status = "{expected_status}"')
def check_status_field(context, expected_status):
    body = context.response.json()
    assert body["status"] == expected_status 

@then('тело ответа содержит "{expected_text}"')
def body_contains_text(context, expected_text):
    assert expected_text in context.response.text, \
        f"'{expected_text}' не найдено в ответе"
    
@then('тело ответа содержит success = {expected_value}')
def check_success_field(context, expected_value):
    body = context.response.json()
    expected = expected_value.lower() == "true"
    assert body.get("success") == expected, \
        f"Ожидалось success = {expected_value}, получено {body.get('success')}"

@then('тело ответа содержит date = "{expected_date}"')
def check_date_field(context, expected_date):
    body = context.response.json()
    assert body.get("date") == expected_date, \
        f"Ожидалась дата {expected_date}, получена {body.get('date')}"

@then('тело ответа содержит weekday = "{expected_weekday}"')
def check_weekday_field(context, expected_weekday):
    body = context.response.json()
    assert body.get("weekday") == expected_weekday, \
        f"Ожидался день недели {expected_weekday}, получен {body.get('weekday')}"

@then('тело ответа содержит error = "{expected_error}"')
def check_error_field(context, expected_error):
    body = context.response.json()
    assert body.get("error") == expected_error, \
        f"Ожидалась ошибка '{expected_error}', получена '{body.get('error')}'"