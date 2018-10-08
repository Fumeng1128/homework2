from turtle import *

def mygoto(x,y):
    up()
    goto(x,y)
    down()

setup(550,400,0,0)
color('yellow')
bgcolor('red')
fillcolor('yellow')

mygoto(-250,70)
begin_fill()
for i in range(5):
    forward(90)
    right(144)
end_fill()

mygoto(-150,130)
begin_fill()
for i in range(5):
    forward(40)
    right(144)
end_fill()

mygoto(-110,80)
begin_fill()
for i in range(5):
    forward(40)
    right(144)
end_fill()

mygoto(-110,30)
begin_fill()
for i in range(5):
    forward(40)
    right(144)
end_fill()

mygoto(-150,-20)
begin_fill()
for i in range(5):
    forward(40)
    right(144)
end_fill()

done()
