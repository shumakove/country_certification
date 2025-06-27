import time

def start_proxy(page):
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("button", name="clear search").click()
    page.get_by_role("combobox", name="Search Workday").fill("start proxy")
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    page.get_by_role("link", name="Start Proxy").click()
    page.get_by_role("textbox", name="User to Proxy As").click()
    page.get_by_role("textbox", name="User to Proxy As").fill("logan")
    page.get_by_role("textbox", name="User to Proxy As").press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="OK").click()
    time.sleep(1)

def stop_proxy(page):
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("combobox", name="Search Workday").fill("stop proxy")
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    page.get_by_role("link", name="Stop Proxy").click()
    page.locator('[data-automation-id="wd-CommandButton_uic_okButton"]').click()