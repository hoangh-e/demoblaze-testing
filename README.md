# README

## Thiết lập môi trường và chạy các test

Dự án này sử dụng **Python**, **Selenium** và **Pytest** để thực hiện các bài kiểm tra tự động trên trình duyệt **Microsoft Edge**. Dưới đây là các bước chi tiết để thiết lập môi trường và chạy các script:

### 1. Yêu cầu hệ thống
- Python (phiên bản từ 3.7 trở lên)
- Trình duyệt Microsoft Edge
- Microsoft Edge WebDriver (phù hợp với phiên bản Edge hiện tại)

### 2. Cài đặt môi trường

#### Bước 1: Tạo môi trường ảo 
Tạo môi trường ảo để quản lý các gói cài đặt:
```bash
python -m venv env
```

Kích hoạt môi trường ảo:
- Windows:
  ```bash
  .\env\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source env/bin/activate
  ```

#### Bước 2: Cài đặt các thư viện cần thiết
Cài đặt Selenium và Pytest:
```bash
pip install selenium pytest
```

#### Bước 3: Cài đặt Microsoft Edge WebDriver
- Tải bản WebDriver mới nhất từ [trang Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
- Giải nén và cài đặt.

### 3. Cấu trúc dự án
Dự án có thể được tổ chức như sau:
```
project-folder/
|-- tests/
|   |-- test_example.py
|-- README.md
```
### 4. Chạy các bài kiểm tra
Để chạy các bài kiểm tra, sử dụng lệnh sau:
```bash
pytest
```
Hoặc chỉ định chạy một tệp cụ thể:
```bash
pytest tests/test_example.py
```
