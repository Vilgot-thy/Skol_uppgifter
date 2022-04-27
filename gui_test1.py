#DEL1 import
import psutil
import PySimpleGUI as sg

sg.theme('DarkTeal')

red_x_base64 = b'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'

red_x_base64 = sg.red_x
def main():
    #DEL2 Layout
    layout1 = [[sg.Push(), sg.Text('stuff'), sg.Push(), sg.Button ('', image_data=red_x_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0, key='Exit'), ],
            [sg.Button('pc Status', key='Pc_status'), sg.Button ('Minniräknare', key='Minniräknare')],
            [sg.Button('?', key='?'), sg.Button('Black Jack', key='Black_Jack')]
    ]



    #DEL3 Window
    window = sg.Window('PSG System Dashbord', layout1, no_titlebar=True, alpha_channel=1, grab_anywhere=True, resizable=True)

    #DEL4 Eventloops

    while True:
        event, values = window.read()
        print(event, values)

        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'Pc_status':
            window.close()
            Pc_status()
        elif event == 'Minniräknare':
            window.close()
            Minniräknaree()
        elif event == 'Black_Jack':
            window.close()
            Black_Jack()
            

    
    #DEL5 Window.close
    window.close()

def Pc_status():
    #DEL2 Layout
    layout1 = [[sg.Push(), sg.Text('new'), sg.Push(), sg.Button ('', image_data=red_x_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0, key='Exit'), ],
            [],
            []
    ]

    #DEL3 Window
    window = sg.Window('PSG System Dashbord', layout1, no_titlebar=True, alpha_channel=1, grab_anywhere=True, resizable=True)

#DEL4 Eventloops
    while True:
        event, values = window.read()
        print(event, values)

        if event == 'Exit' or event == sg.WIN_CLOSED:
            main()
            break
    
    #DEL5 Window.close
    window.close()

def Minniräknaree():
    #DEL2 Layout
    layout = [[sg.Push(), sg.Text('new'), sg.Push(), sg.Button ('', image_data=red_x_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0, key='Exit'), ],
          [sg.Txt(''  * 10)],                      
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='input')],
          [sg.Txt(''  * 10)],
          [sg.ReadFormButton('('), sg.ReadFormButton(')'), sg.ReadFormButton('c'), sg.ReadFormButton('«')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('÷')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('x')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
    ]

    #DEL3 Window
    form = sg.FlexForm('13411_CALCULATOR', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
    form.Layout(layout)

    Equal = ''
    List_Op_Error =  ['+','-','*','/','(']

#DEL4 Eventloops
    while True:
        event, values = form.read()
        print(event, values)

        button, values = form.Read()  
        # Press Button
        if button is 'c':
            Equal = ''
            form.find_element('input').Update(Equal)
        elif button is '«':
            Equal = Equal[:-1]
            form.find_element('input').Update(Equal)
        elif len(Equal) == 16 :
            pass
        elif str(button) in '1234567890+-().':
            Equal += str(button)
            form.find_element('input').Update(Equal) 
        elif button is 'x':
            Equal += '*'
            form.find_element('input').Update(Equal)
        elif button is '÷':
            Equal += '/'
            form.find_element('input').Update(Equal)
        
    # Process Conditional
        elif button is '=':
            # Error Case
            for i in List_Op_Error :  
                if '*' is Equal[0] or '/' is Equal[0] or ')' is Equal[0]  or i is Equal[-1]:   # Check Error Case
                    Answer = "Error Operation" 
                    break
                elif Equal == '6001012630187':
                    Answer = 'Apisit.Khomcharoen'
                    break
                elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                    Answer = "Error Operation" 
                    break
                elif '(' in Equal :
                    if ')' not in Equal :
                        Answer = "Error Operation" 
                        break   
                elif '(' not in Equal:
                    if ')' in Equal:
                        Answer = "Error Operation" 
                        break
        # Calculate Case    
            else :
                Answer = str("%0.2f" %(eval(Equal)))                         # eval(Equal)  
                if '.0' in Answer:
                    Answer = str(int(float(Answer)))                         # convert float to int
            form.FindElement('input').Update(Answer)                         # Update to GUI
            Equal = Answer

        elif event == 'Exit' or event == sg.WIN_CLOSED:
            main()
            break
    
    #DEL5 Window.close
    form.close()

def Black_Jack():
    #DEL2 Layout
    layout1 = [[sg.Push(), sg.Text('new'), sg.Push(), sg.Button ('', image_data=red_x_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()),border_width=0, key='Exit'), ],
            [],
            []
    ]

    #DEL3 Window
    window = sg.Window('PSG System Dashbord', layout1, no_titlebar=True, alpha_channel=1, grab_anywhere=True, resizable=True)

#DEL4 Eventloops
    while True:
        event, values = window.read()
        print(event, values)

        if event == 'Exit' or event == sg.WIN_CLOSED:
            main()
            break
    
    #DEL5 Window.close
    window.close()

if __name__ == '__main__':
    main()