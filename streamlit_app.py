import streamlit as st

st.set_page_config(page_title="Kebutuhan Karbohidrat Harian", layout="centered")

st.title("🥗 Kalkulator Kebutuhan Karbohidrat Harian")

st.markdown(
    """
    Aplikasi ini membantu Anda menghitung estimasi kebutuhan karbohidrat harian berdasarkan data pribadi dan tingkat aktivitas.
    """
)

# Input data pengguna
nama = st.text_input("Nama")
usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
berat = st.number_input("Berat Badan (kg)", min_value=10.0, max_value=200.0, value=60.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0)
aktivitas = st.selectbox(
    "Tingkat Aktivitas",
    [
        "Sangat Rendah (tidak aktif)",
        "Rendah (olahraga ringan 1-3 hari/minggu)",
        "Sedang (olahraga sedang 3-5 hari/minggu)",
        "Tinggi (olahraga berat 6-7 hari/minggu)",
        "Sangat Tinggi (aktivitas fisik berat harian)"
    ]
)

# Faktor aktivitas berdasarkan pilihan
faktor_aktivitas = {
    "Rendah (olahraga ringan 1-3 hari/minggu)": 1.375,
    "Sedang (olahraga sedang 3-5 hari/minggu)": 1.55,
    "Tinggi (olahraga berat 6-7 hari/minggu)": 1.725,
}

# Fungsi menghitung BMR dan TDEE
def hitung_bmr(berat, tinggi, usia, jenis_kelamin):
    if jenis_kelamin == "Laki-laki":
        return 88.36 + (13.4 * berat) + (4.8 * tinggi) - (5.7 * usia)
    else:
        return 447.6 + (9.2 * berat) + (3.1 * tinggi) - (4.3 * usia)

# Tombol Hitung
if st.button("Hitung Kebutuhan Karbohidrat"):
    bmr = hitung_bmr(berat, tinggi, usia, jenis_kelamin)
    tdee = bmr * faktor_aktivitas[aktivitas]  # Total kebutuhan energi_*
