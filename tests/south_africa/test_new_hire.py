import pytest
import time
from playwright.sync_api import sync_playwright, Playwright
from framework.login import login
from framework.new_hire import *


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
        login(self.page)
        position_id = create_position(self.page)
        aprove_position(self.page, position_id)
        #submit_new_hire(self.page)
        