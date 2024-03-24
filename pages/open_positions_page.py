import time

from selenium.webdriver.support.ui import Select

from base import base_test
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class OpenPositionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def filter_job_listings(self):
        """
        İş ilanlarını filtreler ve listelerin varlığını kontrol eder.
        """
        # Filter by Location dropdown menüsünü bul
        filter_by_location_dropdown = self.driver.find_element(By.XPATH,
                                                               "//span[@id='select2-filter-by-location-container']")
        time.sleep(4)
        # Filter by Location dropdown menüsüne tıkla
        filter_by_location_dropdown.click()
        time.sleep(4)
        # Istanbul, Turkey seçeneğini bul ve tıkla
        istanbul_turkey_option = self.driver.find_element(By.XPATH, "//option[@class='job-location istanbul-turkey']")
        istanbul_turkey_option.click()

        # Departman filtresini seç
        # department_filter = driver.find_element(By.XPATH, "//select[@id='filter-by-department']")
        # department_filter.click()
        # qa_option = driver.find_element(By.XPATH, "//option[text()='Quality Assurance']")
        # qa_option.click()

        # İş listelerinin varlığını kontrol et
        # totalResult değerini kontrol et
        time.sleep(2)
        total_result_element = self.driver.find_element(By.CLASS_NAME, "totalResult")
        time.sleep(2)
        total_result = int(total_result_element.text)
        time.sleep(2)
        assert total_result > 0, "No job listings found for Quality Assurance positions in Istanbul, Turkey."

        print("Job listings exist.")

        print(total_result)

    def check_job_listings(self):
        """
        İş ilanlarının belirli kriterlere uygunluğunu kontrol eder.
        """
        # İş listelerini bul
        job_listings = self.driver.find_elements(By.XPATH, "//div[@class='position-list-item']")

        # Her iş ilanı için kontrol et
        for job_listing in job_listings:
            position_title = job_listing.find_element(By.XPATH, ".//p[@class='position-title']").text
            department = job_listing.find_element(By.XPATH, ".//span[@class='position-department']").text
            location = job_listing.find_element(By.XPATH, ".//div[@class='position-location']").text

            # Pozisyon, departman ve lokasyon kontrolü yap
            assert "Quality Assurance" in position_title, f"{position_title} doesn't list 'Quality Assurance' in Position field"
            assert "Quality Assurance" in department, f"{position_title} doesn't list 'Quality Assurance' in Department field"
            assert "Istanbul, Turkey" in location, f"{position_title} doesn't list 'Istanbul, Turkey' in Location field"

        print("All job listings meet the criteria.")

    def verify_lever_app_page(self):
        """
        Lever Application form sayfasının doğruluğunu kontrol eder.
        """
        try:
            selector_View_role = "a[href='https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc']"
            view_role_buttons = self.driver.find_element(By.CSS_SELECTOR, selector_View_role)

            # Butona tıkla
            # view_role_buttons.click()
            self.driver.execute_script("arguments[0].click();", view_role_buttons)
            # Bekleme süresi ekleyebiliriz (sayfanın yüklenmesi için)
            time.sleep(2)

            # Yeni açılan pencereye geçiş yap
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Yeni pencerenin URL'sini al
            current_url = self.driver.current_url

            # Hedef URL'yi kontrol et
            assert current_url.startswith(
                "https://jobs.lever.co/useinsider/"), f"'View Role' didn't redirect to the correct URL.Now:{current_url}"

            # Ana pencereye geri dön
            self.driver.switch_to.window(self.driver.window_handles[0])

            print("'View Role' button redirect to the Lever Application form page successfully.")
        except Exception as e:
            # Hata durumunda ekran görüntüsü al
            base_test.take_screenshot(self, "verify_lever_app_page_error")
            # Hatanın tekrar yükseltilmesi, diğer testlerin hatayı görmesini sağlar
            raise e
