# app.py (Versi Final - Orkestrator Manual)

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Memuat kunci dari .env
load_dotenv()

print("Mempersiapkan Orkestrasi Multi-Langkah...")

try:
    # 1. Definisikan LLM kita
    llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

    # =================================================================
    # LANGKAH 1: JALANKAN AGEN ANALIS DATA CSV
    # =================================================================
    print("\n--- [LANGKAH 1] Menjalankan Agen Analis Data CSV... ---")
    csv_agent = create_csv_agent(llm, 'transactions.csv', allow_dangerous_code=True)
    pertanyaan_csv = "Analisis file transactions.csv ini, lalu berikan rangkuman singkat tentang profil pelanggan utama berdasarkan pekerjaan dan menu yang paling populer."
    hasil_analisis_csv = csv_agent.invoke({"input": pertanyaan_csv})['output']
    
    print("--- Laporan dari Agen Analis Data ---")
    print(hasil_analisis_csv)

    # =================================================================
    # LANGKAH 2: BACA FILE RISET KOMPETITOR
    # =================================================================
    print("\n--- [LANGKAH 2] Membaca File Riset Kompetitor... ---")
    with open('riset_kompetitor.txt', 'r') as file:
        hasil_riset_kompetitor = file.read()
    print("--- Laporan Riset Kompetitor ---")
    print(hasil_riset_kompetitor)

    # =================================================================
    # LANGKAH 3: SINTESIS KEDUA INFORMASI
    # =================================================================
    print("\n--- [LANGKAH 3] Meminta LLM Membuat Kesimpulan Akhir... ---")
    
    # Membuat template prompt untuk tugas akhir
    prompt_sintesis = ChatPromptTemplate.from_template(
        "Anda adalah seorang konsultan bisnis yang cerdas.\n"
        "Anda memiliki dua buah laporan:\n\n"
        "Laporan 1: Analisis Pelanggan Internal\n"
        "-------------------------------------\n"
        "{analisis_pelanggan}\n"
        "-------------------------------------\n\n"
        "Laporan 2: Riset Kompetitor di Pasar\n"
        "-------------------------------------\n"
        "{riset_kompetitor}\n"
        "-------------------------------------\n\n"
        "Tugas Anda: Berdasarkan DUA laporan tersebut, berikan kesimpulan dan rekomendasi singkat dalam Bahasa Indonesia. "
        "Siapakah kompetitor utama yang paling relevan dan harus diwaspadai oleh 'Kopi Arek' mengingat profil pelanggan internal mereka? Berikan alasanmu."
    )

    # Membuat rantai LangChain untuk sintesis
    rantai_sintesis = prompt_sintesis | llm | StrOutputParser()

    # Menjalankan rantai dengan memberikan kedua laporan sebagai input
    rekomendasi_final = rantai_sintesis.invoke({
        "analisis_pelanggan": hasil_analisis_csv,
        "riset_kompetitor": hasil_riset_kompetitor
    })

    print("\n\n==================== REKOMENDASI FINAL ====================")
    print(rekomendasi_final)
    print("==========================================================")
    print("\nProses Selesai dengan Sukses!")

except Exception as e:
    print("\n==================== ERROR ====================")
    print(e)
    print("============================================")