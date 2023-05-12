import base64
import hashlib
import tkinter
from tkinter import messagebox

from cryptography.fernet import Fernet
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=10, pady=10)
window.minsize(width=400, height=500)

# image
image_open = Image.open("./secret_icon.png")
image_secret = ImageTk.PhotoImage(image_open)

label_image = tkinter.Label(image=image_secret)
label_image.pack()

# note title
note_title_label = tkinter.Label(text="Enter your title", font=('Arial', 14, "normal"))
note_title_label.pack()

note_title_entry = tkinter.Entry(width=50)
note_title_entry.pack()

# note text
note_text_label = tkinter.Label(text="Enter your secret", font=('Arial', 14, "normal"))
note_text_label.pack()

note_text_text = tkinter.Text(width=50)
note_text_text.pack()

# master key
master_key_label = tkinter.Label(text="Enter master key", font=('Arial', 14, "normal"))
master_key_label.pack()

master_key_entry = tkinter.Entry(width=50)
master_key_entry.pack()


# buttons
def save_button_onclick():
    if master_key_entry.get() == "" or note_text_text.compare("end-1c", "==", "1.0") or note_title_entry.get() == "":
        return messagebox.showwarning(message="Please enter all information.")
    note_title = note_title_entry.get()
    note_text = note_text_text.get("1.0", "end-1c")
    secret_key = master_key_entry.get()
    secret_note_text = encrypt_note(note_text, secret_key)
    secret_note = note_title + "\n" + secret_note_text
    write_secret_file(secret_note)
    note_title_entry.delete(0, tkinter.END)
    note_text_text.delete("1.0", tkinter.END)
    master_key_entry.delete(0, tkinter.END)


# write secret file
def write_secret_file(note):
    secret_file_path = "./mySecretFile.txt"
    secret_file = open(secret_file_path, 'a+')
    secret_file.write(note + "\n\n")
    secret_file.close()


def encrypt_note(note, key):
    fernet = generate_master_key(key)
    secret_note = fernet.encrypt(note.encode()).decode()
    return secret_note


def decrypt_note(secret_note, key):
    fernet = generate_master_key(key)
    try:
        note = fernet.decrypt(secret_note).decode()
    except:
        messagebox.showerror(message="Please make sure of encrypted info.")
        return secret_note
    return note


def generate_master_key(key):
    generated_key = hashlib.md5(key.encode()).hexdigest()
    encoded_generated_key = base64.urlsafe_b64encode(generated_key.encode())
    fernet = Fernet(encoded_generated_key)
    return fernet


def decrypt_button_onclick():
    if master_key_entry.get() == "" or note_text_text.compare("end-1c", "==", "1.0"):
        return messagebox.showwarning(message="Please enter all information.")
    secret_note = note_text_text.get("1.0", tkinter.END)
    master_key = master_key_entry.get()
    decrypted_note = decrypt_note(secret_note, master_key)
    note_text_text.delete("1.0", tkinter.END)
    note_text_text.insert("1.0", decrypted_note)


save_button = tkinter.Button(text="Save & Encrypt", command=save_button_onclick)
save_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=decrypt_button_onclick)
decrypt_button.pack()

window.mainloop()
