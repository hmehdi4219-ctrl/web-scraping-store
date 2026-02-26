import streamlit as st
import json

st.set_page_config(page_title="فروشگاه تمرین استاد", layout="wide")
st.title("🛒 فروشگاه تمرین استاد")

# بارگذاری داده‌ها
with open("data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# نمایش محصولات در کارت‌ها
cols = st.columns(3)  # 3 محصول در هر ردیف
for i, p in enumerate(products):
    col = cols[i % 3]
    with col:
        st.image(p["img"], use_column_width=True)
        st.markdown(f"**{p['title']}**")
        st.markdown(f"💰 قیمت: {p['price']}")
    
    # هر 3 محصول یک ردیف جدید
    if (i + 1) % 3 == 0:
        cols = st.columns(3)