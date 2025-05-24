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
if page == "สรุปภาพรวม":
    st.subheader("📌 ตัวอย่างข้อมูล")
    st.dataframe(df.head())

    st.subheader("📈 สถิติราคาปิด")
    st.write(df["ราคาปิด"].describe())

    st.subheader("🏆 วันที่ราคาปิดสูงสุด")
    st.write(df[df["ราคาปิด"] == df["ราคาปิด"].max()])

    st.subheader("📊 ความสัมพันธ์ระหว่างราคาปิดกับ SET Index")
    st.write(df[["ราคาปิด", "SET Index"]].corr())
    elif page == "แนวโน้มราคาปิด":
    st.subheader("📉 แนวโน้มราคาปิด (Linear Regression)")
    from sklearn.linear_model import LinearRegression
    import numpy as np

    X = df_sorted["วันที่"].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    y = df_sorted["ราคาปิด"].values
    model = LinearRegression()
    model.fit(X, y)
    trend = model.predict(X)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_sorted["วันที่"], y, label="ราคาปิดจริง")
    ax.plot(df_sorted["วันที่"], trend, linestyle="--", color="red", label="แนวโน้ม (Linear Regression)")
    ax.set_title("แนวโน้มราคาปิด CPALL")
    ax.set_xlabel("วันที่")
    ax.set_ylabel("ราคาปิด (บาท)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    elif page == "เปรียบเทียบกับ SET Index":
    st.subheader("📊 เปรียบเทียบราคาปิด CPALL กับ SET Index")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(df_sorted["วันที่"], df_sorted["ราคาปิด"], label="ราคาปิด CPALL")
    ax2.plot(df_sorted["วันที่"], df_sorted["SET Index"], label="SET Index", alpha=0.7)
    ax2.set_title("CPALL vs SET Index")
    ax2.set_xlabel("วันที่")
    ax2.set_ylabel("ค่า")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)