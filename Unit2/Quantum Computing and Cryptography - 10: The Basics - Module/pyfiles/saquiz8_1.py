from helpermethods import makeQuestion, qonclick,prepareQuestion, makeQuestionBig
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label


#
#   Version 1.0
#
#

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)


q1 = prepareQuestion("1. $\\begin{bmatrix}5\\\\4\\\\10\end{bmatrix}\otimes\\begin{bmatrix}-1\\\\2\end{bmatrix}$",["hint 1","hint 2","hint 3","hint 4","hint 5"], " <font size=\"-1\">$\\begin{bmatrix}5\\\\4\\\\10\end{bmatrix}\otimes\\begin{bmatrix}-1\\\\2\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}5\cdot\\begin{bmatrix}-1\\\\2\end{bmatrix}\\\\4\cdot\\begin{bmatrix}-1\\\\2\end{bmatrix}\\\\10\cdot\\begin{bmatrix}-1\\\\2\end{bmatrix}\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}-5\\\\10\\\\-4\\\\8\\\\-10\\\\20\end{bmatrix}$")
q2 = prepareQuestion("2. $\\begin{bmatrix}2+3i\\\\10-4i\end{bmatrix}\otimes\\begin{bmatrix}4\\\\-1+i\end{bmatrix}$",["hint 1"], "<font size=\"-1\">$\\begin{bmatrix}2+3i\\\\10-4i\end{bmatrix}\otimes\\begin{bmatrix}4\\\\-1+i\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}(2+3i)\cdot\\begin{bmatrix}4\\\\-1+i\end{bmatrix}\\\\(10-4i)\cdot\\begin{bmatrix}4\\\\-1+i\end{bmatrix}\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}8+12i\\\\-5-i\\\\40-16i\\\\-6+14i\end{bmatrix}$")

SAQuiz8_1 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 8.1 Self Assessment Quiz"),
    #widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz8_1 ():
    display(SAQuiz8_1)
    display(widgets.HTMLMath(value="<font size=\"+1\">Calculate the tensor product for the following,"))
    makeQuestionBig(q1, q1onClick)
    makeQuestionBig(q2, q2onClick)
    #display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove that Hadamard matrix is its own inverse."))
