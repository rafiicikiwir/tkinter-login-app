# 🔐 Aplikasi Login & Logout - Tkinter MySQL

<div align="center">

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![MySQL](https://img.shields.io/badge/database-MySQL-orange.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

Aplikasi desktop sederhana untuk sistem login dan logout menggunakan Python Tkinter yang terhubung dengan database MySQL.

</div>

---

## 📖 Tentang

Aplikasi ini adalah program autentikasi sederhana berbasis desktop yang dibuat untuk keperluan pembelajaran dan tugas sekolah. Menggunakan Python Tkinter untuk tampilan GUI dan MySQL sebagai database penyimpanan data user.

## ✨ Fitur

- 🔐 Login dengan validasi username dan password
- 👤 Dashboard yang menampilkan nama user
- 🚪 Tombol logout untuk keluar dari sistem
- 💬 Notifikasi pesan sukses dan error
- 🎨 Tampilan GUI yang sederhana dan menarik

## 🔧 Kebutuhan Sistem

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **XAMPP** - [Download XAMPP](https://www.apachefriends.org/)

## 📦 Instalasi

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/login-logout-app.git
cd login-logout-app
```

### 2️⃣ Install Library Python

```bash
pip install mysql-connector-python
```

### 3️⃣ Setup Database

**a. Jalankan MySQL di XAMPP**
- Buka **XAMPP Control Panel**
- Klik **Start** pada **MySQL**
- Pastikan statusnya **Running**

**b. Import Database**
- Buka browser, ketik: `http://localhost/phpmyadmin`
- Klik **New** untuk buat database baru
- Nama database: `db_login`
- Klik tab **Import**
- Pilih file `db_login.sql`
- Klik **Go**

## 🚀 Cara Menjalankan

```bash
python app.py
```

## 🔑 Akun Default

| Username | Password |
|----------|----------|
| admin    | 12345    |

## 🛠️ Troubleshooting

### ❌ Error: `ModuleNotFoundError: No module named 'mysql'`
**Solusi:**
```bash
pip install mysql-connector-python
```

### ❌ Error: `Can't connect to MySQL server`
**Solusi:**
- Pastikan MySQL di XAMPP sudah Running
- Cek apakah port MySQL (3306) tidak bentrok
- Restart XAMPP dan coba lagi

### ❌ Error: `Access denied for user 'root'@'localhost'`
**Solusi:**
- Buka file `app.py`
- Sesuaikan konfigurasi database dengan setting MySQL kamu

### ❌ Login Gagal Terus
**Solusi:**
- Pastikan database `db_login` sudah ter-import
- Cek apakah tabel `users` ada dan berisi data

## ⚠️ Catatan Penting

> Aplikasi ini dibuat untuk keperluan pembelajaran.
> Password disimpan dalam bentuk teks biasa (tanpa enkripsi).
> Tidak disarankan untuk penggunaan production/real project.

## 👨‍💻 Pembuat

<div align="center">

**Rafi ahmad**,
**Rizki Farel**,
**Naufal Abdillah**,
**M.Fachri**

</div>
