import streamlit as st

# Gaya dan layout
st.set_page_config(page_title="Kebutuhan Karbohidrat Harian 🍚", page_icon="🍠", layout="centered")

st.title("🍚 Kebutuhan Karbohidrat Harian")
st.markdown("### Hitung kebutuhan karbohidrat harianmu dan temukan makanan yang cocok untuk mencapainya!")

# Input data pengguna
st.sidebar.header("📋 Data Pribadi")
berat_badan = st.sidebar.number_input("Masukkan berat badan (kg)", min_value=30, max_value=200, value=60)
aktivitas = st.sidebar.selectbox("Tingkat aktivitas harian", ["Rendah", "Sedang", "Tinggi"])

# Fungsi untuk menentukan kebutuhan karbohidrat
def hitung_kebutuhan_karbo(berat, aktivitas):
    if aktivitas == "Rendah":
        karbo_per_kg = 3
    elif aktivitas == "Sedang":
        karbo_per_kg = 5
    else:
        karbo_per_kg = 7
    return berat * karbo_per_kg

# Hitung kebutuhan
kebutuhan_karbo = hitung_kebutuhan_karbo(berat_badan, aktivitas)

st.success(f"🎯 Kebutuhan karbohidrat harianmu adalah sekitar **{int(kebutuhan_karbo)} gram** per hari.")

# Rekomendasi makanan
st.markdown("## 🥗 Rekomendasi Makanan Harian")

makanan_karbo = [
    {"nama": "Nasi Putih", "karbo_per_100g": 28},
    {"nama": "Kentang Rebus", "karbo_per_100g": 17},
    {"nama": "Ubi Jalar", "karbo_per_100g": 20},
    {"nama
