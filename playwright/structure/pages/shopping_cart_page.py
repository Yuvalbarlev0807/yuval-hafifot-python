from playwright.async_api import Page, expect
from playwright.structure.pages.base_page import BasePage
from playwright.structure.selectors.shopping_cart_page_selectors import shopping_cart_selectors


class ShoppingCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def get_cart_item_locator(self):
        return self.page.locator(shopping_cart_selectors.itemName)

    async def remove_all_items(self):
     remove_item_selector = self.page.locator(shopping_cart_selectors.removeItem)
     if await remove_item_selector.count() == 0:
        return
     await remove_item_selector.check()
     await self.page.locator(shopping_cart_selectors.updateCart).click()
     await expect(self.page.get_by_text("your shopping cart is empty")).toBeVisible()
     await expect(remove_item_selector).toHaveCount(0)

