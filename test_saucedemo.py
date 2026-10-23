import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_tc01_login_success(driver):
    """TC01: Đăng nhập thành công với tài khoản hợp lệ"""
    driver.get(BASE_URL)
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title.upper() == "PRODUCTS"

def test_tc02_login_failure(driver):
    """TC02: Đăng nhập thất bại khi nhập sai mật khẩu"""
    driver.get(BASE_URL)
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()

    error_element = driver.find_element(By.DATA_TEST, "error") if hasattr(By, 'DATA_TEST') else driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert "Username and password do not match" in error_element.text

def test_tc03_sort_products_low_to_high(driver):
    """TC03: Lọc/Sắp xếp sản phẩm theo giá từ thấp đến cao"""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("lohi")
    
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(p.text.replace("$", "")) for p in price_elements]
    
    assert prices == sorted(prices)

def test_tc04_add_to_cart(driver):
    """TC04: Thêm sản phẩm vào giỏ hàng"""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    add_to_cart_btn = driver.find_element(By.XPATH, "(//button[contains(@text, 'Add to cart') or contains(text(), 'Add to cart')])[1]")
    add_to_cart_btn.click()
    
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"

def test_tc05_logout(driver):
    """TC05: Đăng xuất tài khoản"""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_btn.click()
    
    wait = WebDriverWait(driver, 10)
    logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
    logout_link.click()
    
    assert driver.find_element(By.ID, "login-button").is_displayed()
