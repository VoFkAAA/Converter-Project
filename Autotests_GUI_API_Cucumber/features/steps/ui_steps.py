from behave import given, when, then
import data

@given('я кликнул по полю ввода')
def step_open_page(context):
    context.page.wait_for_selector(data.Input_Field_Selector)

@given('включена светлая тема')
def light_theme_is_ON(context):
    context.page.wait_for_selector(data.Switch_Theme_Button_Selector, timeout=2000)
    body = context.page.locator("body")
    class_name = body.get_attribute("class") or ""
    # Переключить, если изначально тема тёмная
    if "dark" in class_name:
        context.page.locator(data.Switch_Theme_Button_Selector).click()
        # Ожидание применения темы
        context.page.wait_for_timeout(1000)  
        body = context.page.locator("body")
        class_name = body.get_attribute("class") or ""
    assert "dark" not in class_name, f"Тема: {class_name}"

@given('включена тёмная тема')
def dark_theme_is_ON(context):
    context.page.wait_for_selector(data.Switch_Theme_Button_Selector, timeout=2000)
    body = context.page.locator("body")
    class_name = body.get_attribute("class") or ""
    if "dark" not in class_name:
        context.page.locator(data.Switch_Theme_Button_Selector).click()
        # Ожидание применения темы
        context.page.wait_for_timeout(1000)  
        body = context.page.locator("body")
        class_name = body.get_attribute("class") or ""
    assert "dark" in class_name

# ==========================================================================

@when('я ввожу дату "{digits}"')
def step_enter_date(context, digits):
    context.page.locator(data.Input_Field_Selector).fill(digits)

@when('я нажимаю кнопку "Конвертировать"')
def step_click_convert(context):
    context.page.locator(data.Convert_button_Selector).click()

@when('я нажимаю кнопку "Очистить поле"')
def click_clear_field_button(context):
    context.page.locator(data.Clear_Button_Selector).click()

@when('я нажимаю на кнопку "Сменить тему"')
def click_switch_theme_button(context):
    context.page.locator(data.Switch_Theme_Button_Selector).click()

@when('я обновляю страницу')
def refresh_page_after_convertation(context):
    context.page.reload()
    context.page.wait_for_selector(data.Input_Field_Selector)

# ==========================================================================

@then('я вижу результат содержащий "{expected_text}"')
def step_check_result(context, expected_text):
    context.page.wait_for_selector(data.Result_Text_Selector, timeout=3000)
    actual = context.page.locator(data.Result_Text_Selector).text_content()
    assert expected_text in actual

@then('я вижу сообщение об ошибке содержащее "{expected_text}"')
def step_check_error(context, expected_text):
    context.page.wait_for_selector(data.Error_Message_Selector, timeout=3000)
    actual = context.page.locator(data.Error_Message_Selector).text_content()
    assert expected_text in actual

@then('я вижу что кнопка неактивна')
def check_convert_button_disabled(context):
    conv_button = context.page.locator(data.Convert_button_Selector)
    assert not conv_button.is_enabled(), "Кнопка должна быть неактивна"

@then('поле ввода очищается')
def input_field_is_empty(context):
    field_is_empty = context.page.locator(data.Input_Field_Selector).get_attribute("value")
    assert field_is_empty == "" or field_is_empty is None

@then('тема меняется на тёмную')
def dark_theme_is_ON(context):
    body = context.page.locator("body")
    class_name = body.get_attribute("class")
    assert "dark" in class_name

@then('тема меняется на светлую')
def light_theme_is_ON(context):
    context.page.wait_for_selector(data.Switch_Theme_Button_Selector, timeout=2000)
    body = context.page.locator("body")
    class_name = body.get_attribute("class") or ""
    assert "dark" not in class_name, f"Тема: {class_name}"

@then('результат конвертации исчезает')
def convertation_result_disappears(context):
    convertation_result = context.page.locator(data.Result_Text_Selector)
    # Проверить, что результат исчез (не виден)
    assert not convertation_result.is_visible()
