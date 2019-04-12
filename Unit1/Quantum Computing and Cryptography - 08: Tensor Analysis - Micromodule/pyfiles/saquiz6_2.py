from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)


q1 = prepareQuestion("1. $\\rvert V_1+V_2\\rvert\leq\\rvert V_1\\rvert+\\rvert V_2\\rvert$",["hint 1","hint 2","hint 3","hint 4","hint 5"], " $|V_1+V_2|$&emsp;=&emsp;$\sqrt{\left&#60;V,V\\right&#62;}$&emsp;=&emsp;$\sqrt{190}$&emsp;$\leq$&emsp;  $|V_1|+|V_2|$&emsp;=&emsp;$125+65$&emsp;=&emsp;$190$")
q2 = prepareQuestion("2. $\\rvert c\cdot V_1\\rvert=\\rvert c\\rvert\\times\\rvert V_1\\rvert$. Let $c=5-5i$.",["hint 1"], "<font size=\"-1\"><b>LHS:&emsp;</b>$|c\cdot V_1|=\left|(5-5i)\cdot\\begin{bmatrix}3\\\\4\\\\-10i\end{bmatrix}\\right|=\sqrt{6250}$ <b>&emsp;RHS:&emsp;</b>$|c|\\times|V_1|=\sqrt{50}\cdot\sqrt{125}=\sqrt{6250}$")

SAQuiz6_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 6.2 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz6_2 ():
    display(SAQuiz6_2)
    display(widgets.HTMLMath(value="<font size=\"+1\">Given $V_1=\\begin{bmatrix}3\\\\4\\\\-10i\end{bmatrix} \mbox{ and } V_2=\\begin{bmatrix}8i\\\\0\\\\1\end{bmatrix}$, verify the following numerically:"))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    #display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove that Hadamard matrix is its own inverse."))
