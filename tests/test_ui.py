from pages.frontendmd_page import FrontendMDPage
from pages.main_page import MainPage


class TestGitHubUI:
    def test_find_contributors(self, driver):
        page = MainPage(driver)
        page.load("https://github.com/hahow/hahow-recruit")
        result = page.find_contributors()
        assert len(result) == 14

    def test_is_wireframe_image_in_the_page(self, driver):
        page = FrontendMDPage(driver)
        page.load("https://github.com/hahow/hahow-recruit/blob/master/frontend.md")
        assert page.check_the_image_exists()

    def test_latest_commitor(self, driver):
        page = FrontendMDPage(driver)
        page.load("https://github.com/hahow/hahow-recruit/blob/master/frontend.md")
        assert page.check_the_latest_commitor() == "dannnyliang"
