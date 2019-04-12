from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)

q1 = prepareQuestion("1. $(A\cdot B)\cdot C $&emsp;=&emsp;$ A\cdot(B\cdot C)$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$(A\cdot B)\cdot C$&emsp;=&emsp;$A\cdot(B\cdot C)$&emsp;=&emsp;$\\begin{bmatrix}46-100i& 15+3i\\\\196-10i& -3+21i\end{bmatrix}$")
q2 = prepareQuestion("2. $A\cdot(B+C) $&emsp;=&emsp;$ (A\cdot B)+(A\cdot C)$",["hint 1"], "$A\cdot(B+C) $&emsp;=&emsp;$ (A\cdot B)+(A\cdot C)$&emsp;=&emsp;$\\begin{bmatrix}26-8i&16\\\\2-26i&1+21i\end{bmatrix}$")
q3 = prepareQuestion("3. $c\cdot(A\cdot B) $&emsp;=&emsp;$ (c\cdot A)\cdot B $&emsp;=&emsp;$ A\cdot(c\cdot B)$",["hint 1","hint 2","hint 3"], "$c\cdot(A\cdot B) $&emsp;=&emsp;$ (c\cdot A)\cdot B $&emsp;=&emsp;$ A\cdot(c\cdot B)$&emsp;=&emsp;$\\begin{bmatrix}-10-80i& 90-60i\\\\110-80i& 90+120i\end{bmatrix}$")

SAQuiz4_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 4.3 Self Assessment Quiz"),
    #widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz4_3 ():
    display(SAQuiz4_2)
    display(widgets.HTMLMath(value="<font size=\"+1\">Let A=$\\begin{bmatrix}2& 1-3i\\\\-1-3i& 4\end{bmatrix}$, $B=\\begin{bmatrix}i&-i\\\\ 4+1i& 5i\end{bmatrix}$,$C=\\begin{bmatrix}10-1i&0\\\\-1&1\end{bmatrix}$ and $c=5-5i$."))
    display(widgets.HTMLMath(value="<font size=\"+1\">Verify the following properties numerically:"))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3,q3onClick)
