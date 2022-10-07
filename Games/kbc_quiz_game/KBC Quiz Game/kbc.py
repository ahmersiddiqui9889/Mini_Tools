from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer

mixer.init()
mixer.music.load('audio/kbc.mp3')
mixer.music.play(-1)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "11:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]


def select(event):
    mixer.music.set_volume(1)
    b = event.widget
    value = b['text']

    callButton.config(image='')
    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()
    for i in range(15):
        if value == correct_answers[i]:
            if value == third_option[14]:
                def playagain():
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    amountlabel.config(image=amountimage)
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()
                    mixer.music.load('audio/kbc.mp3')
                    mixer.music.play(-1)

                def on_closing():
                    root2.destroy()
                    root.destroy()

                amountlabel.config(image=image15)
                mixer.music.stop()
                mixer.music.load('audio/Kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.grab_set()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 1 million Pounds')
                centerimg = PhotoImage(file='images/center.png')
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()

                happyimage = PhotoImage(file='images/happy.png')
                happYLabel = Label(root2, image=happyimage, bg='black')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='black')
                happYLabel1.place(x=30, y=280)

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                     , activebackground='black', cursor='hand2', activeforeground='white',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing)
                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=images[i])

        if value not in correct_answers:
            def tryagain():
                mixer.music.load('audio/kbc.mp3')
                mixer.music.play(-1)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountlabel.config(image=amountimage)
                root1.destroy()

            def on_closing():
                root1.destroy()
                root.destroy()

            mixer.music.stop()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 Pound')
            img = PhotoImage(file='images/center.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack()
            sadimage = PhotoImage(file='images/sad.png')
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()

            break


def lifeline50():
    lifeline50Button.config(image=image50x)
    lifeline50Button.config(state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton4.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)

    progressbarA.place(x=580, y=190)
    progressbarLabelA.place(x=580, y=320)

    progressbarB.place(x=620, y=190)
    progressbarLabelB.place(x=620, y=320)

    progressbarC.place(x=660, y=190)
    progressbarLabelC.place(x=660, y=320)

    progressbarD.place(x=700, y=190)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)

        progressbarB.config(value=60)

        progressbarC.config(value=40)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=90)

        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)

        progressbarB.config(value=10)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=20)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)

        progressbarB.config(value=80)

        progressbarC.config(value=70)

        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)

        progressbarB.config(value=50)

        progressbarC.config(value=70)

        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)

        progressbarB.config(value=20)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=90)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=35)

        progressbarC.config(value=40)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)


def phoneLifeline():
    mixer.music.stop()
    mixer.music.load('audio/calling.mp3')
    mixer.music.play()

    phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load('audio/kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The Answer is {correct_answers[i]}')
            engine.runAndWait()


root = Tk()
root.geometry('1420x1080')
root.title('Kon Banega Crorepati 2022')
root.config(bg='black')

leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='black', padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='black', pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file='images/center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file='images/50-50.png')
image50x = PhotoImage(file='images/50-50-X.png')

lifeline50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                      height=80, command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='images/audiencePole.png')
audiencePolex = PhotoImage(file='images/audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=180, height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='images/phoneAFriend.png')
phoneImageX = PhotoImage(file='images/phoneAFriendX.png')
phoneLifelineButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                     height=80, command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file='images/phone.png')
callButton = Button(root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
callButton.place(x=70, y=260)

amountimage = PhotoImage(file='images/Picture0.png')
image1 = PhotoImage(file='images/Picture1.png')
image2 = PhotoImage(file='images/Picture2.png')
image3 = PhotoImage(file='images/Picture3.png')
image4 = PhotoImage(file='images/Picture4.png')
image5 = PhotoImage(file='images/Picture5.png')
image6 = PhotoImage(file='images/Picture6.png')
image7 = PhotoImage(file='images/Picture7.png')
image8 = PhotoImage(file='images/Picture8.png')
image9 = PhotoImage(file='images/Picture9.png')
image10 = PhotoImage(file='images/Picture10.png')
image11 = PhotoImage(file='images/Picture11.png')
image12 = PhotoImage(file='images/Picture12.png')
image13 = PhotoImage(file='images/Picture13.png')
image14 = PhotoImage(file='images/Picture14.png')
image15 = PhotoImage(file='images/Picture15.png')

images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13
    , image14, image15]

amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file='images/lay.png')
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)


questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), bg='black', fg='white', width=34, height=2,
                        wrap='word',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END, questions[0])




labelA = Label(bottomFrame, font=('arial', 16, 'bold'), text='A:', bg='black', fg='white')
labelA.place(x=60,y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton1.place(x=100,y=100)

labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='black', fg='white')
labelB.place(x=330,y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton2.place(x=370,y=100)

labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='black', fg='white')
labelC.place(x=60,y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton3.place(x=100,y=180)

labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='black', fg='white')
labelD.place(x=330,y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton4.place(x=370,y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()
