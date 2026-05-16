# Tugas Mandiri Modul 6 (DFS)

# Soal 1 – Pencarian Jalur pada Tree (DFS)

### **Studi Kasus:**

Sebuah perusahaan memiliki struktur organisasi berbentuk tree seperti berikut:

* A adalah direktur utama
* B dan C adalah manajer
* D, E adalah bawahan B
* F, G adalah bawahan C

Relasi:

```
A → B, C  
B → D, E  
C → F, G  
```

### **Tugas:**

1. Buat graph menggunakan **NetworkX** sesuai struktur di atas
2. Implementasikan DFS mulai dari node `'A'`
3. Tampilkan urutan edge yang dikunjungi DFS
4. Batasi traversal hanya sampai **depth 2**

### **Output yang diharapkan:**

* Urutan DFS tanpa batas
* Urutan DFS dengan `depth_limit=2`

---

### **Ketentuan:**

* Gunakan `nx.Graph()`
* Gunakan `nx.dfs_edges()`
* Gunakan perulangan untuk mencetak hasil

---

# **Soal 2 – Mencari Jalur ke Tujuan (DFS pada Directed Graph)**

### **Studi Kasus:**

Sebuah sistem navigasi memiliki jalur sebagai berikut:

```
A → B, C  
B → D, E  
C → E, F  
E → F  
```

* Node **A** adalah titik awal (Start)
* Node **F** adalah tujuan (Goal)

---

### **Tugas:**

1. Buat **directed graph** menggunakan `nx.DiGraph()`
2. Implementasikan DFS mulai dari node `'A'`
3. Tampilkan urutan traversal DFS
4. Tentukan apakah node `'F'` dapat dicapai menggunakan DFS
5. (Opsional) Hentikan pencarian saat node tujuan ditemukan

---

### **Output yang diharapkan:**

* Urutan DFS
* Informasi apakah goal ditemukan atau tidak

---

### **Ketentuan:**

* Gunakan `nx.dfs_edges()`
* Gunakan kondisi untuk mengecek apakah node tujuan ditemukan
* Tampilkan hasil dalam bentuk print yang jelas