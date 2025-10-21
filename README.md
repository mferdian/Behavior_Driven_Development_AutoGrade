Berikut contoh **README.md** profesional untuk proyekmu (BDD testing sistem login React + Selenium).
Strukturnya sudah disesuaikan agar langsung bisa dipakai di GitHub 👇

---

```markdown
# 🧪 Automated BDD Testing — Essay Scoring System Login

Proyek ini berisi **pengujian otomatis (BDD)** menggunakan **Selenium + Python (unittest)** untuk memverifikasi proses **login sistem web Essay Scoring System** yang dibangun dengan **Next.js (React)**.  
Tujuan utamanya adalah memastikan alur login untuk **Dosen (Lecturer)** dan **Mahasiswa (Student)** berjalan dengan benar.

---

## 🚀 Fitur Utama

✅ Pengujian otomatis halaman login berbasis browser (UI Testing)  
✅ Dukungan **BDD-style** (Given–When–Then)  
✅ Struktur modular dengan `BaseTest`  
✅ Otomatis unduh & setup ChromeDriver via `webdriver_manager`  
✅ Uji login sukses dan gagal untuk dua role pengguna  
✅ Dukungan toast message asinkron (`sonner`)

---

## 🧩 Struktur Folder

```

📦 BDD
├── utils/
│   └── base_test.py         # Kelas dasar Selenium (setup, teardown, helper)
├── test/
│   └── test_user_login.py   # Test BDD untuk login Dosen & Mahasiswa
├── venv/                    # Virtual environment Python (opsional)
├── requirements.txt         # Dependencies proyek
└── README.md                # Dokumentasi proyek (file ini)

````

---

## 🛠️ Instalasi dan Setup

### 1️⃣ Clone Repositori

```bash
git clone https://github.com/<your-username>/bdd-login-test.git
cd bdd-login-test
````

### 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
```

Aktifkan environment:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Contoh isi `requirements.txt`:

```
selenium
webdriver-manager
unittest-xml-reporting
```

---

## 🧠 Struktur Testing

### 🔹 BaseTest — `utils/base_test.py`

Kelas dasar yang mengatur:

* Inisialisasi ChromeDriver otomatis
* Helper `find()` dan `click_and_wait()`
* TearDown otomatis menutup browser
* Exception handling bawaan Selenium

### 🔹 Test File — `test/test_user_login.py`

Berisi dua kelas pengujian:

* `LecturerLoginTest`
* `StudentLoginTest`

Setiap test mencakup:

* `test_login_success` — login dengan kredensial valid
* `test_login_failed_invalid_credentials` — login dengan kredensial salah

---

## ⚙️ Menjalankan Test

Pastikan server frontend (Next.js) kamu sudah **berjalan di `http://localhost:3000`**.

Lalu jalankan:

```bash
python -m unittest discover -s test
```

Output yang diharapkan:

```
[INFO] ChromeDriver aktif di: ...
....
----------------------------------------------------------------------
Ran 4 tests in 35.5s

OK
```

Jika kredensial salah, test akan menampilkan toast error seperti:

```
❌ Scenario: Failed login due to invalid credentials (Lecturer)
Toast: "Failed login user"
```

---

## 🧾 Contoh Test BDD

```python
def test_lecturer_login_failed_invalid_credentials(self):
    """Scenario: Failed login due to invalid credentials (Lecturer)
    Given Lecturer is on the login page
    When they enter invalid email or password
    Then an error toast should appear
    """
    self.driver.get(self.login_url)
    self.find(By.ID, "email").send_keys("michael01@gmail.com")
    self.find(By.ID, "password").send_keys("wrongpass")
    self.find(By.ID, "login-button").click()

    error_message = self.wait_for_toast()
    self.assertIn("failed", error_message.lower())
```

---

## 🧰 Debugging Tips

🔹 Jika muncul error `NoSuchElementException`, periksa:

* ID element benar (`email`, `password`, `login-button`)
* Toast muncul di DOM (gunakan `print(self.driver.page_source[:1000])`)
* Server lokal sudah berjalan (`npm run dev`)

🔹 Tambahkan `time.sleep(3)` sementara untuk menunggu animasi toast (hanya untuk debugging).
