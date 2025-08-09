# Dự án Nhận diện Đối tượng với YOLOv8 và Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red?style=for-the-badge&logo=streamlit)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange?style=for-the-badge&logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Một ứng dụng web được xây dựng bằng Streamlit, cho phép người dùng thực hiện nhận diện đối tượng trên hình ảnh, video và luồng webcam thời gian thực bằng mô hình YOLOv8.


---

## 📋 Mục lục

- [Tính năng chính](#-tính-năng-chính)
- [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
- [Hướng dẫn Cài đặt](#-hướng-dẫn-cài-đặt-và-chạy-dự-án)



---

## ✨ Tính năng chính

-   **Nhận diện đa nguồn:**
    -   Nhận diện đối tượng từ file hình ảnh (`.jpg`, `.png`, v.v.).
    -   Nhận diện đối tượng từ file video (`.mp4`, `.avi`, v.v.).
    -   Nhận diện đối tượng trong thời gian thực qua webcam.
-   **Trực quan hóa:** Hiển thị các khung bao (bounding box), nhãn và độ tin cậy cho các đối tượng được phát hiện.
-   **Tùy chỉnh:** Giao diện cho phép tùy chỉnh ngưỡng tin cậy (confidence threshold).
-   **Giao diện thân thiện:** Giao diện web được xây dựng bằng Streamlit, trực quan và dễ sử dụng.

---

## 🛠️ Công nghệ sử dụng

-   **Ngôn ngữ:** Python 3.9+
-   **Framework Web:** Streamlit
-   **Mô hình AI:** YOLOv8 (từ Ultralytics)
-   **Thư viện xử lý ảnh/video:** PyTorch, OpenCV-Python

---

## 🚀 Hướng dẫn Cài đặt và Chạy dự án

Để chạy được dự án này trên máy của bạn, hãy làm theo các bước sau:

### Các bước cài đặt

1.  **Clone repository về máy:**
    Mở terminal hoặc command prompt và chạy lệnh sau:
    ```bash
    git clone https://github.com/HoangAnh109/Detect-object-application-based-YOLOv8-with-Streamlit.git detect-app
    cd detect-app
    ```

2.  **Tạo và kích hoạt môi trường Conda:**
    Điều này giúp cô lập các thư viện của dự án, tránh xung đột với các dự án khác.
    ```bash
    # Tạo môi trường mới tên là detect-app với Python 3.9
    conda create --name detect-app python=3.9 -y

    # Kích hoạt môi trường vừa tạo
    conda activate detect-app
    ```
    *Ghi chú: Nếu không sử dụng Conda, có thể tạo môi trường ảo bằng `venv`:*
    ```bash
    # python -m venv venv
    # source venv/bin/activate  (trên Linux/macOS)
    # venv\Scripts\activate  (trên Windows)
    ```

3.  **Cài đặt các thư viện cần thiết:**
    Tất cả các gói cần thiết được liệt kê trong file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Chạy ứng dụng Streamlit:**
    Sau khi cài đặt thành công, chạy lệnh sau để khởi động ứng dụng:
    ```bash
    streamlit run detectapp.py --server.fileWatcherType none
    ```
    -   Lệnh `streamlit run` sẽ khởi động một web server cục bộ.
    -   Tham số `--server.fileWatcherType none` giúp tăng tính ổn định và tránh việc ứng dụng tự chạy lại không cần thiết trong một số môi trường.

Sau khi chạy lệnh, một tab mới trên trình duyệt sẽ tự động mở ra với địa chỉ `http://localhost:8501`, hiển thị ứng dụng.

![Demo](https://raw.githubusercontent.com/HoangAnh109/Detect-object-application-based-YOLOv8-with-Streamlit/main/assets/detection.jpg)

---


