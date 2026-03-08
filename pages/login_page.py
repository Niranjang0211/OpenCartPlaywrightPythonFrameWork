from playwright.sync_api import Page

class LoginPage:

    def __init__(self,page:Page):

        self.page = page

        self.txt_email_address = page.locator("#input-email")
        self.txt_password = page.locator("#input-password")
        self.btn_login = page.locator("input[value='Login']")
        self.txt_error_message = page.locator(".alert.alert-danger.alert-dismissible")

    def set_email(self,email: str):
        try:
            self.txt_email_address.fill(email)
        except Exception as e:
            print(f"Exception while entering email: {e}")

    def set_password(self,password: str):
        try:
            self.txt_password.fill(password)
        except Exception as e:
            print(f"Exception while entering password: {e}")

    def click_login(self):
        self.btn_login.click()


    def login(self,email,password: str):

        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def get_login_error(self):

        try:
            return self.txt_error_message
        except Exception as e:
            print(f"Exception while fetching login error message: {e}")
            return None

