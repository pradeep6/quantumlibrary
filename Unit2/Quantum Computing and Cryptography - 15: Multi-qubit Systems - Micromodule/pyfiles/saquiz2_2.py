from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath, math
from helpermethods import newfillblank,checkComplex, buttonsuccess, makeButton, newfloatbox, checkfloat
#Layouts
numInputLayout=Layout(
    width='55px'
)
strInputLayout1=Layout(
    width='90px'
)
strInputLayout2=Layout(
    width='130px'
)
center = Layout(align_items='center')
#Boxes
SAQuiz2_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 2.2 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

#Logic
def QCheckAnswers2_2(btn):
    count = 0
    for q in qlist2_2_1:
        count += checkfloat(q[1].value,q[0],q[3],q[4])
    for q in qlist2_2_2:
        count += checkComplex(q[1].value,q[0],q[3],q[4])
    buttonsuccess(Qbtn2_2,count,8,5)

def createQuiz2_2():
    display(SAQuiz2_2)
    display(widgets.HTMLMath(value="<font size=\"+1\">Compute to the nearest hundredth the modulus for the following complex numbers."))
    qlist2_2_1.append(newfloatbox("1. $c$ = 3+1$i$",0,math.sqrt(10),strInputLayout2))
    qlist2_2_1.append(newfloatbox("2. $c$ = 1+21$i$",0,math.sqrt(442),strInputLayout2))
    qlist2_2_1.append(newfloatbox("3. $c$ = 10+10$i$",0,math.sqrt(200),strInputLayout2))
    qlist2_2_1.append(newfloatbox("4. $c$ = 5.3",0,5.3,strInputLayout2))
    qlist2_2_1.append(newfloatbox("5. $c$ = 5-7$i$",0,math.sqrt(74),strInputLayout2))
    for q in qlist2_2_1:
        display(q[2])
        display(HBox([q[1],q[3],q[4]]))
    display(widgets.HTMLMath(value="<font size=\"+1\">Compute the conjugate for the following complex numbers."))
    qlist2_2_2.append(newfillblank("1. $c$ = -101$i$",0,101j,strInputLayout1))
    qlist2_2_2.append(newfillblank("2. $c$ = 20+1$i$",0,20-1j,strInputLayout1))
    qlist2_2_2.append(newfillblank("3. $c$ = -1+441$i$",0,-1+441j,strInputLayout1))
    for q in qlist2_2_2:
        display(q[2])
        display(HBox([q[1],q[3],q[4]]))
    display(VBox([Qbtn2_2],layout=center))
#Events
Qbtn2_2 = makeButton()
qlist2_2_1 = []
qlist2_2_2 = []
Qbtn2_2.on_click(QCheckAnswers2_2)
