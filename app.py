import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_login"
)
cursor = db.cursor()

def login():
    username = entry_user.get()
    password = entry_pass.get()

    sql = "SELECT * FROM user WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    hasil = cursor.fetchone()

    if hasil:
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}")
        halaman_index(username)
    else:
        messagebox.showerror("Login Gagal", "Username atau Password salah")

def halaman_index(username):
    root.destroy()

    index = tk.Tk()
    index.title("Halaman Index")
    index.geometry("400x300")
    index.configure(bg="#1e293b")

    frame = tk.Frame(index, bg="#0f172a", bd=0)
    frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=200)

    tk.Label(
        frame,
        text=f"Selamat Datang\n{username}",
        fg="white",
        bg="#0f172a",
        font=("Arial", 16, "bold"),
        justify="center"
    ).pack(pady=30)

    def logout():
        messagebox.showinfo("Logout", "Anda berhasil logout")
        index.destroy()

    tk.Button(
        frame,
        text="Logout",
        command=logout,
        bg="#ef4444",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        width=15,
        pady=5
    ).pack()

    index.mainloop()

root = tk.Tk()
root.title("Login Aplikasi")
root.geometry("400x350")
root.configure(bg="#020617")

frame = tk.Frame(root, bg="#0f172a", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=280)

tk.Label(
    frame,
    text="LOGIN USER",
    fg="white",
    bg="#0f172a",
    font=("Arial", 18, "bold")
).pack(pady=20)

tk.Label(
    frame,
    text="Username",
    fg="white",
    bg="#0f172a",
    font=("Arial", 11)
).pack(anchor="w", padx=30)

entry_user = tk.Entry(
    frame,
    font=("Arial", 11),
    relief="flat"
)
entry_user.pack(padx=30, pady=5, fill="x")

tk.Label(
    frame,
    text="Password",
    fg="white",
    bg="#0f172a",
    font=("Arial", 11)
).pack(anchor="w", padx=30, pady=(10, 0))

entry_pass = tk.Entry(
    frame,
    show="*",
    font=("Arial", 11),
    relief="flat"
)
entry_pass.pack(padx=30, pady=5, fill="x")

tk.Button(
    frame,
    text="LOGIN",
    command=login,
    bg="#22c55e",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="flat",
    pady=6
).pack(pady=25, padx=30, fill="x")

tk.Label(
    frame,
    text="© XI RPL - Login App",
    fg="#94a3b8",
    bg="#0f172a",
    font=("Arial", 9)
).pack(side="bottom", pady=10)

root.mainloop()
