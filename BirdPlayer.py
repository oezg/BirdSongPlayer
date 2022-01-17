import PySimpleGUI as sg
from playsound import playsound

layout = [
    [sg.Text("House Sparrow"), sg.Button("Play")],
    [sg.Button("Close")],
]

window = sg.Window('Bird Song PLayer', layout)

while True:
    event, values = window.read()
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    if event == "Play":
        playsound("./HouseSparrow.mp3")

        

window.close()
