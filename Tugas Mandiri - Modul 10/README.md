# Tugas Mandiri Modul 10 (Greedy Best First Search)

Nama: Rovino Ramadhani <br/>
NIM: 103072400031 <br/>
Mata Kuliah: DKA <br/>
Topik: Greedy Best First Search <br/>

File Github : [https://github.com/rovinor4/Praktikum-Dasar-Kecerdasan-Artifisial/tree/8ab19f9eae13369c6dc533db65b566039406292a/Tugas%20Mandiri%20-%20Modul%2010](https://github.com/rovinor4/Praktikum-Dasar-Kecerdasan-Artifisial/tree/8ab19f9eae13369c6dc533db65b566039406292a/Tugas%20Mandiri%20-%20Modul%2010)

## Import Library
Kode berikut digunakan untuk memanggil library heapq. Library ini dipakai sebagai priority queue agar node dengan nilai heuristik terkecil dapat diproses lebih dahulu.


```python
import heapq
```

## Function Greedy Best First Search

Function greedy_bfs() digunakan sebagai function utama untuk menyelesaikan Soal 1 dan Soal 2. Function ini menerima graph, nilai heuristik, node awal, node tujuan, judul soal, dan parameter show_iteration.

Parameter show_iteration digunakan sebagai pembeda antara Soal 1 dan Soal 2. Pada Soal 1, output hanya menampilkan node yang dikunjungi dan jalur akhir. Pada Soal 2, output ditampilkan lebih detail dengan nomor iterasi dan daftar node yang masuk ke open list.


```python
def greedy_bfs(graph, heuristic, start, goal, title, show_iteration=False):
    print(title)

    open_list = []
    heapq.heappush(open_list, (heuristic[start], start, [start]))

    visited = set()
    iteration = 0

    while open_list:
        h_value, current_node, path = heapq.heappop(open_list)

        if current_node in visited:
            continue

        visited.add(current_node)
        iteration += 1

        if show_iteration:
            print(f"\nIterasi ke-{iteration}")
            print(f"Node dikunjungi: {current_node}")
            print(f"Nilai heuristik: {h_value}")
        else:
            print(f"Node dikunjungi: {current_node}, Heuristik: {h_value}")

        if current_node == goal:
            print("\nNode tujuan berhasil ditemukan.")
            print("Jalur:", " -> ".join(path))

            if show_iteration:
                print("Jumlah total iterasi:", iteration)

            return path

        added_nodes = []

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )
                added_nodes.append(neighbor)

        if show_iteration:
            if added_nodes:
                print("Node ditambahkan ke open list:", ", ".join(added_nodes))
            else:
                print("Node ditambahkan ke open list: Tidak ada")

    print("\nNode tujuan tidak dapat ditemukan.")
    return None
```

## Soal 1 - Pencarian Rute Kota
Pada Soal 1, graph merepresentasikan hubungan antar kota. Node awal adalah S, sedangkan node tujuan adalah G. Algoritma Greedy Best First Search memilih node berdasarkan nilai heuristik terkecil.

Dari node S, terdapat pilihan A dan B. Node A dipilih karena memiliki nilai heuristik 5, lebih kecil daripada B yang bernilai 8. Setelah itu, dari A, node C dipilih karena memiliki nilai heuristik 3. Kemudian, dari C, algoritma menuju G dengan heuristik 0.


```python
graph1 = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': ['G'],
    'E': ['G'],
    'G': []
}

heuristic1 = {
    'S': 10,
    'A': 5,
    'B': 8,
    'C': 3,
    'D': 6,
    'E': 9,
    'G': 0
}

greedy_bfs(
    graph=graph1,
    heuristic=heuristic1,
    start='S',
    goal='G',
    title='SOAL 1 - GREEDY BEST FIRST SEARCH',
    show_iteration=False
)
```

    SOAL 1 - GREEDY BEST FIRST SEARCH
    Node dikunjungi: S, Heuristik: 10
    Node dikunjungi: A, Heuristik: 5
    Node dikunjungi: C, Heuristik: 3
    Node dikunjungi: G, Heuristik: 0
    
    Node tujuan berhasil ditemukan.
    Jalur: S -> A -> C -> G





    ['S', 'A', 'C', 'G']



### Analisis Soal 1

Jalur yang dihasilkan adalah S -> A -> C -> G. Jalur ini dipilih karena Greedy Best First Search selalu memilih node dengan nilai heuristik terkecil dari open list.

Jalur tersebut belum tentu merupakan jalur terpendek secara aktual, karena algoritma hanya melihat nilai heuristik, bukan total biaya atau bobot jarak dari awal sampai tujuan. Selain itu, data pada soal hanya menampilkan hubungan antar node dan nilai heuristik, sehingga tidak ada perhitungan total bobot aktual yang dapat dibandingkan.

____

## Soal 2 - Sistem Rekomendasi Produk
Pada Soal 2, graph merepresentasikan hubungan antar produk dalam katalog. Node awal adalah P1, sedangkan node tujuan adalah GOAL. Berbeda dari Soal 1, Soal 2 menampilkan proses iterasi secara lebih lengkap.

Algoritma dimulai dari P1. Setelah itu, node P2, P3, dan P4 dimasukkan ke open list. Karena P2 memiliki heuristik paling kecil, yaitu 9, maka P2 dipilih. Selanjutnya, P5 dan P6 masuk ke open list. Node P5 dipilih karena heuristiknya 4, lalu algoritma menuju GOAL.


```python
graph2 = {
    'P1': ['P2', 'P3', 'P4'],
    'P2': ['P5', 'P6'],
    'P3': ['P6', 'P7'],
    'P4': ['P7', 'P8'],
    'P5': ['GOAL'],
    'P6': ['GOAL'],
    'P7': ['GOAL'],
    'P8': ['GOAL'],
    'GOAL': []
}

heuristic2 = {
    'P1': 15,
    'P2': 9,
    'P3': 11,
    'P4': 13,
    'P5': 4,
    'P6': 6,
    'P7': 8,
    'P8': 12,
    'GOAL': 0
}

greedy_bfs(
    graph=graph2,
    heuristic=heuristic2,
    start='P1',
    goal='GOAL',
    title='SOAL 2 - GREEDY BEST FIRST SEARCH',
    show_iteration=True
)

```

    SOAL 2 - GREEDY BEST FIRST SEARCH
    
    Iterasi ke-1
    Node dikunjungi: P1
    Nilai heuristik: 15
    Node ditambahkan ke open list: P2, P3, P4
    
    Iterasi ke-2
    Node dikunjungi: P2
    Nilai heuristik: 9
    Node ditambahkan ke open list: P5, P6
    
    Iterasi ke-3
    Node dikunjungi: P5
    Nilai heuristik: 4
    Node ditambahkan ke open list: GOAL
    
    Iterasi ke-4
    Node dikunjungi: GOAL
    Nilai heuristik: 0
    
    Node tujuan berhasil ditemukan.
    Jalur: P1 -> P2 -> P5 -> GOAL
    Jumlah total iterasi: 4





    ['P1', 'P2', 'P5', 'GOAL']



### Analisis Soal 2
Jalur yang dihasilkan adalah P1 -> P2 -> P5 -> GOAL. Jalur ini dipilih karena setiap iterasi Greedy Best First Search selalu mengambil node dengan nilai heuristik terkecil dari open list.

Solusi ini bersifat lokal, bukan solusi terbaik secara global. Hal ini karena Greedy Best First Search hanya mempertimbangkan estimasi heuristik pada node berikutnya, bukan menghitung total biaya dari node awal sampai node tujuan. Dengan kata lain, algoritma memilih pilihan yang terlihat paling baik pada saat itu, tetapi tidak menjamin hasil akhirnya merupakan solusi paling optimal secara keseluruhan.
