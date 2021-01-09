import tkinter as tk

HEIGHT = 400
WIDTH = 500

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='yellow')
frame.place(relwidth = 1, relheight = 1)

root.title("Welcome to LikeGeeks")
botton = tk.Button(root, text = "Hello", bg='gray', fg='red')
botton.pack()
root.mainloop()