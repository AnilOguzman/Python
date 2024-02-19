from DrawingPanel import *
p=DrawingPanel(500,500,background="gray")

for i in range(0,5):
    for j in range(0,5):
        p.fill_oval(20+50*j,20+50*i,50,50,"red")
    print()    
