#!/usr/bin/env python3 

import sys; 
from src import ImpactMainWindow

root = ImpactMainWindow.ImpactMainWindow()
ImpactMainWindow.MyMenu(root)

root.update()
w  = root.winfo_width()
h  = root.winfo_height()
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=True, height=True)
#root.protocol("WM_DELETE_WINDOW", quitConfirm)


root.mainloop()
root.console.stop()
