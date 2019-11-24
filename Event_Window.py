from tkinter import *
from connector import *


class AddEventWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('230x300')
        Label(self.cwin, text="ID is xxxxx").grid(row=0, column=1) #need to change to be an generated id
        Label(self.cwin, text="Event Types").grid(row=1, column=1)
        
        var = IntVar()
        self.host = Label(self.cwin, text="NID")
        show_event = lambda: self.host.config(text='NID')
        external_event = lambda: self.host.config(text='VisitorID')
        Radiobutton(self.cwin, text="Show Event", variable=var, value=1, command=show_event).grid(row=2, column=1)
        Radiobutton(self.cwin, text="External Event", variable=var, value=2, command=external_event).grid(row=3, column=1)
        var.set(1)

        Label(self.cwin, text="Name").grid(row=4, column=0)
        Label(self.cwin, text="Date").grid(row=5, column=0)
        Label(self.cwin, text="Time").grid(row=6, column=0)
        Label(self.cwin, text="Zone").grid(row=7, column=0)
        self.host.grid(row=8, column=0)

        self.entry_name = Entry(self.cwin)
        self.entry_date = Entry(self.cwin)
        self.entry_time = Entry(self.cwin)
        self.entry_zone = Entry(self.cwin)
        self.entry_host = Entry(self.cwin)
        
        self.entry_name.grid(row=4, column=1)
        self.entry_date.grid(row=5, column=1)
        self.entry_time.grid(row=6, column=1)
        self.entry_zone.grid(row=7, column=1)
        self.entry_host.grid(row=8, column=1)

        Button(self.cwin, text ="SUBMIT", command=self.submitNewEvent).grid(row=9, column=1)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=10, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=11, column=1)

        self.cwin.mainloop()
        

    def submitNewEvent(self) :
 
        if self.host.cget('text') == 'NID':
            ret_msg = insert(
                'zoo_event', 
                EDate = self.entry_date.get(),
                EName = self.entry_name.get(),
                ETime = self.entry_time.get(),
                ZName = self.entry_zone.get(),
                SFlag = True,
                NID = self.entry_host.get(),
                EFlag = False
            )
        else:
            ret_msg = insert(
                'zoo_event', 
                EDate = self.entry_date.get(),
                EName = self.entry_name.get(),
                ETime = self.entry_time.get(),
                ZName = self.entry_zone.get(),
                SFlag = False,
                EFlag = True,
                VisitorID = self.entry_host.get()
            )

        self.label_status.config(text=ret_msg[1])


class UpdateEventWin() :

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('250x250')

        Label(self.cwin, text="ID").grid(row=0, column=0)
        Label(self.cwin, text="Event Types").grid(row=1, column=1)
        Label(self.cwin, text="This event is Show/External").grid(row=2, column=1) # need to change to be an output from search
        Label(self.cwin, text="Name").grid(row=4, column=0)
        Label(self.cwin, text="Date").grid(row=5, column=0)
        Label(self.cwin, text="Time").grid(row=6, column=0)
        Label(self.cwin, text="Zone").grid(row=7, column=0)

        self.entry_search = Entry(self.cwin)
        self.entry_name = Entry(self.cwin)
        self.entry_date = Entry(self.cwin)
        self.entry_time = Entry(self.cwin)
        self.entry_zone = Entry(self.cwin)
        
        self.entry_search.grid(row=0, column=1)
        self.entry_name.grid(row=4, column=1)
        self.entry_date.grid(row=5, column=1)
        self.entry_time.grid(row=6, column=1)
        self.entry_zone.grid(row=7, column=1)

        Button(self.cwin, text="SEARCH", command=self.searchEvent).grid(row=0, column=2)
        self.button = Button(self.cwin, text="UPDATE", command=self.updateEvent)
        self.button.grid(row=9, column=1)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=10, column=1)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=11, column=1)

        # self.cwin.mainloop()
        
    def updateEvent(self) :
        ret_msg = update(
            'zoo_event',
            'EventID',
            self.entry_search.get(),
            EDate = self.entry_date.get(),
            EName = self.entry_name.get(),
            ETime = self.entry_time.get(),
            ZName = self.entry_zone.get()
        )
        self.label_status.config(text=ret_msg[1])

    def searchEvent(self) :
        ret_msg = select(
            'zoo_event',
            EventID=self.entry_search.get()
        )

        if ret_msg[0] == "0" :
            result = ret_msg[2]
            self.entry_name.delete(0, END)
            self.entry_date.delete(0, END)
            self.entry_time.delete(0, END)
            self.entry_zone.delete(0, END)
            self.entry_name.insert(0, result['EName'])
            self.entry_date.insert(0, result['EDate'])
            self.entry_time.insert(0, result['ETime'])
            self.entry_zone.insert(0, result['ZName'])
            
        else :
            self.entry_name.delete(0, END)
            self.entry_date.delete(0, END)
            self.entry_time.delete(0, END)
            self.entry_zone.delete(0, END)
            self.entry_name.insert(0, "?????")
            self.entry_date.insert(0, "?????")
            self.entry_time.insert(0, "?????")
            self.entry_zone.insert(0, "?????")
            
        self.label_status.config(text=ret_msg[1])


class DeleteEventWin(UpdateEventWin):

    def __init__(self, title):
        super().__init__(title)
        self.button.config(text='DELETE')

    def updateEvent(self) :
        ret_msg = delete(
            'zoo_event',
            EventID=self.entry_search.get()
        )
        self.label_status.config(text=ret_msg[1])