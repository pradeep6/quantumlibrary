from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath, math

"""
Dependencies

"""
hidden = Layout(visibility='hidden')

visible = Layout(visibility='visible')

colors =["#85C1E9","#BDBDE2","#7676E2","#21618C","#21618C","#A6A6F8","#3B3BE9","#0C0C69"]

def makeButton():
    temp= widgets.Button(
                description='Check Answers',
                disabled=False,
                button_style='success', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Check Answers',
                icon='check'

            )
    temp.style.font_weight = '1000'
    return temp

"""
question creation
"""
def newfillblank(question, fontsize, answer, layouttouse):
    textBox= widgets.Text(
                    placeholder='a + bi',
                    disabled=False,
                    layout = layouttouse
                )
    validcheck = widgets.Valid(value=False,readout="Incorrect",layout=hidden)
    qtoreturn= widgets.HTMLMath(value="<font size=\"+"+str(fontsize)+"\">"+question)
    labeltoreturn = widgets.HTML(value="")
    return [answer, textBox, qtoreturn, validcheck, labeltoreturn]

def newfloatbox(question, fontsize, answer, layouttouse):
    textBox= widgets.FloatText(
                    placeholder='answer',
                    disabled=False,
                    layout = layouttouse
                )
    validcheck = widgets.Valid(value=False,readout="Incorrect",layout=hidden)
    qtoreturn= widgets.HTMLMath(value="<font size=\"+"+str(fontsize)+"\">"+question)
    labeltoreturn = widgets.HTML(value="")
    return [answer, textBox, qtoreturn, validcheck, labeltoreturn]

def newCordBox(question, fontsize, answer, layouttouse):
    textBox= widgets.FloatText(
                    placeholder='answer',
                    disabled=False,
                    layout = layouttouse
                )
    textBox2= widgets.FloatText(
                    placeholder='answer',
                    disabled=False,
                    layout = layouttouse
                )
    validcheck = widgets.Valid(value=False,readout="Incorrect",layout=hidden)
    qtoreturn= widgets.HTMLMath(value="<font size=\"+"+str(fontsize)+"\">"+question)
    labeltoreturn = widgets.HTML(value="")
    return [answer, textBox,textBox2, qtoreturn, validcheck, labeltoreturn]

def newPolar(question, fontsize, answer, layouttouse):
    textBox= widgets.FloatText(
                    placeholder='answer',
                    disabled=False,
                    layout = layouttouse
                )

    floatslider= widgets.FloatSlider(
                    value=0,
                    min=0,
                    max=360.0,
                    step=0.01,
                    description='',
                    disabled=False,
                    continuous_update=False,
                    orientation='horizontal',
                    readout=True,
                    readout_format='.001f',
                )
    floatslider.style.handle_color = random.choice(colors)

    validcheck = widgets.Valid(value=False,readout="Incorrect",layout=hidden)
    qtoreturn= widgets.HTMLMath(value="<font size=\"+"+str(fontsize)+"\">"+question)
    labeltoreturn = widgets.HTML(value="")
    return [answer, textBox, floatslider, qtoreturn, validcheck, labeltoreturn]
def newMatrixAdd(question, fontsize, answer, layouttouse, numVars, formatbase):
    alpha="abcdefghijklmnopqrstuvwxyz"
    textboxes=[]
    for i in range(numVars):
        textboxes.append(widgets.Text(
                        placeholder='a + bi',
                        disabled=False,
                        layout = layouttouse,
                        description = '$'+alpha[i]+' =$'
                    ))
    labeltoreturn = widgets.HTML(value="")
    validcheck = widgets.Valid(value=False,readout="Incorrect",layout=hidden)
    formatbox=widgets.HTMLMath(value="<font size=\"+0\">&emsp; "+formatbase)
    qtoreturn= widgets.HTMLMath(value="<font size=\"+"+str(fontsize)+"\">&emsp;&emsp;"+question+" = ")
    return [answer, textboxes, qtoreturn,formatbox, validcheck, labeltoreturn]
"""
Lable box modification

"""
def qcorrect(validbox, labelthing):
    validbox.value=True
    validbox.readout="Correct"
    labelthing.value=""
    validbox.layout=visible
def qincorrect(validbox,labelthing):
    validbox.value=False
    validbox.readout="Incorrect"
    labelthing.value=""
    validbox.layout=visible
def qformaterror(validbox, labelthing):
    validbox.value=False
    validbox.readout="Invalid Answer"
    labelthing.value="<b>Incorrect Format. Format answers as a + bi</b>"
    validbox.layout=visible
def qunknownerror(validbox, labelthing):
    validbox.value=False
    labelthing.value="Unknown Error"
    labelthing.value="<b>Incorrect Format. Format answers as a + bi</b>"
def notfound():
    rngchoises=['404 answer not found', 'forgetting something?', 'give it a shot!', 'just guess!', '<--- need this?']
    return random.choice(rngchoises)
def empty(validbox, labelthing):
    validbox.value=False
    validbox.readout=notfound()
    labelthing.value=""
    validbox.layout=visible
"""
Answer Grading portion
"""
def buttonsuccess(btn,count,all,some):
    if(count == all ):
        btn.button_style='info'
        btn.description='Way to Go!'
        btn.icon='check'
    if(count == some):
        btn.button_style='warning'
        btn.icon='times'
        btn.description='Close!'
    if(count < some):
        btn.button_style='danger'
        btn.icon='times'
        btn.description='Try Again'


def getComplex(textin):
    complexvalue = str(textin)
    complexvalue = complexvalue.replace(" ","")
    complexvalue = complexvalue.replace("i","j")
    complexvalue = complexvalue.replace("+-","-")
    return complex(complexvalue)

def checkComplex(answer, key, validcheck, labeltoreturn):
    if answer == "":
        empty(validcheck, labeltoreturn)
        return 0
    try:
        if(getComplex(answer) == (key)):
            qcorrect(validcheck,labeltoreturn)
            return 1
        else:
            qincorrect(validcheck,labeltoreturn)
            return 0
    except ValueError as error:
        qformaterror(validcheck,labeltoreturn)
        return 0
    except:
        qunknownerror(validcheck,labeltoreturn)
        return 0

def checkMatrix(answers,keys,validcheck, labeltoreturn):
    count = 0
    for answer in answers:
        if answer.value == "":
            empty(validcheck, labeltoreturn)
            return 0
            break
        try:
            if(getComplex(answer.value) == (keys[count])):
                qcorrect(validcheck,labeltoreturn)
            else:
                qincorrect(validcheck,labeltoreturn)
                return 0
                break
        except ValueError as error:
            qformaterror(validcheck,labeltoreturn)
            return 0
            break
        except:
            qunknownerror(validcheck,labeltoreturn)
            return 0
            break
        finally:
            count+= 1
    return 1

def checkfloat(answer,key,validcheck,labeltoreturn):
    try:
        if(math.isclose(answer,key,rel_tol=.005)):
            qcorrect(validcheck,labeltoreturn)
            return 1
        else:
            qincorrect(validcheck,labeltoreturn)
            return 0
    except:
        qunknownerror(validcheck,labeltoreturn)
        return 0
def checkfloatpair(answer1,answer2,key,validcheck,labeltoreturn):
    try:
        if(math.isclose(answer1,key[0],rel_tol=.005) and math.isclose(answer2,key[1],rel_tol=.005)):
            qcorrect(validcheck,labeltoreturn)
            return 1
        else:
            qincorrect(validcheck,labeltoreturn)
            return 0
    except:
        qunknownerror(validcheck,labeltoreturn)
        return 0

"""
Questions with hints
"""

hiddenanswer = "<font size=\"+3\"> (Answer Hidden)"


def createButton(string,style,icons):
    temp= widgets.Button(
                description=''+string,
                disabled=False,
                button_style=''+style, # 'success', 'info', 'warning', 'danger' or ''
                tooltip=''+string,
                icon=''+icons,
                layout = Layout(width = "100%")
            )
    temp.style.font_weight = '1000'
    return temp

#Compatable with math inputs
def prepareQuestion(questionIn, hintsIn, answerIn):
    currout = widgets.HTMLMath(value="<font size=\"+0\">&emsp;"+hiddenanswer)
    #create each box and their interactions
    priorhint = createButton("Previous Hint","","")
    nexthint = createButton("Next Hint","","")
    answer = createButton("Show Answer","info","check")
    priorhint.disabled = True
    question = widgets.HTMLMath(value="<font size=\"+0\">&emsp;" + questionIn)
    hintcount = widgets.HTML(value=" ")
    #Print it out (we could also return it)
    return[question,currout,hintsIn,answerIn,priorhint,nexthint,answer,-1,hintcount]

def makeQuestion(ques,click):
    printQuesion(ques,105)
    ques[4].on_click(click)
    ques[5].on_click(click)
    ques[6].on_click(click)
def makeQuestionBig(ques,click):
    printQuesion(ques,190)
    ques[4].on_click(click)
    ques[5].on_click(click)
    ques[6].on_click(click)

def printQuesion(question,size):
    display(question[0])

    toprint = VBox([
        VBox([
            HBox([
                question[8],
                Label()
            ],layout=Layout(height="40px")),
            VBox([
                question[1]
            ],layout=Layout(align_items="center",height = str(size)+"px")),
            Label(value="")
        ], layout=Layout(height = str(size+40)+"px",border="solid 1px",width = "75%")),
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
            q[6].description = "Show Answer"
            q[6].button_style="info"
            q[6].icon = "check"

    if(btn.description[:1] == "P"):
        q[6].description = "Show Answer"
        q[6].button_style="info"
        q[6].icon = "check"

        if(q[7] == 0):
            q[7] -= 1
            q[1].value = hiddenanswer
            q[8].value = " "
        if(q[7] > 0 ):
            q[7] -= 1
            q[1].value = q[2][q[7]]
            q[8].value = "Hint "+str(q[7]+1)+" of "+ str(len(q[2]))
    if(btn.description[:1] == "S"):
        q[1].value = "<font size=\"+0\">&emsp;"+q[3]
        q[8].value = " "
        q[6].description = "Hide Answer"
        q[6].button_style = "danger"
        q[6].icon = "times"

    elif(btn.description[:1] == "H"):
        if(q[7] == -1):
            q[1].value = hiddenanswer
        else:
            q[1].value = q[2][q[7]]
            q[8].value = "Hint "+str(q[7]+1)+" of "+ str(len(q[2]))
        q[6].description = "Show Answer"
        q[6].button_style="info"
        q[6].icon = "check"
    if(q[7] == -1):
        q[4].disabled = True
    else:
        q[4].disabled = False
    if(q[7] == len(q[2])-1):
        q[5].disabled = True
    else:
        q[5].disabled = False

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

q1 = prepareQuestion("1. $(A+B)^T = A^T+B^T$",["hint 1","hint 2","hint 3","hint 4","hint 5"], "<b>LHS:</b> $(A+B)^T=\\begin{bmatrix}i&2+5i\\\\3+11i&6-10i\end{bmatrix}^T$$=\\begin{bmatrix}i& 3+11i\\\\2+5i&6-10i\end{bmatrix}$")
q2 = prepareQuestion("2. $(A+B)^T = A^T+B^T$",["hint 1"], "answerzzz")
q3 = prepareQuestion("3. $(A+B)^T = A^T+B^T$",["hint 1","hint 2","hint 3"], "answerzzz")
