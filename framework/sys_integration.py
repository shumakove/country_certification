import time

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

    page.get_by_role("row").filter(has_text="Pay GroupSpecify ValueSpecify").get_by_placeholder("Search").click()
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").fill("GPC_SOUTH_AFRICA_PECI")
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").press("Enter")
    time.sleep(1)

    page.get_by_role("row").filter(has_text="Pay Group MembersSpecify").get_by_placeholder("Search").click()
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").click()
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").fill("27874")
    page.get_by_role("group").filter(has_text="Options Expanded").get_by_placeholder("Search").press("Enter")
    #TODO Implement several members in one sys integration
    #TODO Implement incremental last successful run date picking
    page.get_by_role("button", name="OK").click()

def launch_process_monitor(page):
    page.get_by_role("button", name="clear search").click()
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("combobox", name="Search Workday").fill("process monitor")
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    page.get_by_role("link", name="Process Monitor", exact=True).click()
    page.get_by_role("textbox", name="Process Type").click()
    page.get_by_role("textbox", name="Process Type").fill("integration")
    page.get_by_role("textbox", name="Process Type").press("Enter")
    page.get_by_text("Integration", exact=True).click()
    page.get_by_role("button", name="OK").click()

    #TODO Implement time waiting for sys integration complete
    page.get_by_role("button", name="Refresh GPC_South Africa_PECI").click()
    page.get_by_role("tablist").get_by_text("Output Files (9)").click()
    page.get_by_role("link", name="WDI_SWDAY_20250627141229_ZAPECI_HRMD00 (GPC_SOUTH_AFRICA_PECI).xml").click(button="right")
    #TODO Implement downloader to test folder