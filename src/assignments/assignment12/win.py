import tkinter
from converter import Converter

class Win:
    def __init__(self):
        self.main_window = tkinter.Tk()
        km = 100
        c = Converter()
        miles = c.get_miles_from_km(km)

        self.label1 = tkinter.Label(self.main_window, text = 'Km: '+ str(km))
        self.label2 = tkinter.Label(self.main_window, text = 'Miles: '+ format(miles,'.2f'))

        self.label1.pack(side='top')
        self.label2.pack(side='top')

        tkinter.mainloop()
