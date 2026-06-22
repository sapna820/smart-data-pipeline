import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Smart ETL Dashboard", layout="wide")

st.title("📊 Smart Data Pipeline Dashboard")

# Load data safely
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "output", "sales_output.csv")

df = pd.read_csv(file_path)

# ---------------- KPIs ----------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹ {df['revenue'].sum():,.0f}")
col2.metric("Total Transactions", df.shape[0])
col3.metric("Unique Customers", df['name'].nunique())

st.divider()

# ---------------- FILTERS ----------------
st.subheader("🔍 Filters")

city = st.selectbox("Select City", ["All"] + list(df["city"].unique()))
category = st.selectbox("Select Category", ["All"] + list(df["category"].unique()))

filtered_df = df.copy()

if city != "All":
    filtered_df = filtered_df[filtered_df["city"] == city]

if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]

# ---------------- DATA ----------------
st.subheader("📁 Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# ---------------- CHARTS ----------------
st.subheader("📈 Revenue by Product")
chart_data = filtered_df.groupby("product_name")["revenue"].sum()
st.bar_chart(chart_data)

st.subheader("📊 Business Insights")

st.write("💰 Average Revenue per Sale:", df["revenue"].mean())
st.write("📦 Total Products Sold:", df["quantity"].sum())
st.write("🏙️ Top City:", df.groupby("city")["revenue"].sum().idxmax())
st.write("🏆 Best Selling Product:", df.groupby("product_name")["revenue"].sum().idxmax())