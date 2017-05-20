import tkinter as tk
okno = tk.Tk()
vnosno_polje = tk.Entry(okno)
gumbi = tk.Frame(okno)

gumb = tk.Button(okno, text = "Nova igra 1")
gumb.place(x=100, y=50)


okno.mainloop()
