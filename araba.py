from DrawingPanel import *
def main():
    p = DrawingPanel(200, 100, background="light gray")
    p.fill_rect(10, 30, 100, 50, "black")
    p.fill_oval(20, 70, 20, 20, "red")
    p.fill_oval(80, 70, 20, 20, "red")
    p.fill_rect(80, 40, 30, 20, "cyan")
main()
