import random
from playwright.async_api import Locator, Page, expect
from playwright.structure.pages.base_page import BasePage
from playwright.structure.selectors.digital_downloads_page_selectors import digital_downloads_Selectors

class DigitalDownloadsPage (BasePage) :
    def __init__(self, page: Page):
        super().__init__(page)
        self.  digital_downloads_options:Locator = page.locator(
        digital_downloads_Selectors.downloadOptionList)

    async def add_item_to_cart( self,item_locator: Locator) :
      return item_locator.locator(digital_downloads_Selectors.addItemToCart).click()

    async def get_random_buy_option(self) :
      num_of_options = await self.digital_downloads_options.count()
      expect(num_of_options).to_be_greater_than(0)
      random_index = random.randint(0, num_of_options - 1)
      return self.digital_downloads_options.nth(random_index)

    async def get_item_name(self,item_locator: Locator) :
     return item_locator.locator(digital_downloads_Selectors.itemName).inner_text()


