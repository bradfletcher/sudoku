class Grid: 
    elements = [] 

    def __init__(self ):  
        print("New Grid Init ")  
        for x in range(9) :  
            self.elements.append(0)  

    def addElement(self, spaceNumber, element ) :  
        self.elements[spaceNumber] = element  

    def __str__(self) :  
        printOut = "" 
        for e in self.elements:  
            printOut = printOut + str(e) + ", "   

        return printOut 

class SudokuBoard:  
    # there are 9 grids, each grid has 9 elements in it 
    gridArray = [] 

    def __init__(self  ):  
        for x in range(9) :  
            self.gridArray.append(Grid() ) 

    def addElement(self, gridNumber, spaceNumber, element ):  
        gridArray[gridNumber].addElement(spaceNumber, element) 
    
    def printBoard(self ):  
        for e in self.gridArray: 
            print("Grid ")   
            print(e )  


import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 800, height = 800 )  
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(650, 650, window=entry1) 
  
lblTitle = tk.Label(root, text="Sudoku Solver")  
lblTitle.place(relx = 0.5,  
                   rely = 0.05 , 
                   anchor = 'center') 


horGap = 0
vertGap = 0 

entries = [] 

board = SudokuBoard()  

board.printBoard() 

for x in range(9):  
    vertGap = 0  
    if ( (x % 3 ) == 0 ):  
        horGap = (horGap + 20) 
    for y in range(9):  
        if ( (y % 3) == 0 ) : 
            vertGap = vertGap + 15 
        entries.append( tk.Entry (root, width = 1 ) ) 
        
        canvas1.create_window(110 + 50*x + horGap, 130 + 50*y + vertGap , window=entries[-1]) 

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
    x1 = entries[0].get() 
    
    label1 = tk.Label(root, text= float(x1)**0.5) 
    canvas1.create_window(650, 680, window=label1) 
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot) 
canvas1.create_window(650, 720, window=button1) 
 
root.mainloop() 
 