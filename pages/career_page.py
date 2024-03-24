import time

from selenium.webdriver.support.wait import WebDriverWait

from base import base_test
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.quality_assurance_page import QAJobsPage


class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_accessibility(self):
        """
        Sayfanın erişilebilirliğini doğrular.
        """
        assert "Ready to disrupt? | Insider Careers" in self.driver.title

    def section_accessibility(self):
        """
        Sayfadaki bölümlerin erişilebilirliğini doğrular.
        """
        # Sayfanın tamamen yüklenmesini bekle
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#career-our-location")))

        # Locations, Teams ve Life at Insider bölümlerini içeren elementlerin varlığını kontrol et
        locations_section = self.driver.find_element(By.XPATH,
                                                     "//div[@class='col-12 col-md-6']/h3[contains(.,'Our Locations')]")
        teams_section = self.driver.find_element(By.XPATH,
                                                 "//div[@class='col-12 mb-xl-5 py-xl-4 py-2 text-center']/h3[contains(.,'Find your calling')]")  # Teams olarak bu başlığı düşündüm
        life_at_insider_section = self.driver.find_element(By.XPATH, "//h2[text()='Life at Insider']")

        # Eğer tüm bölümler bulunursa, doğrulama başarılıdır
        assert locations_section is not None
        assert teams_section is not None
        assert life_at_insider_section is not None

    def navigate_to_qa_jobs(self):
        """
        Quality Assurance iş ilanlarına gider.
        """
        try:
            # "See all teams" butonunu bul ve tıkla
            see_all_teams_button = self.driver.find_element(By.CLASS_NAME, 'loadmore')  # See all teams
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollIntoView();", see_all_teams_button)
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", see_all_teams_button)
            time.sleep(2)
            # "Quality Assurance" pozisyonunu bul ve tıkla
            quality_assurance_job = self.driver.find_element(By.XPATH, "//a[contains(@href,'quality-assurance')]/h3")
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollIntoView();", quality_assurance_job)
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", quality_assurance_job)
            time.sleep(2)
            # Yönlendirilen sayfanın yüklenmesini bekle
            return QAJobsPage(self.driver)
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            test_status = "navigate_to_qa_jobs_error"
            base_test.take_screenshot(self, test_status)
            # Hatanın tekrar yükseltilmesi, diğer testlerin hatayı görmesini sağlar
            raise e
