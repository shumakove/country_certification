import time
import datetime
import random
from framework.proxy import *

def generate_name_from_date():
    # List of sample words
    words = ['Falcon', 'Shadow', 'Blaze', 'Nova', 'Echo', 'Storm', 'Phoenix']

    # Pick a random word
    word = random.choice(words)

    # Generate a random 3-digit number
    number = random.randint(100, 999)

    # Combine word and number
    name = f"{word}{number}"
    return name

def create_position(page) -> str:
    position_id = generate_name_from_date()
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("combobox", name="Search Workday").fill("Create position")
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    page.get_by_role("link", name="Create position").click()
    page.get_by_role("textbox", name="Supervisory Organization").click()
    page.get_by_role("textbox", name="Supervisory Organization").fill("Celergo_Master_Division")
    page.get_by_role("textbox", name="Supervisory Organization").press("Enter")
    time.sleep(2)
    page.get_by_role("button", name="OK").click()

    page.get_by_role("textbox", name="Job Posting Title").click()
    page.get_by_role("textbox", name="Job Posting Title").fill(position_id)

    month = 1
    year = datetime.datetime.now().year
    page.locator('[data-automation-id="dateSectionDay-input"]').nth(0).click()
    time.sleep(1)
    page.keyboard.press("1")
    page.locator('[data-automation-id="dateSectionMonth-input"]').nth(0).click()
    time.sleep(1)
    for char in str(month):
        page.keyboard.press(char)
    page.locator('[data-automation-id="dateSectionYear-input"]').nth(0).click()
    time.sleep(1)
    for char in str(year):
        page.keyboard.press(char)
    
    page.locator('[data-automation-id="dateSectionDay-input"]').nth(1).click()
    time.sleep(1)
    page.keyboard.press("1")
    page.locator('[data-automation-id="dateSectionMonth-input"]').nth(1).click()
    time.sleep(1)
    for char in str(month):
        page.keyboard.press(char)
    
    page.locator('[data-automation-id="dateSectionYear-input"]').nth(1).click()
    time.sleep(1)
    for char in str(year):
        page.keyboard.press(char)
    



#    page.get_by_role("textbox", name="Job Family").click()
#    page.get_by_role("textbox", name="Job Family").fill("FA-Risk Management")
#    page.get_by_role("textbox", name="Job Family").press("Enter")

    page.get_by_role("textbox", name="Job Profile").click()
    page.get_by_role("textbox", name="Job Profile").fill("Tax Director")
    page.get_by_role("textbox", name="Job Profile").press("Enter")

    page.get_by_role("textbox", name="Location").click()
    page.get_by_role("textbox", name="Location").fill("Cape town")
    page.get_by_role("textbox", name="Location").press("Enter")

    page.get_by_role("textbox", name="Time Type").click()
    page.get_by_role("textbox", name="Time Type").fill("Full time")
    page.get_by_role("textbox", name="Time Type").press("Enter")

    page.get_by_role("textbox", name="Worker Type").click()
    page.get_by_role("textbox", name="Worker Type").fill("Employee")
    page.get_by_role("textbox", name="Worker Type").press("Enter")




    page.get_by_role("button", name="Submit").click()
    time.sleep(4)
    return position_id

def aprove_position(page, position_name):

    start_proxy(page)
    page.get_by_role("button", name="My Tasks Items").click()
    page.get_by_role("textbox", name="Search: All Items").click()
    page.get_by_role("textbox", name="Search: All Items").fill(position_name)
    page.get_by_role("textbox", name="Search: All Items").press("Enter")
    time.sleep(5)
    

    # Enter Company
    page.get_by_label("Company", exact=True).locator("li").click()
    page.locator('[data-automation-id="searchBox"]').fill("Fox Broadcasting")
    page.locator('[data-automation-id="searchBox"]').press("Enter")
    time.sleep(1)
    page.locator('[data-automation-id="saveButton"]').nth(1).click()

    # Enter cost center
    page.get_by_label("Cost Center", exact=True).locator("li").click()
    page.locator('[data-automation-id="searchBox"]').fill("32100 R&D - Product Strategy")
    page.locator('[data-automation-id="searchBox"]').press("Enter")
    time.sleep(1)
    page.locator('[data-automation-id="saveButton"]').nth(2).click()

    # Enter region
    page.get_by_label("Region", exact=True).locator("li").click()
    page.locator('[data-automation-id="searchBox"]').fill("APA - Australia")
    page.locator('[data-automation-id="searchBox"]').press("Enter")
    time.sleep(1)
    page.locator('[data-automation-id="saveButton"]').nth(3).click()

    page.get_by_role("button", name="Submit").click()
    time.sleep(3)
    page.locator('[data-automation-id="closeButton"]').click()
    stop_proxy(page)
    time.sleep(2)