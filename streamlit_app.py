import streamlit as st

st.set_page_config(page_title="Kebutuhan Karbohidrat Harian", layout="centered")

st.title("🍚 Kalkulator Kebutuhan Karbohidrat Harian + Saran Makanan")

st.markdown("""
Aplikasi ini menghitung kebutuhan karbohidrat harian Anda dan memberi saran makanan berkarbohidrat tinggi.
""")

# Form input data pengguna
with st.form("form_karbo"):
    nama = st.text_input("Nama")
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25)
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    berat = st.number_input("Berat Badan (kg)", min_value=10.0, max_value=200.0, value=60.0)
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=100
