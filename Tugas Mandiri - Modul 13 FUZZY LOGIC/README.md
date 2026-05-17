# Soal Mandiri Fuzzy Logic

Repository ini berisi pengerjaan soal mandiri Fuzzy Logic menggunakan Python. Setiap soal dibuat dalam bentuk notebook
dan mengikuti ketentuan pada modul penugasan, mulai dari fuzzifikasi, evaluasi aturan, sampai defuzzifikasi.

## Informasi Mahasiswa

Nama : Rovino Ramadhani  
NIM : 103072400031  
Program Studi : S1 Informatika  
Universitas : Telkom University

## Daftar Soal

| No | Judul Soal                        | Metode                           | File Notebook |
|----|-----------------------------------|----------------------------------|---------------|
| 1  | Kontrol Kecepatan Kipas AC        | Mamdani                          | `soal1.ipynb` |
| 2  | Estimasi Tip Restoran             | Sugeno Orde-0                    | `soal2.ipynb` |
| 3  | Kontrol Robot Penghindar Halangan | Mamdani Multi-Input Multi-Output | `soal3.ipynb` |

## Soal 1 - Kontrol Kecepatan Kipas AC

Soal pertama membahas sistem fuzzy Mamdani untuk menentukan kecepatan kipas AC berdasarkan suhu dan kelembaban ruangan.

Input yang digunakan adalah suhu ruangan dengan rentang 0 sampai 50 derajat Celsius dan kelembaban ruangan dengan
rentang 0 sampai 100 persen. Output yang dihasilkan berupa kecepatan kipas dalam persentase.

| Komponen        | Keterangan                                |
|-----------------|-------------------------------------------|
| Metode          | Mamdani                                   |
| Input 1         | Suhu ruangan, rentang 0 sampai 50 °C      |
| Input 2         | Kelembaban ruangan, rentang 0 sampai 100% |
| Output          | Kecepatan kipas, rentang 0 sampai 100%    |
| Operator AND    | Min                                       |
| Implikasi       | Clipping                                  |
| Agregasi        | Max                                       |
| Defuzzifikasi   | Centroid                                  |
| Resolusi        | 0.1 atau 1001 titik                       |
| File pengerjaan | `soal1.ipynb`                             |

## Soal 2 - Estimasi Tip Restoran

Soal kedua membahas sistem fuzzy Sugeno orde-0 untuk memperkirakan besaran tip restoran berdasarkan kualitas makanan dan
kualitas pelayanan.

| Komponen            | Keterangan                              |
|---------------------|-----------------------------------------|
| Metode              | Sugeno Orde-0                           |
| Input 1             | Kualitas makanan, rentang 0 sampai 10   |
| Input 2             | Kualitas pelayanan, rentang 0 sampai 10 |
| Output              | Tip dalam persen                        |
| Bentuk output       | Konstanta                               |
| Operator AND        | Min                                     |
| Defuzzifikasi       | Weighted average                        |
| Rumus defuzzifikasi | Σ(wi × zi) / Σ(wi)                      |
| Jumlah aturan       | 9 aturan                                |
| File pengerjaan     | `soal2.ipynb`                           |

Pada metode Sugeno orde-0, setiap aturan menghasilkan nilai output konstan. Nilai akhir tip diperoleh dari rata-rata
berbobot berdasarkan firing strength dari aturan yang aktif.

## Soal 3 - Kontrol Robot Penghindar Halangan

Soal ketiga membahas sistem fuzzy Mamdani untuk mengontrol robot penghindar halangan dengan dua input dan dua output.

Input yang digunakan adalah jarak sensor kiri dan jarak sensor kanan, masing-masing dengan rentang 0 sampai 200 cm.
Output yang dihasilkan adalah kecepatan robot dan arah belok robot.

| Komponen        | Keterangan                                  |
|-----------------|---------------------------------------------|
| Metode          | Mamdani                                     |
| Input 1         | Jarak sensor kiri, rentang 0 sampai 200 cm  |
| Input 2         | Jarak sensor kanan, rentang 0 sampai 200 cm |
| Output 1        | Kecepatan robot, rentang 0 sampai 100 cm/s  |
| Output 2        | Arah belok, rentang -90 sampai 90 derajat   |
| Operator AND    | Min                                         |
| Defuzzifikasi   | Centroid                                    |
| Resolusi        | 0.5 untuk kecepatan dan 0.5 untuk arah      |
| File pengerjaan | `soal3.ipynb`                               |

## Library yang Digunakan

| Library                   | Fungsi                                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| SymPy                     | Digunakan untuk membuat fungsi keanggotaan fuzzy secara simbolik, seperti fungsi triangular dan trapezoidal. |
| SymPy Piecewise           | Digunakan untuk membuat fungsi keanggotaan dengan beberapa kondisi nilai.                                    |
| Python Built-in Function  | Digunakan untuk input, output, konversi tipe data, perulangan, dan perhitungan dasar.                        |
| Python Exception Handling | Digunakan untuk menangani kesalahan input, misalnya input bukan angka.                                       |

### Penjelasan Library

SymPy digunakan karena program membutuhkan fungsi matematika berbasis simbol. Pada program, SymPy dipakai untuk membuat
variabel simbolik `x`, menyusun fungsi keanggotaan fuzzy, dan menghitung nilai keanggotaan berdasarkan input pengguna.

`Piecewise` dari SymPy digunakan untuk membuat fungsi keanggotaan yang memiliki beberapa kondisi. Bentuk ini cocok untuk
fuzzy membership function karena setiap kategori fuzzy memiliki rentang nilai yang berbeda.

Fungsi bawaan Python digunakan untuk menjalankan proses dasar program, seperti menerima input, mencetak hasil,
menghitung nilai minimum dan maksimum, serta melakukan operasi numerik.

Exception handling digunakan agar program tidak berhenti ketika pengguna memasukkan input yang tidak sesuai. Jika input
bukan angka atau berada di luar rentang, program akan meminta pengguna memasukkan ulang nilai yang benar.

## Referensi

1. Modul Praktikum Dasar Kecerdasan Artificial Intelligence, S1 Informatika, School of Computing, Telkom University.

2. Soal Penugasan Mandiri Fuzzy Logic (AI) - Python, Kelas IF-04-01.

3. SymPy Documentation - Piecewise  
   https://docs.sympy.org/latest/modules/functions/elementary.html

4. SymPy Documentation - Basic Operations  
   https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html

5. Python Documentation - Errors and Exceptions  
   https://docs.python.org/3/tutorial/errors.html

6. Python Documentation - Input and Output  
   https://docs.python.org/3/tutorial/inputoutput.html

7. Python Documentation - Built-in Functions  
   https://docs.python.org/3/library/functions.html