
import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

# --- CÀI ĐẶT GIAO DIỆN STREAMLIT ---
st.set_page_config(
    page_title="Nhận diện đối tượng với YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 Ứng dụng nhận diện đối tượng với YOLOv8")
st.write("Tải lên một ảnh và mô hình YOLOv8 sẽ phát hiện các đối tượng trong đó.")

# --- TẢI MÔ HÌNH YOLOv8 ---
@st.cache_resource
def load_model(model_path):
    """Tải mô hình YOLOv8."""
    model = YOLO(model_path)
    return model

# Tải mô hình yolov8n.pt
try:
    model = load_model('yolov8n.pt')
except Exception as e:
    st.error(f"Lỗi khi tải mô hình: {e}")
    st.stop()


# --- CÀI ĐẶT THANH BÊN (SIDEBAR) ---
st.sidebar.header("Cấu hình")
confidence = st.sidebar.slider(
    'Ngưỡng tin cậy (Confidence Threshold)', 
    min_value=0.0, 
    max_value=1.0, 
    value=0.25, 
    step=0.05
)

source_img = st.sidebar.file_uploader(
    "Chọn một ảnh...",
    type=("jpg", "jpeg", "png")
)

# --- XỬ LÝ VÀ HIỂN THỊ KẾT QUẢ ---
if source_img:
    # Chia 2 cột để hiển thị ảnh gốc và ảnh kết quả
    col1, col2 = st.columns(2)

    # Hiển thị ảnh gốc ở cột 1
    with col1:
        try:
            opened_image = Image.open(source_img)
            st.image(source_img, caption="Ảnh gốc", use_container_width=True)
        except Exception as e:
            st.error(f"Lỗi khi mở ảnh: {e}")
            st.stop()
            
    # Nút để bắt đầu nhận diện
    if st.sidebar.button("Nhận diện đối tượng"):
        with st.spinner("Đang xử lý..."):
            image_np = np.array(opened_image)
            image_cv2 = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            
            res = model.predict(image_cv2, conf=confidence)
            boxes = res[0].boxes
            res_plotted = res[0].plot()
            res_plotted_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)

            # Hiển thị ảnh kết quả ở cột 2
            with col2:
                st.image(res_plotted_rgb, caption='Ảnh đã nhận diện',use_container_width=True)
            
        
            try:
                with st.expander("📝 Chi tiết nhận diện"):
                    if len(boxes) > 0:
                        for box in boxes:
                            class_id = int(box.cls[0])
                            class_name = model.names[class_id]
                            conf_score = float(box.conf[0])
                            st.write(f"- Phát hiện đối tượng **{class_name}** với độ tin cậy **{conf_score:.2f}**")
                    else:
                        st.write("Không phát hiện được đối tượng nào với ngưỡng tin cậy đã chọn.")
            except Exception as ex:
                st.write("Không thể hiển thị chi tiết.")
                st.write(ex)
     

else:
    st.info("Vui lòng tải lên một ảnh để bắt đầu.")

st.markdown("---")
