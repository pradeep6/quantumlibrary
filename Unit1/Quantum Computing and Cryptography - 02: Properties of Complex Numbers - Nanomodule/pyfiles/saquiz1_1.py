from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath
#Layouts
numInputLayout=Layout(
    width='55px'
)
strInputLayout=Layout(
    width='90px'
)


hidden = Layout(visibility='hidden')
visible = Layout(visibility='visible')
QValid1_1=widgets.Valid(value=False,readout="Incorrect",layout=hidden)
QValid1_2=widgets.Valid(value=False,readout="Incorrect",layout=hidden)

QButtons1_1 = widgets.RadioButtons(
                options=['a. x=5i', 'b. x=-5i', 'c. x=i','d. x=5'],
                #value='pineapple',
                description='',
                disabled=False
            )
QDropdown1_2 = widgets.Dropdown(
                    options={'1': 1, '-1': 2, ' i': 3, '-i' : 4},
                    value=1,
                    description='----->',
                )

Qbtn_1 = widgets.Button(
            description='Check Answers',
            disabled=False,
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Check Answers',
            icon='check'
        )


SAQuiz1_1 = VBox([
    widgets.HTML(value="<b><font size=\"+2\">Quiz 1.1 Self Assessment Quiz"),
    widgets.HTML(value="<b><font size=\"-1\"<b>Maybe used for in-class hands-on practice.</b>"),
    widgets.HTMLMath(value="<font size=\"+0\">1. Solve for $x$ where $x^2+25=0$. Choose the right answer:"),
    HBox([QButtons1_1,QValid1_1]),
    widgets.HTMLMath(value="<font size=\"+0\">2. Simplify $i^{225}$. (Hint: find a pattern)"),
     HBox([QDropdown1_2,QValid1_2]),
     VBox([HBox([Qbtn_1])],layout=Layout(align_items='center'))

])
def QCheckAnswers_1(btn):
    count = 0
    if(QButtons1_1.value[0] == 'a'):
        QValid1_1.value=True
        QValid1_1.readout="Correct"
        count +=1
    else:
        QValid1_1.value=False
        QValid1_1.readout="Incorrect"
    if(QDropdown1_2.value == 3):
        QValid1_2.value=True
        QValid1_2.readout="Correct"
        count +=1
    else:
        QValid1_2.value=False
        QValid1_2.readout="Incorrect"
    if(count == 2):
        Qbtn_1.button_style='info'
        Qbtn_1.description='Way to Go!'
        Qbtn_1.icon='check'
    if(count == 1):
        Qbtn_1.button_style='warning'
        Qbtn_1.icon='times'
        Qbtn_1.description='Close!'
    if(count == 0):
        Qbtn_1.button_style='danger'
        Qbtn_1.icon='times'
        Qbtn_1.description='Try Again'
    QValid1_1.layout=visible
    QValid1_2.layout=visible
    Qbtn_1.icon
Qbtn_1.on_click(QCheckAnswers_1)
