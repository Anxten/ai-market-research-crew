# 🤖 AI Business Consultant for Market Research

Sebuah aplikasi command-line yang ditenagai oleh AI untuk melakukan analisis pasar dasar, menggabungkan data pelanggan internal dengan data riset kompetitor eksternal untuk menghasilkan rekomendasi strategis.

---

## 📈 Studi Kasus: Ekspansi "Kopi Arek"

Proyek ini lahir dari sebuah studi kasus fiktif: sebuah brand coffee shop lokal bernama "Kopi Arek" yang sukses di Surabaya ingin berekspansi ke kota baru. Mereka dihadapkan pada dua pertanyaan kunci:
1.  Siapakah profil pelanggan setia kita saat ini?
2.  Melihat profil tersebut, siapa kompetitor utama yang harus kita waspadai di kota baru?

Aplikasi ini dirancang untuk menjawab pertanyaan tersebut secara otomatis menggunakan AI.

---

## 🛠️ Arsitektur Solusi

Aplikasi ini menggunakan pendekatan "Orkestrasi Manual" yang andal, di mana alur kerja dikontrol oleh skrip utama untuk memastikan stabilitas dan hasil yang akurat.

1.  **Analisis Data Internal:** Sebuah agen AI khusus (`create_csv_agent`) menganalisis data transaksi (`.csv`) untuk mengidentifikasi profil pelanggan.
2.  **Analisis Data Eksternal:** Program membaca data riset kompetitor yang sudah disiapkan (`.txt`).
3.  **Sintesis & Rekomendasi:** "Otak" utama AI (LLM Groq Llama3) menerima kedua laporan tersebut dan membuat kesimpulan akhir serta rekomendasi strategis.

---

## 💻 Tumpukan Teknologi (Tech Stack)

* **Python**
* **LangChain** (sebagai framework utama)
* **Groq API** (dengan model Llama 3 8B sebagai LLM)
* **Pandas** (untuk pemrosesan data)
* **Argparse** (untuk membuat aplikasi command-line yang dinamis)

---

## 🚀 Instalasi & Setup

1.  **Clone repositori ini:**
    ```bash
    git clone [https://github.com/Anxten/ai-market-research-crew.git](https://github.com/Anxten/ai-market-research-crew.git)
    cd ai-market-research-crew
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt 
    # (Catatan: Anda perlu membuat file requirements.txt terlebih dahulu)
    # Cara cepat untuk sekarang: pip install pandas langchain-groq langchain-experimental langchain-community tabulate python-dotenv
    ```

4.  **Buat file `.env` dan masukkan kunci API Anda:**
    ```
    GROQ_API_KEY='gsk_xxxxxxxxxxxxxxxxxx'
    ```

---

## ⚙️ Cara Penggunaan

Jalankan aplikasi dari terminal dengan menyediakan path ke file data pelanggan dan file data riset.

```bash
python app.py --csv [path_ke_file_csv] --riset [path_ke_file_riset]