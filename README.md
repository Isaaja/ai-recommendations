# 📌 Movie Recommendation App

Aplikasi ini memberikan rekomendasi film berdasarkan kemiripan genre. Ikuti langkah-langkah di bawah ini untuk menginstal dan menggunakan aplikasi dengan benar.

---

## 🚀 Instalasi

1. **Pastikan Python telah terinstal** di sistem Anda.
2. **Unduh atau clone repository** aplikasi ini:
   ```sh
   git clone https://github.com/username/movie-recommendation-app.git
   cd movie-recommendation-app
   ```
3. **Instal semua dependensi** yang dibutuhkan:
   ```sh
   pip install -r requirements.txt
   ```

---

## ▶️ Menjalankan Aplikasi

1. **Pastikan file `movie_data.csv` tersedia** di direktori utama.
2. **Jalankan server Flask** dengan perintah berikut:
   ```sh
   python recommend.py
   ```
3. Jika berhasil, server akan berjalan di: `http://127.0.0.1:5000/`

---

## 🔍 Menggunakan API Rekomendasi

Anda bisa mengakses API menggunakan browser, Postman, atau terminal:

- **Endpoint API:**

  ```
  http://127.0.0.1:5000/recommend?id=<movie_id>
  ```

  Gantilah `<movie_id>` dengan ID film yang valid dari dataset.

- **Contoh penggunaan di terminal dengan `curl`:**
  ```sh
  curl "http://127.0.0.1:5000/recommend?id=123"
  ```

---

## 📌 Hasil yang Diharapkan

- Jika ID film valid, API akan mengembalikan daftar film yang direkomendasikan dalam format JSON.
- Jika ID tidak ditemukan, API akan mengembalikan pesan error.

---

## ❓ Bantuan dan Dukungan

Jika mengalami kendala:

- Pastikan semua dependensi telah terinstal dengan benar.
- Periksa apakah file `movie_data.csv` tersedia dan memiliki format yang benar.
- Jika masih mengalami masalah, hubungi tim pengembang melalui [email/kontak].

---

## 📌 Catatan

- Pastikan aplikasi berjalan di lingkungan Python yang mendukung Flask.
- Gunakan versi terbaru dari dataset agar rekomendasi lebih akurat.

---

✅ Selamat mencoba! 🎬
