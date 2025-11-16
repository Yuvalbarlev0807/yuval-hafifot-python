from playwright.structure.pages.base_page import BasePage
from playwright.async_api import Page


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
