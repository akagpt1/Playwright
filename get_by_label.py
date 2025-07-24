from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto("https://upsc.gov.in/feedback")
    # page.screenshot(path='Playwright/screenshots/screenshot.png')

    name_input=page.get_by_label("Name")
    # name_input.highlight()
    name_input.fill("test")
    page.get_by_label("Email Address").fill("test@uk.in")
    page.get_by_label("Feedback ").fill("This is important to bring your attention")
    page.get_by_label("What code is in the image? ").highlight()
