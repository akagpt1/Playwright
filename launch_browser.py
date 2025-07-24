from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    #Launch a browser
    browser=playwright.chromium.launch(headless=False,slow_mo=1000)
    #create a new page
    page=browser.new_page()
    page.goto("https://playwright.dev/python/")

    #Locate a link element
    link=page.get_by_role('link',name="GET STARTED")
    link.highlight()
    link.click()

    #Get the URL
    print("GetStarted:",page.title())
    browser.close()