import PySimpleGUI as sg
import time
from pomodoro_modules import (  hours_validation,
                                minutes_validation,
                                )
from pomodoro_view import TimerMenu, Optionsmenu

tm = TimerMenu()
tm.start_timer_menu()

