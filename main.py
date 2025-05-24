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
thai_months = {
    "ม.ค.": "01", "ก.พ.": "02", "มี.ค.": "03", "เม.ย.": "04",
    "พ.ค.": "05", "มิ.ย.": "06", "ก.ค.": "07", "ส.ค.": "08",
    "ก.ย.": "09", "ต.ค.": "10", "พ.ย.": "11", "ธ.ค.": "12"
}

def convert_thai_date(thai_date_str):
    for th, num in thai_months.items():
        if th in thai_date_str:
            day, month_th, year_th = thai_date_str.replace(",", "").split()
            month = thai_months[month_th]
            year = int(year_th) - 543
            return f"{year}-{month}-{int(day):02d}"
    return None

df = df[~df["วันที่"].isna() & ~df["วันที่"].str.contains("วันที่")]
df["วันที่"] = df["วันที่"].apply(convert_thai_date)
df["วันที่"] = pd.to_datetime(df["วันที่"])
df = df.dropna()
df_sorted = df.sort_values("วันที่")