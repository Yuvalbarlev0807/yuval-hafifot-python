from playwright.async_api import Page
from playwright.structure.fixtures.registryFields import RegistryFields
from playwright.structure.pages.base_page import BasePage
from playwright.structure.selectors.registry_page_selectors import registry_selectors


class RegistryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def fill_registry_data(self, registry_data: RegistryFields):
        await self.page.get_by_role("radio", name=registry_data["gender"]).check()

        await self.fill_text_field(
            registry_selectors["fields"]["first_name"],
            registry_data["first_name"]
        )

        await self.fill_text_field(
            registry_selectors["fields"]["last_name"],
            registry_data["last_name"]
        )

        await self.fill_text_field(
            registry_selectors["fields"]["email"],
            registry_data["email"]
        )

        await self.fill_text_field(
            registry_selectors["fields"]["password"],
            registry_data["password"]
        )

        await self.fill_text_field(
            registry_selectors["fields"]["confirm_password"],
            registry_data["confirm_password"]
        )
