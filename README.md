# Dự án Nhận diện Đối tượng với YOLOv8 và Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red?style=for-the-badge&logo=streamlit)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange?style=for-the-badge&logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Một ứng dụng web được xây dựng bằng Streamlit, cho phép người dùng thực hiện nhận diện đối tượng trên hình ảnh, video và luồng webcam thời gian thực bằng mô hình YOLOv8.

![Demo GIF](https://github.com/ultralytics/assets/raw/main/yolov8/banner.png)
*> **Lưu ý:** Bạn nên thay thế ảnh trên bằng ảnh GIF hoặc ảnh chụp màn hình thực tế của ứng dụng.*

---

## 📋 Mục lục

- [Tính năng chính](#-tính-năng-chính)
- [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
- [Hướng dẫn Cài đặt](#-hướng-dẫn-cài-đặt-và-chạy-dự-án)
- [Cách sử dụng](#-cách-sử-dụng)
- [Vấn đề đã biết](#-vấn-đề-đã-biết-known-issues)
- [Giấy phép](#-giấy-phép)
- [Tác giả](#-tác-giả)

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

#### **Bước 1: Tải mã nguồn**

Clone repository này về máy của bạn:
```bash
git clone [ĐỊA_CHỈ_GIT_REPO_CỦA_BẠN]
cd [TÊN_THƯ_MỤC_DỰ_ÁN]
