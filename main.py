import tkinter
from tkinter import filedialog
from pdf2docx import Converter

docx_file = "C:/Users/alper/OneDrive/Masaüstü/sample.docx"

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        cv = Converter(file_path)
        cv.convert(docx_file)
        cv.close()

window = tkinter.Tk()
window.title("PDF CONVERTER")
window.minsize(width=400, height=400)

btn = tkinter.Button(text="Select a File", command=open_file_dialog, bg="light blue")
btn.config(height=3, width=9)
btn.place(x=170, y=150)

window.mainloop()