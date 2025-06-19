import pytest
import time
from playwright.sync_api import sync_playwright, Playwright

@pytest.fixture(scope="class") 
def browser_context(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    request.cls.playwright = playwright
    request.cls.browser = browser
    request.cls.context = context
    request.cls.page = page

    yield

    page.close()
    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("browser_context")
class TestHireEmployeeLastMonth:

    def test_hire_employee1(self):
        self.page.goto("https://impl.workday.com/wday/authgwy/celergo_pt1/login.htmld")
        self.page.get_by_label("Username").fill("US_Impl")
        self.page.get_by_label("Password").fill("TestCelergo@1234")
        self.page.locator("button.GDPVGE1BOSC").click()
        self.page.locator("input#tdCheckbox").click()
        self.page.locator("button#submitButton").click()
        