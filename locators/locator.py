from selenium.webdriver.common.by import By


class Locators:
    MAIN_PAGE = (By.XPATH, "//a[@href='/hahow/hahow-recruit'][normalize-space(.)='hahow-recruit']")
    CONTRIBUTORS_BLOCK = (By.XPATH, "//div[./h2/a[contains(text(), 'Contributors')]]")
    CONTRIBUTOR_LINKS = (By.CSS_SELECTOR, "ul.list-style-none > li > a")
    
    FRONTEND_MD_PAGE = (By.ID, "user-content-hahow-frontend-engineer-徵才小專案")
    IMAGE1_XPATH = (By.XPATH, "//img[contains(@src, 'assets/hero-list-page.png')]")
    IMAGE2_XPATH = (By.XPATH, "//img[contains(@src, 'assets/hero-profile-page.png')]")
    LATEST_COMMIT_CONTAINER_XPATH = (By.XPATH, "//div[@data-testid='latest-commit']")
    COMMITOR_NAME_XPATH = (By.XPATH, "//div[@data-testid='author-avatar']/a[2]")
