import time
import datetime
import random
from framework.proxy import *
from framework.sys_integration import *

def submit_new_hire(page, position_id):
    first_name = position_id+"_GivenNameEmployee2"+str(random.randint(0,1000))
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
    page.get_by_role("textbox", name="Given Name(s)").fill(first_name)
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
    
    
    time.sleep(5)
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
    page.get_by_role("textbox", name="Reason").fill("New Hire > New Position")
    page.get_by_role("textbox", name="Reason").press("Enter")
    time.sleep(1)
    page.get_by_role("textbox", name="Reason").press("Enter")

    page.get_by_role("textbox", name="Position").click()
    page.get_by_role("textbox", name="Position").fill(position_id)
    page.get_by_role("textbox", name="Position").press("Enter")
    time.sleep(1)
    page.get_by_role("textbox", name="Position").press("Enter")

    page.get_by_role("textbox", name="Employee Type").click()
    page.get_by_role("textbox", name="Employee Type").fill("Regular")
    page.get_by_role("textbox", name="Employee Type").press("Enter")
    time.sleep(1)
    page.get_by_role("textbox", name="Employee Type").press("Enter")

    page.get_by_role("textbox", name="Location").click()
    page.get_by_role("textbox", name="Location").fill("Cape Town")
    page.get_by_role("textbox", name="Location").press("Enter")
    time.sleep(1)
    page.get_by_role("textbox", name="Location").press("Enter")
    
    page.get_by_role("textbox", name="Job Profile").click()
    page.get_by_role("textbox", name="Job Profile").fill("Tax Director")
    page.get_by_role("textbox", name="Job Profile").press("Enter")
    time.sleep(1)
    page.get_by_role("textbox", name="Job Profile").press("Enter")

    page.get_by_role("button", name="Submit").click()
    return first_name

def aprove_new_hire(page, first_name):
    start_proxy(page)

    page.get_by_role("button", name="My Tasks Items").click()
    page.get_by_role("textbox", name="Search: All Items").click()
    page.get_by_role("textbox", name="Search: All Items").fill(first_name)
    page.get_by_role("textbox", name="Search: All Items").press("Enter")
    time.sleep(5)

    page.get_by_role("button", name="Add Salary").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("General Salary Plan")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    
    page.get_by_role("textbox", name="Error: The field Amount is").click()
    page.get_by_role("textbox", name="Error: The field Amount is").fill("10000")
    page.get_by_role("textbox", name="Error: The field Amount is").press("Enter")

    page.get_by_role("listbox", name="items selected for Frequency").locator("li").click()
    page.get_by_role("textbox", name="Frequency").fill("Monthly")
    page.get_by_role("textbox", name="Frequency").press("Enter")
    page.get_by_role("option", name="Monthly radio button unselected has related actions", exact=True).get_by_role("radio").check()
    page.get_by_role("button", name="Save Salary").click()
    time.sleep(3)

    page.get_by_role("button", name="Add Allowance").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("Unit - Car Allowance Plan")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    page.get_by_role("button", name="Save Allowance").click()
    time.sleep(3)

    page.get_by_role("button", name="Add Allowance").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("CellPhone Allowance")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    page.get_by_role("button", name="Save Allowance Row").click()
    time.sleep(3)

    page.get_by_role("button", name="Add Allowance").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("House Allowance Plan")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    page.get_by_role("button", name="Save Allowance Row").click()

    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("button", name="Close", exact=True).click()
    
    time.sleep(10)
    page.get_by_text("GenderGender").click()
    page.get_by_role("button", name="Gender select one").click()
    page.get_by_role("option", name="Male", exact=True).locator("div").nth(1).click()
    page.get_by_role("button", name="Save Gender").click()

    page.get_by_role("button", name="Edit Date of Birth").click()
    #TODO: Add datepicking logic
    page.get_by_role("button", name="Save Date of Birth").click()
    time.sleep(3)

    page.get_by_text("Country of BirthCountry of").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("South Africa")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Save Place of Birth").click()
    time.sleep(3)

    page.get_by_text("Marital StatusMarital Status").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("Single")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Save Marital Status").click()
    time.sleep(3)

    page.get_by_text("Race/EthnicityRace/Ethnicity").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("African")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Save Race/Ethnicity").click()
    time.sleep(3)

    page.get_by_text("Citizenship StatusCitizenship").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("non-citizen(South africa)")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Save Citizenship Status").click()
    time.sleep(3)

    page.get_by_text("Primary NationalityPrimary").click()
    page.get_by_role("textbox", name="Search", exact=True).fill("South Africa")
    page.get_by_role("textbox", name="Search", exact=True).press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Save Nationality").click()
    time.sleep(3)
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("button", name="Close", exact=True).click()
    
    time.sleep(10)
    page.locator("tbody").filter(has_text="*Country*National ID").get_by_label("Add Row").click()
    page.locator("tbody").filter(has_text="*Country*National ID").get_by_label("Add Row").click()
    page.get_by_role("textbox", name="Country").nth(0).click()
    page.get_by_role("textbox", name="Country").nth(0).fill("South Africa")
    page.get_by_role("textbox", name="Country").nth(0).press("Enter")
    time.sleep(1)
    page.get_by_role("textbox", name="National ID Type").nth(0).click()
    page.get_by_text("ID Number").click()
    page.get_by_role("cell", name="_____________").get_by_role("textbox").click()
    #TODO Implement Backspace several times and fill value


    page.get_by_role("textbox", name="Country").nth(1).click()
    page.get_by_role("textbox", name="Country").nth(1).fill("South Africa")
    page.get_by_role("textbox", name="Country").nth(1).press("Enter")
    page.get_by_role("textbox", name="National ID Type").nth(1).click()
    page.get_by_text("Tax Reference Number").click()
    page.get_by_role("cell", name="__________").get_by_role("textbox").click()
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("button", name="Close", exact=True).click()
    time.sleep(10)
    
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Close", exact=True).click()

    time.sleep(10)
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Close", exact=True).click()

    time.sleep(10)
    page.get_by_role("button", name="Add").click()
    page.get_by_role("textbox", name="One-Time Payment Plan").click()
    page.get_by_role("textbox", name="One-Time Payment Plan").fill("Signing Bonus Plan")
    page.get_by_role("textbox", name="One-Time Payment Plan").press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Save Organizational").click()

    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Close", exact=True).click()

    time.sleep(10)
    page.get_by_role("textbox", name="Proposed Pay Group").click()
    page.get_by_role("textbox", name="Proposed Pay Group").fill("GPC_SOUTH_AFRICA_PECI")
    page.get_by_role("textbox", name="Proposed Pay Group").press("Enter")
    time.sleep(1)
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Close", exact=True).click()

    time.sleep(10)
    page.get_by_role("button", name="Let's Get Started Benefit").click()
    page.get_by_role("button", name="Review and Sign").click()
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Done").click()

    stop_proxy()

    page.get_by_role("button", name="My Tasks Items").click()
    page.get_by_role("textbox", name="Search: All Items").click()
    page.get_by_role("textbox", name="Search: All Items").fill(first_name)
    page.get_by_role("textbox", name="Search: All Items").press("Enter")
    page.get_by_role("button", name="Approve").click()
    page.get_by_role("button", name="Close", exact=True).click()
