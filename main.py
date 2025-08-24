from AI_Component.Crew import *
from AI_Component.validator.validator import *
import Component.Logo as Img
import streamlit as st

Img.image(["./Image/gema.png", "./Image/Unpad.png", "./Image/PENS.png", "./Image/SEAQIS.png"])
st.title("AI perikanan GEMA - FPIK UNPAD - PENS-SEAMEO QIS")
st.write("Model awal pengembangan dan kompilasi bahan ajar dari SMK Perikanan dan D4 FPIK UNPAD difokuskan pada informasi produksi dan pemasaran. Program ini diharapkan bisa dimanfaatkan oleh siswa/mahasiswa/masyarakat yang ingin mendapatkan referensi untuk produksi di daerahnya.")
st.write("Koordinator Gatot HP - www.gaeni.org ")
input = st.text_input("Masukkan pertanyaan ")
lang = "bahasa indonesia"
submit = st.button("Mulai Pencarian")

if submit:
    # Validasi pertanyaan
    if fisheries_validator(input):
        # Jika valid, lanjutkan ke proses utama
        result = KokoaCrew(input, lang).generalCrew().kickoff()
        st.markdown(result)
    else:
        # Jika tidak valid, tampilkan pesan kesalahan
        st.error("Pertanyaan Anda tidak berkaitan dengan topik perikanan. Silakan ajukan pertanyaan yang relevan.")