import time
from pages import contributor_page
from pages.main_page import MainPage, ContributorPage

class TestGitHubUI:
    def test_find_contributors(self, driver):
        page = MainPage(driver)
        page.load("https://github.com/hahow/hahow-recruit")
        result = page.find_contributors()
        assert len(result) == 14
        
