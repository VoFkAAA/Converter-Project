from playwright.sync_api import sync_playwright
import data


def test_date_with_00_in_day():
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
        input_field.fill("00031975")

        page.wait_for_timeout(1000)

        # Нажать на кнопку "Конвертировать"
        button_convert = page.locator(data.Convert_button_Selector)
        button_convert.click()

        # Получить текст элемента
        result_element = page.locator(data.Error_Message_Selector)
        page.wait_for_selector(data.Error_Message_Selector, timeout=3000)
        actual_result = result_element.text_content()

        # Проверить результат
        assert "Некорректная дата" in actual_result
        assert (
            "в январе, марте, мае, июле, августе, октябре, декабре — 31 день"
            in actual_result
        )
        assert "в апреле, июне, сентябре, ноябре — 30 дней" in actual_result

        # Посмотреть на результат - необязательно, влияет на скорость выполнения
        page.wait_for_timeout(1000)

        # Закрыть браузер
        browser.close()


def test_date_with_00_in_month():
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
        input_field.fill("15001975")

        page.wait_for_timeout(1000)

        # Нажать на кнопку "Конвертировать"
        button_convert = page.locator(data.Convert_button_Selector)
        button_convert.click()

        # Получить текст элемента
        result_element = page.locator(data.Error_Message_Selector)
        page.wait_for_selector(data.Error_Message_Selector, timeout=3000)
        actual_result = result_element.text_content()

        # Проверить результат
        assert "Некорректная дата" in actual_result
        assert (
            "в январе, марте, мае, июле, августе, октябре, декабре — 31 день"
            in actual_result
        )
        assert "в апреле, июне, сентябре, ноябре — 30 дней" in actual_result

        # Посмотреть на результат - необязательно, влияет на скорость выполнения
        page.wait_for_timeout(1000)

        # Закрыть браузер
        browser.close()


def test_date_with_0000_in_year():
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
        input_field.fill("15030000")

        page.wait_for_timeout(1000)

        # Нажать на кнопку "Конвертировать"
        button_convert = page.locator(data.Convert_button_Selector)
        button_convert.click()

        # Получить текст элемента
        result_element = page.locator(data.Error_Message_Selector)
        page.wait_for_selector(data.Error_Message_Selector, timeout=3000)
        actual_result = result_element.text_content()

        # Проверить результат
        assert "Некорректная дата" in actual_result
        assert (
            "в январе, марте, мае, июле, августе, октябре, декабре — 31 день"
            in actual_result
        )
        assert "в апреле, июне, сентябре, ноябре — 30 дней" in actual_result

        # Посмотреть на результат - необязательно, влияет на скорость выполнения
        page.wait_for_timeout(1000)

        # Закрыть браузер
        browser.close()
