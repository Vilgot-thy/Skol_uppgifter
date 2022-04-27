import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')

sg.set_options (font = 'Franklin 14')

b_s = (6,3)

layout = [
# Alternativ 1 för första raden
# [sg.Text ('Output', font = 'Frankling 26', justification = 'right', expand_x= True)], 
# Alternativ 2 för första raden
    [sg.Push(), sg.Text ('Output', font = 'Frankling 26', pad = (10,20))],  
    [sg.Button ('Clear', expand_x =True), sg.Button('Enter', expand_x =True)],
    [sg.Button ('7', size = b_s), sg.Button ('8', size = b_s), sg.Button ('9', size = b_s ), sg.Button ('*',  size = b_s)],
    [sg.Button ('4', size = b_s), sg.Button ('5', size = b_s), sg.Button ('6', size = b_s), sg.Button ('/', size = b_s)],
    [sg.Button ('1', size = b_s), sg.Button ('2', size = b_s), sg.Button ('3', size = b_s), sg.Button ('-', size = b_s)],
    [sg.Button ('0', expand_x =True), sg.Button ('.', size = b_s), sg.Button ('+', size = b_s)],
    
         ]


window = sg.Window ('Miniräknare', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
window.close()

