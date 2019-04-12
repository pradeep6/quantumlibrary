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


q1 = prepareQuestion("1. When quantum system states are represented using vectors, what are the elements of such a vector: complex numbers, real numbers or integers?",["hint 1","hint 2","hint 3","hint 4","hint 5"], "<b>Complex numbers:</b>\n The elements can also be real numbers and integers but the set of complex numbers includes them. Therefore the most general case answer is <u>complex numbers.")
q2 = prepareQuestion("2. What type of matrices are valid operators for a quantum system?",["hint 1"], "Unitary Matrices")
q3 = prepareQuestion("3. Are quantum systems reversible? Why?",["hint 1","hint 2","hint 3","hint 4","hint 5"], "Yes, quantum systems are reversible because the evolution of a quantum system can be  modelled using unitary matrices which can be \"inverted\" ")
#q4 = prepareQuestion("4. If we \"look\" at a three state system and find it in state 2, then the probability vector representing our knowledge is given by _____________.",["hint 1"], "$B^\dagger$&emsp;=&emsp;$\\begin{bmatrix}1&1+i&2i\\\\1-i&5&-3\\\\-2i&-3&0\end{bmatrix}=B$")

SAQuiz9_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 9.2 Self Assessment Quiz"),
    #widgets.HTML(value="<b><font size=\"-1\"<b>Fill in the blanks:</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz9_2 ():
    display(SAQuiz9_2)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)
    #makeQuestion(q4, q4onClick)
