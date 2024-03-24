import time

from base import base_test
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.career_page import CareersPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_careers_page(self):
        """
        Ana sayfadan Careers sayfasına geçiş yapar.
        """
        try:
            company_menu_locator = self.driver.find_element(By.LINK_TEXT, "Company")
            company_link = self.wait.until(EC.element_to_be_clickable(company_menu_locator))
            time.sleep(1)
            company_link.click()
            time.sleep(2)
            careers_link_locator = self.driver.find_element(By.XPATH, "//a[@href='https://useinsider.com/careers/']")
            careers_link = self.wait.until(EC.element_to_be_clickable(careers_link_locator))
            time.sleep(1)
            careers_link.click()
            return CareersPage(self.driver)
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            base_test.take_screenshot(self,"navigate_to_careers_page_error")
            # Hatanın tekrar yükseltilmesi, diğer testlerin hatayı görmesini sağlar
            raise e

