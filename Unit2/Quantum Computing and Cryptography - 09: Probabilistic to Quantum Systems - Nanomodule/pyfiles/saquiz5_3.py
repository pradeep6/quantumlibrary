from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)

q1 = prepareQuestion("a. $\\begin{bmatrix}\\frac{\sqrt{2}}{2}\\\\\\frac{\sqrt{2}}{2}\end{bmatrix}$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$\\frac{1}{\sqrt{2}}$&emsp;$\\begin{bmatrix}1&1\\\\1&-1\end{bmatrix}$&emsp;$\cdot$&emsp;$\\begin{bmatrix}\\frac{\sqrt{2}}{2}\\\\\\frac{\sqrt{2}}{2}\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}1\\\\0\end{bmatrix}$")
q2 = prepareQuestion("b. $\\begin{bmatrix}\\frac{i}{\sqrt{3}}\\\\\\frac{\sqrt{2}}{\sqrt{3}}\end{bmatrix}$",["hint 1"], "$\\frac{1}{\sqrt{2}}\\begin{bmatrix}1&1\\\\1&-1\end{bmatrix}$&emsp;$\cdot$&emsp;$\\begin{bmatrix}\\frac{i}{\sqrt{3}}\\\\\\frac{\sqrt{2}}{\sqrt{3}}\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}\\frac{i}{\sqrt{6}}+\\frac{1}{\sqrt{3}}\\\\\\frac{i}{\sqrt{6}}-\\frac{1}{\sqrt{3}}\end{bmatrix}$")
q3 = prepareQuestion("2. Prove that Hadamard matrix is its own inverse.",["hint 1"], "$\\frac{1}{\sqrt{2}}$&emsp;$\\begin{bmatrix}1&1\\\\1&-1\end{bmatrix}$&emsp;$\cdot$&emsp;$\\frac{1}{\sqrt{2}}$&emsp;$\\begin{bmatrix}1&1\\\\1&-1\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}1&0\\\\0&1\end{bmatrix}$")

SAQuiz4_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 5.3 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz5_3 ():
    display(SAQuiz4_2)
    display(widgets.HTMLMath(value="<font size=\"+1\">1. Represent the following vectors with respect to Hadamard basis,"))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    #display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove that Hadamard matrix is its own inverse."))
    makeQuestion(q3, q3onClick)
