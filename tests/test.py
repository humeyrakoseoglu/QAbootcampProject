import time

from base.base_test import BaseTest
from pages.home_page import HomePage


class Test(BaseTest):

    driver = 'chrome'

    def test(self):
        home_page = HomePage(self.driver) # Ana sayfaya git
        carrer_page = home_page.navigate_to_careers_page() # Kariyerler sayfasına yönlendir
        time.sleep(1)
        carrer_page.verify_accessibility() # Erişilebilirliği doğrula
        time.sleep(1)
        carrer_page.section_accessibility() # Bölüm erişilebilirliğini doğrula
        time.sleep(1)
        see_all_qa_jobs_page= carrer_page.navigate_to_qa_jobs()  # QA iş ilanlarına git
        time.sleep(1)
        open_position_page = see_all_qa_jobs_page.clicking_see_all_qa_jobs() # Tüm QA iş ilanlarını görüntüle
        time.sleep(1)
        open_position_page.filter_job_listings() # İş ilanlarını filtrele ve kontrol et
        time.sleep(1)
        open_position_page.check_job_listings() # İş ilanlarını kontrol et
        time.sleep(1)
        open_position_page.verify_lever_app_page() # İş ilanlarını filtrele ve kontrol et

