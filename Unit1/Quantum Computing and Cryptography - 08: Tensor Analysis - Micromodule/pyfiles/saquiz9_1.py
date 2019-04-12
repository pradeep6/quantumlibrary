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


q1 = prepareQuestion("1. If a two state system has $\\frac{3}{4}$ probability of being in state 0 then we can represent this with a proabibility vector _______________.",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$\\begin{bmatrix}\\frac{3}{4}\\\\\\frac{1}{4}\end{bmatrix}$")
q2 = prepareQuestion("2. If I \"look\" at a two state system and find it in state 1, then my knowledge of the state of the system is given by _____________.",["hint 1"], "$\\begin{bmatrix}0\\\\1\end{bmatrix}$")
q3 = prepareQuestion("3. Consider a system that can be in states 1, 2 and 3. We know that at time $t$ the system may be in state 1 with probability $\\frac{1}{4}$, in state 2 with probability $\\frac{1}{2}$ and in state 3 with probability $\\frac{1}{4}$. The probability vector representing our system can be written as ________________.",["hint 1","hint 2","hint 3","hint 4","hint 5"], "<font size=\"-1\"> $\\begin{bmatrix}\\frac{1}{4}\\\\\\frac{1}{2}\\\\\\frac{1}{4}\end{bmatrix}$")
q4 = prepareQuestion("4. If we \"look\" at a three state system and find it in state 2, then the probability vector representing our knowledge is given by _____________.",["hint 1"], "<font size=\"-1\"> $\\begin{bmatrix}0\\\\1\\\\0\end{bmatrix}$")

SAQuiz9_1 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 9.1 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Fill in the blanks:</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz9_1 ():
    display(SAQuiz9_1)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)
    makeQuestion(q4, q4onClick)
