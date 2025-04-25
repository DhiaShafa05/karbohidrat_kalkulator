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
    {"nama": "Roti Gandum", "karbo_per_100g": 40},
    {"nama": "Jagung", "karbo_per_100g": 19},
    {"nama": "Oatmeal", "karbo_per_100g": 66},
]

st.markdown("Berikut beberapa pilihan makanan dan takaran untuk memenuhi kebutuhanmu:")

for makanan in makanan_karbo:
    jumlah_diperlukan = kebutuhan_karbo / makanan["karbo_per_100g"] * 100
    st.markdown(f"- **{makanan['nama']}** → sekitar **{int(jumlah_diperlukan)} gram** per hari.")

st.markdown("---")
st.markdown("💡 Tips: Kombinasikan berbagai sumber karbohidrat agar pola makan lebih seimbang dan tidak membosankan!")

# Tambahan estetika
st.image("https://cdn-icons-png.flaticon.com/512/135/135620.png", width=80, caption="Tetap sehat ya!")

# Footer
st.markdown("---")
st.markdown("<center><small>📘 Projek Tugas Kampus | Dibuat dengan ❤️ oleh [KELOMPOK 3 PMIP E1]</small></center>", unsafe_allow_html=True)
