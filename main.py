import streamlit as st
import matplotlib.pyplot as plt
import matplotlib

# ตั้งค่าฟอนต์สำหรับ matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

st.set_page_config(page_title="CPALL Stock Dashboard", layout="wide")
st.title("📊 วิเคราะห์ราคาหุ้น CPALL")
st.sidebar.header("📌 เมนูหลัก")

# เลือกหน้า
page = st.sidebar.radio("ไปยังหน้า:", ["สรุปภาพรวม", "แนวโน้มราคาปิด", "เปรียบเทียบกับ SET Index", "Moving Average", "ดาวน์โหลดข้อมูล"])