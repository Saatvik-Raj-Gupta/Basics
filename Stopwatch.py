import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    layout = [
        #[sg.Push(), sg.Image(''), pad=0, enable_events = True,key='x'],
        [sg.VPush()],
        [sg.Text('', font = 'Young 50', key='Time')],
        [sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width=0, key='S'), sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width=0, key='L', visible = False)],
        [sg.Column([[]], key = 'LAPS')],
        [sg.VPush()]
        ]

    return sg.Window(
        'Stopwatch',
        layout,
        size = (300, 300),
        no_titlebar = True,
        element_justification = 'center')

window = create_window()  
start_time = 0
active = False
lap_amount = 1
while True:
    event, values = window.read(timeout = 10)
    if event == sg.WIN_CLOSED:
        break


    if event == 'S':
        if active:
            active = False
            window['S'].update('Reset')
            window['L'].update(visible = False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            else:
                start_time = time()
                active = True
                window['S'].update('Stop')
                window['L'].update(visible = True)  


    if active:
        elapsed_time = round(time() - start_time, 1)
        window['Time'].update(elapsed_time)

    if event == 'L':
        window.extend_layout(window['LAPS'], [[sg.Text(lap_amount), sg.VSeperator(), sg.Text(elapsed_time)]])
        lap_amount += 1

window.close()
