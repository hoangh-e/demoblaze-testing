import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Dùng Edge làm trình duyệt
    driver.maximize_window()
    yield driver  
    driver.quit()  

# Test kiểm tra các liên kết của thanh điều hướng
def test_navigation_bar(driver):
    # Mở trang chính
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)

    # Kiểm tra liên kết "Home"
    home_link = driver.find_element(By.CSS_SELECTOR, '#navbarExample ul li:nth-child(1) a')
    home_link.click()
    time.sleep(2)
    assert "index.html" in driver.current_url, "Không chuyển hướng về trang chủ"

    # Kiểm tra liên kết "Contact"
    contact_link = driver.find_element(By.CSS_SELECTOR, '#navbarExample ul li:nth-child(2) a')
    contact_link.click()
    time.sleep(2)
    contact_modal = driver.find_element(By.ID, "exampleModal")
    assert contact_modal.is_displayed(), "Modal 'Contact' không hiển thị"
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer button.btn-secondary').click()  # Đóng modal "Contact"

    # Kiểm tra liên kết "About us"
    about_link = driver.find_element(By.CSS_SELECTOR, '#navbarExample ul li:nth-child(3) a')
    about_link.click()
    time.sleep(2)
    about_modal = driver.find_element(By.ID, "videoModal")
    assert about_modal.is_displayed(), "Modal 'About us' không hiển thị"
    driver.find_element(By.CSS_SELECTOR, '#videoModal .close').click()  # Đóng modal "About us"

    # Kiểm tra liên kết "Cart"
    cart_link = driver.find_element(By.ID, "cartur")
    cart_link.click()
    time.sleep(2)
    assert "cart.html" in driver.current_url
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()  # Quay lại trang chủ
    time.sleep(2)   

    # Kiểm tra liên kết "Log in"
    login_link = driver.find_element(By.ID, "login2")
    login_link.click()
    time.sleep(2)
    login_modal = driver.find_element(By.ID, "logInModal")
    assert login_modal.is_displayed(), "Modal 'Log in' không hiển thị"
    driver.find_element(By.CSS_SELECTOR, '#logInModal .close').click()  # Đóng modal "Log in"

    # Kiểm tra liên kết "Sign up"
    signup_link = driver.find_element(By.ID, "signin2")
    signup_link.click()
    time.sleep(2)
    signup_modal = driver.find_element(By.ID, "signInModal")
    assert signup_modal.is_displayed(), "Modal 'Sign up' không hiển thị"
    driver.find_element(By.CSS_SELECTOR, '#signInModal .close').click()  # Đóng modal "Sign up"
    time.sleep(2)

    # Kiểm tra liên kết sản phẩm "Samsung galaxy s6"
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/a").click()
    time.sleep(5)
    assert "Samsung galaxy s6" == driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/h2").text
