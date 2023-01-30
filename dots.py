import tkinter as tk
import itertools as it

import math, random

# predefined fns
m=math
sin=m.sin
cos=m.cos
tan=m.tan
asin=m.asin
acos=m.acos
atan=m.atan
rand=random.randrange
sqrt=m.sqrt
pow=m.pow
log=m.log
e=m.exp
hypot=m.hypot

root = tk.Tk()
 
t = 0
d = True
pts = []

def wts(x, y):
    return (x*z+ox, -(y*z)+oy)
    
def width(val):
    return 1 if abs(val) >= 1 else abs(val)
    
def color(val):
    return 'red' if val < 0 else 'white'

def redraw(*_):
    global t, d
    
    t += 0.03 #if d else -0.03
    #if t >= 1 or t <= 0:
    #    d = not d

    render()
    g.after(30, redraw)
    
def render():
    g.delete('all')
    i = 0
    for x in range(-9, 10):
        for y in range(-9, 10):
            val = f(t, i, x, y)
            r = width(val) / 2 # - 0.02
            dot = wts(x - r, y - r)+ wts(x + r, y + r)
            g.create_oval(*dot, width=0, fill=color(val))
            i += 1

ox = 400
oy= 350
z=30


def f(t, i, x, y):
    try:
        return -.4/(hypot(x-t%10,y-t%8)-t%2*9)
    except Exception:
        return 0

g = tk.Canvas(root, bg='black', width=200, height=500, bd=0, highlightthickness=0)
g.pack(expand=True, fill=tk.BOTH)

# coord axis
#g.create_line(400,0,400,1000)
#g.create_line(0,500,1000,500)

render()
redraw()

root.mainloop()
