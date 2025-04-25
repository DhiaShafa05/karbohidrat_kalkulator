import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kebutuhan Karbohidrat Harian 🍚", page_icon="🍠", layout="centered")

st.title("🍚 Kebutuhan Karbohidrat Harian")
st.markdown("### Hitung kebutuhan karbohidrat harianmu dan temukan makanan yang cocok untuk mencapainya!")

# Sidebar - Data Pribadi
st.sidebar.header("📋 Data Pribadi")

usia = st.sidebar.number_input("Usia (tahun)", min_value=1, max_value=100, value=25)
jenis_kelamin = st.sidebar.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Fungsi untuk menentukan kebutuhan karbohidrat berdasarkan usia dan jenis kelamin
def kebutuhan_karbohidrat(usia, jenis_kelamin):
    if jenis_kelamin == "Laki-laki":
        if 10 <= usia <= 12:
            return 300
        elif 13 <= usia <= 15:
            return 350
        elif 16 <= usia <= 18:
            return 400
        elif 19 <= usia <= 29:
            return 430
        elif 30 <= usia <= 49:
            return 415
        elif 50 <= usia <= 64:
            return 340
        elif 65 <= usia <= 80:
            return 275
        elif usia > 80:
            return 235
        else:
            return 250  # Default untuk usia di bawah 10 tahun
    else:  # Perempuan
        if 10 <= usia <= 12:
            return 280
        elif 13 <= usia <= 18:
            return 300
        elif 19 <= usia <= 29:
            return 360
        elif 30 <= usia <= 49:
            return 340
        elif 50 <= usia <= 64:
            return 280
        elif 65 <= usia <= 80:
            return 230
        elif usia > 80:
            return 200
        else:
            return 250  # Default untuk usia di bawah 10 tahun

# Hitung kebutuhan karbohidrat
kebutuhan = kebutuhan_karbohidrat(usia, jenis_kelamin)

st.success(f"🎯 Kebutuhan karbohidrat harianmu adalah sekitar **{kebutuhan} gram** per hari.")

# Daftar makanan dengan kandungan karbohidrat per 100 gram
st.markdown("## 🥗 Rekomendasi Makanan Harian")

makanan_karbo = [
    {"nama": "Nasi Putih", "karbo_per_100g": 40},
    {"nama": "Nasi Merah", "karbo_per_100g": 32.5},
    {"nama": "Oatmeal", "karbo_per_100g": 54},
    {"nama": "Pisang Besar", "karbo_per_100g": 31},
    {"nama": "Ubi Rebus", "karbo_per_100g": 21},
    {"nama": "Jagung", "karbo_per_100g": 19},
    {"nama": "Roti Gandum", "karbo_per_100g": 14},
    {"nama": "Spageti", "karbo_per_100g": 73},
    {"nama": "Kacang Merah", "karbo_per_100g": 21.5},
    {"nama": "Apel", "karbo_per_100g": 16},
]

st.markdown("Berikut beberapa pilihan makanan dan takaran untuk memenuhi kebutuhanmu:")

for makanan in makanan_karbo:
    jumlah_diperlukan = kebutuhan / makanan["karbo_per_100g"] * 100
    st.markdown(f"- **{makanan['nama']}** → sekitar **{int(jumlah_diperlukan)} gram** per hari.")

# Gambar ilustrasi
st.image("https://cdn-icons-png.flaticon.com/512/135/135620.png", width=80, caption="Tetap sehat ya!")

# Footer
st.markdown("---")
st.markdown("<center><small>📘 Projek Tugas Kampus | Dibuat dengan ❤️ oleh [kelompok 3 pmip e1]</small></center>", unsafe_allow_html=True)

