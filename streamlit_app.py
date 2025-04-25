import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kebutuhan Karbohidrat Harian 🍚", page_icon="🍠", layout="centered")

st.title("🍚 Kebutuhan Karbohidrat Harian")
st.markdown("### Hitung kebutuhan karbohidratmu berdasarkan usia, berat badan, dan aktivitas harian 💪")

# Sidebar - Data Pribadi
st.sidebar.header("📋 Data Pribadi")

umur = st.sidebar.number_input("Usia (tahun)", min_value=1, max_value=100, value=25)
jenis_kelamin = st.sidebar.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])
berat_badan = st.sidebar.number_input("Berat Badan (kg)", min_value=20.0, max_value=200.0, value=60.0)
tinggi_badan = st.sidebar.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=220.0, value=165.0)
aktivitas = st.sidebar.selectbox(
    "Tingkat Aktivitas Harian",
    ["Rendah (jarang olahraga)", "Sedang (aktivitas fisik ringan)", "Tinggi (sering olahraga/kerja berat)"]
)

# Fungsi kebutuhan berdasarkan usia dan jenis kelamin (data dari Alodokter)
def kebutuhan_karbo_usia(umur, jenis_kelamin):
    if jenis_kelamin == "Laki-laki":
        if 10 <= umur <= 12:
            return 300
        elif 13 <= umur <= 15:
            return 350
        elif 16 <= umur <= 18:
            return 400
        elif 19 <= umur <= 29:
            return 430
        elif 30 <= umur <= 49:
            return 415
        elif 50 <= umur <= 64:
            return 340
        elif 65 <= umur <= 80:
            return 275
        elif umur > 80:
            return 235
        else:
            return 250
    else:  # Perempuan
        if 10 <= umur <= 12:
            return 280
        elif 13 <= umur <= 18:
            return 300
        elif 19 <= umur <= 29:
            return 360
        elif 30 <= umur <= 49:
            return 340
        elif 50 <= umur <= 64:
            return 280
        elif 65 <= umur <= 80:
            return 230
        elif umur > 80:
            return 200
        else:
            return 250

# Fungsi tambahan berdasarkan berat badan dan aktivitas
def faktor_aktivitas(aktivitas):
    if aktivitas == "Rendah (jarang olahraga)":
        return 3
    elif aktivitas == "Sedang (aktivitas fisik ringan)":
        return 5
    else:
        return 7

# Hitung kebutuhan akhir: ambil nilai rata-rata dari dua pendekatan
kebutuhan_dari_usia = kebutuhan_karbo_usia(umur, jenis_kelamin)
kebutuhan_dari_aktivitas = berat_badan * faktor_aktivitas(aktivitas)
kebutuhan_akhir = round((kebutuhan_dari_usia + kebutuhan_dari_aktivitas) / 2)

# Tampilkan hasil
st.success(f"🎯 Kebutuhan karbohidrat harianmu diperkirakan sekitar **{kebutuhan_akhir} gram** per hari.")

# Daftar makanan dan kandungan karbohidrat per 100 gram
st.markdown("## 🥗 Rekomendasi Makanan untuk Mencapai Target")

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

for makanan in makanan_karbo:
    jumlah = kebutuhan_akhir / makanan["karbo_per_100g"] * 100
    st.markdown(f"- **{makanan['nama']}** → sekitar **{int(jumlah)} gram**")

# Gambar ilustrasi
st.image("https://cdn-icons-png.flaticon.com/512/135/135620.png", width=80, caption="Tetap sehat dan seimbang ya!")

# Footer
st.markdown("---")
st.markdown("<center><small>📘 Projek Tugas Kampus | Dibuat dengan ❤️ oleh [kelompok 3 pmip e1]</small></center>", unsafe_allow_html=True)
