from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)

q1 = prepareQuestion("1. $(A+B)^T = A^T+B^T$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$(A+B)^T $&emsp;=&emsp;$ A^T+B^T$&emsp;=&emsp;$\\begin{bmatrix}i& 3+11i\\\\2+5i&6-10i\end{bmatrix}$")
q2 = prepareQuestion("2. $\overline{A+B}=\overline{A}+\overline{B}$",["hint 1"], "$\overline{A+B}=\overline{A}+\overline{B}$&emsp;=&emsp;$\\begin{bmatrix}-i&2-5i\\\\3-11i&6+10i\end{bmatrix}$")
q3 = prepareQuestion("3. $(A+B)^\dagger = A^\dagger+B^\dagger$",["hint 1","hint 2","hint 3"], "<b>LHS =</b> $(A+B)^\dagger$&emsp;=&emsp;$(\overline{A+B})^T$&emsp;=&emsp;$(\overline{A}+\overline{B})^T$&emsp;=&emsp;$\overline{A}^T+\overline{B}^T$&emsp;=&emsp;$A^\dagger+B^\dagger$<b> = RHS</b>")

SAQuiz4_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 4.2 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz4_2 ():
    display(SAQuiz4_2)
    display(widgets.HTMLMath(value="<font size=\"+1\">Given $A=\\begin{bmatrix}1+i&2\\\\-3&1-i\end{bmatrix}$ and $B=\\begin{bmatrix}-1&5i\\\\6+11i&5-9i\end{bmatrix}$, verify the following properties numerically,"))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3,q3onClick)
