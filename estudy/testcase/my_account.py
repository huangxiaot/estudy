from page.start import AppStart


class TestMyAccount:
    def setup_class(self):
        self.my_account = AppStart.start().enter_my_page().enter_my_account_page()

    def test_editor_my_account_name_success(self):
        my_account_name = "woniu"
        self.my_account.editor_my_account_name_success(my_account_name)

    def test_editor_my_account_portrait_photo(self):
        self.my_account.editor_my_account_portrait_photo()

    def test_editor_my_account_portrait_album(self):
        self.my_account.editor_my_account_portrait_album()

    def teardown_class(self):
        AppStart.quit()
