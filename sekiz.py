from DrawingPanel import *



def main():
    panel=DrawingPanel(500,500,background="light gray")
    
    
    for i in range(0,100,20):
        for j in range(0,100,20):
            panel.fill_oval(j,i,20,20,"red")
            panel.sleep(100)

main()
