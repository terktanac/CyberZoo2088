from tkinter import *
from event import Event
from animal import Animal


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

class AddEventWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('250x300')
        Label(self.cwin, text="ID is xxxxx").grid(row=0, column=1) #need to change to be an generated id
        Label(self.cwin, text="Event Types").grid(row=1, column=1)
        var = IntVar()
        Radiobutton(self.cwin, text="Show Event", variable=var, value=1).grid(row=2, column=1)
        Radiobutton(self.cwin, text="External Event", variable=var, value=2).grid(row=3, column=1)

        Label(self.cwin, text="Name").grid(row=4, column=0)
        Label(self.cwin, text="Date").grid(row=5, column=0)
        Label(self.cwin, text="Time").grid(row=6, column=0)
        Label(self.cwin, text="Zone").grid(row=7, column=0)
        Label(self.cwin, text="National ID").grid(row=8, column=0)

        self.entry_name = Entry(self.cwin).grid(row=4, column=1)
        self.entry_date = Entry(self.cwin).grid(row=5, column=1)
        self.entry_time = Entry(self.cwin).grid(row=6, column=1)
        self.entry_zone = Entry(self.cwin).grid(row=7, column=1)
        self.entry_nid = Entry(self.cwin).grid(row=8, column=1)

        self.button_submit = Button(self.cwin, text ="SUBMIT", command=self.submitNewEvent).grid(row=9, column=1)
        self.button_exit = Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=10, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=11, column=1)

        self.cwin.mainloop()
        
    def submitNewEvent(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_id.get(), self.entry_name.get()] #change to Event attributes
        anEvent = Event(dataentry)
        retmsg = anEvent.write()
        self.label_status.config(text=retmsg[1])

class UpdateEventWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('270x300')
        Label(self.cwin, text="ID").grid(row=0, column=0)
        self.entry_search = Entry(self.cwin).grid(row=0, column=1)
        Label(self.cwin, text="Event Types").grid(row=1, column=1)
        Label(self.cwin, text="This event is Show/External").grid(row=2, column=1) # need to change to be an output from search


        Label(self.cwin, text="Name").grid(row=4, column=0)
        Label(self.cwin, text="Date").grid(row=5, column=0)
        Label(self.cwin, text="Time").grid(row=6, column=0)
        Label(self.cwin, text="Zone").grid(row=7, column=0)
        Label(self.cwin, text="National ID").grid(row=8, column=0)

        self.entry_name = Entry(self.cwin).grid(row=4, column=1)
        self.entry_date = Entry(self.cwin).grid(row=5, column=1)
        self.entry_time = Entry(self.cwin).grid(row=6, column=1)
        self.entry_zone = Entry(self.cwin).grid(row=7, column=1)
        self.entry_nid = Entry(self.cwin).grid(row=8, column=1)
        # need to change to be an output from search

        self.button_search = Button(self.cwin, text ="SEARCH", command=self.searchEvent).grid(row=0, column=2)
        self.button_submit = Button(self.cwin, text ="SUBMIT", command=self.updateEvent).grid(row=9, column=1)
        self.button_exit = Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=10, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=11, column=1)

        self.cwin.mainloop()
        
    def updateEvent(self) :
        self.cwin.title("Updated")
    def searchEvent(self) :
        self.cwin.title("Searched")
        dataentry = [self.entry_id.get(), self.entry_name.get()] #change to Event attributes
        anEvent = Event(dataentry)
        
        retmsg = anEvent.search()

        if retmsg[0] == "0" :
            self.entry_id.delete(0, END)
            self.entry_id.insert(0, anEvent.getInfo()[0])
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, anEvent.getInfo()[1])
            
        else :
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, "?????")
        self.label_status.config(text=retmsg[1])

class DelAnimalWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x270')
        Label(self.cwin, text="Animal ID").grid(row=0, column=0)
        self.entry_aid = Entry(self.cwin).grid(row=0, column=1)
    
        Label(self.cwin, text="Animal Type").grid(row=2, column=0)
        Label(self.cwin, text="Animal Nickname").grid(row=3, column=0)
        Label(self.cwin, text="Breed").grid(row=4, column=0)
        Label(self.cwin, text="Date of Birth").grid(row=5, column=0)
        Label(self.cwin, text="Gender").grid(row=6, column=0)
        Label(self.cwin, text="Habitat ID").grid(row=7, column=0)

        self.entry_type = Entry(self.cwin).grid(row=2, column=1)
        self.entry_nickname = Entry(self.cwin).grid(row=3, column=1)
        self.entry_breed = Entry(self.cwin).grid(row=4, column=1)
        self.entry_bd = Entry(self.cwin).grid(row=5, column=1)
        self.entry_gender = Entry(self.cwin).grid(row=6, column=1)
        self.entry_hid = Entry(self.cwin).grid(row=7, column=1)
        # need to change to be an output from search

        self.button_search = Button(self.cwin, text ="SEARCH", command=self.cwin.destroy).grid(row=0, column=2)
        self.button_submit = Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy).grid(row=8, column=1)
        self.button_exit = Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=9, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=11, column=1)

        self.cwin.mainloop()
        self.button_submit.configure(text="Update Event", command=self.updateEvent)
        
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
    def searchAnimal(self) :
        self.cwin.title("Searched")
        dataentry = [self.entry_id.get(), self.entry_name.get()] #change to Event attributes
        anEvent = Event(dataentry)
        
        retmsg = anEvent.search()

        if retmsg[0] == "0" :
            self.entry_id.delete(0, END)
            self.entry_id.insert(0, anEvent.getInfo()[0])
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, anEvent.getInfo()[1])
            
        else :
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, "?????")
        self.label_status.config(text=retmsg[1])
        
Main_GUI()

