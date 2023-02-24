# import tkinter as tk
import tkinter
from tkinter import *
# initialize app
window1 = Tk()
window1.title("Recipe Picker")
window1.eval("tk::PlaceWindow . center")
window1.geometry("400x400")
window2 = tkinter.Toplevel(window1)
window1.eval(f"tk::PlaceWindow {str(window2)} center")




window1.mainloop()