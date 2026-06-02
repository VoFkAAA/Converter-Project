from playwright.sync_api import sync_playwright
import data


def test_valid_data_common_date():
    with sync_playwright() as p:
        # Открыть браузер (Chromium)
        browser = p.chromium.launch(headless=False)
        # Открыть страницу в браузере
        page = browser.new_page()
        # Перейти по адресу:
        page.goto(data.Base_URL)

        # Найти элемент
        input_field = page.locator(data.Input_Field_Selector)

        page.wait_for_timeout(1000)

        # Ввести текст
        input_field.fill("15031975")

        page.wait_for_timeout(1000)

        # Нажать на кнопку "Конвертировать"
        button_convert = page.locator(data.Convert_button_Selector)
        button_convert.click()

        # Получить текст элемента
        result_element = page.locator(data.Result_Text_Selector)
        page.wait_for_selector(data.Result_Text_Selector, timeout=3000)
        actual_result = result_element.text_content()

        # Проверить результат
        assert "15.03.1975 → суббота" in actual_result

        # Посмотреть на результат - необязательно, влияет на скорость выполнения
        page.wait_for_timeout(1000)

        # Закрыть браузер
        browser.close()


def test_clear_date_field():
    with sync_playwright() as p:
        # Открыть браузер (Chromium)
        browser = p.chromium.launch(headless=False)
        # Открыть страницу в браузере
        page = browser.new_page()
        # Перейти по адресу:
        page.goto(data.Base_URL)

        # Найти элемент
        input_field = page.locator(data.Input_Field_Selector)

        page.wait_for_timeout(1000)

        # Ввести текст
        input_field.fill("15041970")

        page.wait_for_timeout(1000)

        # Нажать кнопку "Очистить поле"
        clear_field_button = page.locator(data.Clear_Button_Selector)
        clear_field_button.click()

        # Получить текст элемента
        result_element = page.locator(data.Input_Field_Selector)
        page.wait_for_selector(data.Input_Field_Selector, timeout=3000)
        actual_result = result_element.text_content()

        # Проверить результат
        assert actual_result == ""

        # Посмотреть на результат - необязательно, влияет на скорость выполнения
        page.wait_for_timeout(1000)

        # Закрыть браузер
        browser.close()


def test_switch_theme():
    with sync_playwright() as p:
        # Открыть браузер (Chromium)
        browser = p.chromium.launch(headless=False)
        # Открыть страницу в браузере
        page = browser.new_page()
        # Перейти по адресу:
        page.goto(data.Base_URL)

        theme_button = page.locator(data.Switch_Theme_Button_Selector)

        # Запомнить, какой класс у body до нажатия
        body = page.locator("body")
        original_theme = body.get_attribute("class")

        # Нажать на кнопку "Сменить тему"
        theme_button.click()

        # Проверить, что класс изменился (добавился dark)
        new_theme = body.get_attribute("class")

        # Проверить, что class изменился:
        # Если был dark — убрался, если не было — добавился
        assert original_theme != new_theme

        # Можно проверить конкретно:
        # Но тогда надо учитывать, какой class был изначально

        # if "dark" in original_class:
        # assert "dark" not in new_class
        # else:
        # assert "dark" in new_class

        # Посмотреть на результат - необязательно, влияет на скорость выполнения
        page.wait_for_timeout(1000)

        # Закрыть браузер
        browser.close()


# test_03_ui.py (или добавить в test_01_positive.py)


def test_refresh_page_without_convertation():
    with sync_playwright() as p:
        # Открыть браузер (Chromium)
        browser = p.chromium.launch(headless=False)
        # Открыть страницу в браузере
        page = browser.new_page()
        # Перейти по адресу:
        page.goto(data.Base_URL)

        input_field = page.locator(data.Input_Field_Selector)
        input_field.fill("15031975")

        page.wait_for_timeout(500)

        # Обновить страницу
        page.reload()

        # Проверить, что поле очистилось
        input_field_after_reload = page.locator(data.Input_Field_Selector)
        actual_value = input_field_after_reload.get_attribute("value")

        # Проверить, что поле очистилось
        assert actual_value == "" or actual_value is None

        browser.close()


def test_refresh_page_after_convertation():
    with sync_playwright() as p:
        # Открыть браузер (Chromium)
        browser = p.chromium.launch(headless=False)
        # Открыть страницу в браузере
        page = browser.new_page()
        # Перейти по адресу:
        page.goto(data.Base_URL)

        input_field = page.locator(data.Input_Field_Selector)
        input_field.fill("15031975")

        page.wait_for_timeout(500)

        button_convert = page.locator(data.Convert_button_Selector)
        button_convert.click()

        result_area = page.locator(data.Result_Text_Selector)
        page.wait_for_selector(data.Result_Text_Selector)
        actual_result = result_area.text_content()

        assert "15.03.1975" in actual_result
        assert "суббота" in actual_result

        # Обновить страницу
        page.reload()

        # Проверить, что поле очистилось
        input_field_after_reload = page.locator(data.Input_Field_Selector)
        actual_value = input_field_after_reload.get_attribute("value")

        # Проверить, что поле очистилось
        assert actual_value == "" or actual_value is None

        browser.close()
