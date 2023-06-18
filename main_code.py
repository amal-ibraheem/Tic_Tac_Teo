from tkinter import *

class main_tab():
    def __init__(self):
        self.ty = Tk()
        self.settings = self.ty.title('TIC TAC TOE'),self.ty.resizable(False,False)

        self.icon = self.ty.iconbitmap('ic_icon.ico')

        self.frame  = LabelFrame(self.ty)
        self.frame.pack(padx=34, pady= 8)

        self.title = Label(self.frame, text= "TIC-TAC-TOE",foreground="#5FFB17",font=("Saira-Bold", 12))
        self.title.grid(column=0,row=0)

        self.button_frame = Frame(self.frame, bg="#E1D9D1")
        self.button_frame.grid(column=0, row=1,padx= 8)

        self.checking = 0

        self.prize = Label(self.frame,text="")
        self.prize.grid(column=0,row=2)

        def restart():
            self.ty.destroy()
            main_tab()



        self.restart_button = Button(self.frame, text= "Restart", command= restart)
        self.restart_button.grid(column=0, row= 3, sticky= "EN",padx=5)

        self.quit_button = Button(self.frame, text= "Exit",command= self.ty.destroy)
        self.quit_button.grid(column=0, row= 3, sticky= "W")

        def cut_everything():
            but1.configure(state=["disabled"])
            but2.configure(state=["disabled"])
            but3.configure(state=["disabled"])
            but4.configure(state=["disabled"])
            but5.configure(state=["disabled"])
            but6.configure(state=["disabled"])
            but7.configure(state=["disabled"])
            but8.configure(state=["disabled"])
            but9.configure(state=["disabled"])


        # the self.prize buckets 
        self.bucket1 = ""
        self.bucket2 = ""
        self.bucket3 = ""
        self.bucket4 = ""
        self.bucket5 = ""
        self.bucket6 = ""
        self.bucket7 = ""
        self.bucket8 = ""


        # the 8 fuctions of buckets
        def giver1(x):
            # global self.bucket1
            self.bucket1 += x
            if self.bucket1 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket1 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()      


        def giver2(x):
            # global self.bucket2
            self.bucket2 += x
            if self.bucket2 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket2 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()


        def giver3(x):
            # global self.bucket3
            self.bucket3 += x
            if self.bucket3 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket3 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()


        def giver4(x):
            # global self.bucket4
            self.bucket4 += x
            if self.bucket4 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket4 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()


        def giver5(x):
            # global self.bucket5
            self.bucket5 += x
            if self.bucket5 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket5 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()


        def giver6(x):
            # global self.bucket6
            self.bucket6 += x
            if self.bucket6 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket6 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()


        def giver7(x):
            # global self.bucket7
            self.bucket7 += x
            if self.bucket7 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket7 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()


        def giver8(x):
            # global self.bucket8
            self.bucket8 += x
            if self.bucket8 == "XXX":
                self.prize.configure(text="X is the winner")
                cut_everything()
            elif self.bucket8 == "OOO":
                self.prize.configure(text="O is the winner")
                cut_everything()

        #button 1
        def clicked1():
            # global self.checking
            if self.checking % 2 == 0:
                but1.configure(text="X",state=["disabled"],disabledforeground="black")
                giver1("X")
                giver4("X")
                giver7("X")
            else:
                but1.configure(text="O",state=["disabled"],disabledforeground="black")
                giver1("O")
                giver4("O")
                giver7("O")
            self.checking += 1

        but1 = Button(self.button_frame,text="",bg= "#34A56F",width= 3,activebackground="#306754",borderwidth=1,command=clicked1)
        but1.grid(column=0,row=0,padx= 5, pady= 5)

        #button 2
        def clicked2():
            # global self.checking
            if self.checking % 2 == 0:
                but2.configure(text="X",state=["disabled"],disabledforeground="black")
                giver1("X")
                giver5("X")
            else:   
                but2.configure(text="O",state=["disabled"],disabledforeground="black")
                giver1("O")
                giver5("O")
            self.checking += 1

        but2 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked2,borderwidth=1)
        but2.grid(column=1,row=0)

        #button 3
        def clicked3():
            # global self.checking
            if self.checking % 2 == 0:
                but3.configure(text="X",state=["disabled"],disabledforeground="black")
                giver1("X")
                giver6("X")
                giver8("X")
            else:
                but3.configure(text="O",state=["disabled"],disabledforeground="black")
                giver1("O")
                giver6("O")
                giver8("O")
            self.checking += 1

        but3 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked3,borderwidth=1)
        but3.grid(column=2,row=0, padx= 5)

        #button 4
        def clicked4():
            # global self.checking
            if self.checking % 2 == 0:
                but4.configure(text="X",state=["disabled"],disabledforeground="black")
                giver2("X")
                giver4("X")
            else:
                but4.configure(text="O",state=["disabled"],disabledforeground="black")
                giver2("O")
                giver4("O")
            self.checking += 1

        but4 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked4,borderwidth=1)
        but4.grid(column=0,row=1)

        #button 5
        def clicked5():
            # global self.checking
            if self.checking % 2 == 0:
                but5.configure(text="X",state=["disabled"],disabledforeground="black")
                giver2("X")
                giver5("X")
                giver7("X")
                giver8("X")
            else:
                but5.configure(text="O",state=["disabled"],disabledforeground="black")
                giver2("O")
                giver5("O")
                giver7("O")
                giver8("O")
            self.checking += 1

        but5 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked5,borderwidth=1)
        but5.grid(column=1,row=1)

        #button 6
        def clicked6():
            # global self.checking
            if self.checking % 2 == 0:
                but6.configure(text="X",state=["disabled"],disabledforeground="black")
                giver2("X")
                giver6("X")
            else:
                but6.configure(text="O",state=["disabled"],disabledforeground="black")
                giver2("O")
                giver6("O")
            self.checking += 1

        but6 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked6,borderwidth=1)
        but6.grid(column=2,row=1)

        #button 7
        def clicked7():
            # global self.checking
            if self.checking % 2 == 0:
                but7.configure(text="X",state=["disabled"],disabledforeground="black")
                giver3("X")
                giver4("X")
                giver8("X")
            else:
                but7.configure(text="O",state=["disabled"],disabledforeground="black")
                giver3("O")
                giver4("O")
                giver8("O")
            self.checking += 1

        but7 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked7,borderwidth=1)
        but7.grid(column=0,row=2, pady= 5)

        #button 8
        def clicked8():
            # global self.checking
            if self.checking % 2 == 0:
                but8.configure(text="X",state=["disabled"],disabledforeground="black")
                giver3("X")
                giver5("X")
            else:
                but8.configure(text="O",state=["disabled"],disabledforeground="black")
                giver3("O")
                giver5("O")
            self.checking += 1

        but8 = Button(self.button_frame,text="",bg= "#34A56F",activebackground = "#306754",width= 3,command=clicked8,borderwidth=1)
        but8.grid(column=1,row=2)

        #button 9
        def clicked9():
            # global self.checking
            if self.checking % 2 == 0:
                but9.configure(text="X",state=["disabled"],disabledforeground="black")
                giver3("X")
                giver6("X")
                giver7("X")
            else:
                but9.configure(text="O",state=["disabled"],disabledforeground="black")
                giver3("O")
                giver6("O")
                giver7("O")
            self.checking += 1

        but9 = Button(self.button_frame,text="",bg= "#34A56F", activebackground = "#306754",width= 3,command=clicked9,borderwidth=1)
        but9.grid(column=2,row=2)




        self.ty.mainloop()

my_app = main_tab()
