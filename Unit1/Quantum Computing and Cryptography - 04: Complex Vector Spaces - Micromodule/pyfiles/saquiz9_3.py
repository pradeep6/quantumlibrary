from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)
def q4onClick(btn):
    qonclick(btn,q4)


q1 = prepareQuestion("2. About $\\frac{1}{3}$ bright.",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$cos^2 ( \\theta_1-90^{\\circ})$&emsp;$ cos^2(0^{\\circ} - \\theta_1) $&emsp;=&emsp;$ \\frac{1}{4}$\n&emsp;&emsp;&emsp; After solving you find $\\theta = 45^{\\circ}$")
q2 = prepareQuestion("1. The brightest.",["hint 1"], "It turns out that no value of $\\theta$ will result in $\\frac{1}{3}$. Therefore, it is not achievable")
#q3 = prepareQuestion("3. Are quantum systems reversible? Why?",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$A^\dagger$&emsp;=&emsp;$\\begin{bmatrix}2&-i\\\\i&1\end{bmatrix}=A$")
#q4 = prepareQuestion("4. If we \"look\" at a three state system and find it in state 2, then the probability vector representing our knowledge is given by _____________.",["hint 1"], "$B^\dagger$&emsp;=&emsp;$\\begin{bmatrix}1&1+i&2i\\\\1-i&5&-3\\\\-2i&-3&0\end{bmatrix}=B$")

SAQuiz9_3 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 9.3 Self Assessment Quiz"),
    widgets.HTML(value="<font size=\"+0\">What angle should the middle filter be polarized at so that the screen is:"),
    #widgets.HTML(value="<b><font size=\"-1\"<b>Fill in the blanks:</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz9_3 ():
    display(SAQuiz9_3)

    makeQuestion(q2, q2onClick)
    makeQuestion(q1, q1onClick)
    #makeQuestion(q3, q3onClick)
    #makeQuestion(q4, q4onClick)
