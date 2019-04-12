from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath
from helpermethods import newfillblank,checkComplex, buttonsuccess, makeButton, newMatrixAdd, checkMatrix


hiddenanswer = "<font size=\"+3\"> Hints"


def createButton(string,style,icons):
    temp= widgets.Button(
                description=''+string,
                disabled=False,
                button_style=''+style, # 'success', 'info', 'warning', 'danger' or ''
                tooltip=''+string,
                icon=''+icons,
                layout = Layout(width = "33.33%")
            )
    temp.style.font_weight = '1000'
    return temp

#Compatable with math inputs
def prepareQuestion(questionIn, hintsIn, answerIn):
    currout = widgets.HTMLMath(value="<font size=\"+0\">&emsp;"+hiddenanswer)
    #create each box and their interactions
    priorhint = createButton("Previous Hint","success","")
    nexthint = createButton("Next Hint","success","")
    answer = createButton("Answer","warning","check")
    question = widgets.HTMLMath(value="<font size=\"+0\">&emsp;" + questionIn)
    hintcount = widgets.HTML(value=" ")
    #Print it out (we could also return it)
    return[question,currout,hintsIn,answerIn,priorhint,nexthint,answer,-1,hintcount]

def makeQuestion(ques,click):
    printQuesion(ques)
    ques[4].on_click(click)
    ques[5].on_click(click)
    ques[6].on_click(click)
def printQuesion(question):
    display(question[0])

    toprint = VBox([
        VBox([
            HBox([
                question[8],
                Label()
            ]),
            VBox([
                question[1]
            ],layout=Layout(align_items="center")),
            Label(value="")
        ], layout=Layout(height = "125px",border="solid 1px",width = "75%")),
        HBox([
            #question[4],
            #question[5],
            question[6]
        ],layout=Layout(width="75%"))
    ], layout=Layout(align_items="center"))
    display(toprint)




def qonclick(btn,q):

    if(btn.description[:1] == "N"):
        if(q[7] < len(q[2])-1):
            q[7] += 1
            q[1].value = q[2][q[7]]
            q[8].value = "Hint "+str(q[7]+1)+" of "+ str(len(q[2]))
    if(btn.description[:1] == "P"):
        if(q[7] == 0):
            q[7] -= 1
            q[1].value = hiddenanswer
            q[8].value = " "
        if(q[7] > 0 ):
            q[7] -= 1
            q[1].value = q[2][q[7]]
            q[8].value = "Hint "+str(q[7]+1)+" of "+ str(len(q[2]))
    if(btn.description[:1] == "A"):
        if(q[1].value == "<font size=\"+0\">&emsp;"+q[3]):
            if(q[7] == -1):
                q[1].value = hiddenanswer

            else:
                q[1].value = q[2][q[7]]
                q[8].value = "Hint "+str(q[7]+1)+" of "+ str(len(q[2]))
        else:
            q[1].value = "<font size=\"+0\">&emsp;"+q[3]
            q[8].value = " "


def test ():
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3,q3onClick)

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)
"""
q1 = prepareQuestion("1. $(A+B)^T = A^T+B^T$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "<b>They are equal</b>test $(A+B)^T=\\begin{bmatrix}i&2+5i\\\\3+11i&6-10i\end{bmatrix}^T$$=\\begin{bmatrix}i& 3+11i\\\\2+5i&6-10i\end{bmatrix}$")
q2 = prepareQuestion("2. $(A+B)^T = A^T+B^T$",["hint 1"], "answerzzz")
q3 = prepareQuestion("3. $(A+B)^T = A^T+B^T$",["hint 1","hint 2","hint 3"], "answerzzz")
"""









































#
