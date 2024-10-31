import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Dùng Edge làm trình duyệt
    driver.maximize_window()
    yield driver  
    driver.quit()  

# Danh sách các kích thước màn hình
screen_sizes = [(1920, 1080), (1366, 768), (768, 1024)]

# Test cho từng kích thước màn hình screen_sizes
@pytest.mark.parametrize("size", screen_sizes)
def test_responsive_design(driver, size):
    width, height = size  
    driver.set_window_size(width, height)  # Đặt kích thước trình duyệt
    driver.get("https://www.demoblaze.com/") 
    
    # Kiểm tra header hiển thị
    header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "narvbarx"))  # Chờ cho phần tử có ID 'narvbarx' hiển thị
    )
    assert header.is_displayed()  # check header hiển thị

    # Check menu chính hiển thị
    menu = driver.find_element(By.ID, "navbarExample")
    assert menu.is_displayed()

    # Check hình ảnh carousel
    image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "carousel-inner"))  # Chờ class 'carousel-inner' xuất hiện
    )
    assert image.is_displayed()  # Check carousel hiển thị

    # Kiểm tra footer hiển thị
    footer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "footer"))  # Chờ footer hiển thị
    )
    assert footer.is_displayed()   # Check footer hiển thị
