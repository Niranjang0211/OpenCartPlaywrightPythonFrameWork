from playwright.sync_api import Page

class HomePage:

    def __init__(self,page:Page):

        self.page = page

        self.link_my_account = page.locator("span:has-text('My Account')")
        self.link_register = page.locator("a:has-text('Register')")
        self.link_login = page.locator("a:has-text('Login')")
        self.txt_search_box = page.locator("input[placeholder='Search']")
        self.btn_search = page.locator("#search button[type='button']")

    def get_home_page_title(self) -> str:
        title = self.page.title()
        return title

    def click_my_account(self):
        try:
            self.link_my_account.click()
        except Exception as e:
            print(f"Exception while clicking 'My Account' : {e}")
            raise

    def click_register(self):
        try:
            self.link_register.click()
        except Exception as e:
            print(f"Exception while clicking 'Register': {e}")
            raise

    def click_login(self):
        try:
            self.link_login.click()
        except Exception as e:
            print(f"Exception while clicking 'Login' : {e}")
            raise

    def enter_product_name(self,product_name:str):
        try:
            self.txt_search_box.fill(product_name)
        except Exception as e:
            print(f"Exception while entering product name: {e}")
            raise

    def click_search(self):
        try:
            self.btn_search.click()
        except Exception as e:
            print(f"Exception while clicking search: {e}")
            raise