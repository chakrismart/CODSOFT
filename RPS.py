import tkinter as tk #to import tkinter
from PIL import Image,ImageTk #to put out images
from random import randint
window=tk.Tk()
window.title("ROCK PAPER SCISSORS")
window.configure(background="yellow")

computer_score=tk.Label(window,width=3,text=0,font=('arial',60,'bold'),fg="red",bg="maroon")
computer_score.grid(row=1,column=1)
player_score=tk.Label(window,text=0,width=3,font=('arial',60,'bold'),fg="red",bg="maroon")
player_score.grid(row=1,column=3)
image_rock1 =ImageTk.PhotoImage(Image.open("rock.png"))
image_rock2 =ImageTk.PhotoImage(Image.open("r.png")) #photoimage() is used to out image,open() is used to apply image
image_paper1 =ImageTk.PhotoImage(Image.open("pap.jpg")) 
image_paper2 =ImageTk.PhotoImage(Image.open("p.png"))
image_scissors1 =ImageTk.PhotoImage(Image.open("sci.png"))
image_scissors2 =ImageTk.PhotoImage(Image.open("s.png"))
restart=tk.Button(window,width=10,height=3,text='RESTART',font=('arial',15,'bold'),bg="grey",fg="white",command=lambda:res())
restart.grid(row=1,column=8)
button_rock =  tk.Button(window,width=15,height=3,text='ROCK',font=('arial',15,'bold'),bg="blue",fg="black",command=lambda:choice_update("rock"))
button_rock.grid(row=3,column=0)   #creating buttons
button_paper =  tk.Button(window,width=15,height=3,text='PAPER',font=('arial',15,'bold'),bg="lightgreen",fg="black",command=lambda:choice_update("paper"))
button_paper.grid(row=3,column=2)
button_scissors =  tk.Button(window,width=15,height=3,text='SCISSORS',font=('arial',15,'bold'),bg="orange",fg="black",command=lambda:choice_update("scissors"))
button_scissors.grid(row=3,column=4)
label_player = tk.Label(window,image=image_rock2)
label_player.grid(row=1,column=4)
label_player.image = image_rock1 #save a reference to the image object
label_computer = tk.Label(window,image=image_rock1)
label_computer.grid(row=1,column=0)
label_computer.image = image_rock2 #save a reference to the image object
player_indicator=tk.Label(window,font=("arial",40,"bold"),text="PLAYER",bg="blue",fg="orange")
player_indicator.grid(row=0,column=3)
computer_indicator=tk.Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="blue",fg="orange")
computer_indicator.grid(row=0,column=1)
final_message=tk.Label(window,font=("arial",40,"bold"),bg="red",fg="green")
final_message.grid(row=5,column=2)
def res():
    computer_score['text']='0'
    player_score['text']='0'
def msg_updation(a):
    final_message['text']=a
def computer_update():
    final=int(computer_score['text'])
    final+=1
    computer_score['text']=str(final)
def player_update():
    final=int(player_score['text'])
    final+=1
    player_score['text']=str(final)

def winner_check(p,c):
    if p==c:
        msg_updation("it's tie")
    elif p=='rock':
        if c=='paper':
            msg_updation('COMPUTER WINS')
            computer_update()
        else:
            msg_updation('PLAYER WINS')
            player_update()
    elif p=='paper':
        if c=='scissors':
            msg_updation('COMPUTER WINS')
            computer_update()
        else:
            msg_updation('PLAYER WINS')
            player_update()
    elif p=='scissors':
        if c=='rock':
            msg_updation('COMPUTER WINS')
            computer_update()
        else:
            msg_updation('PLAYER WINS')
            player_update()
    else:
        pass
to_select=["rock","paper","scissors"]
def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer=="rock":
        label_computer.configure(image=image_rock1)
        label_computer.image = image_rock1 #save a reference to the image object
    elif choice_computer=="paper":
        label_computer.configure(image=image_paper1)
        label_computer.image = image_paper1 #save a reference to the image object
    else:
        label_computer.configure(image=image_scissors1)
        label_computer.image = image_scissors1 #save a reference to the image object
    if a=="rock":
        label_player.configure(image=image_rock2)
        label_player.image = image_rock2 #save a reference to the image object
    elif a=="paper":
        label_player.configure(image=image_paper2)
        label_player.image = image_paper2 #save a reference to the image object
    else:
        label_player.configure(image=image_scissors2)
        label_player.image = image_scissors2 #save a reference to the image object
    winner_check(a,choice_computer)




window.mainloop()
