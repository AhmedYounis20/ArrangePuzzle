################## import or install if not installed ############
import time
import threading

try:

    from tkinter import Button, Label, Tk,Frame, font, messagebox,PhotoImage
    from screeninfo import get_monitors
    from PIL import Image,ImageTk
    from random import randrange
    from functions import *
    from SearchAgent import *

except:
    import os
    os.system('pip install pillow')
    os.system('pip install screeninfo')
    os.system('pip install tk')
    try:
        from tkinter import Button, Label, Tk,Frame, font, messagebox,PhotoImage
        from screeninfo import get_monitors
        from PIL import Image,ImageTk
        from random import randrange
        from functions import *
        from SearchAgent import *

    except:
        exit();



### initial condition
buttons_start=[(0,0,4),(0,1,1),(0,2,3),(1,0,2),(1,2,5),(2,0,8),(2,1,7),(2,2,6),]
start_space=(1,1)

# global varibal 
movesLabel=None
moves =0
space=(2,2)
buttons=[]
Main=None

########
class square:
    def __init__(self,Place,x,y,number):
        self.distance=307.20000000000005
        self.x=x
        self.y=y
        self.number=number;
        self.Place=Place
        self.button=Button(Place,bg='yellow',relief="ridge",font=("Helvetica", 32),text=str(self.number),command=lambda:self.moveTo(space[0],space[1]))
        self.button.place(x=self.x*self.distance,y=self.y*self.distance,width=self.distance,height=self.distance)
    
    def validMove(self):
        if ((abs(self.x-space[0])==1 and self.y==space[1]) or  (abs(self.y-space[1])==1) and self.x==space[0]) and abs(self.x-space[0]) !=abs(self.y-space[1]) : return True;
        return False;
    def moveTo(self,x,y):
        global space 
        if self.validMove():
            self.button.destroy()
            self.button=Button(self.Place,bg='yellow',relief="ridge",font=("Helvetica", 32),text=str(self.number),command=lambda:self.moveTo(space[0],space[1]));
            space=(self.x,self.y)
            self.x=x
            self.y=y
            self.button.place(x=self.x*self.distance,y=self.y*self.distance,width=self.distance,height=self.distance)
            buttonMoved()
            if success():
                font1 = font.Font(name='TkCaptionFont', exists=True)
                font1.config(family='courier new', size=40)

                message=messagebox.showwarning('winning',"You Won!🎉")
                MainDesign(Main)
            print(getPlaces())
        else:
            font1 = font.Font(name='TkCaptionFont', exists=True)
            font1.config(family='courier new', size=40)
            message=messagebox.showwarning('Loser','Game Over☠️')
            MainDesign(Main)




def buttonMoved():
    global moves,movesLabel
    moves+=1
    movesLabel.configure(text="Moves: {}".format(moves))
    
def success():
    check=1
    global buttons
    for button in buttons:
        print(button.y*3+button.x,button.number)
        if button.y*3+button.x!=button.number:
            return False
    return True

def getPlaces():
    global buttons
    places=[]
    for button in buttons:
        places+=[(button.y*3+button.x,button.number)]
    places.sort()
    sortednumbers=[]
    zero_place=space[1]*3+space[0];
    places+=[(zero_place,0)]
    places.sort()

    for place in places:
        sortednumbers+=[place[1]]

    return sortednumbers

    



def solveUsingAi():
    threading.Thread(target=solveUsingAi1).start()


def solveUsingAi1():
    global buttons
    print(getPlaces())
    moves=solve("BFS",getPlaces())['solution']
    print(moves)
    moveschar={'^':(0,1),'>':(-1,0),'V':(0,-1),'<':(1,0)}
    for move in moves:
        for button in buttons:
            if button.x==space[0]+moveschar[move][0]and button.y==space[1]+moveschar[move][1] :
                time.sleep(0.5)
                threading.Thread(target=button.moveTo(space[0],space[1])).start()
                break;

def getwindowSize():

    monitor=get_monitors()[0]
    windowWidth=int(monitor.width*0.4);
    windowHeight=int(monitor.height*0.6);
    return (windowWidth,windowHeight,int(windowWidth//1.5),int(windowHeight//10));


def validMove(button,space,distance):

    if abs(button[0]-space[0])==distance or abs(button[1]-space[1])==distance: return True;
    return False;


def reset():
    global moves,movesLabel,space,start_space
    shuffle_puzzle(50)

    space=start_space
    print(space,start_space)
    moves=0
    movesLabel.configure(text="Moves: {}".format(moves))
    for button in buttons:
        button.button.destroy()


def MainDesign(Main):

    winodwSize=getwindowSize()
    
    table=Frame(Main,bg="brown")
    table.place(relx=0.2,rely=0.1,height=winodwSize[0]*0.6,width=winodwSize[0]*0.6)
    print(table.winfo_geometry())
    global buttons,moves,movesLabel


    reset()
    print(buttons_start,"good")
    buttons=[]
    for index in buttons_start:
        a=square(table,index[0],index[1],index[2])
        buttons.append(a)

    # buttons[-1].button.destroy()
    # buttons.pop()






def shuffle_puzzle(n):
    global buttons_start,start_space

    puzzle=[0,1, 2, 3, 4, 5, 6, 7, 8]

    for _ in range(n):
        actions=possibleMoves(puzzle)
        rand_index=randrange(0,len(actions))
        puzzle=Move(puzzle,actions[rand_index])
    start_space=(puzzle.index(0)%3,puzzle.index(0)//3)
    buttons_start=[]

    for i in range(0,9):
        if puzzle[i]!=0:
            buttons_start+=[(i%3,i//3,puzzle[i])]

if __name__=="__main__":

    Main=Tk()
    
    MainSize=getwindowSize()

    Main.geometry("{}x{}+{}+{}".format(MainSize[0],MainSize[1],MainSize[2],MainSize[3]))
    background_image= ImageTk.PhotoImage(Image.open("background.jpg").resize((MainSize[0],MainSize[1])))
    background_label = Label(Main, image=background_image)
    Main.title("Arrange Puzzle 🤗       Younis©")
    Main.resizable(False,False)
    movesLabel=Label(Main,text="Moves: {}".format(moves),font=("Arial",32,'bold'),fg='red',bg="blue")

    movesLabel.place(rely=0.02,relx=0.01,width=300,height=90)
    resetGame=Button(Main,text="Reset",font=("Arial",32,'bold'),fg='blue',bg='orange',command=lambda:MainDesign(Main))
    resetGame.place(relx=0.1,rely=0.9,relheight=0.05,relwidth=0.2)
    AiButton=Button(Main,text="Solve Using AI",font=("Arial",32,'bold'),fg='blue',bg='green',command=solveUsingAi)
    AiButton.place(relx=0.7,rely=0.9,relheight=0.05,relwidth=0.2)
    c=MainDesign(Main)
    background_label.place(x=0, y=0,)

    Main.mainloop()
