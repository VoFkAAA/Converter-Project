from playwright.sync_api import sync_playwright
import data

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.base_url = data.Base_URL

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.goto(context.base_url)

def after_scenario(context, scenario):
    context.page.close()
    print("=== ENVIRONMENT.PY LOADED ===") 
