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

TOP_LEFT_X = 100 
TOP_LEFT_Y = 100 
TOP_RIGHT_X = 600 
TOP_RIGHT_Y = 100
BOTTOM_LEFT_X = 100 
BOTTOM_LEFT_Y = 600 
BOTTOM_RIGHT_X = 600 
BOTTOM_RIGHT_Y = 600  

TOP_1_3_X = ((TOP_RIGHT_X - TOP_LEFT_X) / 3 ) + TOP_LEFT_X 
TOP_1_3_Y = TOP_RIGHT_Y 
TOP_2_3_X = ((TOP_RIGHT_X - TOP_LEFT_X) / 3 ) * 2 + TOP_LEFT_X 
TOP_2_3_Y = TOP_RIGHT_Y 
LEFT_1_3_X = TOP_LEFT_X
LEFT_1_3_Y = ((BOTTOM_LEFT_Y - TOP_LEFT_Y ) / 3 ) + TOP_LEFT_Y 
RIGHT_1_3_X = TOP_RIGHT_X 
RIGHT_1_3_Y = ((BOTTOM_RIGHT_Y - TOP_RIGHT_Y ) / 3 ) + TOP_RIGHT_Y 
LEFT_2_3_X = TOP_LEFT_X
LEFT_2_3_Y = ((BOTTOM_LEFT_Y - TOP_LEFT_Y ) / 3 ) * 2 + TOP_LEFT_Y 
RIGHT_2_3_X = TOP_RIGHT_X 
RIGHT_2_3_Y = ((BOTTOM_RIGHT_Y - TOP_RIGHT_Y ) / 3 ) * 2 + TOP_RIGHT_Y 
BOTTOM_1_3_X = ((BOTTOM_RIGHT_X - BOTTOM_LEFT_X) / 3 ) + BOTTOM_LEFT_X 
BOTTOM_1_3_Y = BOTTOM_RIGHT_Y 
BOTTOM_2_3_X = ((BOTTOM_RIGHT_X - BOTTOM_LEFT_X) / 3 ) * 2 + BOTTOM_LEFT_X 
BOTTOM_2_3_Y = BOTTOM_RIGHT_Y 

canvas1.create_line(TOP_LEFT_X, TOP_LEFT_Y, TOP_RIGHT_X, TOP_RIGHT_Y ) 
canvas1.create_line(TOP_LEFT_X, TOP_LEFT_Y, BOTTOM_LEFT_X, BOTTOM_LEFT_Y ) 
canvas1.create_line(TOP_RIGHT_X, TOP_RIGHT_Y, BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y ) 
canvas1.create_line(BOTTOM_LEFT_X, BOTTOM_LEFT_Y, BOTTOM_RIGHT_X, BOTTOM_RIGHT_Y )  
canvas1.create_line(TOP_1_3_X, TOP_1_3_Y, BOTTOM_1_3_X, BOTTOM_1_3_Y ) 
canvas1.create_line(TOP_2_3_X, TOP_2_3_Y, BOTTOM_2_3_X, BOTTOM_2_3_Y ) 
canvas1.create_line(LEFT_1_3_X, LEFT_1_3_Y, RIGHT_1_3_X, RIGHT_1_3_Y ) 
canvas1.create_line(LEFT_2_3_X, LEFT_2_3_Y, RIGHT_2_3_X, RIGHT_2_3_Y ) 

def getSquareRoot ():  
    x1 = entry1.get() 
    
    label1 = tk.Label(root, text= float(x1)**0.5) 
    canvas1.create_window(650, 680, window=label1) 
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot) 
canvas1.create_window(650, 720, window=button1) 
 
root.mainloop() 
 