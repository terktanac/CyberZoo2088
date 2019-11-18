from tkinter import *



class RootWin() :
    def __init__(self) :
        root = Tk()
        
        header = Label(root, text="Cyber Zoo 2088\n", font=("Arial Bold", 20))
        header.pack()
        header2 = Label(root, text="Event Management", font=("Arial Bold", 10))
        header2.pack()
        addEventButton = Button(root, text="Add New Event", command=self.popAddEventWin)
        addEventButton.pack(side=TOP)
        updateEventButton = Button(root, text="Update Event", command=self.popUpdateEventWin)
        updateEventButton.pack(side=TOP)
        header3 = Label(root, text="\nAnimal Management", font=("Arial Bold", 10))
        header3.pack()
        delAnimalButton = Button(root, text="Delete Animal", command=self.popDelAnimalWin)
        delAnimalButton.pack(side=TOP)
        queryButton = Button(root, text="Some Query", command=self.popQueryWin)
        queryButton.pack(side=TOP)
        header4 = Label(root, text="\n", font=("Arial Bold", 10))
        header4.pack()
        exitButton = Button(root, text="Exit", command=self.exitProgram)
        exitButton.pack(side=TOP)
        root.geometry('600x400')
        root.mainloop()
        
    def popAddEventWin(self) :
        r1 = AddEventWin("Event Registration")
    def popUpdateEventWin(self) :
        s1 = UpdateEventWin("Event Updating")
    def popDelAnimalWin(self) :
        s1 = DelAnimalWin("Animal Deleting")
    def popQueryWin(self) :
        s1 = QueryWin("Query")
    def exitProgram(self) :
        exit()



class CustomerWindow() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('600x400')
        
        self.label_name=Label(self.cwin, text="Name")
        self.label_date=Label(self.cwin, text="Date")
        self.label_time=Label(self.cwin, text="Time")
        self.label_zone=Label(self.cwin, text="Zone")
        self.label_nid=Label(self.cwin, text="National ID")

        self.entry_name=Entry(self.cwin)
        self.entry_date=Entry(self.cwin)
        self.entry_time=Entry(self.cwin)
        self.entry_zone=Entry(self.cwin)
        self.entry_nid=Entry(self.cwin)


        self.button_submit=Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_id.grid(row=0,column=0)
        self.label_name.grid(row=1,column=0)
        
        self.entry_id.grid(row=0,column=1)
        self.entry_name.grid(row=1,column=1)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=5, columnspan=2)

class AddEventWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.configure(text="Add New Event", command=self.submitNewEvent)
        
    def submitNewCust(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        anEvent = Event(dataentry)
        retmsg = anEvent.write()
        self.label_status.config(text=retmsg[1])
class UpdateEventWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.configure(text="Update Event", command=self.updateEvent)
        
    def updateEvent(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        anEvent = Event(dataentry)
        retmsg = anEvent.write()
        self.label_status.config(text=retmsg[1])
class DelAnimalWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Delete", command=self.delAnimal)
        self.button_submit=Button(self.cwin)
        
    def delAnimal(self) :
        self.cwin.title("Deleted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        anAnimal = Animal(dataentry)
        
        retmsg = anAnimal.delete()

        if retmsg[0] == "0" :
            self.entry_id.delete(0, END)
            self.entry_name.delete(0, END)
        else :
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, "?????")
        self.label_status.config(text=retmsg[1])
Mainmenu = RootWin()

