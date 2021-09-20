from typing import Text
import PySimpleGUI as gui
import random

val = int(0)
cps = int(0)

layout = [[gui.Button("Start")],[gui.Text(str(val), key='count')],[gui.InputText("1", key='min')],[gui.InputText("100", key='max')]]
window = gui.Window("Random Number Generator", layout, margins=(100, 50))
while True:
    event, values = window.read()
    if event == "Start":
        val = random.randint(int(values['min']) ,int(values['max']))
        window['count'].update(str(val))
    if event == gui.WIN_CLOSED:
        break
