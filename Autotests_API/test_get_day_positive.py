import data
import config
import receive_data


def test_check_valid_common_date():
    response = receive_data.check_get_date(data.valid_common_date)

    assert response.status_code == 200

    body_data = response.json()

    assert body_data["date"] == "15.03.1975"
    assert body_data["success"] == True
    assert body_data["weekday"] == "суббота"

    assert isinstance(body_data["date"], str)
    assert isinstance(body_data["success"], bool)
    assert isinstance(body_data["weekday"], str)


def test_check_send_double_parameter_date():
    response = receive_data.check_get_date(data.double_param_date_same_dates)

    assert response.status_code == 200

    body_data = response.json()

    assert body_data["date"] == "15.03.1975"
    assert body_data["success"] == True
    assert body_data["weekday"] == "суббота"

    assert isinstance(body_data["date"], str)
    assert isinstance(body_data["success"], bool)
    assert isinstance(body_data["weekday"], str)


def test_check_send_double_parameter_different_dates():
    response = receive_data.check_get_date(data.double_param_date_different_dates)

    assert response.status_code == 200

    body_data = response.json()

    assert body_data["date"] == "01.07.1980"
    assert body_data["success"] == True
    assert body_data["weekday"] == "вторник"

    assert isinstance(body_data["date"], str)
    assert isinstance(body_data["success"], bool)
    assert isinstance(body_data["weekday"], str)
