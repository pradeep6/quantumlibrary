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


q1 = prepareQuestion("a. $\\begin{bmatrix}2&-4\\\\-1&-1\end{bmatrix}$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "<b>Eigenvalues = &emsp;</b>$\lambda=-2$ and $\lambda=3$&emsp;&emsp;<b>Eigenvectors =&emsp; </b> $\\begin{bmatrix}1\\\\1\end{bmatrix}$ and $\\begin{bmatrix}-4\\\\1\end{bmatrix}$")
q2 = prepareQuestion("b. $\\begin{bmatrix}3&-2\\\\4&-1\end{bmatrix}$",["hint 1"], "<b>Eigenvalues = &emsp;</b>$\lambda=1+2i$ and $\lambda=1-2i$&emsp;&emsp;<b>Eigenvectors =&emsp; </b> $\\begin{bmatrix}\\frac{1}{2}+i\\frac{1}{2}\\\\1\end{bmatrix}$ and $\\begin{bmatrix}\\frac{1}{2}-i\\frac{1}{2}\\\\1\end{bmatrix}$")
q3 = prepareQuestion("a. $A$&emsp;=&emsp;$\\begin{bmatrix}2&-i\\\\i&1\end{bmatrix}$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$A^\dagger$&emsp;=&emsp;$\\begin{bmatrix}2&-i\\\\i&1\end{bmatrix}=A$")
q4 = prepareQuestion("b. $B$&emsp;=&emsp;$\\begin{bmatrix}1&1+i&2i\\\\1-i&5&-3\\\\-2i&-3&0\end{bmatrix}$",["hint 1"], "$B^\dagger$&emsp;=&emsp;$\\begin{bmatrix}1&1+i&2i\\\\1-i&5&-3\\\\-2i&-3&0\end{bmatrix}=B$")

SAQuiz7_1 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 7.1 Self Assessment Quiz"),
    #widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz7_1 ():
    display(SAQuiz7_1)
    display(widgets.HTMLMath(value="<font size=\"+1\">1. Compute the eigenvectors and eigenvalues associated with the following matrices."))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

    display(widgets.HTMLMath(value="<font size=\"+1\">2. Verify that the following matrices are Hermitian."))
    makeQuestion(q3, q3onClick)
    makeQuestion(q4, q4onClick)
    #display(widgets.HTMLMath(value="<font size=\"+1\">2. Prove that Hadamard matrix is its own inverse."))
