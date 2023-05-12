import tkinter
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
save_button = tkinter.Button(text="Save & Encrypt")
save_button.pack()

decrypt_button = tkinter.Button(text="Decrypt")
decrypt_button.pack()

window.mainloop()
