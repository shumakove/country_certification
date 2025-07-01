import time
from playwright.sync_api import expect
def launch_sys_integrtion(page, integration_name):
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("combobox", name="Search Workday").fill("intsys:" + integration_name)
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    time.sleep(3)
  
    page.get_by_role("link", name="GPC_South Africa_PECI").click()
    time.sleep(1)
    page.locator('[data-automation-id="relatedIconContainer"]').click()
    time.sleep(3)
    page.get_by_role("menuitem", name="Integration", exact=True).click()
    time.sleep(3)
    page.get_by_role("button", name="OK").click()

    page.get_by_role("button", name="Toggle Fullscreen Viewing Mode").click()
    page.locator('[data-automation-id="promptIcon"]').nth(0).click()
    page.get_by_role("row").filter(has_text="Pay GroupSpecify ValueSpecify").get_by_placeholder("Search").fill("GPC_SOUTH_AFRICA_PECI")
    page.get_by_role("row").filter(has_text="Pay GroupSpecify ValueSpecify").get_by_placeholder("Search").press("Enter")
    time.sleep(1)
    
    page.get_by_role("row").filter(has_text="Pay Group MembersSpecify").get_by_placeholder("Search").click(force=True)
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").click(force=True)
    locator = page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search")
    expect(locator).to_be_enabled()
    locator.fill("27874")
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").press("Enter")
    time.sleep(1)
    page.get_by_role("group").filter(has_text="Options").get_by_placeholder("Search").click()
    page.get_by_role("group").filter(has_text="Options").get_by_placeholder("Search").fill("27875")
    page.get_by_role("group").filter(has_text="Options").get_by_placeholder("Search").press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Toggle Fullscreen Viewing Mode").click()
    page.get_by_role("button", name="OK").click()

def launch_process_monitor(page):
    #page.get_by_role("button", name="clear search").click()
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("combobox", name="Search Workday").fill("process monitor")
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    page.get_by_role("link", name="Process Monitor", exact=True).click()
    page.get_by_role("textbox", name="Process Type").click()
    page.get_by_role("textbox", name="Process Type").fill("integration")
    page.get_by_role("textbox", name="Process Type").press("Enter")
    page.get_by_text("Integration", exact=True).click()
    page.get_by_role("textbox", name="Status").click()
    page.get_by_role("textbox", name="Status").fill("Processing")
    page.get_by_role("textbox", name="Status").press("Enter")
    page.get_by_label("Processing checkbox Not").get_by_text("Processing").click()

    page.get_by_role("button", name="OK").click()
 
    page.get_by_role("button", name="Request Filter column").click()
    page.get_by_role("textbox", name="Value").click()
    page.get_by_label("Value, Options Expanded").get_by_text("GPC_South Africa_PECI").click()
    page.get_by_role("dialog", name="Request").locator("svg").nth(2).click()
    page.locator('[data-automation-id="uic_filterButton"]').click()
    #TODO Implement time waiting for sys integration complete
    page.locator('[data-automation-id="row"]').nth(0).locator('[data-automation-id="cell"]').nth(4).click()
    
  
    start_time = time.time()
    target = page.locator('[data-automation-label="Completed"]')
    refresh_button = page.get_by_role("button", name="Refresh GPC_South Africa_PECI")

    while True:
        try:
            if target.is_visible():
                print("Элемент найден.")
                break
        except:
            pass  # элемент может не существовать ещё

        if time.time() - start_time > 3600:
            raise TimeoutError("Элемент не появился в течение заданного времени.")

        print("Элемент не найден. Нажимаем Refresh...")
        refresh_button.click()
        time.sleep(3)

    page.get_by_role("tab").nth(3).click()
    page.get_by_role("button", name="Type Sort and filter column").click()
    page.get_by_role("textbox", name="Value").click()
    page.get_by_role("option", name="XML Document (XML) checkbox").get_by_role("checkbox").check()
    page.get_by_role("button", name="Filter", exact=True).click()
    page.get_by_role("button", name="Filter", exact=True).click()
    time.sleep(10)
    #TODO Implement downloader to test folder