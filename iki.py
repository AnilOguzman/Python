from DrawingPanel import *

panel=DrawingPanel(500,500,background="light gray")


for i in range(0, 10):
    panel.draw_rectangle (20, 20 +10* i, 100 - 10 * i, 10)
