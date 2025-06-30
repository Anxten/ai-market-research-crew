# app.py (Versi 2.0 - Aplikasi Dinamis)

import os
import pandas as pd
import argparse # <-- PERKAKAS BARU KITA
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =================================================================
# BAGIAN BARU: MEMBUAT "LUBANG INPUT" (ARGUMENT PARSER)
# =================================================================
# Ini akan mendefinisikan input apa yang kita harapkan dari pengguna saat mereka menjalankan file ini
parser = argparse.ArgumentParser(description="AI Business Consultant")
parser.add_argument('--csv', type=str, required=True, help='Path ke file CSV data transaksi pelanggan.')
parser.add_argument('--riset', type=str, required=True, help='Path ke file .txt berisi data riset kompetitor.')
args = parser.parse_args()
# =================================================================

# Memuat kunci dari .env
load_dotenv()

print("Mempersiapkan Proses Analisis Dinamis...")

try:
    # 1. Definisikan LLM kita
    llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

    # 2. Baca data dari file yang ditentukan oleh pengguna
    print(f"Membaca data pelanggan dari file: {args.csv}")
    df = pd.read_csv(args.csv) # <-- MENGGUNAKAN INPUT DARI TERMINAL
    data_pelanggan_str = df.to_string()

    print(f"Membaca data riset dari file: {args.riset}")
    with open(args.riset, 'r') as file: # <-- MENGGUNAKAN INPUT DARI TERMINAL
        data_kompetitor_str = file.read()

    # 3. Minta LLM membuat kesimpulan (langkah ini sama persis seperti sebelumnya)
    print("Mengirim semua data ke Groq untuk dibuat kesimpulan...")
    prompt_template = ChatPromptTemplate.from_template(
        "Anda adalah seorang konsultan bisnis super cerdas.\n"
        "Anda memiliki dua buah laporan:\n\n"
        "Laporan 1: Analisis Pelanggan Internal\n"
        "-------------------------------------\n"
        "{data_pelanggan}\n"
        "---------------------\n\n"
        "Laporan 2: Riset Kompetitor di Pasar\n"
        "-------------------------------------\n"
        "{data_kompetitor}\n"
        "----------------------\n\n"
        "TUGAS AKHIR: Berdasarkan DUA set data di atas, jawab pertanyaan ini dalam Bahasa Indonesia:\n"
        "1. Siapa profil pelanggan utama 'Kopi Arek'? (lihat dari pekerjaan & usia).\n"
        "2. Mengingat profil pelanggan tersebut, siapa kompetitor yang paling relevan dan harus diwaspadai? Berikan alasan singkat."
    )
    rantai_final = prompt_template | llm | StrOutputParser()
    rekomendasi_final = rantai_final.invoke({
        "data_pelanggan": data_pelanggan_str,
        "data_kompetitor": data_kompetitor_str
    })

    print("\n\n==================== REKOMENDASI FINAL ====================")
    print(rekomendasi_final)
    print("==========================================================")
    print("\nProses Selesai dengan Sukses!")

except Exception as e:
    print("\n==================== ERROR ====================")
    print(e)
    print("============================================")