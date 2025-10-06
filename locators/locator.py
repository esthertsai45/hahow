from selenium.webdriver.common.by import By


class Locators:
    MAIN_PAGE = (By.XPATH, "//a[@href='/hahow/hahow-recruit'][normalize-space(.)='hahow-recruit']")
    CONTRIBUTORS_BLOCK = (By.XPATH, "//div[./h2/a[contains(text(), 'Contributors')]]")
    CONTRIBUTOR_LINKS = (By.CSS_SELECTOR, "ul.list-style-none > li > a")
    
    # GitHub contributors page locators - updated based on actual DOM structure
    CHART_READY_XPATH = (By.XPATH, "//li[contains(@class, 'Index-module__chartListItem')][1]//div[@data-highcharts-chart and @aria-label]")
    CONTRIBUTOR_LIST_ITEM_XPATH = (By.XPATH, "//ul[contains(@class, 'Index-module__chartList--RemPq')]/li")
    CONTRIBUTOR_NAME = (By.XPATH, ".//h2//a")   # can't use span[@class='sr-only'] because it's not always present (Screen Reader Only)
    