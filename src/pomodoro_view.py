import PySimpleGUI as sg
import time, datetime


class Optionsmenu():

    default_break_time = 5
    default_session_time = 20
    default_big_break_time = 20
    default_big_break_count = 4
    DEFAULTS = [5, 20, 20, 4]
    sg.theme('DarkAmber')
    
    def start_options_window(self):
        options_layout = [[[sg.Text("Default session time(min):"), sg.Button('+', key='DSTP'), sg.Input(self.default_session_time,key='DST'), sg.Button('-', key='DSTM')]],
                            [[sg.Text("Default break time(min):"), sg.Button('+', key='DBTP'), sg.Input(self.default_break_time,key='DBT'), sg.Button('-', key='DBTM')]],
                            [[sg.Text("Default big break time(min):"), sg.Button('+', key='DBBTP'), sg.Input(self.default_big_break_time,key='DBBT'), sg.Button('-', key='DBBTM')]],
                            [[sg.Text("Default sessions count before big break:"), sg.Button('+', key='DBBCP'), sg.Input(self.default_big_break_count,key='DBBC'), sg.Button('-', key='DBBCM')]],
                            [sg.Button('DEFAULTS'), sg.Button('BACK'), sg.Button('APPLY')]
                        ]   
        options_window = sg.Window('Options', options_layout)
        
        while True:
            event, values = options_window.read(timeout=0)

            if event == sg.WIN_CLOSED:
                break

            if event == 'DSTP':
                self.default_session_time += 1
                options_window['DST'].update(self.default_session_time)\
            
            if event == 'DSTM':
                self.default_session_time -= 1
                options_window['DST'].update(self.default_session_time)

            if event == 'DBTP':
                self.default_break_time += 1
                options_window['DBT'].update(self.default_break_time)

            if event == 'DBTM':
                self.default_break_time -= 1
                options_window['DBT'].update(self.default_break_time)

            if event == 'DBBTP':
                self.default_big_break_time += 1
                options_window['DBBT'].update(self.default_big_break_time)

            if event == 'DBBTM':
                self.default_big_break_time -= 1
                options_window['DBBT'].update(self.default_big_break_time)

            if event == 'DBBCP':
                self.default_big_break_count += 1
                options_window['DBBC'].update(self.default_big_break_count)
            
            if event == 'DBBCM':
                self.default_big_break_count -= 1
                options_window['DBBC'].update(self.default_big_break_count)

            if event == 'DEFAULTS':
                self.default_break_time = self.DEFAULTS[0]
                self.default_session_time = self.DEFAULTS[1]
                self.default_big_break_time = self.DEFAULTS[2]
                self.default_big_break_count = self.DEFAULTS[3]
                options_window['DBBC'].update(self.default_big_break_count)
                options_window['DBBT'].update(self.default_big_break_time)
                options_window['DBT'].update(self.default_break_time)
                options_window['DST'].update(self.default_session_time)
            
            if event == 'BACK':
                options_window.close()
                return
            
            if event == 'APPLY':
                self.default_break_time = int(values['DBT'])
                self.default_session_time = int(values['DST'])
                self.default_big_break_time = int(values['DBBT'])
                self.default_big_break_count = int(values['DBBC'])
                print(self.default_big_break_count)


class TimerMenu(Optionsmenu):
    hour = 0
    min = 0
    sec = 0
    running = True
    sg.theme('DarkAmber')
   
    def start_timer_menu(self):
        layout = [  [sg.Text("Nmber of hours:"), sg.Button('+', key='Hp'), sg.Input(self.hour,key='HOURS'), sg.Button('-', key='Hm')],
        [sg.Text("Number of minutes:"), sg.Button('+', key='Mp'), sg.Input(self.hour,key='MINUTES'), sg.Button('-', key='Mm')],
        [sg.Text("Number of seconds:"), sg.Button('+', key='Sp'), sg.Input(self.hour,key='SECONDS'), sg.Button('-', key='Sm')],
        [sg.Button('START SESSION')],
        ]
        window = sg.Window('Pomodoro-App', layout, finalize=True)

        while True:
            event, values = window.read(timeout=0)
            
            
            if event == sg.WIN_CLOSED:
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
                self.hour = int(values['HOURS'])
                self.min = int(values['MINUTES'])
                self.sec = int(values['SECONDS'])
                window.Hide()  
                Tm = TimerWindow
                Tm.start_timer_window(self)
                window.UnHide()
                
        window.close()

class TimerWindow(TimerMenu, Optionsmenu):


    def start_timer_window(self):
        self.running = True
        total_countdown_time = self.hour * 3600 + self.min * 60 + self.sec
        time_gone = 0
        total_pomodoros = 0
        timer = datetime.timedelta(seconds=total_countdown_time)
        layout1 = [
                    [sg.Text('', justification='center', key='LABEL')],
                    [sg.Text(timer, justification='center', key='TIMER')],
                    [sg.Button('Cancel', key='CANCEL')]
                   ]
        
        timer_window = sg.Window('Timer', layout1)

        while self.running is True:
            event, values = timer_window.read(timeout=0)
            timer_window['LABEL'].update('Time to learn!')

            while total_countdown_time > 0:
                event, values = timer_window.read(timeout=0)
                if event == sg.WIN_CLOSED or total_countdown_time == -1 or event == 'CANCEL':
                    break

                total_countdown_time -= 1
                if time_gone == self.default_session_time*60:
                    total_pomodoros += 1
                    time_gone = 0

                    if total_pomodoros % self.default_big_break_count*60 == 0:
                        timer_window['LABEL'].update('Time for big break!')

                        while time_gone < self.default_big_break_time*60:
                            timer_window['TIMER'].update(timer)
                            if total_countdown_time == -1:
                                break
                            timer = datetime.timedelta(seconds=total_countdown_time)
                            event = timer_window.read(timeout=0)
                            timer_window['TIMER'].update(timer)
                            total_countdown_time -= 1
                            time.sleep(1)
                            time_gone += 1
                    else:
                        timer_window['LABEL'].update('Time for break!')

                        while time_gone < self.default_break_time*60:
                            
                            if total_countdown_time == -1:
                                break
                            timer = datetime.timedelta(seconds=total_countdown_time)
                            event = timer_window.read(timeout=0)
                            timer_window['TIMER'].update(timer)
                            total_countdown_time -= 1 
                            time.sleep(1)
                            time_gone += 1                            
                        time_gone = 0
                event = timer_window.read(timeout=0)
                timer_window['LABEL'].update('Time to learn!')
                timer = datetime.timedelta(seconds=total_countdown_time)
                timer_window['TIMER'].update(timer)
                time.sleep(1)
                time_gone +=1
                
            self.running = False
        timer_window.close()
        return


class MainMenu(TimerMenu):
    sg.theme('DarkAmber')
    
    def start_main_menu(self):
        op = Optionsmenu()
        tm = TimerMenu()
        main_menu_layout = [[sg.Text('Main Menu')],
                        [sg.Button('Timer Menu', key='TM')],
                        [sg.Button('Your Sessions', key='YS')],
                        [sg.Button('Options', key='OP')],
                        [sg.Button('Quit', key='QT')],
                      ]
        main_menu_window = sg.Window('Pomodoro App', main_menu_layout, finalize=True)
        while True:
            event, values = main_menu_window.read(timeout=0)

            if event == 'TM':
                main_menu_window.Hide() 
                tm.start_timer_menu()
                main_menu_window.UnHide()
            
            if event == 'YS': #to-do
                continue

            if event == 'OP':
                main_menu_window.Hide()
                op.start_options_window()
                main_menu_window.UnHide()
            
            if event == sg.WIN_CLOSED or event == "QT":
                main_menu_window.Close()
                return



        

    