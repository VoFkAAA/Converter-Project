import requests
import data 

def check_service_health():
    return requests.get(f"{data.Base_URL}{data.API_health}")

def check_service_health_by_method_POST():
    return requests.post(f"{data.Base_URL}{data.API_health}")

def check_get_date(payload):
    return requests.post(f"{data.Base_URL}{data.API_get_day}", json=payload)

def check_get_date_by_method_GET(payload):
    return requests.get(f"{data.Base_URL}{data.API_get_day}", json=payload)

def check_get_date_raw(json_string):
    return requests.post(f"{data.Base_URL}{data.API_get_day}", data=json_string, headers={"Content-Type": "application/json"})
