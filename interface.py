import tkinter as tk

HEIGHT = 400
WIDTH = 700

root = tk.Tk()
root.title("Welcome to LikeGeeks")
# Tao giao dien cha
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()
# Tao khung ben trong giao dien cha
frame = tk.Frame(root, bg='#ADD7F6', bd=5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor='n')
# Tao mot vung nhap
entry = tk.Entry(frame, bg='white')
entry.place(relwidth = 0.65, relheight = 1)
# Tao node button
button = tk.Button(frame, text = "Submit", bg='gray', fg='white')
button.place(relx=0.7, relheight=1, relwidth=0.3)
# Tao mot nhan
# label = tk.Label(frame, text='this is lable', bg='yellow')
# label.grid(row=1, column=1)

root.mainloop()