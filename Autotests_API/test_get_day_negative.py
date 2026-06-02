import data
import receive_data


def test_check_date_by_method_GET():
    response = receive_data.check_get_date_by_method_GET(data.valid_common_date)

    assert response.status_code == 405

    # В ответе нет JSON, а есть HTML
    # Не вариант: body_data = health_response.json()
    # Проверить что в полученном ответе содержится определённый текст
    assert "405 Method Not Allowed" in response.text


def test_send_date_with_0_symbol_empty_string():
    response = receive_data.check_get_date(data.date_0_symbols_empty_string)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_1_symbol():
    response = receive_data.check_get_date(data.date_1_symbol)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_5_symbols():
    response = receive_data.check_get_date(data.date_5_symbols)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_8_symbols():
    response = receive_data.check_get_date(data.date_8_symbols)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_9_symbols():
    response = receive_data.check_get_date(data.date_9_symbols)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_11_symbols():
    response = receive_data.check_get_date(data.date_11_symbols)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_12_symbols():
    response = receive_data.check_get_date(data.date_12_symbols)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_45_symbols():
    response = receive_data.check_get_date(data.date_45_symbols)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_without_dots():
    response = receive_data.check_get_date(data.date_without_dots)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_onle_one_dot():
    response = receive_data.check_get_date(data.date_with_only_one_dot)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_three_dots():
    response = receive_data.check_get_date(data.date_with_three_dots)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_letters_in_the_beginning():
    response = receive_data.check_get_date(data.date_with_letters_in_the_beginning)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_letters_in_center():
    response = receive_data.check_get_date(data.date_with_letters_in_center)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_letters_in_the_ending():
    response = receive_data.check_get_date(data.date_with_letters_in_the_ending)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_letters_instead_of_date():
    response = receive_data.check_get_date(data.date_with_dots_instead_of_date)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_specials_in_the_beginning():
    response = receive_data.check_get_date(data.date_with_specials_in_the_beginning)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_specials_in_center():
    response = receive_data.check_get_date(data.date_with_specials_in_center)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_specials_in_the_ending():
    response = receive_data.check_get_date(data.date_with_specials_in_the_ending)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_specials_instead_of_date():
    response = receive_data.check_get_date(data.date_with_specials_instead_of_date)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_spaces_in_the_beginning():
    response = receive_data.check_get_date(data.date_with_spaces_in_the_beginning)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_spaces_in_center():
    response = receive_data.check_get_date(data.date_with_spaces_in_center)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_spaces_in_the_ending():
    response = receive_data.check_get_date(data.date_with_spaces_in_the_ending)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_spaces_instead_of_date():
    response = receive_data.check_get_date(data.date_with_spaces_instead_of_date)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_date_with_incorrect_type_in_date():
    response = receive_data.check_get_date(data.date_with_incorrect_type)

    assert response.status_code == 400
    ## Будет статус-код 500: Заведён баг-репорт

    body_data = response.json()

    assert body_data["error"] == "Некорректная дата"
    assert body_data["success"] == False


def test_send_request_with_empty_object():
    response = receive_data.check_get_date(data.request_with_empty_object)

    assert response.status_code == 400

    body_data = response.json()

    assert body_data["error"] == "Дата не передана"
    assert body_data["success"] == False
