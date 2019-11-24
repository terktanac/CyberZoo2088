from tkinter import *
from connector import *


class AddAnimalWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('250x250')
    
        Label(self.cwin, text="Animal Type").grid(row=2, column=0)
        Label(self.cwin, text="Animal Nickname").grid(row=3, column=0)
        Label(self.cwin, text="Breed").grid(row=4, column=0)
        Label(self.cwin, text="Date of Birth").grid(row=5, column=0)
        Label(self.cwin, text="Gender").grid(row=6, column=0)
        Label(self.cwin, text="Come From").grid(row=7, column=0)
        Label(self.cwin, text="Habitat ID").grid(row=8, column=0)
        Label(self.cwin, text="Parent ID").grid(row=9, column=0)

        self.entry_type = Entry(self.cwin)
        self.entry_nickname = Entry(self.cwin)
        self.entry_breed = Entry(self.cwin)
        self.entry_bd = Entry(self.cwin)
        self.entry_gender = Entry(self.cwin)
        self.entry_comefrom = Entry(self.cwin)
        self.entry_hid = Entry(self.cwin)
        self.entry_pid = Entry(self.cwin)

        self.entry_type.grid(row=2, column=1)
        self.entry_nickname.grid(row=3, column=1)
        self.entry_breed.grid(row=4, column=1)
        self.entry_bd.grid(row=5, column=1)
        self.entry_gender.grid(row=6, column=1)
        self.entry_comefrom.grid(row=7, column=1)
        self.entry_hid.grid(row=8, column=1)
        self.entry_pid.grid(row=9, column=1)

        Button(self.cwin, text ="ADD", command=self.submitNewAnimal).grid(row=10, column=1)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=11, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=12, column=1)

        self.cwin.mainloop()


    def submitNewAnimal(self) :
 
        ret_msg = insert(
            'animal', 
            AType = self.entry_type.get(),
            Nickname = self.entry_nickname.get(),
            Breed = self.entry_breed.get(),
            ABDate = self.entry_bd.get(),
            Gender = self.entry_gender.get(),
            Comefrom = self.entry_comefrom.get(),
            ParentID = self.entry_pid.get(),
            HabitatID = self.entry_hid.get()
        )

        self.label_status.config(text=ret_msg[1])


class UpdateAnimalWin():

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x250')

        Label(self.cwin, text="ID").grid(row=0, column=0)
        self.entry_search = Entry(self.cwin)
        self.entry_search.grid(row=0, column=1)
        
        Label(self.cwin, text="Animal Type").grid(row=2, column=0)
        Label(self.cwin, text="Animal Nickname").grid(row=3, column=0)
        Label(self.cwin, text="Breed").grid(row=4, column=0)
        Label(self.cwin, text="Date of Birth").grid(row=5, column=0)
        Label(self.cwin, text="Gender").grid(row=6, column=0)
        Label(self.cwin, text="Come From").grid(row=7, column=0)
        Label(self.cwin, text="Habitat ID").grid(row=8, column=0)
        Label(self.cwin, text="Parent ID").grid(row=9, column=0)

        self.entry_type = Entry(self.cwin)
        self.entry_nickname = Entry(self.cwin)
        self.entry_breed = Entry(self.cwin)
        self.entry_bd = Entry(self.cwin)
        self.entry_gender = Entry(self.cwin)
        self.entry_comefrom = Entry(self.cwin)
        self.entry_hid = Entry(self.cwin)
        self.entry_pid = Entry(self.cwin)

        self.entry_type.grid(row=2, column=1)
        self.entry_nickname.grid(row=3, column=1)
        self.entry_breed.grid(row=4, column=1)
        self.entry_bd.grid(row=5, column=1)
        self.entry_gender.grid(row=6, column=1)
        self.entry_comefrom.grid(row=7, column=1)
        self.entry_hid.grid(row=8, column=1)
        self.entry_pid.grid(row=9, column=1)

        Button(self.cwin, text="SEARCH", command=self.searchAnimal).grid(row=0, column=2)
        self.button = Button(self.cwin, text="UPDATE", command=self.updateAnimal)
        self.button.grid(row=10, column=1)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=11, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=12, column=1)

        # self.cwin.mainloop()
        
    def updateAnimal(self) :
        ret_msg = update(
            'animal',
            'AnimalID',
            self.entry_search.get(),
            AType=self.entry_type.get(),
            Nickname=self.entry_nickname.get(),
            Breed=self.entry_breed.get(),
            ABDate=self.entry_bd.get(),
            Gender=self.entry_gender.get(),
            ComeFrom=self.entry_comefrom.get(),
            HabitatID=self.entry_hid.get(),
            ParentID=self.entry_pid.get()
        )
        self.label_status.config(text=ret_msg[1])

    def searchAnimal(self) :
        ret_msg = select(
            'animal',
            AnimalID=self.entry_search.get()
        )

        if ret_msg[0] == "0" :
            result = ret_msg[2]
            self.entry_type.delete(0, END)
            self.entry_nickname.delete(0, END)
            self.entry_breed.delete(0, END)
            self.entry_bd.delete(0, END)
            self.entry_gender.delete(0, END)
            self.entry_comefrom.delete(0, END)
            self.entry_hid.delete(0, END)
            self.entry_pid.delete(0, END)
            self.entry_type.insert(0, result['AType'])
            self.entry_nickname.insert(0, result['Nickname'])
            self.entry_breed.insert(0, result['Breed'])
            self.entry_bd.insert(0, result['ABDate'])
            self.entry_gender.insert(0, result['Gender'])
            self.entry_comefrom.insert(0, result['ComeFrom'])
            self.entry_hid.insert(0, result['HabitatID'])
            self.entry_pid.insert(0, result['ParentID'])
            
        else :
            self.entry_type.delete(0, END)
            self.entry_nickname.delete(0, END)
            self.entry_breed.delete(0, END)
            self.entry_bd.delete(0, END)
            self.entry_gender.delete(0, END)
            self.entry_comefrom.delete(0, END)
            self.entry_hid.delete(0, END)
            self.entry_pid.delete(0, END)
            self.entry_type.insert(0, "?????")
            self.entry_nickname.insert(0, "?????")
            self.entry_breed.insert(0, "?????")
            self.entry_bd.insert(0, "?????")
            self.entry_gender.insert(0, "?????")
            self.entry_comefrom.insert(0, "?????")
            self.entry_hid.insert(0, "?????")
            self.entry_pid.insert(0, "?????")
            
        self.label_status.config(text=ret_msg[1])


class DeleteAnimalWin(UpdateAnimalWin):

    def __init__(self, title):
        super().__init__(title)
        self.button.config(text='DELETE')
    
    def updateAnimal(self) :
        ret_msg = delete(
            'animal',
            AnimalID=self.entry_search.get()
        )
        self.label_status.config(text=ret_msg[1])
