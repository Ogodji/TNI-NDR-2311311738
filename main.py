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
import pandas as pd

# โหลดข้อมูล
df = pd.read_excel(r"C:\Users\charoenk\Desktop\Project ENG-494\CPALLSET-23May2025-6M.xlsx",
                   sheet_name="CPALL", skiprows=1)
df.columns = [
    "วันที่", "ราคาเปิด", "ราคาสูงสุด", "ราคาต่ำสุด", "ราคาเฉลี่ย", "ราคาปิด",
    "เปลี่ยนแปลง", "เปลี่ยนแปลง(%)", "ปริมาณ(พันหุ้น)", "มูลค่า(ล้านบาท)",
    "SET Index", "SET เปลี่ยนแปลง(%)"
]