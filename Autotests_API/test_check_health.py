import receive_data


def test_positive_check_service_health_by_method_GET():
    health_response = receive_data.check_service_health()

    assert health_response is not None, "Упс... Сервер почему-то недоступен"

    assert health_response.status_code == 200

    body_data = health_response.json()

    assert body_data["message"] == "Converter is running"
    assert body_data["status"] == "ok"


def test_negative_check_service_health_by_method_POST():
    health_response = receive_data.check_service_health_by_method_POST()

    assert health_response.status_code == 405

    # В ответе нет JSON, а есть HTML
    # Не вариант: body_data = health_response.json()
    # Проверить что в полученном ответе содержится определённый текст
    assert "405 Method Not Allowed" in health_response.text
