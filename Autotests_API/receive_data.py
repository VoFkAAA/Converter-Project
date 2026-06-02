import requests
import config

# ==========HEALTH==========


def check_service_health():
    return requests.get(f"{config.Base_URL}{config.endpoint_health}")


def check_service_health_by_method_POST():
    return requests.post(f"{config.Base_URL}{config.endpoint_health}")


# ==========GET_DAY==========


def check_get_date(payload):
    return requests.post(f"{config.Base_URL}{config.endpoint_get_day}", json=payload)


def check_get_date_by_method_GET(payload):
    return requests.get(f"{config.Base_URL}{config.endpoint_get_day}", json=payload)
