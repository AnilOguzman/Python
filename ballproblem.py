from DrawingPanel import *
# Simulates the dropping of two balls from various heights.


def displacement(v0, a, t):
    d = v0 * t + 0.5 * a * (t ** 2)
    return d

def main():
    panel = DrawingPanel(600, 600)
    ball1x = 100
    ball1y = 0 
    v01 = 25
    ball2x = 200 
    ball2y = 100 
    v02 = 15
    for time in range(60): 
        disp1 = displacement(v01, time/10, 9.81)
        panel.fill_oval(ball1x, ball1y + disp1, ball1x + 10, ball1y + 10 + disp1)
        disp2 = displacement(v02, time/10, 9.81)
        panel.fill_oval(ball2x, ball2y + disp2, ball2x + 10, ball2y + 10 + disp2)
        panel.sleep(200) # pause for 50 ms
        panel.fill_rect(0, 0, 600, 600, "white")




main()
