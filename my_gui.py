import tkinter as tk
from tkinter import ttk

def convert():
    print(entryInt.get())
    output_string.set('test')
#window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master =  window, text = 'Miles to Kilometers', font = 'Calibri 12 bold')
title_label.pack()

#input
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame , textvariable=entryInt)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side='left', padx = 10)
button.pack(side='left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_lable = ttk.Label(master = window, text = 'Output' ,textvariable= output_string)
output_lable.pack(pady = 5)

#run
window.mainloop()