from turtle import*
import colorsys
bgcolor("black")
tracer(10)
pensize(2)
h=0
for i in range(280):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.004
    width(i/100+3)
    color(c)
    right(120)
    circle(-i*0.8,120)
    circle(i*0.2,120)
    circle(i*0.8,60)
    circle(-i*0.4,10)
done()

