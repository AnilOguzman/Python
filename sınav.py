from DrawingPanel import *

def main():
    panel = DrawingPanel(500, 500, background="light gray") 

    for i in range(0, 10):
     draw_car(panel, 10 + i * 50, 130, 40);
     panel.sleep(500)
     panel.fill_rect(0,0,500,500,"light gray")
def draw_car(p, x, y, size):
    p.fill_rect(x, y, size, size / 2, "black")
    p.fill_oval(x + size / 10, y + size / 5 * 2, size / 5, size / 5, "red")
    p.fill_oval(x + size / 10 * 7, y + size / 5 * 2, size / 5, size / 5, "red")
    p.fill_rect(x + size / 10 * 7, y + size / 10, size / 10 * 3, size / 5, "cyan")

main()
