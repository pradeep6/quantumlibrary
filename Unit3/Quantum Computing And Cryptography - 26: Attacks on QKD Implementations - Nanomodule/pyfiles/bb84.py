from ipywidgets import Layout, Button, Box, widgets, VBox, HBox, interact, Label
import random, cmath, math
from helpermethods import makeButton
import time
import ipywidgets as widgets
from helpermethods import notfound
border = Layout(border='solid 1px',width="100%")
heightcell = Layout(height='14.2857%')
hiddenrow = Layout(visibility='hidden',height='14.2857%')
cell = Layout(
    display='flex',
    #flex_flow='column',
    border='solid 1.5px',
    align_items='center',
    width='9.375%'
)

btn1 = Layout(
    display='flex',
    #flex_flow='column',
    #border='solid 1.5px',
    align_items='center',
    width='90%',
    height = '100%',
    fontsize='30px'
)

heading = Layout(
    display='flex',
    #flex_flow='column',
    border='solid 1.5px',
    align_items='center',
    width='25%'
)
heading2 = Layout(
    display='flex',
    #flex_flow='column',
    border='solid 1.5px',
    align_items='center',
    width='75%'
)

def defaultBtn(btn):
    btn.style.font_weight = '1000'

one= VBox([widgets.HTML(value="<font size=\"+1\"> 1")],layout=cell)


file1 = open("pyfiles/images/aup.PNG", "rb")
aup = file1.read()
file2 = open("pyfiles/images/aright.PNG", "rb")
aright = file2.read()
file3 = open("pyfiles/images/aupleft.PNG", "rb")
aupleft = file3.read()
file4 = open("pyfiles/images/aupright.PNG", "rb")
aupright = file4.read()
#file5 = open("pyfiles/images/giftest.gif", "rb")
file5 = open("pyfiles/images/ulx.PNG", "rb")
#tempimg = file5.read()
ulx = file5.read()
file6 = open("pyfiles/images/ult.PNG", "rb")
ult = file6.read()
file7 = open("pyfiles/images/ux.PNG", "rb")
ux = file7.read()
file8 = open("pyfiles/images/ut.PNG", "rb")
ut = file8.read()
file9 = open("pyfiles/images/urx.PNG", "rb")
urx = file9.read()
file10 = open("pyfiles/images/urt.PNG", "rb")
urt = file10.read()
file11 = open("pyfiles/images/lx.PNG", "rb")
lx = file11.read()
file12 = open("pyfiles/images/lt.PNG", "rb")
lt = file12.read()

#arr = os.listdir()
#print(arr)
rone = []
ronehelp = []
rtwo = []
rtwohelp = []
rthree = []
rthreehelp = []
rfour = []
rfourhelp = []
rfive = []
rfivehelp = []
rsix = []
rsixhelp = []
rseven = []
rsevenhelp = []
def randomrone(btn):
    for i in range(8):
        ronehelp[i].description = "" + str(random.randint(0,1))
    makerone()
    checkpolar()
    takemesurment()
    resetbtn()

def swapChoice(btn):
    if(btn.description=="1"):
        btn.description="0"
    elif(btn.description=="0"):
        btn.description="1"
    elif(btn.icon=='times'):
        btn.icon='plus'
    elif(btn.icon=='plus'):
        btn.icon='times'
    checkpolar()

    takemesurment()
def swapChoice2(btn):
    if(btn.description=="1"):
        btn.description="?"
    elif(btn.description=="0"):
        btn.description="1"
    elif(btn.description==" "):
        btn.description="0"
    elif(btn.description=="?"):
        btn.description="0"
def createrone():
    ronehelp.clear()
    for i in range(8):
        temp=widgets.Button(description="0",layout=btn1)
        defaultBtn(temp)
        ronehelp.append(temp)
        ronehelp[i].on_click(swapChoice)
    makerone()
def createrseven():
    rsevenhelp.clear()
    for i in range(8):
        temp=widgets.Button(description=" ",layout=btn1)
        defaultBtn(temp)
        rsevenhelp.append(temp)
        rsevenhelp[i].on_click(swapChoice2)
    makerseven()

def makerone():
    rone.clear()
    for i in range(8):
        rone.append(VBox([ronehelp[i]],layout=cell))
def makerseven():
    rseven.clear()
    for i in range(8):
        rseven.append(VBox([rsevenhelp[i]],layout=cell))
def makersix():
    rsix.clear()
    for i in range(8):
        rsix.append(VBox([Label()],layout=cell))
def randomrtwo(btn):
    foo=['times','plus']
    for i in range(8):
        rtwohelp[i].icon = "" + str(random.choice(foo))
    makertwo()
    checkpolar()
    takemesurment()
    resetbtn()
def creatertwo():
    rtwohelp.clear()
    for i in range(8):
        rtwohelp.append(widgets.Button(description="",icon='plus',layout=btn1))
        rtwohelp[i].on_click(swapChoice)
    makertwo()
def randomrfour(btn):

    foo=['times','plus']
    for i in range(8):
        rfourhelp[i].icon = "" + str(random.choice(foo))
    makerfour()
    checkpolar()
    takemesurment()
    resetbtn()
def createrfour():
    rfourhelp.clear()
    for i in range(8):
        rfourhelp.append(widgets.Button(description="",icon='plus',layout=btn1))
        rfourhelp[i].on_click(swapChoice)
    makerfour()
def createrthree():
    for i in range(8):
        rthreehelp.append(widgets.Image(
    value=aup,
    format='png',
    width=30,
    height=30,
    ))
        #rtwohelp[i].on_click(swapChoice)
    makerthree()
def createrfive():
    for i in range(8):
        rfivehelp.append(widgets.Image(
    value=aup,
    format='png',
    width=30,
    height=30,
    ))

    makerfive()


def makertwo():
    rtwo.clear()
    for i in range(8):
        rtwo.append(VBox([rtwohelp[i]],layout=cell))
def makerfour():
    rfour.clear()
    for i in range(8):
        rfour.append(VBox([rfourhelp[i]],layout=cell))

def makerthree():
    rthree.clear()
    for i in range(8):
        rthree.append(VBox([rthreehelp[i]],layout=cell))

def makerfive():
    rfive.clear()
    for i in range(8):
        rfive.append(VBox([rfivehelp[i]],layout=cell))


def checkpolar():
    for i in range(8):
        if (rtwohelp[i].icon == "plus"):
            if(ronehelp[i].description == "0"):
                rthreehelp[i].value=aup
            else:
                rthreehelp[i].value=aright
        else:
            if(ronehelp[i].description == "0"):
                rthreehelp[i].value=aupright
            else:
                rthreehelp[i].value=aupleft


def takemesurment():
    for i in range(8):
        if (rfourhelp[i].icon == "plus"):
            if(rthreehelp[i].value == aup):
                rfivehelp[i].value=aup
            else:
                rfivehelp[i].value=aright
        else:
            if(rthreehelp[i].value == aupleft):
                rfivehelp[i].value=aupleft
            else:
                rfivehelp[i].value=aupright
def checkKey(i):

    if rsevenhelp[i].description == " ":
        return 2
    if(rtwohelp[i].icon == rfourhelp[i].icon):
        if rsevenhelp[i].description == ronehelp[i].description:
            return 1
        else:
            return 0
    else:
        if rsevenhelp[i].description == "?":
            return 1
        else:
            return 0

def testbutton(btn):
    print(checkKey(2))
def reset(btn):
    slider.value = 0
    for i in range (8):
        ronehelp[i].description="0"
        rtwohelp[i].icon="plus"
        rfourhelp[i].icon="plus"
        rsevenhelp[i].description = " "
        rsevenhelp[i].button_style=""
        enablerow(i)
    checkpolar()
    takemesurment()
    btnrtwo.disabled = False
    btnrone.disabled = False
    btnrfour.disabled = False
    checkanswers.disabled = False
    clearcolor()
    resetbtn()
def randomAll(btn):
    reset("lol")
    resetbtn()
    randomrone("not actually a button <3")
    randomrtwo("not actually a button <3")
    randomrfour("not actually a button <3")

play = widgets.Play(
    interval=1000,
    value=0,
    min=0,
    max=8,
    description="Press play",
)
slider = widgets.IntSlider(
    value=0,
    min=0,
    max=8,
    step=1,
    continuous_update=True,
    disabled=True
)

discuss = widgets.HTML(value="<font size=\"+1\">Alice and Bob compare basis")

widgets.jslink((play, 'value'), (slider, 'value'))
playbox = widgets.HBox([Label(layout=Layout(width="19%")),play, slider],layout=Layout(align_items='center'))
def createTable():
    createrone()
    creatertwo()
    createrthree()
    createrfour()
    createrfive()
    makersix()
    createrseven()
    row1 = HBox([HBox([VBox([widgets.HTML(value="<font size=\"+1\">Alice's bit")],layout=heading),rone[0],rone[1],rone[2],rone[3],rone[4],rone[5],rone[6],rone[7]],layout=border),])
    row2 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Alice's basis")],layout=heading),rtwo[0],rtwo[1],rtwo[2],rtwo[3],rtwo[4],rtwo[5],rtwo[6],rtwo[7]],layout=border)
    row3 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Alice's polarization")],layout=heading),rthree[0],rthree[1],rthree[2],rthree[3],rthree[4],rthree[5],rthree[6],rthree[7]],layout=border)
    #row1 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Alice's bit")],layout=heading),rone[0],rone[1],rone[2],rone[3],rone[4],rone[5],rone[6],rone[7]],layout=border)
    row4 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Bob's basis")],layout=heading),rfour[0],rfour[1],rfour[2],rfour[3],rfour[4],rfour[5],rfour[6],rfour[7]],layout=border)
    row5 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Bob's measurement")],layout=heading),rfive[0],rfive[1],rfive[2],rfive[3],rfive[4],rfive[5],rfive[6],rfive[7]],layout=border)
    row6 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Public discussion")],layout=heading),VBox([widgets.HTML(value="<font size=\"+1\"><b>Alice and Bob Compare Basis")],layout=heading2)],layout=border)
    row7 = HBox([VBox([widgets.HTML(value="<font size=\"+1\">Secret key")],layout=heading),rseven[0],rseven[1],rseven[2],rseven[3],rseven[4],rseven[5],rseven[6],rseven[7]],layout=border)
    bb84box = HBox([VBox([row1,row2,row3,row4,row5,row6,row7],layout=Layout(
        display='flex',
        #flex_flow='column',
        border='solid 1.5px',
        align_items='stretch',
        width='75%'
    )),Label(layout=Layout(width='5%')),VBox([btnrone,btnrtwo,placeholders,btnrfour,placeholders,placeholders,checkanswers],layout = Layout(height='center'))])
    display(curimg)
    display (bb84box)
    display (playbox)

    display(buttonbox)



checkCorrect = widgets.Valid(value=False,readout="Incorrect",layout=hiddenrow)

#Animation
curimg = widgets.Image(
    value=ux,
    format='gif',
    width="70%",
    height = "20%"
    )





#Buttons!



checkanswers = widgets.Button(
            description='Check Answers',
            #disabled=False,
            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Check Answers!',
            icon='check',
            #height = '100px'
            layout=heightcell

        )
checkanswers.style.font_weight = '1000'
def makeRandomBtn():
    temp= widgets.Button(
                description='Randomise Row',
                #disabled=False,
                button_style='', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Random!',
                icon='',
                #height = '100px'
                layout=heightcell

            )
    temp.style.font_weight = '600'
    temp.style.button_color ='#D7BDE2'

    return temp

botbtn = Layout(width = "50%",height="50px")
restartbtn = widgets.Button(
                description='Restart',
                #disabled=False,
                button_style='', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Restart!',
                icon='',
                height = '75px',
                layout=botbtn

            )
randombtn = widgets.Button(
                description='Randomise All',
                #disabled=False,
                button_style='', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Randomise All!',
                icon='',
                height = '75px',
                #height = '100px'
                layout=botbtn

            )
randombtn.style.button_color ='#8E44AD'
randombtn.style.font_weight = '1000'
restartbtn.style.font_weight = '1000'
restartbtn.style.button_color ='#EC7063'
slider.style.handle_color = '#21618C'
buttonbox = widgets.HBox([restartbtn,Label(layout=Layout(width="1%")), randombtn],layout=Layout(
    display='flex',
    #flex_flow='column',
    align_items='stretch',
    width='75%'
))


btnrone = makeRandomBtn()
btnrtwo = makeRandomBtn()
btnrfour = makeRandomBtn()

placeholders= Label(layout=heightcell)



def disablerow(row):
    rsevenhelp[row].disabled = True
    ronehelp[row].disabled = True
    rtwohelp[row].disabled = True
    rfourhelp[row].disabled = True
    btnrone.disabled = True
    btnrtwo.disabled = True
    btnrfour.disabled = True
    checkanswers.disabled = True
def enablerow(row):
    rsevenhelp[row].disabled = False
    ronehelp[row].disabled = False
    rtwohelp[row].disabled = False
    rfourhelp[row].disabled = False
def wasChange(change):
    imagerow(change['new']-1)
    checkall(checkanswers)
def clearcolor():
    ronehelp[0].button_style=''
    ronehelp[1].button_style=''
    ronehelp[2].button_style=''
    ronehelp[3].button_style=''
    ronehelp[4].button_style=''
    ronehelp[5].button_style=''
    ronehelp[6].button_style=''
    ronehelp[7].button_style=''
    rtwohelp[0].button_style=''
    rtwohelp[1].button_style=''
    rtwohelp[2].button_style=''
    rtwohelp[3].button_style=''
    rtwohelp[4].button_style=''
    rtwohelp[5].button_style=''
    rtwohelp[6].button_style=''
    rtwohelp[7].button_style=''
    rfourhelp[0].button_style=''
    rfourhelp[1].button_style=''
    rfourhelp[2].button_style=''
    rfourhelp[3].button_style=''
    rfourhelp[4].button_style=''
    rfourhelp[5].button_style=''
    rfourhelp[6].button_style=''
    rfourhelp[7].button_style=''

def imagerow(row):
    clearcolor()
    ronehelp[row].button_style='info'
    rtwohelp[row].button_style='info'
    rfourhelp[row].button_style='info'


    if(rfourhelp[row].icon == "times"):
        if (rtwohelp[row].icon == "plus"):
            if(ronehelp[row].description == "0"):
                curimg.value = ux
            else:
                curimg.value = lx
        else:
            if(ronehelp[row].description == "0"):
                curimg.value =urx
            else:
                curimg.value =ulx
    else:
        if (rtwohelp[row].icon == "plus"):
            if(ronehelp[row].description == "0"):
                curimg.value = ut
            else:
                curimg.value = lt
        else:
            if(ronehelp[row].description == "0"):
                curimg.value =urt
            else:
                curimg.value =ult
def resetbtn():
    for i in range(8):
        rsevenhelp[i].button_style=''
        rsevenhelp[i].description=" "

    checkanswers.button_style='success'
    checkanswers.description='Check Answers'
    checkanswers.icon="check"

def checkall(btn):
    count = 0
    for i in range(8):
        if checkKey(i) == True:
            count +=1
            rsevenhelp[i].button_style= "success"
        elif checkKey(i) == 2:
            rsevenhelp[i].button_style= "warning"
            count -=10
        else:
            rsevenhelp[i].button_style= "danger"
    if count < 0:
        btn.description= "Answer Missing"
        btn.icon='times'
        btn.button_style=''
    elif count == 8:
        btn.description= "Great Job!"
        btn.button_style='info'
        btn.icon='check'
    elif count > 5:
        btn.description= "Close!"
        btn.button_style='warning'
        btn.icon='check'
    else:
        btn.description= "Not Quite!"
        btn.button_style='danger'
        btn.icon='times'

slider.observe(wasChange,'value')
btnrone.on_click(randomrone)
btnrtwo.on_click(randomrtwo)
btnrfour.on_click(randomrfour)
randombtn.on_click(randomAll)
restartbtn.on_click(reset)
checkanswers.on_click(checkall)
