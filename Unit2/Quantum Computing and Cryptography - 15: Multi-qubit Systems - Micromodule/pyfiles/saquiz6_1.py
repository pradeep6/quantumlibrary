from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath
from helpermethods import newfillblank,checkComplex, buttonsuccess, makeButton
def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)
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
q1 = prepareQuestion("a. $\left&#60;V_1,c\cdot V_2\\right&#62;=\overline{c}\left&#60;V_1,V_2\\right&#62;$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "<font size=\"-1\"><b> LHS = </b>&emsp;$\left&#60;V_1,c\cdot V_2\\right&#62;$&emsp;=&emsp;$V_1^\dagger c\cdot V_2$&emsp;=&emsp;$ c\cdot V_1^\dagger\cdot V_2$&emsp;=&emsp;$ (\overline{c}\cdot V_1)^\dagger\cdot V_2$&emsp;=&emsp;$ \left&#60;\overline{c}V_1, V_2\\right&#62;$&emsp;=&emsp;$ \overline{c}\left&#60;V_1, V_2\\right&#62;$&emsp;<b> = RHS</b>.")
q2 = prepareQuestion("b. $\left&#60;V_1,V_2\\right&#62;=\overline{\left&#60;V_2,V_1\\right&#62;}$",["hint 1"], "<b>LHS = </b>$\left&#60;V_1,V_2\\right&#62;=V_1^\dagger\cdot V_2=(V_2^\dagger\cdot V_1)^\dagger=(\left&#60;V_2,V_1\\right&#62;)^\dagger=\overline{\left&#60;V_2,V_1\\right&#62;}$<b> = RHS</b>")

SAQuiz6_1 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 6.1 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))
def QCheckAnswers6_1(btn):
    count = 0
    for q in qlist6_1:
        count += checkComplex(q[1].value,complex(q[0]),q[3],q[4])
    buttonsuccess(Qbtn6_1,count,3,2)

def createQuiz6_1 ():
    display(SAQuiz6_1)
    display(widgets.HTMLMath(value="<font size=\"+1\">1. Compute the inner product of the following."))

    qlist6_1.append(newfillblank("a. $V_1=\\begin{bmatrix}3\\\\4\\\\-10i\end{bmatrix}$ and $V_2=\\begin{bmatrix}3-2i\\\\0\\\\1+i\end{bmatrix}$",0,-1+4j,strInputLayout2))
    qlist6_1.append(newfillblank("b. $V_1=\\begin{bmatrix}-3\\\\-4\\\\10i\end{bmatrix}$ and $V_2=\\begin{bmatrix}-3+2i\\\\0\\\\-1-i\end{bmatrix}$",0,19-16j,strInputLayout2))
    qlist6_1.append(newfillblank("c. A&emsp;=&emsp;$\\begin{bmatrix}-2i& 0& 5+4i\\\\ 1& -1&-i-1\\\\ 0& 4-5i& 1\end{bmatrix}$ and B&emsp;=&emsp;$\\begin{bmatrix}4-2i& 1& -5\\\\ i& -i+2&1\\\\ 1& 0& 3+4i\end{bmatrix}$",0,-21-5j,strInputLayout2))
    for q in qlist6_1:
        display(q[2])
        display(HBox([Label(layout=Layout(width="40px")),q[1],q[3],q[4]]))
    display(VBox([Qbtn6_1],layout=center))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    #display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove that Hadamard matrix is its own inverse."))

Qbtn6_1 = makeButton()
Qbtn6_1.on_click(QCheckAnswers6_1)

qlist6_1 = []
