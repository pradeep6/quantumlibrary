from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)

q1 = prepareQuestion("a.&emsp; $B_1$ =&emsp; $\left\{\\begin{bmatrix}1\\\\0\end{bmatrix}, \\begin{bmatrix}0\\\\1\end{bmatrix}\\right\}$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "$\\begin{bmatrix}1&0\\\\0&1\end{bmatrix}\\begin{bmatrix}c_1\\\\c_2\end{bmatrix}$&emsp;=&emsp;$\\begin{bmatrix}x\\\\y\end{bmatrix}$&emsp;&emsp;&emsp;&emsp;&emsp;Because we can find the coefficients c1 and c2 for every<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; possible value of x and y; $B_1$ forms a basis for $\mathbb{C}^2$ ")
q2 = prepareQuestion("b.&emsp; $B_2$ = &emsp;$\left\{\\begin{bmatrix}1\\\\1\end{bmatrix}, \\begin{bmatrix}1\\\\-1\end{bmatrix}\\right\}$",["hint 1"], "$\left|\\begin{matrix}1&1\\\\1&-1\end{matrix}\\right|$&emsp;=&emsp;-2. &emsp;&emsp;Therefore, the set of vectors is linearly independent, and because the vectors &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;form is invertible, $B_2$ is a basis set for $\mathbb{C}^2$")

SAQuiz4_2 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 5.2 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
],layout=Layout(display='flex_flow',height='100%'))

def createQuiz5_2 ():
    display(SAQuiz4_2)
    display(widgets.HTMLMath(value="<font size=\"+1\"> Verify that the following are basis for $\mathbb{C}^2$"))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
