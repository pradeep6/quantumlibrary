"""
This is an example of a self quiz thing. Run the block to generate.
"""
from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath
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
"""
Exercise 1

"""
#questions 1.1
valid_1_1=widgets.Valid(value=False,readout="Incorrect",layout=hidden)

intbox1_1 = widgets.FloatText(layout=numInputLayout)

intbox1_1_2 = widgets.FloatText(layout=numInputLayout)

exercise1_1=HBox([
    widgets.HTML(value="<font size=\"+1\">&emsp;&emsp;(-8 +"),
    intbox1_1,
    widgets.HTML(value="<font size=\"+1\">i) + ("),
    intbox1_1_2,
    widgets.HTML(value="<font size=\"+1\"> + i) = (4 - 7i)"),
    valid_1_1

])

#question 1.2
valid_1_2=widgets.Valid(value=False,readout="Incorrect",layout=hidden)

intbox1_2 = widgets.FloatText(layout=numInputLayout)

intbox1_2_2 = widgets.FloatText(layout=numInputLayout)

exercise1_2=HBox([
    widgets.HTML(value="<font size=\"+1\">&emsp;&emsp;("),
    intbox1_2,
    widgets.HTML(value="<font size=\"+1\"> + 6i) + -(9 - 3i) = (10 + "),
    intbox1_2_2,
    widgets.HTML(value="<font size=\"+1\">i)"),
    valid_1_2

])

#question 1.3
valid_1_3=widgets.Valid(value=False,readout="Incorrect",layout=hidden)

intbox1_3 = widgets.FloatText(layout=numInputLayout)

intbox1_3_2 = widgets.FloatText(layout=numInputLayout)

exercise1_3=HBox([
    widgets.HTML(value="<font size=\"+1\">&emsp;&emsp;( 9 + 6i)(-10 - 2i) = ("),
    intbox1_3,
    widgets.HTML(value="<font size=\"+1\"> + "),
    intbox1_3_2,
    widgets.HTML(value="<font size=\"+1\">i)"),
    valid_1_3
])



#question 1.4
valid_1_4=widgets.Valid(value=False,readout="Incorrect",layout=hidden)
intbox1_4 = widgets.FloatText(layout=numInputLayout)

intbox1_4_2 = widgets.FloatText(layout=numInputLayout)

exercise1_4=HBox([
    widgets.HTML(value="<font size=\"+1\">&emsp;&emsp;( 5 )(4 + 3i) = ("),
    intbox1_4,
    widgets.HTML(value="<font size=\"+1\"> + "),
    intbox1_4_2,
    widgets.HTML(value="<font size=\"+1\">i)"),
    valid_1_4
])

#check answers
btn_1= widgets.Button(
            description='Check Answers',
            disabled=False,
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Check Answers',
            icon='check'

        )

#compile exercise 1
exercise1=VBox([
    widgets.HTML(value="<font size=\"+1\">Make all functions true.</font>"),
    widgets.HTML(value="1 &#10097;"),
    exercise1_1,
    widgets.HTML(value="2 &#10097;"),
    exercise1_2,
    widgets.HTML(value="3 &#10097;"),
    exercise1_3,
    widgets.HTML(value="4 &#10097;"),
    exercise1_4,
    VBox([btn_1],layout=Layout(align_items='center'))
])


"""
Exercise 2

"""
#floatboxes
intbox2_1 = widgets.FloatText(layout=numInputLayout2)

intbox2_2 = widgets.FloatText(layout=numInputLayout2)

#Text
probstatment = widgets.HTML(value="<font size=\"+1\">Solve 5 randomly generated problems in a row.")

#buttons!
btn_2_restart= widgets.Button(
            description='Restart',
            disabled=False,
            button_style='warning', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Don\'t give up :)',

        )
btn_2_check= widgets.Button(
            description='Check 1/5',
            disabled=False,
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Check Answer',
            icon='check'

        )

#exercise2rng
problem =  widgets.HTML(value="<font size=\"+1\">&emsp;&emsp;( 5 )(4 + 3i)")

exercise2rng=HBox([
    problem,
    widgets.HTML(value="<font size=\"+1\"> = ("),
    intbox2_1,
    widgets.HTML(value="<font size=\"+1\"> + "),
    intbox2_2,
    widgets.HTML(value="<font size=\"+1\">i)")
])

#compile exercise 2
exercise2=VBox([
    probstatment,
    Label(),
    exercise2rng,
    Label(),
    VBox([HBox([btn_2_check,Label(),btn_2_restart])],layout=Layout(align_items='center'))
])


"""
Accordion code
"""

accordion = widgets.Accordion(children=[exercise1, exercise2, ])
accordion.set_title(0, 'Exercise 1')
accordion.set_title(1, 'Exercise 2')
accordion.set_title(2, 'Exercise 3')
accordion
form_items = [
    VBox([Label(),widgets.HTML(value="<font size=\"+2\">Complete the exercises.</font>"),Label()],layout=Layout(align_items='center')),
    HBox([widgets.HTML(value="", layout=Layout(width='15%')),widgets.HTML(value="", layout=Layout(width='70%'))],layout=Layout(align_items='stretch')),
    VBox([Label(),accordion],layout=Layout(align_items='stretch',width='100%')),
]

SAQuiz1_3 = VBox(form_items, layout=Layout(
    display='flex',
    flex_flow='column',
    border='solid 1px',
    align_items='stretch',
    width='100%'
))

"""
Exercise 1 Logic
"""

def checkAnswers_1(btn):
    count=0
    if(intbox1_1.value==-8 and intbox1_1_2.value == 12):
        intbox1_1.disabled=True
        intbox1_1_2.disabled=True
        valid_1_1.value=True
        count+=1
    if(intbox1_2.value==19 and intbox1_2_2.value == 9):
        intbox1_2.disabled=True
        intbox1_2_2.disabled=True
        valid_1_2.value=True
        count+=1
    if(intbox1_3.value==-78 and intbox1_3_2.value == -78):
        intbox1_3.disabled=True
        intbox1_3_2.disabled=True
        valid_1_3.value=True
        count+=1
    if(intbox1_4.value==20 and intbox1_4_2.value == 15):
        intbox1_4.disabled=True
        intbox1_4_2.disabled=True
        valid_1_4.value=True
        count+=1
    if count is 4:
        btn_1.button_style='info'
        btn_1.description='Nice Work!'
        accordion.set_title(0, 'Exercise 1 (Completed)')
    else:
        btn_1.button_style='warning'
    valid_1_1.layout=visible
    valid_1_2.layout=visible
    valid_1_3.layout=visible
    valid_1_4.layout=visible

btn_1.on_click(checkAnswers_1)

#slider1_1.observe(handle_slider_change, names='value')

"""
Exercise 2 Logic
"""

def flipCoin():
    return (random.randint(0,1))
def genProblem(btn):
    #problem.value="<font size=\"+1\">&emsp;&emsp;(" + str(random.randint(-15,15)) + " " + str(random.choice('-*+')) +" " + str(random.randint(15)) +"i) "
    problem.value="<font size=\"+1\">&emsp;&emsp;(" + str(random.randint(-15,15)) + " " + random.choice('-+') +" " + str(random.randint(0,15)) +"i) "+ random.choice('-*+') + " (" + str(random.randint(-15,15)) + " " + random.choice('-+') + " " + str(random.randint(0,15)) +"i)"
    #genSumProblem() if flipCoin() is 1 else genProductProblem()
def nextifneeded():
    #print(btn_2_check.description)
    if((btn_2_check.description[6] != "5")):
        btn_2_check.description = "Check " + str(int(btn_2_check.description[6])+1) + "/5"
        genProblem("not a btn")
        intbox2_1.value = 0.0
        intbox2_2.value = 0.0
    else:
        btn_2_check.description ="Complete"
        btn_2_check.disabled=True
        intbox2_1.disabled=True
        intbox2_2.disabled=True
        btn_2_check.button_style='info'

def restart_2(btn):
    btn_2_check.description ="Check 1/5"
    btn_2_check.disabled=False
    intbox2_1.disabled=False
    intbox2_2.disabled=False
    btn_2_check.button_style='success'
    intbox2_1.value = 0.0
    intbox2_2.value = 0.0
    genProblem("not a btn")
    probstatment.value="<font size=\"+1\">Solve 5 randomly generated problems in a row."


def checkAnswers_2(btn):
    formatedproblem=problem.value[29:-1].replace("i","j").replace(" ","")
    questions = formatedproblem.split(")+(")
    while(True):
        if len(questions) == 2:
            answer=(complex(questions[0])+complex(questions[1]))
            break;
        questions = formatedproblem.split(")*(")
        if len(questions) == 2:
            answer=(complex(questions[0])*complex(questions[1]))
            break;
        questions = formatedproblem.split(")-(")
        if len(questions) == 2:
            answer=(complex(questions[0])-complex(questions[1]))
            break;
    if((cmath.isclose(answer.real,intbox2_1.value)) and (cmath.isclose(answer.imag,intbox2_2.value))):
        nextifneeded()
    else:
        btn_2_check.description ="Incorrect :("
        btn_2_check.disabled=True
        intbox2_1.disabled=True
        intbox2_2.disabled=True
        btn_2_check.button_style='danger'
        probstatment.value="<font size=\"+1\"> The correct answer was: ("+str(answer.real) +" + "+ str(answer.imag) + "i)"


btn_2_check.on_click(checkAnswers_2)
btn_2_restart.on_click(restart_2)
#btn_2_check.on_click(checkAnswers_1)


"""
Exercise 3 Logic
"""
genProblem("not a btn")
#checkAnswer()
#launch
