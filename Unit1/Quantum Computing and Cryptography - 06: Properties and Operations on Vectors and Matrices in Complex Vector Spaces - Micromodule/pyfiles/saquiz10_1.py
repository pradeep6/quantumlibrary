from helpermethods import makeQuestion, qonclick,prepareQuestion
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath

curquestion = numCorrect= 0
#numCorrect = 0
color='lightblue'
"""
Layouts
"""
numInputLayout=Layout(
    width='55px'
)
numInputLayout2=Layout(
    width='60px'
)
center = Layout(align_items='center')
hidden = Layout(visibility='hidden')
visible = Layout(visibility='visible')

questionlist = [("&emsp;$\\rvert-\\rangle=\\frac{1}{\sqrt{2}}(\\rvert0\\rangle-\\rvert1\\rangle)$",True,"Yes, because $\left|\\frac{1}{\sqrt{2}}\\right|^2 + \left|\\frac{1}{\sqrt{2}}\\right|^2 = 1$ "),
                ("&emsp;$\\frac{1}{\sqrt{2}}\\rvert0\\rangle-\\frac{1+i}{2}\\rvert1\\rangle$",True,"Yes, because $\left|\\frac{1}{\sqrt{2}}\\right|^2 + \left|\\frac{-1-i}{2}\\right|^2=\\frac{1}{2} + (\ \\frac{1}{4} + \\frac{1}{4} )= 1$"),
                ("&emsp;$\\frac{1+i}{3}\\rvert0\\rangle-\\frac{1-i}{2}\\rvert1\\rangle$",False,"No, because $\left|\\frac{1+i}{3}\\right|^2+\left|\\frac{-i+1}{2}\\right|^2 = (\ \\frac{1}{3})^2+(\ \\frac{1}{3})^2+(\ \\frac{-1}{2})^2+(\ \\frac{1}{2})^2 \\ne 1$",1),
                ("&emsp;$\\frac{i}{10}\\rvert0\\rangle+\\frac{99}{10}\\rvert1\\rangle$",False,"No, because $\left|\\frac{i}{10}\\right|^2+\left|\\frac{99}{10}\\right|^2 \\ne 1$",2),
                ("&emsp;$\\frac{\sqrt{3}}{2}\\rvert0\\rangle+\\frac{1}{3}\\rvert1\\rangle$",False,"No, because $\left|\\frac{\sqrt{3}}{2}\\right|^2+\left|\\frac{1}{3}\\right|^2 = \\frac{3}{4} + \\frac{1}{9} \\ne 1$",3),
                ("&emsp;$\\frac{i}{\sqrt{2}}(\\rvert0\\rangle+\\rvert1\\rangle)$",True,"Yes, because $\left|\\frac{i}{\sqrt{2}}\\right|^2 + \left|\\frac{i}{\sqrt{2}}\\right|^2 = \\frac{1}{2} + \\frac{1}{2} = 1$"),
                ("&emsp;$\\frac{1}{\sqrt{2}}(\\rvert0\\rangle+e^{\\frac{i\pi}{2}}\\rvert1\\rangle)$",True,"Yes, because $\left|\\frac{1}{\sqrt{2}}\\right|^2 + \left|\\frac{e^{\\frac{i\pi}{2}}}{\sqrt{2}}\\right|^2 = \\frac{1}{2} + \left|\\frac{\cos(\ \\frac{\pi}{2})+i\sin(\ \\frac{\pi}{2})}{\sqrt{2}}\\right|^2=\\frac{1}{2}+\\frac{\cos^2\\frac{\pi}{2}}{2}+\\frac{\sin^2\\frac{\pi}{2}}{2}=1$"),
                ("&emsp;$\\frac{1}{2}\\rvert0\\rangle-\\frac{i}{2}\\rvert1\\rangle$",False,"No, because $\left|\\frac{1}{2}\\right|^2+\left|\\frac{-i}{2}\\right|^2 = \\frac{1}{4} + \\frac{1}{4} \\ne 1$",4),
                ("&emsp;$\\frac{\sqrt{3}}{2}\\rvert0\\rangle+\\frac{1}{4}\\rvert1\\rangle$",False,"No, because $\left|\\frac{\sqrt{3}}{2}\\right|^2+\left|\\frac{1}{4}\\right|^2 = \\frac{3}{4} + \\frac{1}{16} \\ne 1$",5),
                ("&emsp;$e^{i\pi}\\rvert-\\rangle$",True,"Yes, because $\left|e^{i\pi}\\right|^2=1$")]

random.shuffle(questionlist)

qcount = len(questionlist)

def makeEnd():
    return str(curquestion+1) + "/" + str(qcount)
#floatboxes
intbox2_1 = widgets.FloatText(layout=numInputLayout2)

intbox2_2 = widgets.FloatText(layout=numInputLayout2)

botbtn = Layout(width = "275px",height = "35px")

sidebtn = Layout(width = "110px",height = "40px")
#Text
probstatment = widgets.HTML(value="<font size=\"+2\">Is this a valid qubit?")

#buttons!
btn_2_restart= widgets.Button(
            description='Restart',
            disabled=False,
            button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Don\'t give up :)',
            layout=botbtn

        )
btn_2_check= widgets.Button(
            description='Check '+ makeEnd(),
            disabled=True,
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Check Answer',
            icon='check',
            layout=botbtn

        )

btn_yes = widgets.Button(
            description='Yes.',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='This is a valid qubit',
            icon='',
            layout=sidebtn
        )
btn_no = widgets.Button(
            description='No.',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='This is not a valid qubit',
            icon='',
            layout=sidebtn
        )
btn_solution = widgets.Button(
            description='Solution',
            disabled=True,
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Show Explanation',
            icon='',
            layout=botbtn
        )
btn_back = widgets.Button(
            description='Go Back!',
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Return to question',
            layout=Layout(width="100%",height="50px")
        )
btn_solution.style.button_color = "#885ead"
btn_back.style.button_color = "#885ead"
btn_back.style.font_weight = '1000'
btn_yes.style.font_weight = '1000'
btn_no.style.font_weight = '1000'
btn_2_check.style.font_weight = '1000'
btn_solution.style.font_weight = '1000'
btn_2_restart.style.font_weight = '1000'
curq = widgets.HTMLMath(value="<font size=\"+1\"> question not generated")
qsolution = widgets.HTMLMath(value="<font size=\"+1\"> question not generated",layout=Layout(height = "100px",width="600px"))

def makeSolution():
    qsolution.value="<font size=\"+1\">" + questionlist[curquestion][2]

def hideSolution():
    qsolution.value="<font size=\"+2\"> Solve a question first!"

def refreshq():
    curq.value="<font size=\"+1\">"+questionlist[curquestion][0]
    solutionquestion.value="<font size=\"+1\">Is"+questionlist[curquestion][0]+ "  a valid qubit?"

def nextq():
    global curquestion
    curquestion = curquestion + 1
    refreshq()

#compile exercise 2
exercise1=VBox([
    probstatment,
    VBox([HBox([VBox([Label(),curq],layout=Layout(width="400px")),Label(),VBox([btn_yes,Label(),btn_no])])],layout=Layout(align_items='center')),
    Label(),
    VBox([HBox([btn_solution,Label(),btn_2_check,Label(),btn_2_restart])],layout=Layout(align_items='center'))
])

def q1onClick(btn):
    qonclick(btn,q1)
def q2onClick(btn):
    qonclick(btn,q2)
def q3onClick(btn):
    qonclick(btn,q3)
def q4onClick(btn):
    qonclick(btn,q4)
def q5onClick(btn):
    qonclick(btn,q5)

q1 = prepareQuestion("Make $\\frac{1+i}{3}\\rvert0\\rangle-\\frac{1-i}{2}\\rvert1\\rangle$  a valid qubit",["hint 1","hint 2","hint 3","hint 4","hint 5"], "length = $\sqrt{\\frac{13}{18}}$  <br>"+
"<font size=\"-1\">Therefore, $\\rvert\psi\\rangle  = \\frac{1+i}{3} \\times \\frac{1}{\sqrt{\\frac{13}{18}}} \\rvert0\\rangle - \\frac{1-i}{2} \\times \\frac{1}{\sqrt{\\frac{13}{18}}}\\rvert1\\rangle = \\frac{\sqrt{18}}{3} \\times \\frac{1+i}{\sqrt{13}}\\rvert0\\rangle - \\frac{\sqrt{18}}{2} \\times \\frac{1-i}{\sqrt{13}}\\rvert1\\rangle$ is a valid qubit.")
q2 = prepareQuestion("Make $\\frac{i}{10}\\rvert0\\rangle+\\frac{99}{10}\\rvert1\\rangle$  a valid qubit",["hint 1"], "length = $\sqrt{\\frac{9802}{100}}$  <br>"+
"<font size=\"-1\">Therefore, $\\rvert\psi\\rangle = \sqrt{\\frac{100}{9802}}\\times\\frac{i}{10} \\rvert0\\rangle+ \sqrt{\\frac{100}{9802}}\\times\\frac{99}{10} \\rvert1\\rangle$ is a valid qubit.")
q3 = prepareQuestion("Make $\\frac{\sqrt{3}}{2}\\rvert0\\rangle+\\frac{1}{3}\\rvert1\\rangle$  a valid qubit",["hint 1","hint 2","hint 3","hint 4","hint 5"], "length = $\sqrt{\\frac{9802}{100}}$  <br>"+
"<font size=\"-1\">Therefore, $\\rvert\psi\\rangle = \sqrt{\\frac{100}{9802}}\\times\\frac{i}{10} \\rvert0\\rangle+ \sqrt{\\frac{100}{9802}}\\times\\frac{99}{10} \\rvert1\\rangle$ is a valid qubit.")
q4 = prepareQuestion("Make $\\frac{1}{2}\\rvert0\\rangle-\\frac{i}{2}\\rvert1\\rangle$  a valid qubit",["hint 1"], "length = $\sqrt{\\frac{1}{2}}$  <br>"+
"<font size=\"-1\">Therefore, $\\rvert\psi\\rangle = \sqrt{2}\\times\\frac{1}{2}\\rvert0\\rangle- \sqrt{2}\\times\\frac{i}{2}\\rvert1\\rangle$is a valid qubit.")
q5 = prepareQuestion("Make $\\frac{\sqrt{3}}{2}\\rvert0\\rangle+\\frac{1}{4}\\rvert1\\rangle$  a valid qubit",["hint 1"], "length = $\sqrt{\\frac{13}{16}}$  <br>"+
"<font size=\"-1\">Therefore, $\\rvert\psi\\rangle = \sqrt{\\frac{16}{13}}\\times\\frac{\sqrt{3}}{2}\\rvert0\\rangle + \sqrt{\\frac{16}{13}}\\times\\frac{1}{4}\\rvert1\\rangle$ is a valid qubit.")


oneneeded = twoneeded = threeneeded = fourneeded = fiveneeded = True

def launchifneeded():
    global oneneeded, twoneeded, threeneeded, fourneeded, fiveneeded
    if (not questionlist[curquestion][1]):
        if(questionlist[curquestion][3]==1 and oneneeded == True):
            oneneeded = False
            makeQuestion(q1, q1onClick)
        elif(questionlist[curquestion][3]==2 and twoneeded == True):
            twoneeded = False
            makeQuestion(q2, q2onClick)
        elif(questionlist[curquestion][3]==3 and threeneeded == True):
            threeneeded = False
            makeQuestion(q3, q3onClick)
        elif(questionlist[curquestion][3]==4 and fourneeded == True):
            fourneeded = False
            makeQuestion(q4, q4onClick)
        elif(questionlist[curquestion][3]==5 and fiveneeded == True):
            fiveneeded = False
            makeQuestion(q5, q5onClick)

"""
Accordion code
"""
solutionquestion = widgets.HTMLMath(value="<font size=\"+2\">Is this a valid qubit?")
workedout = VBox([
    solutionquestion,
    Label(),
    Label(),
    VBox([HBox([VBox([qsolution])])],layout=Layout(align_items='center')),
    Label(),
    Label(),
    Label(),
    VBox([HBox([btn_back],layout=Layout(width="100%",align_items = "center"))],layout=Layout(width="100%",align_items='center'))
])

accordion = widgets.Accordion(children=[exercise1, workedout, ])
accordion.set_title(0, 'Exercise 1')
accordion.set_title(1, 'Exercise 1 (solutions)')

#accordion.set_title(2, 'Exercise 2')

form_items = [
    VBox([Label(),widgets.HTML(value="<font size=\"+2\">Complete the exercises.</font>"),Label()],layout=Layout(align_items='center')),
    HBox([widgets.HTML(value="", layout=Layout(width='15%')),widgets.HTML(value="", layout=Layout(width='70%'))],layout=Layout(align_items='stretch')),
    VBox([Label(),accordion],layout=Layout(align_items='stretch',width='100%')),
]

SAQuiz10_3 = VBox(form_items, layout=Layout(
    display='flex',
    flex_flow='column',
    border='solid 1px',
    align_items='stretch',
    width='100%'
))

"""
Exercise 2 Logic
"""

def restart_2(btn):
    global numCorrect, curquestion
    probstatment.value="<font size=\"+2\">Is this a valid qubit?"
    btn_solution.disabled = True
    clearbtns()
    numCorrect = 0
    curquestion = 0
    refreshq()
    clearcheck()
    hideSolution()

def clearcheck():
    btn_2_check.description = 'Check '+ makeEnd()
    btn_2_check.disabled = True
    btn_2_check.icon = "check"
    btn_2_check.button_style = "success"

def checkAnswers_2(btn):
    global numCorrect
    if(btn_yes.disabled==True):
        #clicking next question
        hideSolution()
        btn_solution.disabled = True
        clearbtns()
        probstatment.value="<font size=\"+2\">Is this a valid qubit?"
        clearcheck()
        #curquestion+=1
        nextq()
    else:
        #clicking check answer
        launchifneeded()
        makeSolution()
        btn_solution.disabled=False
        if(questionlist[curquestion][1] == (btn_yes.style.button_color == color)):

            numCorrect += 1

            probstatment.value = "<font size=\"+2\">Correct!"
            btn_2_check.description = "Next Question"
            btn_2_check.icon="star"

            if(questionlist[curquestion][1]):
                clearbtn(btn_yes)
                btn_yes.button_style = 'success'
            else:
                clearbtn(btn_no)
                btn_no.button_style = 'success'
        else:
            probstatment.value = "<font size=\"+2\">Incorrect"
            btn_2_check.description = "Next Question"
            btn_2_check.button_style = "danger"
            btn_2_check.icon = "times"
            if(not questionlist[curquestion][1]):
                clearbtn(btn_yes)
                btn_yes.button_style = 'danger'
            else:
                clearbtn(btn_no)
                btn_no.button_style = 'danger'
        disablebtns()
        if(curquestion+1==qcount):
            btn_2_check.disabled=True
            btn_2_check.description = "Complete"
            disablebtns()
            accordion.set_title(2, 'Exercise 2')
            probstatment.value="<font size=\"+1\"> You got "+str(numCorrect)+ " out of "+ str(qcount)+" correct."
def clearbtn(btn):
    btn.icon = ""
    btn.button_style=''
    btn.style.button_color = None
    btn.disabled = False

def clearbtns():
    clearbtn(btn_yes)
    clearbtn(btn_no)
def disablebtns():
    btn_yes.disabled=True
    btn_no.disabled=True
def answerpress(btn):
    clearbtns()
    btn_2_check.disabled=False
    btn.style.button_color = color

def showSolution(btn):
    accordion.selected_index = 1

def goBack(btn):
    accordion.selected_index = 0

btn_2_check.on_click(checkAnswers_2)
btn_2_restart.on_click(restart_2)
btn_yes.on_click(answerpress)
btn_no.on_click(answerpress)
btn_solution.on_click(showSolution)
btn_back.on_click(goBack)
def createQuiz10_1 ():
    hideSolution()
    refreshq()
    display(SAQuiz10_3)
    display(widgets.HTMLMath(value="<b><font size=\"+2\">Exercise 2"))
    display(widgets.HTMLMath(value="<font size=\"+1\">For each non-valid qubit, re-normalize the coefficients to convert them into valid qubits."))
    display(Label())
