/**
 * ## Cara Menggunakan Aplikasi Rekomendasi Movie
 *
 * Aplikasi ini dirancang untuk memberikan rekomendasi film berdasarkan kemiripan genre.
 * Berikut adalah langkah-langkah untuk menggunakan aplikasi ini:
 *
 * 1. **Instalasi**:
 *    - Pastikan Python telah terinstal di sistem Anda.
 *    - Unduh atau clone repository aplikasi ini.
 *    - Jalankan perintah berikut untuk menginstal semua dependensi yang dibutuhkan:
 *      ```sh
 *      pip install -r requirements.txt
 *      ```

 * 2. **Menjalankan Aplikasi**:
 *    - Pastikan file `movie_data.csv` tersedia di direktori yang sama dengan aplikasi.
 *    - Jalankan perintah berikut untuk memulai server Flask:
 *      ```sh
 *      python app.py
 *      ```
 *    - Jika berhasil, server akan berjalan di `http://127.0.0.1:5000/`.
 *
 * 3. **Menggunakan API Rekomendasi**:
 *    - Buka browser atau gunakan tools seperti Postman untuk mengakses endpoint berikut:
 *      ```
 *      http://127.0.0.1:5000/recommend?id=<movie_id>
 *      ```
 *    - Gantilah `<movie_id>` dengan ID film yang valid dari dataset.
 *    - Contoh penggunaan di terminal menggunakan `curl`:
 *      ```sh
 *      curl "http://127.0.0.1:5000/recommend?id=123"
 *      ```
 *
 * 4. **Hasil yang Diharapkan**:
 *    - Jika ID film valid, API akan mengembalikan daftar film yang direkomendasikan dalam format JSON.
 *    - Jika ID tidak ditemukan, API akan mengembalikan pesan error.
 *
 * 5. **Bantuan dan Dukungan**:
 *    - Jika mengalami kendala, pastikan semua dependensi telah terinstal dengan benar.
 *    - Periksa kembali apakah file `movie_data.csv` tersedia dan memiliki format yang benar.
 *    - Jika masih mengalami masalah, hubungi tim pengembang melalui [email/kontak].
 *
 * ### Catatan:
 * - Pastikan aplikasi berjalan di lingkungan Python yang mendukung Flask.
 * - Gunakan versi terbaru dari dataset agar rekomendasi lebih akurat.
 */
