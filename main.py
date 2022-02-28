################## import or install if not installed ############
try:

    from tkinter import Button, Label, Tk,Frame, font, messagebox,PhotoImage
    from screeninfo import get_monitors
    from PIL import Image,ImageTk
except:
    import os
    os.system('pip install pillow')
    os.system('pip install screeninfo')
    os.system('pip install tk')
    try:
        from tkinter import Button, Label, Tk,Frame, font, messagebox,PhotoImage
        from screeninfo import get_monitors
        from PIL import Image,ImageTk
    except:
        exit();

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
    for i in range(len(buttons)):
        print(buttons[i].y*3+buttons[i].x,buttons[i].number)
        if buttons[i].y*3+buttons[i].x!=buttons[i].number:
            return False
    return True


def getwindowSize():

    monitor=get_monitors()[0]
    windowWidth=int(monitor.width*0.4);
    windowHeight=int(monitor.height*0.6);
    return (windowWidth,windowHeight,int(windowWidth//1.5),int(windowHeight//10));


def validMove(button,space,distance):

    if abs(button[0]-space[0])==distance or abs(button[1]-space[1])==distance: return True;
    return False;


def reset():
    global moves,movesLabel,space
    space=(2,2)
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
    buttons=[]
    for i in range(3):
        for j in range(3):
            a=square(table,i,j,j*3+i+1)
            buttons.append(a)
            print(buttons[-1].x,buttons[-1].y)
    buttons[-1].button.destroy()
    buttons.pop()








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
    AiButton=Button(Main,text="Solve Using AI",font=("Arial",32,'bold'),fg='blue',bg='green',)
    AiButton.place(relx=0.7,rely=0.9,relheight=0.05,relwidth=0.2)
    c=MainDesign(Main)
    background_label.place(x=0, y=0,)

    Main.mainloop()
