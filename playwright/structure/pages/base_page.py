from abc import ABC
from playwright.async_api import Page

class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        await self.page.goto(url)

    async def click(self, locator: str):
        await self.page.locator(locator).click()

    async def fill_text_field(self, locator: str, text_value: str):
        await self.page.locator(locator).fill(text_value)
