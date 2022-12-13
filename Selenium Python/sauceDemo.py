import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SauceDemo(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def testLoginPositive(self):
        driver = self.driver

        # Akses halaman web saucedemo.com
        driver.get("https://www.saucedemo.com/")

        # Menunggu hingga element username muncul dan mengisi username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

        # Menunggu hingga element password muncul dan mengisi password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

        # Login dengan mengklik tombol login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button"))).click()

        # Identifikasi element yang muncul setelah login berupa title dengan text "Products"
        self.assertEqual(
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='title']"))).text,
            "PRODUCTS",
            "Login Success"
        )

    def testLoginNegative(self):
        driver = self.driver

        # Akses halaman web saucedemo.com
        driver.get("https://www.saucedemo.com/")

        # Menunggu hingga element username muncul dan mengisi username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(
            "standards_user")

        # Menunggu hingga element password muncul dan mengisi password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("password_salah")

        # Login dengan mengklik tombol login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button"))).click()

        # Identifikasi element yang muncul setelah login berupa title dengan text "Products"
        self.assertEqual(
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))).text,
            "Epic sadface: Username and password do not match any user in this service",
            "Login Failed"
        )

    def testAddProductToCartPositive(self):
        driver = self.driver

        # Akses halaman web saucedemo.com
        driver.get("https://www.saucedemo.com/")

        # Menunggu hingga element username muncul dan mengisi username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

        # Menunggu hingga element password muncul dan mengisi password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

        # Login dengan mengklik tombol login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button"))).click()

        # Memilih product dengan mengklik tombol add to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']"))).click()

        # Identifikasi product berhasil ditambahkan ke cart
        self.assertEqual(
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))).text,
            "1",
            "Product Added to Cart"
        )

    def testProductAddedToCart(self):
        driver = self.driver

        # Akses halaman web saucedemo.com
        driver.get("https://www.saucedemo.com/")

        # Menunggu hingga element username muncul dan mengisi username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

        # Menunggu hingga element password muncul dan mengisi password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

        # Login dengan mengklik tombol login

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button"))).click()

        # Memilih product dengan mengklik tombol add to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']"))).click()

        # mengambil text dengan nama Sauce Labs Backpack
        text1 = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]"))).text

        # klik tombol cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))).click()

        # Identifikasi product berhasil ditambahkan ke cart

        self.assertEqual(
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_name']"))).text,
            text1,
            "Product Added to Cart"
        )

    def testLogout(self):
        driver = self.driver

        # Akses halaman web saucedemo.com
        driver.get("https://www.saucedemo.com/")

        # Menunggu hingga element username muncul dan mengisi username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

        # Menunggu hingga element password muncul dan mengisi password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

        # Login dengan mengklik tombol login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button"))).click()

        # klik tombol open menu
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Open Menu')]"))).click()

        # klik tombol logout
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logout')]"))).click()

        # Identifikasi element yang muncul setelah logout berupa field username
        self.assertEqual(
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user-name"))).text,
            "",
            "Logout Success"
        )

    def tearDown(self) -> None:
        self.driver.quit()
