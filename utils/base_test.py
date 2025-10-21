# utils/base_test.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        try:
            service = Service(ChromeDriverManager().install())
            print(f"[INFO] ChromeDriver aktif di: {service.path}")
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)
        except WebDriverException as e:
            raise RuntimeError(f"[ERROR] Gagal memulai ChromeDriver: {e}")

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def find(self, by, locator, timeout=10):
        """Cari elemen dengan menunggu hingga muncul di DOM (belum tentu terlihat)."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def wait_for(self, by, locator, timeout=10):
        """Tunggu sampai elemen terlihat di layar (bisa diambil teks atau diklik)."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def click_and_wait(self, by, locator, wait_for_by=None, wait_for_locator=None, timeout=10):
        """Klik elemen lalu tunggu elemen lain muncul (misal halaman berpindah)."""
        el = self.find(by, locator, timeout=timeout)
        el.click()
        if wait_for_by and wait_for_locator:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((wait_for_by, wait_for_locator))
            )
        return None
