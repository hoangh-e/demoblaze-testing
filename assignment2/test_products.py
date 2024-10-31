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

#Kiểm tra số lượng sản phẩm trên trang đầu tiên của danh mục và chuyển sang trang kế tiếp
def test_next_products_in_home(driver):
    # Mở trang chủ
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    
    # Kiểm tra số lượng sản phẩm trên trang đầu tiên của danh mục
    products = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/div')
    assert len(products) == 9

    # Nhấn nút "Next" để chuyển sang trang kế tiếp
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button').click()
    time.sleep(2)

    # Kiểm tra số lượng sản phẩm trên trang kế tiếp
    products_next_page = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/div')
    assert len(products_next_page) == 6
    
#Kiểm tra trang category "Phone" 7 sản phẩm vẫn tạo nút "Next" trên trang danh mục Phone
def test_products_in_category(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)

    # Chọn category "Phone"
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[2]").click()
    time.sleep(2)

    # Lấy ra các sản phẩm hiển thị
    products = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/div')
    product_names = ["Samsung galaxy s6", "Nokia lumia 1520", "Nexus 6", "Samsung galaxy s7", "Iphone 6 32gb", "Sony xperia z5", "HTC One M9"]
   
    # Kiểm tra chính xác 7 sản phẩm hiển thị
    for i, product in enumerate(products):
        title = product.find_element(By.CLASS_NAME, 'card-title').text
        assert title == product_names[i]
    # Kiểm tra không còn sản phẩm thuộc "Phone", nút "Next" sẽ không hiển thị
    assert driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button') is None
