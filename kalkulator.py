import tkinter as tk
okno = tk.Tk()
vnosno_polje = tk.Entry(okno)
gumbi = tk.Frame(okno)

gumb = tk.Button(okno, text = "Nova igra")
gumb.place(x=50, y=50)


okno.mainloop()
