import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Dùng Edge làm trình duyệt
    driver.maximize_window()
    yield driver  
    driver.quit()  

# Hàm accept khi alert xuất hiện
def accept_alert(driver):
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

# Test thêm sản phẩm vào giỏ hàng và kiểm tra thứ tự sản phẩm trong giỏ
def test_add_products_to_cart(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Thêm sản phẩm Nexus 6 vào giỏ hàng
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)

    # Thêm Nokia Lumia 1520 vào giỏ hàng hai lần
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)

    # Tới trang giỏ hàng và kiểm tra sản phẩm
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a').click()
    time.sleep(5)
    # Lấy ra các sản phẩm trong giỏ hàng
    cart_items = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/tr')
    expected_product_names = ["Nokia lumia 1520", "Nexus 6", "Nexus 6"]
    product_names = [item.find_element(By.XPATH, './td[2]').text for item in cart_items]

    # Kiểm tra chính xác thứ tự sản phẩm trong giỏ hàng
    # 90% Fail: load product not sequencely
    assert product_names == expected_product_names

# Test kiểm tra tổng tiền trong giỏ hàng
def test_check_total_price_products_to_cart(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Thêm 2 "Nexus 6" và "Nokia Lumia 1520" vào giỏ hàng
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)

    # Kiểm tra tổng tiền hiển thị trong giỏ
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a').click()
    time.sleep(5)
    # Lấy ra các sản phẩm trong giỏ hàng
    cart_items = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/tr')
    expected_product_names = ["Nokia lumia 1520", "Nexus 6", "Nexus 6"]
    product_names = [item.find_element(By.XPATH, './td[2]').text for item in cart_items]
    # Lấy ra tổng tiền
    total = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/h3').text

    # check total price and product names
    assert sorted(product_names) == sorted(expected_product_names) and total == "2120"

# Test xóa sản phẩm từ giỏ hàng
def test_delete_product_from_cart(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(10)

    # Thêm 2 "Nexus 6" và "Nokia Lumia 1520" vào giỏ hàng
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)

    # Tới trang giỏ hàng 
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a').click()
    time.sleep(5)
    # Lấy ra các sản phẩm trong giỏ hàng
    cart_items = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/tr')
    for item in cart_items:
        # Tìm sản phẩm có product name là "Nokia lumia 1520" và xóa
        product_name = item.find_element(By.XPATH, './td[2]').text
        if product_name == "Nokia lumia 1520":
            delete_button = item.find_element(By.XPATH, './td[4]/a')
            delete_button.click()
            time.sleep(5)
            break

    # Lấy ra các sản phẩm trong giỏ hàng sau khi xóa
    cart_items2 = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/tr')
    product_names = [item.find_element(By.XPATH, './td[2]').text for item in cart_items2]

    # Tổng tiền sau khi xóa sản phẩm
    total = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/h3').text
    # Kiểm tra sản phẩm và tổng tiền sau khi xóa
    assert sorted(product_names) == sorted(["Nexus 6", "Nexus 6"]) and total == "1300"

# Test thanh toán với thông tin hợp lệ
def test_checkout_with_valid_information(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Thêm Nexus 6 và Nokia Lumia 1520 vào giỏ hàng
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)

    # Tiến hành thanh toán
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button').click()
    time.sleep(5)
    # Điền vào form với thông tin hợp lệ
    driver.find_element(By.ID, "name").send_keys("John")
    driver.find_element(By.ID, "country").send_keys("US")
    driver.find_element(By.ID, "city").send_keys("New York")
    driver.find_element(By.ID, "card").send_keys("1234 5678")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
    time.sleep(0.1)
    # Kiểm tra thanh toán thành công
    assert "Thank you for your purchase!" == driver.find_element(By.XPATH, "/html/body/div[10]/h2").text

# Test thanh toán với thông tin không hợp lệ
def test_checkout_with_invalid_information(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(5)

    # Thêm Nexus 6 và Nokia Lumia 1520 vào giỏ hàng
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/a/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    accept_alert(driver)

    # Tiến hành thanh toán 
    driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button').click()
    time.sleep(5)

    # Điền vào form với thông tin thiếu name
    driver.find_element(By.ID, "country").send_keys("United States")
    driver.find_element(By.ID, "city").send_keys("New York")
    driver.find_element(By.ID, "card").send_keys("1234 5678 9012 3456")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")
    #submit
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
    time.sleep(0.1)
    # Đợi alert hiện ra và lấy alert text
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    # Kiểm tra cảnh báo
    assert "Please fill out Name and Creditcard." == alert_text
