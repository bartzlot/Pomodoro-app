import PySimpleGUI as sg
import time, datetime

from pomodoro_modules import (saving_defaults_to_file,
                              reading_defaults_from_file,
                              notify, ErrorsHandling
                              )


class OptionsMenu(ErrorsHandling):
    plus_base64 = b'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'
    minus_base64 = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAFa0lEQVRogd2aa0xTVwDHzz2lpXp59El5twjFiR1YN6AZCuIWZDJx4MREY2LYJjgGdsui2cyyRbMPmzMk+AWmsPHFzBLrlNXhnDxGoIS5DQpNfYClyKPIo4K2pfS1DwOCULD33tLL9vt07z3nnvP75+bee+49B3E6nYAok2ZzYHNPT/odnS6pc2Bga//EhGDCZGKNG43chfVoFIpFwGY/jAkKuv9qZGR7clRUa5JAoPT18bEQdUDwBrHa7dRalSrne6Xy6O89PelOpxPiaQel0Z7tiotT7BOLL+8Wia5TILTjaQdzEIvN5lutVL537vbtT4cnJ8PwdLocfBZLW5SWVvpuSko5lUKxYjkXUxBFd3f2Cbm87JHBwMdsiYGXgoPVZ3NyStJiY+vdPcetIAaTiSmtqSm/2tGRR8gQI4Xbt5ed3rPnJJ1KnX5R3RcGUQ0ObjlYWXm132AQeEoQC3EhIV1Xjh7dHcZgDKxUb8UgyocPt+VWVPxinJnx87ghBrh+fiPygoI3E8LD/16uzrJB1kqIOVgoOnazuDh1I4+ncVXuMkj30FD8rrKy5qcWS8CqG2KAhaJj9VKpZAOH07u4bMmzf9JsDjxUVSVfayEAAGDCaOQcqa6+PG210heXLQlSIpN9px0fj/aOGnY6BgZe+by29pvFx58Loujuzvb2IxYPFc3NH7b39UkWHpsPYrHZfE/I5WXe18IFclwmq3A4HPP+8xsXW1qOrfYb25Ooh4fjb6jV2XP7EIB/r0ZZQ8Mn5Gnh48yNG2fmtiEAACi6uvZ6egDoDTR6vahNq30NgNkg8v/ADb4cF1taPgAAADhttdLr1Oq3yBbCy021OsvucFDgHzqdZMZu9yVbCC+T09OMP/v7E2Frb+92smWI0qbVpvi0abUpnm44kc8Ht6VSl2VVra1AWlPj0f56R0eFcC0PR9ylZ3Q0Fg4+eRJOtghRRqamghF/qZT4/6BF0KlUEMVmuywzmExAPzXl0f5YKDrm49EWZ5m2WoFGr1+Npl1iMJlYuP5FrTWoEFr/F0H86fQpuJ5GM5ItQhSURjPCCCZTR7YIUWJ5vLswnMF4RLYIUYRBQfegKCysk2wRomwODVXBZIFASbYIUdKEwnqYKhTW0ygUwvMTZMH18xvhs1h9MIBOn3pj06Y6soXwkisWywCY/UI8lJhYTa4OfvaJxT8CMBtkt0h0fQOH00OuEnYS+fw2SVRUKwCzQSgQ2j/aufNrcrWwU7xjx7m57fkhyqGkpB+EXO49cpSwkxId3bQ3IeHK3P58EB8KxVa6f/8xcrSwARHEfjY3twRBkPlPkOcGjalCYcPh5ORK76th47PMzC9FoaGqhceWzI+YZmbW7ygtbb+r12/2qp2bJAsErXXFxamLp7GXDOPX02imS/n5OSwUHfOenntEsdm9l/Lzc1zNxbv8Honhch9cKyzMWEthIphMnbygIJPr7//YVfmKk6HqoaGX95aX//r46dPgVTN0gwgmU6coKkoXsNna5eq8cHr6kcEQmXfhQq16eDje44ZukBId3VR1+PDBkMDAoZXqubVgwGKz+Z5WKL4639j4MQAA8ZTkSkAEsZekp3/7RVbWKXfWp2BawtHe1yc5LpNVrPbVEUdE3Dl/4MD78WFhHe6eg3lRjcPhgPKOjryzt26d0uj1IsyWK5AQHv7XyYyMM1ki0bWFLzt3wL3Myel0Io3377/+U2fnOz93db09+uwZD087bBQd3RMff/WIRHJha2TkHVwygECQxegmJgS/aTSZqsHBLXdHRuIGDYYIs9W6btJsZgAAQOC6dU94AQF6FoqOR3M4DzbyeJptMTFNopAQFYTQQbT/fwAvJBKZLZwaxgAAAABJRU5ErkJggg=='
    defaults_base64 = b'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'
    back_base64 = b'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'
    apply_base64 = b'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'
    default_break_time = 5
    default_session_time = 20
    default_big_break_time = 20
    default_big_break_count = 4
    DEFAULTS = [5, 20, 20, 4]
    DEFAULTS_TO_SAVE = []
    sg.theme('LightGrey')
    
    def assigning_values(self):
        if ErrorsHandling.file_existence("default_settings.json"):

            self.DEFAULTS_TO_SAVE = reading_defaults_from_file("default_settings.json")

        else:
            saving_defaults_to_file(self.DEFAULTS, "default_settings.json")
            self.DEFAULTS_TO_SAVE = reading_defaults_from_file("default_settings.json")
            
        self.default_break_time = self.DEFAULTS_TO_SAVE[0]
        self.default_session_time = self.DEFAULTS_TO_SAVE[1]
        self.default_big_break_time = self.DEFAULTS_TO_SAVE[2]
        self.default_big_break_count = self.DEFAULTS_TO_SAVE[3]


    def start_options_window(self):
        self.assigning_values()
        options_layout = [[[sg.Text("Default session time(min):", font=('Open Sans Bold', 30), size=(31,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), key='DSTP'),
                             sg.Input(self.default_session_time,  text_color='#9650d4',font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True,key='DST'), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='DSTM')]],
                            [[sg.Text("Default break time(min):", font=('Open Sans Bold', 30), size=(31,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0,  key='DBTP'),
                               sg.Input(self.default_break_time, text_color='#9650d4',font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True,key='DBT'), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0,  key='DBTM')]],
                            [[sg.Text("Default big break time(min):", font=('Open Sans Bold', 30), size=(31,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='DBBTP'),
                               sg.Input(self.default_big_break_time, text_color='#9650d4',font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True,key='DBBT'), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='DBBTM')]],
                            [[sg.Text("Default sessions count before big break:", font=('Open Sans Bold', 30), size=(31,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='DBBCP'),
                               sg.Input(self.default_big_break_count, text_color='#9650d4',font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True,key='DBBC'), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0,  key='DBBCM')]],
                            [sg.Button('', image_data=self.back_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='BACK'),
                             sg.Button('', image_data=self.apply_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='APPLY' ),
                             sg.Text('', size=(63, 0)),
                             sg.Button('', image_data=self.defaults_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='DEFAULTS')]
                        ]   
        
        
        options_window = sg.Window('Options', options_layout)
        
        while True:
            event, values = options_window.read(timeout=0)

            if event == sg.WIN_CLOSED:
                break

            if event == 'DSTP':
                self.default_session_time += 1
                self.default_session_time = ErrorsHandling.handling_negatives(self.default_session_time, 360)
                options_window['DST'].update(self.default_session_time)
            
            if event == 'DSTM':
                self.default_session_time -= 1
                self.default_session_time = ErrorsHandling.handling_negatives(self.default_session_time, 360)
                options_window['DST'].update(self.default_session_time)

            if event == 'DBTP':
                self.default_break_time += 1
                self.default_break_time = ErrorsHandling.handling_negatives(self.default_break_time, 360)
                options_window['DBT'].update(self.default_break_time)

            if event == 'DBTM':
                self.default_break_time -= 1
                self.default_break_time = ErrorsHandling.handling_negatives(self.default_break_time, 360)
                options_window['DBT'].update(self.default_break_time)

            if event == 'DBBTP':
                self.default_big_break_time += 1
                self.default_big_break_time = ErrorsHandling.handling_negatives(self.default_big_break_time, 360)
                options_window['DBBT'].update(self.default_big_break_time)

            if event == 'DBBTM':
                self.default_big_break_time -= 1
                self.default_big_break_time = ErrorsHandling.handling_negatives(self.default_big_break_time, 360)
                options_window['DBBT'].update(self.default_big_break_time)

            if event == 'DBBCP':
                self.default_big_break_count += 1
                self.default_big_break_count = ErrorsHandling.handling_negatives(self.default_big_break_count, 360)
                options_window['DBBC'].update(self.default_big_break_count)
            
            if event == 'DBBCM':
                self.default_big_break_count -= 1
                self.default_big_break_count = ErrorsHandling.handling_negatives(self.default_big_break_count, 360)
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
                if (ErrorsHandling.handling_popups_empty_value(values['DBT'], "ERROR: Default break time value is empty\n(try adding 0 to the box)") or
                    ErrorsHandling.handling_popups_empty_value(values['DST'], "ERROR: Default session time value is empty\n(try adding 0 to the box)") or
                    ErrorsHandling.handling_popups_empty_value(values['DBBT'], "ERROR: Default big break time value is empty\n(try adding 0 to the box)") or
                    ErrorsHandling.handling_popups_empty_value(values['DBBC'], "ERROR: Default big break count value is empty\n(try adding 0 to the box)")):
                    pass
                else:
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
    ss_base64 = b'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'
    if ErrorsHandling.file_existence("previous_sessions.json"):
        previous_sessions = reading_defaults_from_file("previous_sessions.json")
    else:
        previous_sessions = []
    hour = 0
    min = 0
    sec = 0
    running = True
    sg.theme('LightGrey')

    def start_timer_menu(self):
        self.current_session_info = []
        layout = [  [sg.Text("Session title:", font=('Open Sans Bold', 30)), sg.InputText(self.session_title, expand_y=True, text_color='#9650d4', background_color=(sg.theme_background_color()), font=('Open Sans Bold', 30), size=(14,2), key='TITLE')],
                    [sg.Text("Number of hours:", font=('Open Sans Bold', 30) , size=(16,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), 
                    border_width=0, key='Hp'), sg.Input(self.hour,key='HOURS', text_color='#9650d4',font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Hm')],
                    [sg.Text("Number of minutes:", font=('Open Sans Bold', 30) , size=(16,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), 
                    border_width=0, key='Mp'), sg.Input(self.hour,key='MINUTES', text_color='#9650d4', font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Mm')],
                    [sg.Text("Number of seconds:", font=('Open Sans Bold', 30) , size=(16,1)), sg.Button('', image_data=self.plus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), 
                    border_width=0, key='Sp'), sg.Input(self.hour,key='SECONDS', text_color='#9650d4', font=('Open Sans Bold', 30), border_width=0, background_color=(sg.theme_background_color()),size=(2,5), expand_y=True), sg.Button('', image_data=self.minus_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='Sm')],
                    [sg.Button('', image_data=self.back_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='BACK'),
                     sg.Text('', size=(28,0)),
                     sg.Button('', image_data=self.ss_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='START SESSION' )]
                ]
        window = sg.Window('Pomodoro-App', layout, finalize=True)

        while True:
            event, values = window.read(timeout=0)
            
            
            if event == sg.WIN_CLOSED or event == 'BACK':
                break

            if event == 'Hp':
                self.hour += 1
                self.hour = ErrorsHandling.handling_negatives(self.hour, 24)
                window['HOURS'].update(value=str(self.hour))
                
            if event == 'Hm':
                self.hour -= 1
                self.hour = ErrorsHandling.handling_negatives(self.hour, 24)
                window['HOURS'].update(value=str(self.hour))

            if event == 'Mm':
                self.min -= 1
                self.min = ErrorsHandling.handling_negatives(self.min, 60)
                window['MINUTES'].update(value=str(self.min))

            if event == 'Mp':
                self.min += 1
                self.min = ErrorsHandling.handling_negatives(self.min, 60)
                window['MINUTES'].update(value=str(self.min))

            if event == 'Sm':
                self.sec -= 1
                self.sec = ErrorsHandling.handling_negatives(self.sec, 60)
                window['SECONDS'].update(value=str(self.sec))

            if event == 'Sp':
                self.sec += 1
                self.sec = ErrorsHandling.handling_negatives(self.sec, 60)
                window['SECONDS'].update(value=str(self.sec))

            if event == 'START SESSION':
                
                if (ErrorsHandling.handling_popups_empty_value_title(values['TITLE'], "Please add session title") or
                    ErrorsHandling.handling_popups_empty_value(values['HOURS'], "ERROR: Hour value is empty\n(try adding 0 to the box)") or
                    ErrorsHandling.handling_popups_empty_value(values['MINUTES'], "ERROR: Minutes value is empty\n(try adding 0 to the box)") or
                    ErrorsHandling.handling_popups_empty_value(values['SECONDS'], "ERROR: Seconds value is empty\n(try adding 0 to the box)")):
                    pass
                else:
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


class TimerWindow(TimerMenu):


    def start_timer_window(self):
        OptionsMenu.assigning_values(self)
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
                if time_gone == (self.default_session_time*60):
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
        notify(f'Session {self.session_title} ended', 'You can start a new one, keep It up!')
        timer_window.close()
        return


class SessionsMenu(TimerWindow):
    LABELS = ['Title', 'Session Time', 'Date', 'Pomodoros Count']
    def start_sessions_menu(self):
        table = sg.Table(values=self.previous_sessions,
                        headings=self.LABELS,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        header_background_color='#0d7070',  
                        hide_vertical_scroll=True,
                        justification='center',
                        key='TABLE',
                        expand_x=True,
                        expand_y=True)
        sessions_menu_layout = [[table],
                                [sg.Button('', image_data=self.back_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='BACK')]]
        sessions_window = sg.Window("Previous Sessions", sessions_menu_layout, resizable=True)
        while True:
            event, values = sessions_window.read(timeout=0)
            if event == sg.WIN_CLOSED or event == 'BACK':
                sessions_window.close()
                break
        return
class MainMenu(SessionsMenu):  
    sg.theme('LightGrey')
    Ys_base64 = b'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'
    Op_base64 = b'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'
    Qt_base64 = b'iVBORw0KGgoAAAANSUhEUgAAAMgAAAAyCAYAAAAZUZThAAAKYElEQVR4nO3deVRTVx4H8G8WAhLWQAyyBhFBxQhtWQqtgFpbdcSBVttat8oMtqO4zOl0OV1PazedHiv29Ehd0PG0VpyiVXG0HSyWo1BFB1DEyo4ggWAgQhKyMn8oKVkgYcsLcj9/5b5378uPc/Ijue/+3nu0np4eDJdELnctqKpKLK6vjyptbHykQSzmi2Uyzl2plDvsgxOEGSwGQ8H38KiZMnHircf8/S9FBwZejOLzC+2ZTMVwj00baoKoNBq7k2VlyVmFhWm/VlUl9vT00IcbDEGMFDaL1fX09Om5z0ZEHFkYFnaCQadrhnKcQSeIQq22P1hY+Jcv8vLeapZIfIbypgRhTQEcTu36+PgdqXFxu+0YDNVgxg4qQXKvX096PScn43Z7e8CgoyQIioV6eZVvT07eGD916jlLx1iUIO0ymfvmo0d3HyspWTasCAnCBrzy5JMZHy5e/IaDnV23ub5mE6SsqSl8+b59xxra2/kjFSBBUG36pEnXfkhLW+jj5tY4UL8BE6SwpuaJlMzM/0iVSqcRj5AgKMZ1cmrJWbduwSxf3//116ffBCHJQYwHHDa77Wx6+uwQHq/C1H6TCXL9zh3B0xkZBZ0KhcuoR0gQFOOw2W3nNm+OmezpWW24z2jtQiKXu760f38OSQ5ivBBLpZ5rDh480q1SORjuM0qQjdnZ39TevRtkndAIwjaUNDY++u7Jk9sMt+slSO7160nkVC4xXmUWFGy4VFcX03ebLkEUarX96zk5GdYPiyBsBm1TdnamVqvV5YXuxd4LF14lK+TEeFfe3Cw4XV6e1NumA/e/PTJ++eU16sIiCNvx0enTH/W+pgNA7rVrS0jh4djz7sKFuP3JJ6jbuhWb5syhOpyHRoVQGFZUWxsLAEwAyCETc4vRaDQsnjkTC2bMQCSfD66TE5zs7dEhk6GxowMXqqvx76tXcfX27VGNg+PoiH889ZSu/cGiRfj6/HmoNEOq6iYM7L1w4W8xgYEXmd0qlcOZ8vI/UR3QWCDw8cG+lSsRwuMZ7eM6O4Pr7IwIPz9sSEjAibIyrD98GJJus/VwQ6JQq6HSaGDHYAAApEol1Fqtyb4M+v2ppqaf/YSxs+XlizRaLYN5ub4+RqnR2FMdkK2LCwrCD2lpcGSxLOqfJBAghMfDUzt3okMuH/F4pEolUg8dwtrYWKi1WnyVnw9TVRHJ4eE4uHo1AGDlgQP4sbR0xGN5GEm6u92uNDREMi9WVz9JdTC2jsNm48CqVXrJodFqkX3lCvJv3YJELsckV1ckh4djdnCwrk8Ij4evXngBK7KyRiWu46WlOG7mA78iKmpU3ns8KKqtjWMW1dbGUR2IrdsQHw+eyx+VN1KFAsmZmSiqrdXrt+/iRaQnJODjJUt025IEAjzq748rDQ1Wi7eXl4sL5oSEWP19HxbVIlEwk5SVmLc6Rm9xFZ+ePWuUHL125edjXmgoEvt8MF+OjdVLEDaLhebPP9e1K5qbEb3NqMoBF157DTN9/ji56PfWW3pzGtH27bBnMgEArZ2dmPLee7p980JDsT0lRTf/AIBDa9boHX/Znj04c+OGyb+DAKpEoqn0po4OX6oDsWUhPB64zs66tkqjwb+KigYcs7+wUK8dN3nyqMTWn+ciIpCzbh2CuOSmMsPRcu+eF1OhVhtVMBJ/mOntrdeuEArNTrov1dXptYO4XLBZLEiVypEOzyQ7BgOtnZ1wsrfXmzd1yOVQqtW6dnef14SxNqmUy6Q6CFvHYbP12rfFYrNjmiUSaLRavZ837o6OVkuQw8XFOFxcjK1JSdiYmKjbnn7kCDmLNQjtMhmH3MvKDLa9/hlwucqyu8YY9nN2IF/UY40dna4iCWJGl0L/5nwT7OwsGmfYr9vCxCJsh7ODwz26I4slpToQW3a3q0uv7evubnaMt6ur3s8r4P5ZpsGi02iDHkOMHDaLJaX7ubvXUx2ILbvW1KTXnublBRczP5eiAwP12vVi8ZDmH4Y/7wjrmsrj3aT7urmNblXdGFcpEkEokejaLCYTK6OjBxyTGhur1/7l998H7O9kIuEc7Ozg6+Y2iEiJkRY8ceLv9DAfH3Jaw4wsg3WNtxcsQFSA6WvLtsydq1duAgAHDdZNDCfw3q6umNhnrQUAlggEYD4oRBwqrUFxYu+iImGZGd7eZcxoPr/QfNfxbXdBAVbHxMD7wX90J3t7nElPx9GrV/FrZSUk3d3wcXNDSng4HjdYFDxeUmJUZqLt6UGDWAx/DgfA/Wrb3cuX4/2TJyGWyRAfHIzPkpOHHbdYJtNrp8bGorSxEXKlEiE8HsQyGSUlMGNFfHDwOebs4OBzLAZDQSp6+9cuk+HlQ4eQk5ammxcwGQy8GBmJFyMj+x13UyjExuxsk/tOlJVhQ0KCrj0vNBTzQkP1+hiupQzWbwYLlo9PnozLb76pa79z4gRJkH5wnZxaAjicOrqLg8O9edOmnaE6IFtXWFODp3ftwk2h0KL+x0pKBix13/bTT6hsbe13fGljI9K+/XZIsfYqrKnBr5WVwzrGeJUSEZENPLjk9qXIyIPUhjM2lDU1IXrbNqzIysJ3ly+jsrUVErnc6DqMBrEYW44eHfBiqQ65HHO//BI78vJwq6UFCrUaUoUCZU1N+ODUKczbuRNnb9wY9kVOy/buxZd5eagWiaBUq9GlUKC2rU1Xqk+Y9mxExPfAg1uParRaxqOffnqzpq1tCtWBjUUcR0ec27IFkz09dduK6+ux+OuvrVZeQoycyICAorzNmx8HHnyDMOh0zZY5cz4feBjRH7FMhqXffIP2PpPixwICcDg1FaxhnokirC89IeGL3te6GeBLUVEHgrncgU/YE/2qFImwIitL76YJCVOnYv+qVWRFfAyJCwo6v2TWrB9627oEYTIY6h1Ll75KTVgPh4KqKmwyOGuVJBAgYxm5acxYQKfRNNtTUjbSaDTdpNLo8Qfrv/9+76Hffku1enQEQbF3Fix49/X587f23WaUIDKl0jFhx45LN4XCGVaNjiAoFM3nXzyTnj7b8HHRRqtQjiyW7Lu1a5M5bHab9cIjCOoEenhUf7d2bbKpZ6mbXKadwuVW/vjKK/NJkhAPOz939/qcdeue4To7m1y1HfAhnuV37sxcsnv3T62dnV6jFiFBUMTP3b0+d/36RL6Hh+lb1MCCx0Dfbm/3X7Znz8ny5mbBiEdIEBSJCwo6v3/lyuWTXF3vDNTPbIIA9x+P8GFu7se78vP/DoCc1CfGLDqNptmYmPjP9xctetvUnMOQRQnS61JdXcym7OxM8m1CjEURfn7Fu55//q8CH58SS8cMKkEAQKvV0nNKSpZt//nntyuEwrBBR0kQVjbL1/fqG/Pnf7QoLOzHvouAlhh0gvTq6emh5d+6Nfd4aelzp65d+7Ooq8v4mQAEQREPNlu0WCA4tiYmZs8j/v7FQz3OkBPEUL1YzP9vRcUzZU1N4TdbWqY3tbf7yVWqCRK53I1cjEWMBhaDoXCdMKGD5+Ii5LDZd4M8PStDeLyKJ6ZMOR82aVIZnU4f9gNR/g/rr/H3YSBFPgAAAABJRU5ErkJggg=='
    Tm_base64 = b'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'
    
    
    def start_main_menu(self):
        op = OptionsMenu()
        tm = TimerMenu()
        sm = SessionsMenu()
        main_menu_layout = [[sg.Text('Main Menu', size=10)],
                        [sg.Button('', image_data=self.Tm_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='TM')],
                        [sg.Button('', image_data=self.Ys_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='YS')],
                        [sg.Button('', image_data=self.Op_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='OP')],
                        [sg.Button('', image_data=self.Qt_base64, button_color=(sg.theme_background_color(),sg.theme_background_color()), border_width=0, key='QT')],
                      ]
        main_menu_window = sg.Window('Pomodoro App', main_menu_layout, finalize=True, resizable=True )
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



        

    