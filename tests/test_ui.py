from pages.main_page import MainPage

class TestGitHubUI:
    def test_search_and_watch_video(self, driver):
        page = MainPage(driver)
        page.load("https://github.com/hahow/hahow-recruit")
