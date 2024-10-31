import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Dùng Edge làm trình duyệt
    driver.maximize_window()
    yield driver  
    driver.quit()  

# Hàm tạo chuỗi ký tự và số ngẫu nhiên
def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # Bao gồm cả chữ và số
    result = ''.join(random.choice(characters) for _ in range(length))
    return result

# Test đăng ký với tài khoản hợp lệ
def test_regis_valid_account(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(0.1)  # Đợi 0.1 giây để tải trang
    driver.find_element(By.XPATH, '//*[@id="signin2"]').click()  # Click vào nút đăng ký
    account = generate_random_string(10)  # Tạo tài khoản ngẫu nhiên
    time.sleep(1)  # Đợi phần tử tải
    driver.find_element(By.XPATH, '//*[@id="sign-username"]').send_keys(f'{account}@example.com')  # Nhập username
    driver.find_element(By.XPATH, '//*[@id="sign-password"]').send_keys('Valid@--Password123')  # Nhập password
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # Click vào nút đăng ký
    time.sleep(0.1)
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Đợi alert xuất hiện
    alert = driver.switch_to.alert  # Chuyển sang alert
    alert_text = alert.text
    assert "Sign up successful." == alert_text  # Xác minh thông báo thành công

# Test đăng ký với tài khoản đã tồn tại
def test_regis_existed_account(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="signin2"]').click()  # Click vào nút đăng ký
    account = generate_random_string(10)  # Tạo tài khoản ngẫu nhiên
    time.sleep(2)  # Đợi phần tử tải
    driver.find_element(By.XPATH, '//*[@id="sign-username"]').send_keys('valid_user1@example.com')  # Tài khoản đã tồn tại
    driver.find_element(By.XPATH, '//*[@id="sign-password"]').send_keys('Valid@--Password123')
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # Click đăng ký
    time.sleep(0.1)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "This user already exist." == alert_text  # Xác minh cảnh báo tài khoản tồn tại

# Test đăng ký không nhập tài khoản
def test_regis_blank_account(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="signin2"]').click()  # Click vào nút đăng ký
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()  # Click đăng ký
    time.sleep(0.1)
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Đợi alert hiện ra
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "Please fill out Username and Password." == alert_text  # Xác minh cảnh báo không nhập tài khoản

# Test đăng nhập với tài khoản hợp lệ và đăng xuất
def test_login_valid_account_and_logout(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="login2"]').click()  # Click vào nút login
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginusername"]').send_keys('valid_user1@example.com')  # Nhập username hợp lệ
    driver.find_element(By.XPATH, '//*[@id="loginpassword"]').send_keys('Valid@--Password123')  # Nhập password hợp lệ
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()  # Click đăng nhập
    time.sleep(2)
    user = driver.find_element(By.XPATH, '//*[@id="nameofuser"]').text  # Kiểm tra tên người dùng hiển thị trên navbar
    assert "Welcome valid_user1@example.com" == user
    driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[6]').click()  # Click logout
    time.sleep(2)
    assert driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[7]/a').text == ""  # Xác minh tên người dùng không hiển thị

# Test đăng nhập với mật khẩu sai
def test_login_invalid_password(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//*[@id="login2"]').click()  # Click vào nút login
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginusername"]').send_keys('valid_user1@example.com')  # Nhập username
    driver.find_element(By.XPATH, '//*[@id="loginpassword"]').send_keys('zzz')  # Nhập mật khẩu sai
    time.sleep(0.1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()  # Click đăng nhập
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Đợi alert hiện ra
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "Wrong password." == alert_text  # Xác minh cảnh báo mật khẩu sai
