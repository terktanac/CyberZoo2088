from tkinter import *
from connector import *

class EventQueryWin():

    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('450x300')

        Label(self.cwin, text="Year").grid(row=0, column=0)
        self.entry_search = Entry(self.cwin)
        self.entry_search.grid(row=0, column=1)
        Button(self.cwin, text="SEARCH", command=self.searchEvent).grid(row=0, column=2)
        Label(self.cwin, text="\n").grid(row=1, column=2)

        Label(self.cwin, text="\n").grid(row=10, column=2)
        Button(self.cwin, text="EXIT", command=self.cwin.destroy).grid(row=11, column=2)

        self.label_status = Label(self.cwin, text="")
        self.label_status.grid(row=12, column=2)

        self.cells = []
        # self.cwin.mainloop()
        

    def searchEvent(self) :
        ret_msg = select(
            'zoo_event',
            one_row=False,
            command="select * from zoo_event where extract(year from EDate)={year};".format(year=self.entry_search.get())
        )

        for i in self.cells:
            i.config(text='')

        if ret_msg[0] == "0" :
            rows = ret_msg[2]
            
            self.cells = []
            for i, row in enumerate(rows): #Rows
                for j, element in enumerate(row): #Columns
                    b = Label(self.cwin, text=element)
                    b.grid(row=3+i, column=j)
                    self.cells += [b]
            
        self.label_status.config(text=ret_msg[1])



# EventQueryWin("Event Income")