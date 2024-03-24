import time

from base import base_test
from base.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.open_positions_page import OpenPositionsPage


class QAJobsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def clicking_see_all_qa_jobs(self):
        """
        "See all QA jobs" butonuna tıklar ve OpenPositionsPage'e yönlendirir.
        """
        try:
            # "See all QA jobs" butonuna tıkla
            see_all_qa_jobs_button = self.driver.find_element(By.LINK_TEXT, "See all QA jobs")
            self.driver.execute_script("arguments[0].click();", see_all_qa_jobs_button)
            return OpenPositionsPage(self.driver)
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            base_test.take_screenshot(self, "clicking_see_all_qa_jobs_error")
            # Hatanın tekrar yükseltilmesi, diğer testlerin hatayı görmesini sağlar
            raise e

