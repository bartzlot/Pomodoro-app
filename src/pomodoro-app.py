import PySimpleGUI as sg
import time
from pomodoro_modules import (  hours_validation,
                                minutes_validation,
                                )
from pomodoro_view import TimerMenu, Optionsmenu, MainMenu


# tm = TimerMenu()
# tm.start_timer_menu()

op = MainMenu()
op.start_main_menu()

