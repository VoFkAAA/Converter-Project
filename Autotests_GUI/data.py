# data.py

Base_URL = "https://converter-project.onrender.com"

API_health = "/health"
API_get_day = "/get_day"

# Селекторы (для API автотестов):

Input_Field_Selector = "//input[@id='dateInput']"
Convert_button_Selector = "//button[@id='convertBtn']"
Result_Text_Selector = "//div[@id='resultText']"
Error_Message_Selector = "//div[@id='errorMessage']"
Clear_Button_Selector = "//button[@id='clearBtn']"
Switch_Theme_Button_Selector = "//button[@id='themeBtn']"
