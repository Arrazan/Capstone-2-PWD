# CAPSTONE PROJECT MODULE 2 
# STUDY CASE DATA NILAI SISWA


from tabulate import tabulate

#==========================================================
# Struktur Data Siswa

# PASSLOGIN ===============================================
while True:
    passuser = input("Masukkan password: ")

    ada_huruf = False
    ada_angka = False

    for karakter in passuser:
        if karakter.isalpha():
            ada_huruf = True
        elif karakter.isnumeric():
            ada_angka = True

    if len(passuser) != 7:
        print('Password harus terdiri 7 karakter')
    elif ada_angka and ada_huruf:
        print('Login Berhasil!')
        break
    elif ada_huruf:
        print('Silahkan coba lagi password tidak boleh huruf semua')
    elif ada_angka:
        print('Silahkan coba lagi password tidak boleh angka semua')
    else:
        print("Silahkan Coba Lagi")


# =========================================================
# FUNCTION BANTUAN (HELPER)
# =========================================================

def dataKosong():

    if len(data_murid) == 0:
        print('Belum ada data siswa.')
        return True
    return False


def inputPilihan(pesan, pilihan_valid):

    while True:
        jawaban = input(pesan).upper()
        if jawaban in pilihan_valid:
            return jawaban
        print(f"Input tidak valid. Pilihan yang tersedia: {', '.join(pilihan_valid)}")


def inputNilai(namaMapel):
 
    while True:
        nilai = input(f"Nilai {namaMapel}: ")
        if not nilai.isdigit():
            print("Nilai harus berupa angka!")
        else:
            nilai = int(nilai)
            if 0 <= nilai <= 100:   # penulisan rentang khas Python, sama dengan (nilai>=0 and nilai<=100)
                return nilai
            print("Nilai hanya dalam rentang 0-100!")


def nilaiRata(murid):
  
    # CALLBACK: ambil nilai pembanding berupa RATA-RATA seluruh mapel seorang murid.
    # Dipakai untuk ranking keseluruhan & per kelas.
  
    return rataRata(murid['Nilai'])


def urutkanMurid(daftar, ambil_nilai=nilaiRata, mapel=None):

    daftar = daftar[:]          # salin list (slicing) agar list asli tidak ikut teracak
    n = len(daftar)
    for i in range(n):
        index_terbesar = i
        for j in range(i + 1, n):
            # Tentukan nilai pembanding: pakai mapel kalau diberikan, kalau tidak pakai callback.
            if mapel is None:
                nilai_j = ambil_nilai(daftar[j])
                nilai_terbesar = ambil_nilai(daftar[index_terbesar])
            else:
                nilai_j = daftar[j]['Nilai'][mapel]
                nilai_terbesar = daftar[index_terbesar]['Nilai'][mapel]

            if nilai_j > nilai_terbesar:
                index_terbesar = j
        daftar[i], daftar[index_terbesar] = daftar[index_terbesar], daftar[i]
    return daftar


def buatNIS():
#    Membuat NIS baru 3 digit berdasarkan NIS terbesar yang ada.
    if len(data_murid) == 0:
        nomor = 1
    else:
        nomor_terbesar = 0
        for murid in data_murid:
            angka_nis = int(murid['NIS'])
            if angka_nis > nomor_terbesar:
                nomor_terbesar = angka_nis
        nomor = nomor_terbesar + 1

    # Ubah angka jadi NIS 3 digit dengan menambah '0' di depan sesuai panjangnya.
    if nomor < 10:
        nisBaru = '00' + str(nomor)
    elif nomor < 100:
        nisBaru = '0' + str(nomor)
    else:
        nisBaru = str(nomor)

    return nisBaru


# karena Nama mapel dipakai di banyak tempat -> simpan di Dictionary lalu dipakai ulang. 
NAMA_MAPEL = {
    'MTK': 'Matematika',
    'IPA': 'IPA',
    'B_IND': 'Bahasa Indonesia',
    'B_ING': 'Bahasa Inggris',
    'ART': 'Kesenian',
    'PE': 'Olahraga',
}


data_murid = [
    {'NIS': '001', 'Nama': 'Budi',   'Gender': 'L', 'Kelas': 'A',
     'Nilai': {'MTK': 85, 'IPA': 78, 'B_IND': 90, 'B_ING': 82, 'ART': 88, 'PE': 75}},
    {'NIS': '002', 'Nama': 'Siti',   'Gender': 'P', 'Kelas': 'B',
     'Nilai': {'MTK': 95, 'IPA': 92, 'B_IND': 88, 'B_ING': 90, 'ART': 85, 'PE': 80}},
    {'NIS': '003', 'Nama': 'Joko',   'Gender': 'L', 'Kelas': 'C',
     'Nilai': {'MTK': 89, 'IPA': 84, 'B_IND': 92, 'B_ING': 84, 'ART': 78, 'PE': 82}},
    {'NIS': '004', 'Nama': 'Azizah', 'Gender': 'P', 'Kelas': 'A',
     'Nilai': {'MTK': 77, 'IPA': 67, 'B_IND': 89, 'B_ING': 78, 'ART': 87, 'PE': 83}},
    {'NIS': '005', 'Nama': 'David',  'Gender': 'L', 'Kelas': 'B',
     'Nilai': {'MTK': 82, 'IPA': 85, 'B_IND': 93, 'B_ING': 88, 'ART': 70, 'PE': 89}},
    {'NIS': '006', 'Nama': 'Alice',  'Gender': 'P', 'Kelas': 'C',
     'Nilai': {'MTK': 89, 'IPA': 90, 'B_IND': 85, 'B_ING': 85, 'ART': 93, 'PE': 84}},
    {'NIS': '007', 'Nama': 'Sidu',  'Gender': 'L', 'Kelas': 'A',
     'Nilai': {'MTK': 76, 'IPA': 89, 'B_IND': 65, 'B_ING': 88, 'ART': 80, 'PE': 88}},
    {'NIS': '008', 'Nama': 'Ciro',  'Gender': 'L', 'Kelas': 'B',
     'Nilai': {'MTK': 86, 'IPA': 79, 'B_IND': 80, 'B_ING': 77, 'ART': 90, 'PE': 74}},
    {'NIS': '009', 'Nama': 'Eliza',  'Gender': 'P', 'Kelas': 'C',
     'Nilai': {'MTK': 86, 'IPA': 79, 'B_IND': 95, 'B_ING': 78, 'ART': 87, 'PE': 78}},
]


# =========================================================
# FUNCTION UNTUK MENAMPILKAN TABEL (biar tidak berulang)
# =========================================================
def tampilkanTabelSiswa(daftar):
    tabel = []
    for murid in daftar:
        tabel.append([murid['NIS'], murid['Nama'], murid['Gender'], murid['Kelas']])
    print(tabulate(tabel, headers=['NIS', 'Nama', 'Gender', 'Kelas'], tablefmt='fancy_grid'))


# CRUD ====================================================
def add_murid():
    NIS = buatNIS()
    Nama = input('Masukkan Nama: ')

    # Dua validasi di bawah memakai inputPilihan() yang sama, hanya beda daftar pilihannya
    Gender = inputPilihan('Masukkan Gender (L/P): ', ('L', 'P'))
    Kelas = inputPilihan('Masukkan Kelas (A/B/C): ', ('A', 'B', 'C'))


    nilai = {}
    for kode, nama in NAMA_MAPEL.items():
        nilai[kode] = inputNilai(nama)

    murid_baru = {
        'NIS': NIS,
        'Nama': Nama,
        'Gender': Gender,
        'Kelas': Kelas,
        'Nilai': nilai,
    }

    data_murid.append(murid_baru)
    print("Data Murid Berhasil Ditambahkan! NIS:", NIS)


def list_murid():
    if dataKosong():
        return
    tampilkanTabelSiswa(data_murid)


def editMurid():
    nis_dicari = input('Masukkan NIS Murid yang diinginkan: ')

    for murid in data_murid:                       # cukup keliling dict-nya langsung,
        if murid['NIS'] == nis_dicari:             # tidak perlu range(len(...)) + index
            print('Data Ditemukan!\nNama murid:', murid['Nama'])

            while True:
                print('----EDIT DATA----')
                print('''
1. Kelas
2. Nilai Matematika
3. Nilai IPA
4. Nilai Bahasa Indonesia
5. Nilai Bahasa Inggris
6. Nilai Kesenian
7. Nilai Olahraga
8. Kembali
    ''')
                menuEdit = input('Pilih nomor yang ingin anda ubah: ')

                if menuEdit == '1':
                    murid['Kelas'] = inputPilihan('Masukkan kelas Baru (A/B/C): ', ('A', 'B', 'C'))
                    print('Data Murid Berhasil diperbarui!')


                elif menuEdit in ('2', '3', '4', '5', '6', '7'):
                    peta = {'2': 'MTK', '3': 'IPA', '4': 'B_IND',
                            '5': 'B_ING', '6': 'ART', '7': 'PE'}
                    kode = peta[menuEdit]
                    murid['Nilai'][kode] = inputNilai(NAMA_MAPEL[kode])
                    print('Data Murid Berhasil diperbarui!')

                elif menuEdit == '8':
                    print('Terimakasih Guru!')
                    return
                else:
                    print('tidak ada pilihan tersebut!')

    print('Tidak ada Murid dengan NIS tersebut.')


def delMurid():
    nis_dicari = input('Masukkan NIS Murid yang diinginkan: ')

    for i in range(len(data_murid)):
        if data_murid[i]['NIS'] == nis_dicari:
            print('Data Ditemukan! Nama Murid:', data_murid[i]['Nama'])

            konfirmasi = inputPilihan(
                f"Yakin ingin menghapus data {data_murid[i]['Nama']}? (y/n): ",
                ('Y', 'N'))
            if konfirmasi == 'Y':
                print('Menghapus Data Murid:', data_murid[i]['Nama'])
                data_murid.pop(i)
                print('Data berhasil dihapus.')
            else:
                print('Penghapusan dibatalkan.')
            return

    print('Murid dengan NIS tersebut tidak ditemukan.')


# MENCARI MURID ===========================================
def cariNIS():
    nis_dicari = input('Masukkan NIS Murid: ')

    for murid in data_murid:
        if murid['NIS'] == nis_dicari:

            tabel_nilai = [
                ['NIS', murid['NIS']],
                ['Nama Murid', murid['Nama']],
                ['Gender', murid['Gender']],
                ['Kelas', murid['Kelas']],
            ]
            for kode, nama in NAMA_MAPEL.items():
                tabel_nilai.append([nama, murid['Nilai'][kode]])
            print(tabulate(tabel_nilai, tablefmt='fancy_grid'))
            return

    print('Murid dengan NIS tersebut tidak ditemukan.')


def cariNama():
    nama_dicari = input('Masukkan Nama Murid: ')
    # Kumpulkan yang cocok memakai list comprehension singkat.
    hasil = [m for m in data_murid if m['Nama'].lower() == nama_dicari.lower()]

    if hasil:
        tampilkanTabelSiswa(hasil)
    else:
        print('Tidak ada Murid dengan nama Tersebut.')


def cariKelas():
    kelas_dicari = input('Masukkan Nama Kelas: ')
    hasil = [m for m in data_murid if m['Kelas'].lower() == kelas_dicari.lower()]

    if hasil:
        tampilkanTabelSiswa(hasil)
    else:
        print('Kelas tidak ditemukan.')


# RATA-RATA, GRADE, LULUS/TIDAK ===========================
def rataRata(nilai_dict):
    """
    Rata-rata dari semua nilai mapel.

    KENAPA sum(nilai_dict.values()) / len(nilai_dict)?
    Versi lama menjumlahkan 6 key satu per satu ('MTK'+'IPA'+...). Kalau suatu
    saat mapel bertambah/berkurang, rumus lama harus diedit manual dan rawan
    lupa. Versi ini otomatis mengikuti isi dictionary. (Materi: Dictionary + Math.)
    """
    return sum(nilai_dict.values()) / len(nilai_dict)


def gradeMurid(rata2):
    if rata2 >= 90:
        return 'Grade A'
    elif rata2 >= 80:
        return 'Grade B'
    elif rata2 >= 70:
        return 'Grade C'
    elif rata2 >= 60:
        return 'Grade D'
    else:
        return 'Grade E'


def statusMurid(rata2):
    # Kembalikan hanya status singkat 'Lulus'/'Remedial' supaya mudah dibandingkan.
    if rata2 >= 75:
        return 'Lulus'
    else:
        return 'Remedial'


# MENU STATISTIK ==========================================
def dashboard():
    if dataKosong():
        return

    jumlah_siswa = len(data_murid)

    #  hitung yang 'L', karena sisanya pasti 'P'.
    jumlah_laki = 0
    daftar_rata = []                 # kumpulkan dulu semua rata-rata ke list
    for murid in data_murid:
        if murid['Gender'] == 'L':
            jumlah_laki += 1
        daftar_rata.append(rataRata(murid['Nilai']))
    jumlah_perempuan = jumlah_siswa - jumlah_laki

    # max/min/sum agar simple
    nilai_tertinggi = max(daftar_rata)
    nilai_terendah = min(daftar_rata)
    rata_sekolah = sum(daftar_rata) / jumlah_siswa

    tabel_dashboard = [
        ['Jumlah Siswa', jumlah_siswa],
        ['Jumlah Laki-laki', jumlah_laki],
        ['Jumlah Perempuan', jumlah_perempuan],
        ['Nilai Tertinggi', round(nilai_tertinggi, 2)],
        ['Nilai Terendah', round(nilai_terendah, 2)],
        ['Rata-rata Sekolah', round(rata_sekolah, 2)],
    ]
    print("=== DASHBOARD ===")
    print(tabulate(tabel_dashboard, tablefmt='fancy_grid'))


def rankSeluruh():
    if dataKosong():
        return

    urutan = urutkanMurid(data_murid)

    tabel = []
    peringkat = 1
    for murid in urutan:
        rata = rataRata(murid['Nilai'])
        tabel.append([peringkat, murid['Nama'], murid['Kelas'],
                      round(rata, 2), gradeMurid(rata), statusMurid(rata)])
        peringkat += 1

    print(tabulate(tabel,
                   headers=['Peringkat', 'Nama', 'Kelas', 'Rata-rata', 'Grade', 'Status'],
                   tablefmt='fancy_grid'))


def rankMapel():
    if dataKosong():
        return

    # inputPilihan memvalidasi mapel; pilihan valid diambil dari key NAMA_MAPEL.
    # tuple(NAMA_MAPEL) menghasilkan ('MTK','IPA','B_IND','B_ING','ART','PE').
    mapel = inputPilihan(
        "Mapel yang mau dirangking (MTK/IPA/B_IND/B_ING/ART/PE): ",
        tuple(NAMA_MAPEL))

    # Urutkan berdasarkan mapel terpilih: cukup kirim kode mapel lewat parameter 'mapel'.
    urutan = urutkanMurid(data_murid, mapel=mapel)

    tabel = []
    peringkat = 1
    for murid in urutan:
        tabel.append([peringkat, murid['Nama'], murid['Kelas'], murid['Nilai'][mapel]])
        peringkat += 1

    print(f"--- Ranking {NAMA_MAPEL[mapel]} ---")
    print(tabulate(tabel,
                   headers=['Peringkat', 'Nama', 'Kelas', f'Nilai {mapel}'],
                   tablefmt='fancy_grid'))


def rankKelas():
    kelas_dicari = inputPilihan("Kelas apa yang mau dilihat? (A/B/C): ", ('A', 'B', 'C'))
    if dataKosong():
        return

    # Saring dulu murid di kelas itu, lalu urutkan pakai function yang sama.
    anggota = [m for m in data_murid if m['Kelas'] == kelas_dicari]
    if len(anggota) == 0:
        print("Tidak ada siswa di kelas tersebut.")
        return

    urutan = urutkanMurid(anggota)   # default: urut berdasarkan rata-rata

    tabel = []
    peringkat = 1
    for murid in urutan:
        rata = rataRata(murid['Nilai'])
        tabel.append([peringkat, murid['Nama'], round(rata, 2), gradeMurid(rata)])
        peringkat += 1

    print(f"---- RANKING KELAS {kelas_dicari} ----")
    print(tabulate(tabel, headers=['Peringkat', 'Nama', 'Rata-rata', 'Grade'],
                   tablefmt='fancy_grid'))


def remedial():
    if dataKosong():
        return

    tabel = []
    for murid in data_murid:
        rata = rataRata(murid['Nilai'])
        if statusMurid(rata) == 'Remedial':
            tabel.append([murid['NIS'], murid['Nama'], murid['Kelas'], round(rata, 2)])

    if tabel:
        print('---DAFTAR REMEDIAL---')
        print(tabulate(tabel, headers=['NIS', 'Nama', 'Kelas', 'Rata-rata'],
                       tablefmt='fancy_grid'))
    else:
        print('Tidak ada yang remedial.')


def siswaPres():
    if dataKosong():
        return

    tabel = []
    for murid in data_murid:
        rata = rataRata(murid['Nilai'])
        if gradeMurid(rata) == 'Grade A':
            tabel.append([murid['NIS'], murid['Nama'], murid['Kelas'], round(rata, 2)])

    if tabel:
        print('---Murid Berprestasi---')
        print(tabulate(tabel, headers=['NIS', 'Nama', 'Kelas', 'Rata-rata'],
                       tablefmt='fancy_grid'))
    else:
        print('Belum ada murid berprestasi.')


# MENU SELEKSI LOMBA ======================================
def seleksiLomba(kode_mapel, judul):
 
    if dataKosong():
        return

    # Urutkan pakai function bersama; kirim kode mapel lewat parameter 'mapel'.
    urutan = urutkanMurid(data_murid, mapel=kode_mapel)

    tabel = []
    for i in range(min(3, len(urutan))):     # ambil maksimal 3 teratas
        tabel.append([i + 1, urutan[i]['Nama'], urutan[i]['Kelas'],
                      urutan[i]['Nilai'][kode_mapel]])

    print(f'---{judul}---') #judul tiap tabel menyesuaikan
    print(tabulate(tabel,
                   headers=['Kandidat', 'Nama', 'Kelas', f'Nilai {kode_mapel}'],
                   tablefmt='fancy_grid'))


# MENU-MENU ===============================================

def menuDataSiswa():
    while True:
        print('''
-----DATA MURID-----
1. Tambah Data
2. Lihat Semua Data
3. Edit Data
4. Hapus Data
5. Kembali ke Menu Utama
        ''')
        pilihan = input("Pilih: ")

        if pilihan == '1':
            add_murid()
        elif pilihan == '2':
            list_murid()
        elif pilihan == '3':
            editMurid()
        elif pilihan == '4':
            delMurid()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")


def menuPencarian():
    while True:
        print('''
-----PENCARIAN-----
1. NIS
2. Nama
3. Kelas
4. Kembali ke Menu Utama
        ''')
        pilihan = input("Pilih: ")

        if pilihan == '1':
            cariNIS()
        elif pilihan == '2':
            cariNama()
        elif pilihan == '3':
            cariKelas()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")


def menuStatistik():
    while True:
        print('''
-----STATISTIK SEKOLAH-----
1. Dashboard
2. Ranking Keseluruhan
3. Ranking per Mata Pelajaran
4. Ranking per Kelas
5. Remedial
6. Murid Berprestasi
7. Kembali ke Menu Utama
        ''')
        pilihan = input("Pilih: ")

        if pilihan == '1':
            dashboard()
        elif pilihan == '2':
            rankSeluruh()
        elif pilihan == '3':
            rankMapel()
        elif pilihan == '4':
            rankKelas()
        elif pilihan == '5':
            remedial()
        elif pilihan == '6':
            siswaPres()
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid.")


def menuSeleksi():
    while True:
        print('''
-----SELEKSI LOMBA-----
1. OSN Matematika
2. OSN IPA
3. O2SN
4. FLS2N
5. Kembali ke Menu Utama
        ''')
        pilihan = input("Pilih: ")

        if pilihan == '1':
            seleksiLomba('MTK', 'SELEKSI OSN MATEMATIKA')
        elif pilihan == '2':
            seleksiLomba('IPA', 'SELEKSI OSN IPA')
        elif pilihan == '3':
            seleksiLomba('PE', 'SELEKSI O2SN')
        elif pilihan == '4':
            seleksiLomba('ART', 'SELEKSI FLS2N')
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")


# MENU UTAMA ==============================================
while True:
    print('---------- SELAMAT DATANG ----------')
    print('---------------- DI -----------------')
    print('------------ MENU UTAMA -------------')
    print('------------ TEACHERISM ------------')
    print('''
1. Data Siswa
2. Pencarian
3. Statistik
4. Seleksi Lomba
5. Exit
          ''')
    choose = input('Pilih nomor yang diinginkan wahai guru: ')

    if choose == '1':
        menuDataSiswa()
    elif choose == '2':
        menuPencarian()
    elif choose == '3':
        menuStatistik()
    elif choose == '4':
        menuSeleksi()
    elif choose == '5':
        print('Sampai jumpa lagi, Guru!')
        break
    else:
        print('Pilihanmu Tidak Valid Guru!')