import time
import datetime
import random
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
    page.locator('[data-automation-id="datePickerButton"]').nth(0).click()
    page.locator('[data-automation-id="datePickerSelectedToday"]').click()
    time.sleep(1)
    page.locator('[data-automation-id="datePickerButton"]').nth(1).click()
    time.sleep(1)
    page.locator('[data-automation-id="datePickerSelectedToday"]').click()

    page.locator(".WIDF").first.click()
    page.get_by_role("button", name="Submit").click()
    time.sleep(4)
    return position_id

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

def submit_new_hire(page, position_id):
    # Open New Hire wizzard
    page.get_by_role("combobox", name="Search Workday").click()
    page.get_by_role("combobox", name="Search Workday").fill("Hire Employee")
    page.get_by_role("combobox", name="Search Workday").press("Enter")
    page.get_by_role("link", name="Hire Employee").click()

    # Basic information
    page.get_by_role("textbox", name="Supervisory Organization").click()
    page.get_by_role("textbox", name="Supervisory Organization").fill("Celergo_Master_division")
    page.get_by_role("textbox", name="Supervisory Organization").press("Enter")
    page.get_by_role("radio", name="Create a New Pre-Hire").check()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("listbox", name="items selected for Country").locator("li").click()
    page.get_by_role("textbox", name="Country").fill("south africa")
    page.get_by_role("textbox", name="Country").press("Enter")
    page.get_by_role("textbox", name="Given Name(s)").click()
    page.get_by_role("textbox", name="Given Name(s)").fill(position_id+"_GivenNameEmployee2"+str(random.randint(0,1000)))
    page.get_by_role("textbox", name="Middle Name").click()
    page.get_by_role("textbox", name="Middle Name").fill("MiddleNameEmployee1")
    page.get_by_role("textbox", name="Family Name").click()
    page.get_by_role("textbox", name="Family Name").fill("FamilyName")

    # Contact information

    # Enter home phone
    page.get_by_role("tablist").get_by_text("Contact Information").click()
    page.get_by_role("button", name="Add Phone").click()
    page.get_by_role("textbox", name="Country Phone Code").click()
    page.get_by_role("textbox", name="Phone Number").click()
    page.get_by_role("textbox", name="Phone Number").fill("681906056")
    page.get_by_role("button", name="Phone Device select one").click()
    page.get_by_label("Mobile").click()
    page.get_by_role("textbox", name="Type").click()
    page.get_by_text("Home", exact=True).click()

    # Enter Home address
    page.mouse.wheel(0, 10)
    page.get_by_role("button", name="Add Address").click()
    page.get_by_role("textbox", name="Street Number").click()
    page.get_by_role("textbox", name="Street Number").fill("1")
    page.get_by_role("textbox", name="Street Name").click()
    page.get_by_role("textbox", name="Street Name").fill("StreetName")
    page.get_by_role("textbox", name="Unit Number").click()
    page.get_by_role("textbox", name="Unit Number").fill("2")
    page.get_by_role("textbox", name="Complex").click()
    page.get_by_role("textbox", name="Complex").fill("2")
    page.get_by_role("textbox", name="Additional Address").click()
    page.get_by_role("textbox", name="Additional Address").fill("AdditionalAddress")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill("CapeTown")
    page.get_by_role("textbox", name="Suburb").click()
    page.get_by_role("textbox", name="Suburb").fill("Suburb")
    page.get_by_role("textbox", name="Postal Code").click()
    page.get_by_role("textbox", name="Postal Code").fill("080912")
    page.get_by_role("textbox", name="Province").click()
    page.get_by_role("textbox", name="Province").fill("Western Cape")
    page.get_by_role("textbox", name="Province").press("Enter")
    page.get_by_role("group", name="Address").get_by_label("Type").click()
    page.get_by_role("option", name="Home checkbox Not Checked").get_by_role("checkbox").check()
    
   
    # Enter Email
    page.mouse.wheel(0, 10)
    page.get_by_role("button", name="Add Email").click()
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("employee1@test.sa")
    page.get_by_role("group", name="Email").get_by_placeholder("Search").click()
    page.get_by_role("option", name="Home checkbox Not Checked").get_by_role("checkbox").check()
    page.get_by_role("button", name="OK").click()
    
    # Open Hire information
    #page.get_by_role("spinbutton", name="Hire Date").click()
    #page.get_by_role("spinbutton", name="First Day of Work").click()
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    if month == 1:
        month = 12
        year -= year
    
    
    time.sleep(3)
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

    page.get_by_role("textbox", name="Reason").click()
    page.get_by_text("New Hire").click()
    page.get_by_text("New Hire > New Position").click()
    page.get_by_role("textbox", name="Position").click()
    page.get_by_role("textbox", name="Position").fill(position_id)
    page.get_by_role("textbox", name="Position").press("Enter")

    page.get_by_role("textbox", name="Location").click()
    page.get_by_role("textbox", name="Location").fill("cape")
    page.get_by_role("textbox", name="Location").press("Enter")
    page.get_by_role("textbox", name="Job Profile").click()
    page.get_by_role("textbox", name="Job Profile").fill("tax")
    page.get_by_role("textbox", name="Job Profile").press("Enter")
    page.get_by_text("Tax Accountant").click()
    page.get_by_role("button", name="Submit").click()
    time.sleep(30)