import PySimpleGUI as sg
import time, datetime

from pomodoro_modules import (saving_defaults_to_file,
                              reading_defaults_from_file,
                              notify
                              )


class OptionsMenu():

    default_break_time = 5
    default_session_time = 20
    default_big_break_time = 20
    default_big_break_count = 4
    DEFAULTS = [5, 20, 20, 4]
    DEFAULTS_TO_SAVE = []
    sg.theme('DarkAmber')
    
    def start_options_window(self):
        self.DEFAULTS_TO_SAVE = reading_defaults_from_file("default_settings.json")
        self.default_break_time = self.DEFAULTS_TO_SAVE[0]
        self.default_session_time = self.DEFAULTS_TO_SAVE[1]
        self.default_big_break_time = self.DEFAULTS_TO_SAVE[2]
        self.default_big_break_count = self.DEFAULTS_TO_SAVE[3]
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
                self.DEFAULTS_TO_SAVE = []
                self.DEFAULTS_TO_SAVE.extend((self.default_break_time, self.default_session_time, self.default_big_break_time, self.default_big_break_count))
                saving_defaults_to_file(self.DEFAULTS_TO_SAVE, "default_settings.json")


class TimerMenu(OptionsMenu):
    session_title = ""
    current_session_info = []
    previous_sessions = reading_defaults_from_file("previous_sessions.json")
    hour = 0
    min = 0
    sec = 0
    running = True
    sg.theme('DarkAmber')
   
    def start_timer_menu(self):
        self.current_session_info = []
        layout = [  [sg.Text("Session title:"), sg.InputText(self.session_title,key='TITLE')],
                    [sg.Text("Number of hours:"), sg.Button('+', key='Hp'), sg.Input(self.hour,key='HOURS'), sg.Button('-', key='Hm')],
                    [sg.Text("Number of minutes:"), sg.Button('+', key='Mp'), sg.Input(self.hour,key='MINUTES'), sg.Button('-', key='Mm')],
                    [sg.Text("Number of seconds:"), sg.Button('+', key='Sp'), sg.Input(self.hour,key='SECONDS'), sg.Button('-', key='Sm')],
                    [sg.Button('START SESSION'), sg.Button('BACK')]
                ]
        window = sg.Window('Pomodoro-App', layout, finalize=True)

        while True:
            event, values = window.read(timeout=0)
            
            
            if event == sg.WIN_CLOSED or event == 'BACK':
                break

            if event == 'Hp':
                self.hour += 1
                window['HOURS'].update(value=str(self.hour))
                
            if event == 'Hm':
                self.hour -= 1
                window['HOURS'].update(value=str(self.hour))

            if event == 'Mm':
                self.min -= 1
                window['MINUTES'].update(value=str(self.min))

            if event == 'Mp':
                self.min += 1
                window['MINUTES'].update(value=str(self.min))

            if event == 'Sm':
                self.sec -= 1
                window['SECONDS'].update(value=str(self.sec))

            if event == 'Sp':
                self.sec += 1
                window['SECONDS'].update(value=str(self.sec))

            if event == 'START SESSION':
                self.current_session_info = []
                self.session_title = values['TITLE']
                self.hour = int(values['HOURS'])
                self.min = int(values['MINUTES'])
                self.sec = int(values['SECONDS'])
                window.Hide()
                date = datetime.date.today()
                date = date.strftime("%d/%m/%Y")
                self.current_session_info.extend((self.session_title, '{:02d}:{:02d}:{:02d}'.format(self.hour, self.min, self.sec), date))
                Tm = TimerWindow
                Tm.start_timer_window(self)
                window.UnHide()
                
        window.close()


class TimerWindow(TimerMenu, OptionsMenu):


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
                        notify('Time for big break!', f'You made through {total_pomodoros} pomodoros!')
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
                        notify('Time for break!', f'You made through {total_pomodoros} pomodoros!')
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
            if total_countdown_time == 0:
                self.current_session_info.append(str(total_pomodoros))
                self.previous_sessions.append(self.current_session_info)
            self.running = False
        timer_window.close()
        return


class SessionsMenu(TimerWindow):
    LABELS = ['Title','Session Time', 'Date', 'Pomodoros Count']
    def start_sessions_menu(self):
        table = sg.Table(values=self.previous_sessions,
                        headings=self.LABELS,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='center',
                        key='TABLE',
                        expand_x=True,
                        expand_y=True)
        sessions_menu_layout = [[table],
                                [sg.Button('BACK', key='BACK')]]
        sessions_window = sg.Window("Previous Sessions", sessions_menu_layout, resizable=True)
        while True:
            event, values = sessions_window.read(timeout=0)
            if event == sg.WIN_CLOSED or event == 'BACK':
                sessions_window.close()
                break
        return
class MainMenu(SessionsMenu):
    sg.theme('DarkAmber')
    
    def start_main_menu(self):
        op = OptionsMenu()
        tm = TimerMenu()
        sm = SessionsMenu()
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
            
            if event == 'YS':
                main_menu_window.Hide()
                sm.start_sessions_menu()
                main_menu_window.UnHide()

            if event == 'OP':
                main_menu_window.Hide()
                op.start_options_window()
                main_menu_window.UnHide()
            
            if event == sg.WIN_CLOSED or event == "QT":
                main_menu_window.Close()
                saving_defaults_to_file(self.previous_sessions, 'previous_sessions.json')
                return



        

    