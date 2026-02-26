from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import json
import requests

# مسیر chromedriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://kalatik.com")  # آدرس صفحه محصولات
    time.sleep(5)  # صبر برای لود شدن صفحه

    products = []

    # پیدا کردن محصولات با CSS Selector مطابق HTML سایت
    items = driver.find_elements(By.CSS_SELECTOR, ".product-item")

    # ایجاد پوشه‌ها
    os.makedirs("data", exist_ok=True)
    os.makedirs("images", exist_ok=True)

    for idx, item in enumerate(items, start=1):
        try:
            title = item.find_element(By.CSS_SELECTOR, ".product-title").text
            price = item.find_element(By.CSS_SELECTOR, ".product-price").text
            img_url = item.find_element(By.TAG_NAME, "img").get_attribute("src")

            # دانلود تصویر
            img_data = requests.get(img_url).content
            img_name = f"images/product_{idx}.jpg"
            with open(img_name, "wb") as img_file:
                img_file.write(img_data)

            products.append({
                "title": title,
                "price": price,
                "img": img_name  # مسیر محلی تصویر
            })
        except:
            continue

finally:
    driver.quit()

# ذخیره JSON
with open("data/products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"✅ {len(products)} محصول ذخیره شد همراه با تصاویر")