import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets   #you have to enable extensions for jupyter notebook after installing
import sys
from ipywidgets import interact

from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath, math


strInputLayout1=Layout(
    width='90px'
)

def clearall(btn):
    floatslide.value=0
    textBox.value = 0
def setGraph(real,imag):
    textBox.value = real
    floatslide.value = imag

def rad2deg(radians):
	pi = math.pi
	degrees = 180 * radians / pi
	return degrees
def deg2rad(degrees):
	pi = math.pi
	radians = pi * degrees / 180
	return radians
def argand(real,imag):
    #add some spacing
    #tograph = cmath.rect(real,deg2rad(imag))
    if(abs(real) < 10 and abs(imag) < 10):
        limit=np.max(10.5)
    elif(abs(real) < 25 and abs(imag) < 25):
        limit=np.max(25.5)
    elif(abs(real) < 75 and abs(imag) < 75):
        limit=np.max(75.5)
    elif(abs(real) < 150 and abs(imag) < 150):
        limit=np.max(150)
    elif(abs(real) < 350 and abs(imag) < 350):
        limit=np.max(350)
    elif(abs(real) < 500 and abs(imag) < 500):
        limit=np.max(500)
    elif(abs(real) < 800 and abs(imag) < 800):
        limit=np.max(800)    
    else:
        limit = np.max(1000)
    tograph = real + (imag*1j)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.plot([0,tograph.real],[0,tograph.imag],'c^-',label='complex')
    #limit=np.max(10.5) # set limits for axis
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()
    #print("You are graphing:\n"+ str(tograph).strip("()"))


def createGraph():
    out = widgets.interactive_output(argand,{'imag' : floatslide, 'real' : textBox})
    out.clear_output = True
    display(out)
    display(HBox([Label(value="Real $=$",),textBox,Label(value="Imaginary $=$",),floatslide]))
    display(btnone)
    #print("\nMove the sliders to graph a complex number as a vector\n")
    #interact(argand, real=(-10,10,.5), imag=(-10,10,.5))
    #interact(argand, real=floatslide, imag=textBox)
floatslide= widgets.FloatText(
                placeholder='answer',
                disabled=True,
                layout = strInputLayout1,
            )

textBox= widgets.FloatText(
                placeholder='answer',
                disabled=True,
                layout = strInputLayout1,
            )


btnone = widgets.Button(
            description='Clear',
            disabled=False,
            button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Check Answers',
            icon='check',
            layout=Layout(width = '25%')
        )

btnone.on_click(clearall)
#def onChange(change):
#    argand(floatslide.value,textBox.value)

#floatslide.observe(onChange,'value')

#floatslide.style.handle_color = random.choice(colors)
