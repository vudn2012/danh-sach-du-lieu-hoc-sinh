import streamlit as st
import pandas as pd
import os

# Đọc dữ liệu từ file nếu tồn tại
file_path = "students.csv"
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    data = pd.DataFrame(columns=["Tên", "Toán", "Văn", "Anh"])

st.title("📚 Quản Lý Điểm Học Sinh")

# Hiển thị bảng điểm hiện tại
st.subheader("📋 Bảng điểm hiện tại")
st.dataframe(data)

# Nhập thông tin học sinh mới
st.subheader("➕ Thêm học sinh mới")
ten = st.text_input("Tên học sinh")
toan = st.number_input("Điểm Toán", min_value=0.0, max_value=10.0)
van = st.number_input("Điểm Văn", min_value=0.0, max_value=10.0)
anh = st.number_input("Điểm Anh", min_value=0.0, max_value=10.0)

if st.button("Thêm học sinh"):
    if ten.strip() == "":
        st.warning("⚠️ Vui lòng nhập tên học sinh.")
    else:
        new_data = {"Tên": ten, "Toán": toan, "Văn": van, "Anh": anh}
        data = pd.concat([data, pd.DataFrame([new_data])], ignore_index=True)
        data.to_csv(file_path, index=False)
        st.success(f"✅ Đã thêm học sinh: {ten}")
        st.dataframe(data)

# Thống kê điểm số
st.subheader("📊 Thống kê điểm số")
st.write("🔝 Điểm cao nhất từng môn:")
st.write(data[["Toán", "Văn", "Anh"]].max())

st.write("🔻 Điểm thấp nhất từng môn:")
st.write(data[["Toán", "Văn", "Anh"]].min())

# Top 3 học sinh điểm Toán cao nhất
st.subheader("🏆 Top 3 học sinh có điểm Toán cao nhất")
top_toan = data.nlargest(3, "Toán")
st.dataframe(top_toan)