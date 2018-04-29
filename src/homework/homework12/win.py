from src.homework.homework12.converter import Converter
from tkinter import Tk, Label, Button

#hw12 modification of assign12 to add display and quit buttons
class Win(Tk):

    def __init__(self):
        Tk.__init__(self, None, None)

        self.display_labels = Button(self, text='Display Conversion',
                                     command=self.display_labels).grid(row=3)

        self.quit_button = Button(self, text='Quit', command=self.destroy).grid(row=3, column=1)

        self.mainloop()

    def display_labels(self):
        converter = Converter()
        miles = converter.get_miles_from_km(100)
        self.label1 = Label(self, text='Km: 100 ').grid(row=1)
        self.label2= Label(self, text='Miles: ' + miles).grid(row=2)
