<div align='center'>
    <h1>Ujian Praktikum Dasar Kecerdasan Artifisial</h1>
    <h2>Nama &nbsp;&nbsp;: Rovino Ramadhani</h2>
    <h2>NIM &nbsp;&nbsp;&nbsp;&nbsp;: 103072400031</h2>
    <h2>Kelas &nbsp;: IF 04-01</h2>
</div>

---

**Petunjuk Pengerjaan:**
- Kerjakan semua soal sesuai instruksi.
- Setiap soal memiliki sub-soal (cabang) dengan bobot nilai masing-masing.
- Total bobot keseluruhan soal adalah **100 poin**.
- Ganti setiap `None` dengan jawaban yang sesuai.

---

## Soal 1: Pengenalan Python `(Total Bobot: 15 Poin)`

---

### 1a. Prosedur dan Fungsi `(Bobot: 5 Poin)`

Buatlah sebuah **fungsi** bernama `hitung_diskon` yang menerima dua parameter:
- `harga`, harga asli suatu barang (float)
- `persen_diskon`, persentase diskon (float, contoh: 20 untuk 20%)

Fungsi tersebut harus **mengembalikan harga setelah diskon**.

Kemudian, minta *input* dari pengguna untuk `harga` dan `persen_diskon`, panggil fungsinya, dan cetak hasilnya.

*Test case* program:

| **Input** | **Output** |
|---|---|
| Masukkan harga: `200000`<br>Masukkan persen diskon: `25` | `Harga setelah diskon: 150000.0` |
| Masukkan harga: `500000`<br>Masukkan persen diskon: `10` | `Harga setelah diskon: 450000.0` |


```python
# [1a] Prosedur dan Fungsi

def hitung_diskon(harga, persen_diskon):
    return harga - (harga * persen_diskon / 100)

harga = float(input("Masukkan harga: "))
persen_diskon = float(input("Masukkan persen diskon: "))

hasil = hitung_diskon(harga, persen_diskon)
print("Harga setelah diskon:", hasil)
```

    Harga setelah diskon: 450000.0


### 1b. Perulangan dan Pengkondisian `(Bobot: 5 Poin)`

Buat program yang meminta *input* bilangan bulat positif `n` dari pengguna. Program harus menampilkan **FizzBuzz** dari 1 hingga `n` dengan aturan:
- Jika bilangan habis dibagi 3 **dan** 5, cetak `"FizzBuzz"`
- Jika bilangan habis dibagi 3 saja, cetak `"Fizz"`
- Jika bilangan habis dibagi 5 saja, cetak `"Buzz"`
- Selain itu, cetak bilangannya

*Test case* (n = 15):
```
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
```


```python
# [1b] Perulangan dan Pengkondisian - FizzBuzz

n = int(input("Masukkan n: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz


### 1c. List, Dictionary, dan Soal Cerita `(Bobot: 5 Poin)`

Sebuah toko ingin merekap stok barang. Data stok disimpan dalam **dictionary** dengan `key` nama barang dan `value` jumlah stok. Buat program yang:
1. Menerima input nama barang dan jumlah stok dari pengguna, diulang terus hingga user mengetik `"selesai"` sebagai nama barang.
2. Setelah selesai input, tampilkan **daftar barang** beserta stoknya.
3. Tampilkan barang dengan **stok terbanyak**.

*Test case:*
```
Masukkan nama barang (atau 'selesai'): Apel
Masukkan jumlah stok: 50
Masukkan nama barang (atau 'selesai'): Mangga
Masukkan jumlah stok: 30
Masukkan nama barang (atau 'selesai'): selesai

Daftar Stok Barang:
- Apel: 50
- Mangga: 30
Barang dengan stok terbanyak: Apel (50)
```


```python
# [1c] List, Dictionary, dan Soal Cerita

stok_barang = {}

while True:
    nama = input("Masukkan nama barang (atau 'selesai'): ")
    if nama.lower() == "selesai":
        break
    jumlah = int(input("Masukkan jumlah stok: "))
    stok_barang[nama] = jumlah

print("\nDaftar Stok Barang:")
for nama, jumlah in stok_barang.items():
    print(f"- {nama}: ", jumlah)

barang_terbanyak = max(stok_barang, key=stok_barang.get)
print(f"Barang dengan stok terbanyak: {barang_terbanyak} {stok_barang[barang_terbanyak]}")
```

    
    Daftar Stok Barang:
    - Apel:  50
    - Mangga:  30
    Barang dengan stok terbanyak: Apel 50


---
## Soal 2: NumPy dan Matplotlib `(Total Bobot: 25 Poin)`

---

### 2a. Deklarasi dan Atribut Array NumPy `(Bobot: 10 Poin)`

Lengkapi kode berikut untuk:
1. Membuat array 2D berukuran **4x4** berisi bilangan acak bulat antara **1 dan 50** menggunakan NumPy.
2. Cetak atribut array: dimensi, bentuk (shape), ukuran (size), dan tipe data (dtype).
3. Hitung dan cetak **nilai maksimum**, **nilai minimum**, dan **rata-rata** dari array tersebut.

*Contoh output:*
```
Array:
[[23  7 45  1]
 [12 38  9 50]
 [ 4 17 42  6]
 [29 33 11 18]]
Dimensi: 2
Bentuk: (4, 4)
Ukuran: 16
Tipe Data: int64
Nilai Maksimum: 50
Nilai Minimum: 1
Rata-rata: 21.5625
```


```python
# [2a] Deklarasi dan Atribut Array NumPy
import numpy as np

array = np.random.randint(1, 51, size=(4, 4))

print("Array:")
print(array)

print("Dimensi:", array.ndim)
print("Bentuk:", array.shape)
print("Ukuran:", array.size)
print("Tipe Data:", array.dtype)

print("Nilai Maksimum:", array.max())
print("Nilai Minimum:", array.min())
print("Rata-rata:", array.mean())
```

    Array:
    [[48 47 19 16]
     [ 7 41 24 50]
     [49 24 43 35]
     [ 9 39 22 39]]
    Dimensi: 2
    Bentuk: (4, 4)
    Ukuran: 16
    Tipe Data: int64
    Nilai Maksimum: 50
    Nilai Minimum: 7
    Rata-rata: 32.0


### 2b. Operasi Array NumPy `(Bobot: 5 Poin)`

Diberikan dua array nilai ujian mahasiswa berikut. Lakukan operasi berikut:
1. Gabungkan `nilai_uts` dan `nilai_uas` menjadi array 2D berukuran 2×5.
2. Hitung **rata-rata nilai akhir** setiap mahasiswa dengan rumus: `nilai_akhir = 0.4 * UTS + 0.6 * UAS`
3. Cetak array 2D gabungan dan nilai akhir.

*Contoh output:*
```
Gabungan UTS dan UAS:
[[70 80 65 90 75]
 [80 75 70 85 90]]
Nilai Akhir: [76. 77. 68. 87. 84.]
```


```python
# [2b] Operasi Array NumPy
import numpy as np

nilai_uts = np.array([70, 80, 65, 90, 75])
nilai_uas = np.array([80, 75, 70, 85, 90])

gabungan = np.array([nilai_uts, nilai_uas])
print("Gabungan UTS dan UAS:")
print(gabungan)

nilai_akhir = 0.4 * nilai_uts + 0.6 * nilai_uas
print("Nilai Akhir:", nilai_akhir)
```

    Gabungan UTS dan UAS:
    [[70 80 65 90 75]
     [80 75 70 85 90]]
    Nilai Akhir: [76. 77. 68. 87. 84.]


### 2c. Visualisasi Data dengan Matplotlib `(Bobot: 10 Poin)`

Gunakan data nilai akhir dari soal **2b** untuk membuat dua visualisasi dalam **satu figure** (2 subplot berdampingan):

- **Subplot kiri**: *Bar chart* nilai akhir setiap mahasiswa (label sumbu x: nama mahasiswa, sumbu y: nilai)
- **Subplot kanan**: *Pie chart* proporsi mahasiswa yang **Lulus** (nilai akhir ≥ 70) vs **Tidak Lulus**

Ketentuan:
- Ukuran figure: 12×5, DPI 100
- Judul subplot kiri: `"Nilai Akhir Mahasiswa"`
- Judul subplot kanan: `"Proporsi Kelulusan"`
- Nama mahasiswa: `["Andi", "Budi", "Citra", "Deni", "Eva"]`
- Gunakan warna berbeda untuk setiap bar pada bar chart



```python
# [2c] Visualisasi Data dengan Matplotlib
import numpy as np
import matplotlib.pyplot as plt

mahasiswa = ["Andi", "Budi", "Citra", "Deni", "Eva"]
nilai_uts = np.array([70, 80, 65, 90, 75])
nilai_uas = np.array([80, 75, 70, 85, 90])
nilai_akhir = 0.4 * nilai_uts + 0.6 * nilai_uas

fig, ax = plt.subplots(1, 2, figsize=(12, 5), dpi=100)

warna = ['blue', 'green', 'orange', 'purple', 'red']
ax[0].bar(mahasiswa, nilai_akhir, color=warna)
ax[0].set_title("Nilai Akhir Mahasiswa")
ax[0].set_xlabel("Nama Mahasiswa")
ax[0].set_ylabel("Nilai")

lulus = np.sum(nilai_akhir >= 70)
tidak_lulus = np.sum(nilai_akhir < 70)
ax[1].pie([lulus, tidak_lulus], labels=["Lulus", "Tidak Lulus"], autopct='%1.1f%%')
ax[1].set_title("Proporsi Kelulusan")

plt.tight_layout()
plt.show()
```


    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_14_0.png)
    


---
## Soal 3: Pengenalan Library NetworkX `(Total Bobot: 20 Poin)`

---

### Fungsi Pendukung (!! Tidak usah dimodifikasi !!)


```python
import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=2000,
            font_color='white', font_weight='bold', width=5)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                  font_color='blue', font_weight='bold', font_size=12)
    plt.margins(0.2)
    plt.title(title)
    plt.show()
```

### 3a. Undirected Graph `(Bobot: 7 Poin)`

Buat *undirected graph* dengan node dan edge berikut, kemudian:
1. Inisialisasi graf tidak berarah.
2. Tambahkan node: `1, 2, 3, 4, 5`.
3. Tambahkan edge: `1-2`, `1-3`, `2-4`, `3-4`, `4-5`.
4. Cetak daftar node, edge, dan derajat setiap node.
5. Tampilkan graf menggunakan `show_graph()`.

*Contoh output cetak:*
```
Node: [1, 2, 3, 4, 5]
Edge: [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
Derajat 1: 2
Derajat 2: 2
Derajat 3: 2
Derajat 4: 3
Derajat 5: 1
```


```python
# [3a] Undirected Graph

pos_3a = {1: (0,1), 2: (1,2), 3: (1,0), 4: (2,1), 5: (3,1)}

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5])

G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

print("Node:", list(G.nodes()))
print("Edge:", list(G.edges()))
for node in G.nodes():
    print(f"Derajat {node}:", G.degree[node])

show_graph(G, pos_3a, title="Undirected Graph")
```

    Node: [1, 2, 3, 4, 5]
    Edge: [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    Derajat 1: 2
    Derajat 2: 2
    Derajat 3: 2
    Derajat 4: 3
    Derajat 5: 1



    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_19_1.png)
    


### 3b. Directed Graph `(Bobot: 7 Poin)`

Buat *directed graph* dengan node dan edge berikut:
1. Inisialisasi graf berarah.
2. Tambahkan node: `1, 2, 3, 4, 5`.
3. Tambahkan edge berarah: `1→2`, `1→3`, `3→4`, `4→2`, `4→5`.
4. Cetak daftar node, edge, dan **in-degree** serta **out-degree** setiap node.
5. Tampilkan graf menggunakan `show_graph()`.

*Contoh output cetak:*
```
Node: [1, 2, 3, 4, 5]
Edge: [(1, 2), (1, 3), (3, 4), (4, 2), (4, 5)]
In-degree 1: 0  | Out-degree 1: 2
In-degree 2: 2  | Out-degree 2: 0
...
```


```python
# [3b] Directed Graph

pos_3b = {1: (0,1), 2: (1,2), 3: (1,0), 4: (2,1), 5: (3,1)}

DG = nx.DiGraph()

DG.add_nodes_from([1, 2, 3, 4, 5])

DG.add_edges_from([(1, 2), (1, 3), (3, 4), (4, 2), (4, 5)])

print("Node:", list(DG.nodes()))
print("Edge:", list(DG.edges()))
for node in DG.nodes():
    print(f"In-degree {node}: {DG.in_degree[node]}  | Out-degree {node}: {DG.out_degree[node]}")

show_graph(DG, pos_3b, title="Directed Graph")
```

    Node: [1, 2, 3, 4, 5]
    Edge: [(1, 2), (1, 3), (3, 4), (4, 2), (4, 5)]
    In-degree 1: 0  | Out-degree 1: 2
    In-degree 2: 2  | Out-degree 2: 0
    In-degree 3: 1  | Out-degree 3: 1
    In-degree 4: 1  | Out-degree 4: 2
    In-degree 5: 1  | Out-degree 5: 0



    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_21_1.png)
    


### 3c. Graf Berbobot `(Bobot: 6 Poin)`

Buat **graf berarah berbobot** yang merepresentasikan jaringan distribusi barang antar kota. Buat graf lengkap sesuai data berikut:

| Asal | Tujuan | Jarak (km) |
|------|--------|------------|
| Jakarta | Bandung | 150 |
| Jakarta | Bogor | 60 |
| Bogor | Bandung | 120 |
| Bandung | Cirebon | 130 |
| Bogor | Cirebon | 200 |

Kemudian tampilkan graf menggunakan `show_graph()`. Gunakan `pos` yang sudah disediakan di bawah.


```python
# [3c] Graf Berbobot

pos_3c = {
    'Jakarta': (0, 1),
    'Bogor': (1, 0),
    'Bandung': (2, 2),
    'Cirebon': (3, 1)
}

G = nx.DiGraph()

G.add_weighted_edges_from([
    ('Jakarta', 'Bandung', 150),
    ('Jakarta', 'Bogor', 60),
    ('Bogor', 'Bandung', 120),
    ('Bandung', 'Cirebon', 130),
    ('Bogor', 'Cirebon', 200)
])

show_graph(G, pos_3c, title="Graf Berbobot")
```


    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_23_0.png)
    


---
## Soal 4: Implementasi BFS dan DFS `(Total Bobot: 20 Poin)`

---

### Fungsi Pendukung (!! Tidak usah dimodifikasi !!)


```python
import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=3500,
            font_color='white', font_weight='bold', width=5)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                  font_color='blue', font_weight='bold', font_size=16)
    plt.margins(0.2)
    plt.title(title)
    plt.show()
```

### 4a. Implementasi BFS pada Weighted Undirected Graph `(Bobot: 10 Poin)`

Seorang penjelajah sedang menjelajahi kota **BojongCity**. Kota ini memiliki beberapa titik penting yang dihubungkan oleh jalan dengan jarak tertentu. Bantu penjelajah tersebut dengan membuat program menggunakan algoritma **BFS**.

**Graf Kota BojongCity:**
- Node: `PK` (Pusat Kota), `Terminal`, `Stasiun`, `Pasar`, `RS` (Rumah Sakit)
- Edge (tidak berarah) dengan weight:
  - PK ↔ Terminal: 4 km
  - PK ↔ Stasiun: 3 km
  - Stasiun ↔ RS: 5 km
  - Terminal ↔ Pasar: 3 km
  - Pasar ↔ Stasiun: 1 km
  - Terminal ↔ Stasiun: 6 km

Lakukan langkah berikut:
1. Buat graf dan tambahkan node serta edge-nya.
2. Tampilkan graf menggunakan `show_graph()`.
3. Implementasikan fungsi `bfs_search(bfs_tree, start, end)` untuk menemukan jalur BFS.
4. Implementasikan fungsi `calculate_total_distance(graph, path)` untuk menghitung total jarak.
5. Minta input `start_node` dan `end_node` dari pengguna, tampilkan rute BFS dan total jarak.

*Test case:*

| Input | Output |
|-------|--------|
| Start: `Pasar`, End: `PK` | `Rute terpendek dari Pasar ke PK: ['Pasar', 'Terminal', 'PK']`<br>`Total jarak tempuh: 7 km` |


```python
# [4a] Implementasi BFS

pos_kota = {
    'PK': (0, 0), 'Terminal': (-1, 1),
    'Stasiun': (1, 0), 'Pasar': (-1, -1), 'RS': (2, 0)
}

kota = nx.Graph()

nodes = ['PK', 'Terminal', 'Stasiun', 'Pasar', 'RS']
kota.add_nodes_from(nodes)

edges = [
    ('PK', 'Terminal', 4),
    ('PK', 'Stasiun', 3),
    ('Stasiun', 'RS', 5),
    ('Terminal', 'Pasar', 3),
    ('Pasar', 'Stasiun', 1),
    ('Terminal', 'Stasiun', 6)
]
kota.add_weighted_edges_from(edges)

show_graph(kota, pos=pos_kota, title="Graf Kota BojongCity")

def bfs_search(bfs_tree, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = bfs_tree[current_node]
    path.append(start)
    path.reverse()
    return path

def calculate_total_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        node_awal = path[i]
        node_tujuan = path[i + 1]
        total_distance += graph[node_awal][node_tujuan]['weight']
    return total_distance

start_node = input("Masukkan titik awal: ")
end_node = input("Masukkan titik tujuan: ")

bfs_edges = list(nx.bfs_edges(kota, start_node))
bfs_tree = {}
for u, v in bfs_edges:
    bfs_tree[v] = u

shortest_path = bfs_search(bfs_tree, start_node, end_node)
if shortest_path:
    total_distance = calculate_total_distance(kota, shortest_path)
    print(f"Rute terpendek dari {start_node} ke {end_node}: {shortest_path}")
    print(f"Total jarak tempuh: {total_distance} km")
```


    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_28_0.png)
    


    Rute terpendek dari Pasar ke PK: ['Pasar', 'Terminal', 'PK']
    Total jarak tempuh: 7 km


### 4b. Implementasi DFS pada Tree `(Bobot: 10 Poin)`

Budi memiliki struktur folder di laptopnya yang direpresentasikan sebagai *tree* berarah. Bantu Budi menemukan file yang ia cari menggunakan algoritma **DFS**.

**Struktur Tree:**
- `Root` berisi: `Documents`, `Images`, `Videos`
- `Documents` berisi: `File4.docx`, `File1.txt`
- `Images` berisi: `File2.jpg`
- `Videos` berisi: `File3.mp4`

Lakukan langkah berikut:
1. Buat graf berarah `data_budi`, tambahkan node dan edge sesuai struktur di atas.
2. Tampilkan graf menggunakan `show_graph()`.
3. Cetak setiap folder beserta isinya.
4. Implementasikan fungsi `dfs_search(graph, start, goal)` menggunakan stack.
5. Minta input `start_node` dan `end_node` dari pengguna dan tampilkan rute DFS.

*Test case:*

| Input | Output |
|-------|--------|
| Start: `Root`, End: `File2.jpg` | `Rute dari Root ke File2.jpg: ['Root', 'Images', 'File2.jpg']` |


```python
# [4b] Implementasi DFS

pos_budi = {
    'Root': (0, 0), 'Documents': (-1, -1), 'Images': (1, -1), 'Videos': (2, -1),
    'File1.txt': (-1, -2), 'File4.docx': (-1.5, -2),
    'File2.jpg': (1, -2), 'File3.mp4': (2, -2)
}

data_budi = nx.DiGraph()

nodes = ['Root', 'Documents', 'Images', 'Videos', 'File1.txt', 'File4.docx', 'File2.jpg', 'File3.mp4']
data_budi.add_nodes_from(nodes)

edges = [
    ('Root', 'Documents'),
    ('Root', 'Images'),
    ('Root', 'Videos'),
    ('Documents', 'File4.docx'),
    ('Documents', 'File1.txt'),
    ('Images', 'File2.jpg'),
    ('Videos', 'File3.mp4')
]
data_budi.add_edges_from(edges)

show_graph(data_budi, pos=pos_budi, title="Struktur Folder Budi")

print("Daftar Folder beserta isinya di laptop Budi")
for node in data_budi.nodes():
    children = list(data_budi.successors(node))
    if children:
        print(f"- {node} berisi: {children}")

def dfs_search(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        current_node, path = stack.pop()
        if current_node == goal:
            return path
        for neighbor in graph.successors(current_node):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    return None

start_node = input("Masukkan folder/file awal: ")
end_node = input("Masukkan folder/file tujuan: ")
path = dfs_search(data_budi, start_node, end_node)

if path:
    print(f"Rute yang harus dilalui dari {start_node} ke {end_node}: {path}")
else:
    print(f"Tidak ada rute dari {start_node} ke {end_node}.")
```


    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_30_0.png)
    


    Daftar Folder beserta isinya di laptop Budi
    - Root berisi: ['Documents', 'Images', 'Videos']
    - Documents berisi: ['File4.docx', 'File1.txt']
    - Images berisi: ['File2.jpg']
    - Videos berisi: ['File3.mp4']
    Rute yang harus dilalui dari Root ke File2.jpg: ['Root', 'Images', 'File2.jpg']


---
## Soal 5: Implementasi Uniform Cost Search (UCS) `(Total Bobot: 20 Poin)`

---

### Fungsi Pendukung (!! Tidak usah dimodifikasi !!)


```python
import networkx as nx
import matplotlib.pyplot as plt

pos_network = {
    'S': (0, 4), 'R-A': (-2, 2), 'R-B': (2, 2),
    'Sw-A1': (-3, 0), 'Sw-A2': (-1, 0), 'Sw-B1': (2, 0),
    'C-A1': (-3, -2), 'C-A2': (-1, -2), 'C-B1': (1, -2), 'C-B2': (3, -2)
}

def show_graph(G, pos=None, title=''):
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=2000,
            font_color='white', font_weight='bold', width=5)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                  font_color='blue', font_weight='bold', font_size=16)
    plt.margins(0.2)
    plt.title(title)
    plt.show()
```

### 5a. Membangun Graf Jaringan Komputer `(Bobot: 8 Poin)`

Seorang insinyur jaringan ingin memetakan infrastruktur jaringan komputer perusahaan sebagai sebuah *tree* tidak berarah.

**Daftar Perangkat:**
| Nama | Kode |
|------|------|
| Server Utama | S |
| Router-A | R-A |
| Router-B | R-B |
| Switch-A1 | Sw-A1 |
| Switch-A2 | Sw-A2 |
| Switch-B1 | Sw-B1 |
| Computer-A1 | C-A1 |
| Computer-A2 | C-A2 |
| Computer-B1 | C-B1 |
| Computer-B2 | C-B2 |

**Koneksi dan Latency (ms):**
| Sumber | Tujuan | Latency |
|--------|--------|--------|
| S | R-A | 5 |
| S | R-B | 3 |
| R-A | Sw-A1 | 2 |
| R-A | Sw-A2 | 4 |
| R-B | Sw-B1 | 6 |
| Sw-A1 | C-A1 | 3 |
| Sw-A2 | C-A2 | 7 |
| Sw-B1 | C-B1 | 5 |
| Sw-B1 | C-B2 | 2 |

Buat graf tidak berarah, tambahkan semua node dan edge-nya, lalu tampilkan menggunakan `show_graph(network, pos_network, title='Graf Jaringan Komputer')`.


```python
# network hilang
network = nx.Graph()

nodes = ['S', 'R-A', 'R-B', 'Sw-A1', 'Sw-A2', 'Sw-B1', 'C-A1', 'C-A2', 'C-B1', 'C-B2']
network.add_nodes_from(nodes)

edges = [
    ('S', 'R-A', 5),
    ('S', 'R-B', 3),
    ('R-A', 'Sw-A1', 2),
    ('R-A', 'Sw-A2', 4),
    ('R-B', 'Sw-B1', 6),
    ('Sw-A1', 'C-A1', 3),
    ('Sw-A2', 'C-A2', 7),
    ('Sw-B1', 'C-B1', 5),
    ('Sw-B1', 'C-B2', 2)
]
network.add_weighted_edges_from(edges)

show_graph(network, pos_network, title="Graf Jaringan Komputer")
```


    
![png](ujian_dka_rovino%20ramadhani_103072400031_files/ujian_dka_rovino%20ramadhani_103072400031_35_0.png)
    


### 5b. Cetak Koneksi Setiap Perangkat `(Bobot: 4 Poin)`

Buat program yang mencetak setiap perangkat beserta perangkat lain yang terhubung langsung dengannya.

*Contoh output:*
```
Koneksi setiap perangkat:
- S terhubung dengan: ['R-A', 'R-B']
- R-A terhubung dengan: ['S', 'Sw-A1', 'Sw-A2']
...
```


```python
# [5b] Cetak Koneksi Setiap Perangkat

print("Koneksi setiap perangkat:")
for node in network.nodes():
    neighbors = list(network.neighbors(node))
    if neighbors:
        print(f"- {node} terhubung dengan: {neighbors}")
```

    Koneksi setiap perangkat:
    - S terhubung dengan: ['R-A', 'R-B']
    - R-A terhubung dengan: ['S', 'Sw-A1', 'Sw-A2']
    - R-B terhubung dengan: ['S', 'Sw-B1']
    - Sw-A1 terhubung dengan: ['R-A', 'C-A1']
    - Sw-A2 terhubung dengan: ['R-A', 'C-A2']
    - Sw-B1 terhubung dengan: ['R-B', 'C-B1', 'C-B2']
    - C-A1 terhubung dengan: ['Sw-A1']
    - C-A2 terhubung dengan: ['Sw-A2']
    - C-B1 terhubung dengan: ['Sw-B1']
    - C-B2 terhubung dengan: ['Sw-B1']


### 5c. Implementasi UCS untuk Mencari Rute Latency Terendah `(Bobot: 8 Poin)`

Implementasikan algoritma **Uniform Cost Search (UCS)** menggunakan `nx.astar_path()` dengan heuristik 0 untuk menemukan rute dengan latency terendah dari perangkat sumber ke perangkat tujuan.

Lakukan:
1. Buat fungsi `heuristable(a, b)` yang mengembalikan 0.
2. Minta input `perangkat sumber` dan `perangkat tujuan` dari pengguna.
3. Temukan rute menggunakan `astar_path()`.
4. Hitung total latency menggunakan `astar_path_length()`.
5. Tampilkan rute dan total latency.

*Test case:*

| Input | Output |
|-------|--------|
| Sumber: `S`, Tujuan: `C-B1` | `Perangkat yang dikunjungi dari S ke C-B1: ['S', 'R-B', 'Sw-B1', 'C-B1']`<br>`Besar latency dari S ke C-B1: 14ms` |


```python
# [5c] Implementasi UCS

# Fungsi heuristik UCS (selalu 0)
def heuristable(a, b):
    return 0;

# Minta input dari pengguna
start_node = input("Masukkan perangkat sumber: ")
end_node = input("Masukkan perangkat tujuan: ")

# Cari rute dengan astar_path (UCS dengan heuristik 0)
path = nx.astar_path(
    network, start_node, end_node,
    heuristic=heuristable,
    weight='weight'
)

# Hitung total latency
path_latency = nx.astar_path_length(
    network, start_node, end_node,
    heuristic=heuristable,
    weight='weight'
)

print(f"Perangkat yang dikunjungi dari {start_node} ke {end_node}: {path}")
print(f"Besar latency dari {start_node} ke {end_node}: {path_latency}ms")
```

    Perangkat yang dikunjungi dari S ke C-B1: ['S', 'R-B', 'Sw-B1', 'C-B1']
    Besar latency dari S ke C-B1: 14ms


---
<div align='center'>
    <h3>--- Selamat Mengerjakan ---</h3>
</div>
