from tkinter import Label
from appJar import gui

# Canvas
app = gui(title="La App del pitufo gruñón", showIcon=False)
app.setBg('LightGrey')
app.setSize("1080x720")
app.setIcon('E:\\Imagenes\\Gif\\Sticking_Out_Tongue.gif')

# Diseño 

app.addEntry("e1", row=1, column=0)
app.addLabelEntry("Name", row=1, column=1)
app.addLabelDirectoryEntry('Pdf Input Directory', row=1, column=2)

'''app.startFrame("LEFT", row=0, column=0)
app.setBg("blue")
app.setSticky("NEW")
app.setStretch("COLUMN")

app.addLabel("LEFT LABEL", "Label on the left 1")
app.setLabelBg("LEFT LABEL", "red")
app.addLabel("LEFT LABEL2", "Label on the left 2")
app.setLabelBg("LEFT LABEL2", "orange")
app.addLabel("LEFT LABEL3", "Label on the left 3")
app.setLabelBg("LEFT LABEL3", "yellow")
app.stopFrame()

app.startFrame("CENTER", row=0, column=1)
app.setBg("green")
app.setFg("white")
for x in range(5):
    app.addRadioButton("RADIO", "Choice " + str(x))
app.stopFrame()

app.startFrame("RIGHT", row=0, column=2)
app.setBg("black")
app.setFg("white")
for z in range(5):
    app.addRadioButton("RADIO2", "Choice " + str(z))
app.stopFrame()
'''

app.go()


