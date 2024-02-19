from random import *
from DrawingPanel import *


def main():
    panel = DrawingPanel(260, 100, background="light gray") 
    draw_car(panel, 10, 30)
    draw_car(panel, 150, 10)
def draw_car(p, x, y):
    p.fill_rect(x, y, 100, 50, "black")
    p.fill_oval(x + 10, y + 40, 20, 20, "red")
    p.fill_oval(x + 70, y + 40, 20, 20, "red")
    p.fill_rect(x + 70, y + 10, 30, 20, "cyan")

main()
