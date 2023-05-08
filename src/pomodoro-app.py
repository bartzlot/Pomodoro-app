import PySimpleGUI as sg
import time
from pomodoro_modules import (  hours_validation,
                                minutes_validation,
                                )
from pomodoro_view import TimerMenu

tm = TimerMenu()
tm.start_timer_menu()


# sg.theme('DarkAmber')   # Add a touch of color
# hour = 0
# min = 0
# sec = 0
# temp = 0
# layout = [  [sg.Text("Ilość godzin:"), sg.Button('+', key='Hp'), sg.Input(str(hour),key='HOURS'), sg.Button('-', key='Hm')],
#             [sg.Text("Ilość minut:"), sg.Button('+', key='Mp'), sg.Input(str(hour),key='MINUTES'), sg.Button('-', key='Mm')],
#             [sg.Text("Ilość sekund:"), sg.Button('+', key='Sp'), sg.Input(str(hour),key='SECONDS'), sg.Button('-', key='Sm')],
#             [sg.Button('START SESSION')],
#             [sg.Text(str(temp), key='TIMER')]
#         ]

# # Create the Window
# window = sg.Window('Pomodoro-App', layout)
# # Event Loop to process "events" and get the "values" of the inputs

# while True:
#     event, values = window.read(timeout=10)
    
#     if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
#         break

#     if event == 'Hp':
#         hour += 1
#         hour = hours_validation(hour)
#         window['HOURS'].update(value=str(hour))
        
#     if event == 'Hm':
#         hour -= 1sss
#         hour = hours_validation(hour)
#         window['HOURS'].update(value=str(hour))

#     if event == 'Mm':
#         min -= 1
#         min = minutes_validation(min)
#         window['MINUTES'].update(value=str(min))

#     if event == 'Mp':
#         min += 1
#         min = minutes_validation(min)
#         window['MINUTES'].update(value=str(min))

#     if event == 'Sm':
#         sec -= 1
#         sec = minutes_validation(sec)
#         window['SECONDS'].update(value=str(sec))

#     if event == 'Sp':
#         sec += 1
#         sec = minutes_validation(sec)
#         window['SECONDS'].update(value=str(sec))
#     if event == 'START SESSION':
#         layout1 = [[sg.Text('', justification='center', key='timer')]]
#         window = sg.Window('Timer', layout1)
#         t = 0
#         while True:
#             event, values = window.read(timeout=0)
#             window['timer'].update(str(t))
#             time.sleep(1)
#             t+=1


# window.close()