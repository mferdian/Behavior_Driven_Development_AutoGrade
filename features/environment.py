# environment.py
from utils.base_test import BaseTest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

BASE_URL_API = "http://localhost:8000/api"
BASE_URL_WEB = "http://localhost:3000"

def before_all(context):
    # --- Setup Selenium ---
    context.base = BaseTest()
    context.base.setUp()
    context.driver = context.base.driver

    # --- Login via API ---
    response = requests.post(f"{BASE_URL_API}/auth/login", json={
        "email": "michael01@gmail.com",
        "password": "password123"
    })
    if response.status_code != 200:
        raise Exception(f"API login failed: {response.text}")

    data = response.json().get("data", {})
    context.access_token = data.get("access_token")
    context.refresh_token = data.get("refresh_token")

    if not context.access_token or not context.refresh_token:
        raise Exception("Access token or refresh token not found in API response.")

    # --- Buka halaman root HTTP supaya localStorage bisa diakses ---
    context.driver.get(f"{BASE_URL_WEB}/teachers/dashboard")

    # Tunggu sampai root element muncul (agar React/SPA siap)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard-teachers"))
    )

    # --- Set token di localStorage ---
    auth_storage = {
        "state": {
            "accessToken": context.access_token,
            "refreshToken": context.refresh_token
        },
        "version": 0
    }

    # --- Simpan ke localStorage ---
    context.driver.execute_script(
        "localStorage.setItem('auth-storage', arguments[0]);",
        json.dumps(auth_storage)
    )

    # --- Refresh supaya front-end membaca token ---
    context.driver.refresh()

    # Tunggu dashboard muncul (opsional tapi disarankan)
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard-teachers"))
        )
    except:
        print("Warning: Dashboard element not found, pastikan login berhasil.")

def after_all(context):
    context.base.tearDown()
