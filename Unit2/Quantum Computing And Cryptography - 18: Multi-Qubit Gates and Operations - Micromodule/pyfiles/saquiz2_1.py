from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath
from helpermethods import newfillblank,checkComplex, buttonsuccess, makeButton
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
SAQuiz2_1 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 2.1 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

#Logic
def QCheckAnswers2_1(btn):
    count = 0
    for q in qlist2_1:
        count += checkComplex(q[1].value,complex(q[0]),q[3],q[4])
    buttonsuccess(Qbtn2_1,count,3,2)

def createQuiz2_1():
    display(SAQuiz2_1)
    display(widgets.HTMLMath(value="<font size=\"+1\">Solve the following using cartesian representation. Given that $c_1=3i+4$, $c_2=5+11i$ and $c_3=4i$."))
    qlist2_1.append(newfillblank("1. Compute: $c_1$ &#10005; $c_2$",0,-13+59j,strInputLayout2))
    qlist2_1.append(newfillblank("2. Calculate: <sup>${c_1}$</sup>&frasl;<sub>${c_3}$</sub> ",0,.75-1j,strInputLayout2))
    qlist2_1.append(newfillblank("3. Resolve: <sup>${c_2}$</sup>&frasl;<sub>${c_1}$</sub> ",0,2.12+1.16j,strInputLayout2))
    for q in qlist2_1:
        display(q[2])
        display(HBox([q[1],q[3],q[4]]))
    display(VBox([Qbtn2_1],layout=center))
#Events
Qbtn2_1 = makeButton()
qlist2_1 = []
Qbtn2_1.on_click(QCheckAnswers2_1)
