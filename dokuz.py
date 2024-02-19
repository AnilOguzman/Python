from DrawingPanel import *

def deneme():
    p = DrawingPanel(500, 500, background="light gray")
    y=100
    w=20
    h=0
    for i in range(0,5):
        x=80
        for j in range(0,5):
            p.fill_oval(x+w,y+h,20,20,"red")
            x=x+20
        print()
        h=h+20
        p.sleep(300)
        

deneme()
