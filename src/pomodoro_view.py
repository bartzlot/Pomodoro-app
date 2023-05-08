import PySimpleGUI as sg
import time
from pomodoro_modules import(  hours_validation,
                                minutes_validation,
                             )
class TimerMenu:
    hour = 0
    min = 0
    sec = 0
    sg.theme('DarkAmber') 
    layout = [  [sg.Text("Ilość godzin:"), sg.Button('+', key='Hp'), sg.Input(str(hour),key='HOURS'), sg.Button('-', key='Hm')],
            [sg.Text("Ilość minut:"), sg.Button('+', key='Mp'), sg.Input(str(hour),key='MINUTES'), sg.Button('-', key='Mm')],
            [sg.Text("Ilość sekund:"), sg.Button('+', key='Sp'), sg.Input(str(hour),key='SECONDS'), sg.Button('-', key='Sm')],
            [sg.Button('START SESSION')],
            ]
    
    
    def start_timer_menu(self):
        
        # Create the Windowss
        window = sg.Window('Pomodoro-App', self.layout)
        # Event Loop to process "events" and get the "values" of the inputs

        while True:
            event, values = window.read(timeout=10)
            
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break

            if event == 'Hp':
                self.hour += 1
                # hour = hours_validation(hour)
                window['HOURS'].update(value=str(self.hour))
                
            if event == 'Hm':
                self.hour -= 1
                # hour = hours_validation(hour)
                window['HOURS'].update(value=str(self.hour))

            if event == 'Mm':
                self.min -= 1
                # min = minutes_validation(min)
                window['MINUTES'].update(value=str(self.min))

            if event == 'Mp':
                self.min += 1
                # min = minutes_validation(min)
                window['MINUTES'].update(value=str(self.min))

            if event == 'Sm':
                self.sec -= 1
                # sec = minutes_validation(sec)
                window['SECONDS'].update(value=str(self.sec))

            if event == 'Sp':
                self.sec += 1
                # sec = minutes_validation(sec)
                window['SECONDS'].update(value=str(self.sec))
            if event == 'START SESSION':
                layout1 = [[sg.Text('', justification='center', key='timer')]]
                window = sg.Window('Timer', layout1)
                t = 0
                while True:
                    event, values = window.read(timeout=0)
                    window['timer'].update(str(t))
                    time.sleep(1)
                    t+=1


        window.close()