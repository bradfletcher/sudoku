import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 800, height = 800 )
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(650, 650, window=entry1) 

for x in range(9):  
    for y in range(9):  
        valueEntry = tk.Entry (root, width = 1 ) 
        canvas1.create_window(100 + 50*x, 100 + 50*y , window=valueEntry) 

def getSquareRoot ():  
    x1 = entry1.get() 
    
    label1 = tk.Label(root, text= float(x1)**0.5) 
    canvas1.create_window(650, 680, window=label1) 
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot) 
canvas1.create_window(650, 720, window=button1) 
 
root.mainloop() 
 