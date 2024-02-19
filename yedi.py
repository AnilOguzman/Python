from random import *
from DrawingPanel import *

panel=DrawingPanel(500,500,background="light gray")


for i in range (0,5):
    for j in range(0,5):
        panel.fill_oval(100+20*j,100,20,20,"red")
    print(" ")


