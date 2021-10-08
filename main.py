from turtle import Screen, goto, exitonclick;from math import pi, sin, cos
for i in range(1300): vt=i/40*pi;y=(vt*5+5) * sin(vt);x=(vt*5+5) * cos(vt);goto(x,y)
Screen().exitonclick()
