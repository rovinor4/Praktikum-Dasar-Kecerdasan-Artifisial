# Soal

## Soal 1
Sebuah perusahaan travel ingin membuat sistem optimasi rute perjalanan wisata menggunakan algoritma Hill Climbing. Setiap kota direpresentasikan sebagai titik koordinat (x, y), dan jarak antar kota dihitung menggunakan jarak Euclidean.

Program harus dapat menentukan rute perjalanan yang menghasilkan total jarak minimum dengan mengunjungi setiap kota tepat satu kali (Traveling Salesman Problem sederhana).

### Ketentuan Program:
1. Representasikan kota dalam bentuk list koordinat, contoh:
   ```python
   cities = [(0,0), (2,3), (5,1), ...]
   ```
2. Buat fungsi untuk menghitung jarak antar kota (Euclidean Distance).
3. Buat fungsi untuk menghitung total jarak dari suatu rute.
4. Implementasikan algoritma Hill Climbing dengan ketentuan:
   - Solusi awal di-generate secara acak.
   - Neighbor diperoleh dengan menukar dua posisi kota (swap).
   - Pilih neighbor dengan nilai terbaik (jarak minimum).
5. Program harus menampilkan:
   - Rute awal.
   - Rute terbaik hasil optimasi.
   - Total jarak sebelum dan sesudah optimasi.
6. Jika tidak ditemukan solusi yang lebih baik, tampilkan pesan:
   "Solusi optimal lokal telah ditemukan."

## Soal 2
Sebuah perusahaan ingin mengoptimalkan penjadwalan tugas karyawan menggunakan algoritma Hill Climbing. Setiap solusi merepresentasikan urutan pengerjaan tugas, dan setiap urutan memiliki nilai "cost" berdasarkan waktu penyelesaian total.

Program harus membantu menemukan urutan tugas dengan waktu total paling minimum.

### Ketentuan Program:
1. Representasikan tugas dalam bentuk list, contoh:
   ```python
   tasks = ['A', 'B', 'C', 'D', 'E']
   ```
2. Tentukan sendiri fungsi evaluasi (cost function), misalnya:
   - Berdasarkan waktu pengerjaan tiap tugas.
   - Atau kombinasi waktu dan prioritas.
3. Implementasikan Hill Climbing dengan ketentuan:
   - Solusi awal berupa urutan acak tugas.
   - Neighbor dihasilkan dengan menukar dua tugas.
   - Pilih solusi dengan cost lebih kecil.
4. Tambahkan fitur:
   - Menampilkan setiap iterasi perubahan solusi.
   - Menampilkan nilai cost pada setiap iterasi.
5. Output program harus mencakup:
   - Solusi awal.
   - Proses iterasi (perubahan solusi).
   - Solusi terbaik.
   - Total cost akhir.
6. Analisis:
   - Jelaskan apakah solusi yang diperoleh merupakan global optimum atau hanya local optimum, serta alasan yang mendukung.
