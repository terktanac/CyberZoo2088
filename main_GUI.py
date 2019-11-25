from tkinter import *
from Event_Window import *
from Animal_Window import *
from Query_Window import *

class Main_GUI() :

    """ Main_GUI

        This class (window GUI) will be popped up
        when the program is initiallized
        
    """

    def __init__(self) :
    
        self.root = Tk()
        self.root.title('SMART ZOO DATABASE')
        self.add_label('SMART ZOO', 40, True)

        self.add_label('\nEvent Management')
        self.add_button('Add New Event', self.popAddEventWin)
        self.add_button('Update Event', self.popUpdateEventWin)
        self.add_button('Delete Event', self.popDeleteEventWin)
        self.add_button('Event Income', self.popQueryEventWin)

        self.add_label('\nAnimal Management')
        self.add_button('Add New Animal', self.popAddAnimalWin)
        self.add_button('Update Animal', self.popUpdateAnimalWin)
        self.add_button('Delete Animal', self.popDeleteAnimalWin)

        self.add_label('\n')        
        self.add_button('   Exit   ', self.exitProgram) 
        self.root.geometry('600x450')
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
        
    def popDeleteEventWin(self) :
        DeleteEventWin("Event Deleting")

    def popQueryEventWin(self):
        EventQueryWin("Event Income")

    def popAddAnimalWin(self) :
        AddAnimalWin("Animal Registration")

    def popUpdateAnimalWin(self) :
        UpdateAnimalWin("Animal Updating")

    def popDeleteAnimalWin(self) :
        DeleteAnimalWin("Animal Deleting")

    def exitProgram(self) :
        exit()

        
Main_GUI()

