# 🎓 TEACHERISM — Aplikasi Data Nilai Siswa

> **Capstone Project Module 2 — Study Case: Data Nilai Siswa**
> Aplikasi berbasis terminal (CLI) untuk membantu guru mengelola data siswa, menghitung nilai, membuat peringkat, dan menyeleksi kandidat lomba.

---

## 🇮🇩 Bahasa Indonesia

### Deskripsi

**TEACHERISM** adalah program Python sederhana yang berjalan di terminal untuk mengelola data akademik siswa. Program menyimpan data siswa (NIS, nama, gender, kelas, dan nilai 6 mata pelajaran) lalu menyediakan fitur CRUD, pencarian, statistik, ranking, serta seleksi lomba. Data disimpan di memori (list of dictionary) selama program berjalan.

### ✨ Fitur Utama

- **Login berpassword** — password wajib 7 karakter dan mengandung kombinasi huruf + angka.
- **Data Siswa (CRUD)** — tambah, lihat, edit, dan hapus data siswa. NIS dibuat otomatis (3 digit).
- **Pencarian** — cari siswa berdasarkan NIS, Nama, atau Kelas.
- **Statistik Sekolah**
  - Dashboard (jumlah siswa, gender, nilai tertinggi/terendah, rata-rata sekolah)
  - Ranking keseluruhan (dengan grade & status kelulusan)
  - Ranking per mata pelajaran
  - Ranking per kelas
  - Daftar siswa remedial (rata-rata < 75)
  - Daftar siswa berprestasi (Grade A)
- **Seleksi Lomba** — otomatis mengambil 3 kandidat terbaik untuk OSN Matematika, OSN IPA, O2SN, dan FLS2N.

### 📚 Mata Pelajaran

| Kode | Mata Pelajaran |
|------|----------------|
| MTK | Matematika |
| IPA | IPA |
| B_IND | Bahasa Indonesia |
| B_ING | Bahasa Inggris |
| ART | Kesenian |
| PE | Olahraga |

### 🏅 Sistem Grade & Status

| Rata-rata | Grade | Status |
|-----------|-------|--------|
| ≥ 90 | A | Lulus |
| 80 – 89 | B | Lulus |
| 75 – 79 | C | Lulus |
| 70 – 74 | C | Remedial |
| 60 – 69 | D | Remedial |
| < 60 | E | Remedial |

> Batas kelulusan adalah rata-rata **≥ 75** (di bawahnya → Remedial).

### ⚙️ Cara Menjalankan

1. Pastikan **Python 3** sudah terpasang.
2. Pasang dependensi:
   ```bash
   pip install tabulate
   ```
3. Jalankan program:
   ```bash
   python "cs 2 tes 2.py"
   ```
4. Masukkan password (contoh valid: `abc1234`), lalu ikuti menu.

### 🗂️ Struktur Data

Setiap siswa disimpan sebagai *dictionary* di dalam list `data_murid`:

```python
{
    'NIS': '001',
    'Nama': 'Budi',
    'Gender': 'L',
    'Kelas': 'A',
    'Nilai': {'MTK': 85, 'IPA': 78, 'B_IND': 90,
              'B_ING': 82, 'ART': 88, 'PE': 75}
}
```

### 🧭 Struktur Menu

```
MENU UTAMA
├── 1. Data Siswa   → Tambah / Lihat / Edit / Hapus
├── 2. Pencarian    → NIS / Nama / Kelas
├── 3. Statistik    → Dashboard / Ranking / Remedial / Berprestasi
├── 4. Seleksi Lomba→ OSN MTK / OSN IPA / O2SN / FLS2N
└── 5. Exit
```

---

## 🇬🇧 English

### Description

**TEACHERISM** is a simple terminal-based (CLI) Python program for managing students' academic data. It stores student records (ID/NIS, name, gender, class, and 6 subject scores) and provides CRUD operations, search, statistics, rankings, and competition candidate selection. Data lives in memory (a list of dictionaries) while the program runs.

### ✨ Key Features

- **Password login** — must be exactly 7 characters and contain both letters and digits.
- **Student Data (CRUD)** — add, view, edit, and delete records. NIS is generated automatically (3 digits).
- **Search** — find students by NIS, Name, or Class.
- **School Statistics** — dashboard, overall ranking, per-subject ranking, per-class ranking, remedial list (average < 75), and honor-roll list (Grade A).
- **Competition Selection** — automatically picks the top 3 candidates for Math Olympiad (OSN MTK), Science Olympiad (OSN IPA), Sports (O2SN), and Arts (FLS2N).

### ⚙️ How to Run

1. Make sure **Python 3** is installed.
2. Install the dependency:
   ```bash
   pip install tabulate
   ```
3. Run the program:
   ```bash
   python "cs 2 tes 2.py"
   ```
4. Enter a password (a valid example: `abc1234`), then follow the menu.

---

## 📦 Dependensi / Dependencies

- [`tabulate`](https://pypi.org/project/tabulate/) — menampilkan tabel rapi di terminal / pretty terminal tables.

## 📝 Catatan / Notes

- Data bersifat sementara (in-memory) dan **akan hilang** saat program ditutup. / Data is in-memory and **will be lost** when the program closes.
- Disarankan mengganti nama file menjadi tanpa spasi, misalnya `data_nilai_siswa.py`, agar lebih mudah dijalankan. / Consider renaming the file without spaces, e.g. `data_nilai_siswa.py`, for easier execution.

## 👤 Author

Capstone Project Module 2 — Study Case: Data Nilai Siswa.
