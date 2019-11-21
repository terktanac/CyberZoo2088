from tkinter import *
from event import Event


class Main_GUI() :

    """ Main_GUI

        This class (window GUI) will be popped up
        when the program is initiallized
        
    """

    def __init__(self) :
    
        self.root = Tk()
        self.root.title('SMART ZOO DATABASE')

        # Generate GUI
        self.add_label('SMART ZOO', 40, True)
        self.add_label('\nEvent Management')
        
        self.add_button('Add New Event', self.popAddEventWin)
        self.add_button('Update Event', self.popUpdateEventWin)

        self.add_label('\nAnimal Management')
        
        self.add_button('Delete Animal', self.popDelAnimalWin)
        # self.add_button('Some Query', self.popQueryWin)

        self.add_label('\n')        

        self.add_button('Exit', self.exitProgram) 

        self.root.geometry('600x400')
        self.root.mainloop()

    def add_label(self, text, size=15, bold=False):
        Label(
            self.root, 
            text=text, 
            font=("product sans" + " Bold" if bold else "", size)
        ).pack()

    def add_button(self, text, command):
        Button(
            self.root,
            text=text, 
            command=command
        ).pack(side=TOP)
        
    def popAddEventWin(self) :
        AddEventWin("Event Registration")

    def popUpdateEventWin(self) :
        UpdateEventWin("Event Updating")

    def popDelAnimalWin(self) :
        DelAnimalWin("Animal Deleting")

    # def popQueryWin(self) :
    #     QueryWin("Query")

    def exitProgram(self) :
        exit()


class CustomerWindow():

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('600x400')
        
        Label(self.cwin, text="Name").grid(row=0, column=0)
        Label(self.cwin, text="Date").grid(row=1, column=0)
        Label(self.cwin, text="Time").grid(row=2, column=0)
        Label(self.cwin, text="Zone").grid(row=3, column=0)
        Label(self.cwin, text="National ID").grid(row=4, column=0)

        self.entry_name = Entry(self.cwin).grid(row=0, column=1)
        self.entry_date = Entry(self.cwin).grid(row=1, column=1)
        self.entry_time = Entry(self.cwin).grid(row=2, column=1)
        self.entry_zone = Entry(self.cwin).grid(row=3, column=1)
        self.entry_nid = Entry(self.cwin).grid(row=4, column=1)

        Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy).grid(row=6, column=1)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=7, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=5, column=1)

        self.cwin.mainloop()


"""class AddEventWin(CustomerWindow) :

    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.configure(text="Add New Event", command=self.submitNewEvent)
        
    def submitNewCust(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        anEvent = Event(dataentry)
        retmsg = anEvent.write()
        self.label_status.config(text=retmsg[1])"""

class AddEventWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('600x400')
        
        Label(self.cwin, text="Name").grid(row=0, column=0)
        Label(self.cwin, text="Date").grid(row=1, column=0)
        Label(self.cwin, text="Time").grid(row=2, column=0)
        Label(self.cwin, text="Zone").grid(row=3, column=0)
        Label(self.cwin, text="National ID").grid(row=4, column=0)
        Label(self.cwin, text="Event Types").grid(row=5, column=1)
        Radiobutton(self.cwin, text="Show Event").grid(row=6,column=1)
        Radiobutton(self.cwin, text="External Event").grid(row=7,column=1)

        self.entry_name = Entry(self.cwin).grid(row=0, column=1)
        self.entry_date = Entry(self.cwin).grid(row=1, column=1)
        self.entry_time = Entry(self.cwin).grid(row=2, column=1)
        self.entry_zone = Entry(self.cwin).grid(row=3, column=1)
        self.entry_nid = Entry(self.cwin).grid(row=4, column=1)

        Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy).grid(row=8, column=1)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=9, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=5, column=1)

        self.cwin.mainloop()
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
        
Main_GUI()

