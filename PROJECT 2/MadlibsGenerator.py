import tkinter as tk
from tkinter import messagebox
import pygame
import os

# Setup pygame buat musik
pygame.mixer.init()
pygame.mixer.music.load("sound_velocity.mp3")  # Ganti musik absurd aesthetic kamu
pygame.mixer.music.play(-1)  # Looping terus biar makin vibes

# Fungsi buat muat cerita dari file
def muat_cerita():
    with open("cerita.txt", "r", encoding="utf-8") as file:
        return file.read()

# Ambil kata-kata yang ada di dalam tanda < >
def ambil_kata_khusus(teks):
    kata = set()
    mulai = -1
    for i, char in enumerate(teks):
        if char == "<":
            mulai = i
        elif char == ">" and mulai != -1:
            kata.add(teks[mulai:i + 1])
            mulai = -1
    return list(kata)

# Pop-up buat input kata dari user
def input_popup(pesan):
    popup = tk.Toplevel(root)
    popup.title("Isi kata absurd kamu!")
    popup.geometry("300x100")
    popup.config(bg="#fef2f2")

    label = tk.Label(popup, text=pesan, bg="#fef2f2", font=("Comic Sans MS", 10, "bold"))
    label.pack(pady=5)

    entri = tk.Entry(popup)
    entri.pack()

    nilai = {"hasil": None}

    def simpan():
        nilai["hasil"] = entri.get()
        popup.destroy()

    tombol = tk.Button(popup, text="Oke Gas!", command=simpan, bg="#fb7185", fg="white")
    tombol.pack(pady=5)

    popup.transient(root)
    popup.grab_set()
    root.wait_window(popup)
    return nilai["hasil"]

# Fungsi isi cerita
def isi_cerita():
    try:
        cerita = muat_cerita()
    except FileNotFoundError:
        messagebox.showerror("Error", "File cerita.txt gak ketemu. Simpen dulu ya!")
        return

    kata_khusus = ambil_kata_khusus(cerita)
    jawaban = {}

    for kata in kata_khusus:
        isi = input_popup(f"Masukin {kata[1:-1]}:")
        if isi is None:
            return
        jawaban[kata] = isi

    for kata in kata_khusus:
        cerita = cerita.replace(kata, jawaban[kata])

    hasil_output.delete(1.0, tk.END)
    hasil_output.insert(tk.END, cerita)

# GUI
root = tk.Tk()
root.title("Cerita Absurd Interaktif")
root.geometry("700x500")
root.config(bg="#fff1f2")

judul = tk.Label(root, text="Cerita Absurd Interaktif", font=("Comic Sans MS", 18, "bold"), bg="#fff1f2", fg="#e11d48")
judul.pack(pady=15)

tombol_mulai = tk.Button(root, text="Mulai Cerita", command=isi_cerita, bg="#f43f5e", fg="white", font=("Arial", 12, "bold"))
tombol_mulai.pack(pady=10)

hasil_output = tk.Text(root, wrap=tk.WORD, font=("Courier", 11), bg="#ffe4e6", fg="#111827")
hasil_output.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
