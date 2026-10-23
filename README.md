# Báo Cáo Thực Hành Kiểm Thử Tự Động Với Selenium

- **Họ và tên:** Nguyễn Thế Thịnh
- **Mã sinh viên:** 23010497
- **Công cụ sử dụng:** Selenium WebDriver, Python (pytest)
- **Website kiểm thử:** [SauceDemo](https://www.saucedemo.com/)

---

## 1. Môi trường & Thư viện sử dụng
- Python 3.x
- `selenium`
- `pytest`

---

## 2. Danh sách Test Cases & Kết quả

| STT | Mã TC | Tên Test Case | Các bước thực hiện | Kết quả mong đợi | Trạng thái |
|---|---|---|---|---|---|
| 1 | TC01 | Đăng nhập thành công | 1. Truy cập trang web<br>2. Nhập user/pass đúng<br>3. Bấm Login | Chuyển đến trang `/inventory.html` | **PASSED** |
<img width="975" height="491" alt="image" src="https://github.com/user-attachments/assets/8e480b61-f6c7-4155-8081-403295ae034c" />

| 2 | TC02 | Đăng nhập thất bại | 1. Truy cập trang web<br>2. Nhập sai mật khẩu<br>3. Bấm Login | Hiển thị thông báo lỗi | **PASSED** |
<img width="975" height="277" alt="image" src="https://github.com/user-attachments/assets/57645502-cabd-4f02-9451-90876dab20b2" />

| 3 | TC03 | Sắp xếp sản phẩm | 1. Đăng nhập thành công<br>2. Chọn filter "Price (low to high)" | Danh sách sắp xếp tăng dần theo giá | **PASSED** |
<img width="975" height="491" alt="image" src="https://github.com/user-attachments/assets/78ebd9b5-8e46-44dc-92ed-912b6d85b73c" />

| 4 | TC04 | Thêm vào giỏ hàng | 1. Đăng nhập thành công<br>2. Bấm "Add to cart" sản phẩm 1 | Badge giỏ hàng hiển thị số 1 | **PASSED** |
<img width="975" height="404" alt="image" src="https://github.com/user-attachments/assets/2adab14f-760e-4ed8-a3d9-ff8ba763bf62" />

| 5 | TC05 | Đăng xuất | 1. Mở Hamburger Menu<br>2. Bấm "Logout" | Quay về trang Login | **PASSED** |
<img width="975" height="659" alt="image" src="https://github.com/user-attachments/assets/2cbe2a22-a1a5-47a3-aa6d-698521ee2f92" />
<img width="975" height="280" alt="image" src="https://github.com/user-attachments/assets/7e0c1728-f1b3-4efc-ba96-0d52ecae3dfb" />


---

## 3. Hướng dẫn chạy Test Case
1. Cài đặt các thư viện phụ thuộc:
   ```bash
   pip install -r requirements.txt
