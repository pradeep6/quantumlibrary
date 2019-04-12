from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)


q1 = prepareQuestion("a. $\\frac{1}{2}\\begin{bmatrix}1+i& 1+i\\\\1-i&-1+i\end{bmatrix}$",["hint 1","hint 2","hint 3","hint 4","hint 5"], " $A^\dagger\cdot A$&emsp;=&emsp;$\\frac{1}{2}\\begin{bmatrix}1-i&1+i\\\\1-i&-1-i\end{bmatrix}$&emsp;$\cdot$&emsp;$\\frac{1}{2}\\begin{bmatrix}1+i& 1+i\\\\1-i&-1+i\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}1&0\\\\0&1\end{bmatrix}$")
q2 = prepareQuestion("b. $\\begin{bmatrix}cos\\theta&-sin\\theta&0\\\\sin\\theta&cos\\theta&0\\\\0&0&1\end{bmatrix}$",["hint 1"], "$B^\dagger\cdot B$&emsp;=&emsp;$\\begin{bmatrix}cos\\theta& sin\\theta& 0\\\\-sin\\theta& cos\\theta& 0\\\\0&0&1\end{bmatrix}$&emsp;$\cdot$&emsp;$\\begin{bmatrix}cos\\theta&-sin\\theta&0\\\\sin\\theta&cos\\theta&0\\\\0&0&1\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}1&0&0\\\\0&1&0\\\\0&0&1\end{bmatrix}$")
q3 = prepareQuestion("$\left&#60;UV,UV'\\right&#62;$&emsp;=&emsp;$\left&#60;V,V'\\right&#62;$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "Thats a goooood question lol")

SAQuiz7_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 7.2 Self Assessment Quiz"),
    #widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz7_2 ():
    display(SAQuiz7_2)
    display(widgets.HTMLMath(value="<font size=\"+1\">1. Verify that the following matrices are unitary,"))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

    display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove the following. For a unitary matrix $U$,"))
    makeQuestion(q3, q3onClick)
    #display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove that Hadamard matrix is its own inverse."))
