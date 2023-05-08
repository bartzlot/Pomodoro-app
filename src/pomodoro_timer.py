import time


class PomodoroTimer:
    hour = 0
    minute = 0
    second = 0
    running = True
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s


    def __str__(self) -> str:
        return f"{self.hour}{self.minute}{self.second}"

    
    def data_validation(self):
        if self.minute > 60 or self.second > 60:
            return False
        
        if self.minute < 0 or self.second < 0 or self.hour < 0:
            return False
        return True
    
    def pomodoro_timer(self):
        self.running = True
        total_time_in_seconds = self.hour * 3600 + self.minute * 60 + self.second
        total_pomodoros, time_left_over = divmod(total_time_in_seconds, 60)
        total_pomodoros, rest = divmod(total_pomodoros, 25)
        time_left_over += rest * 60
        if total_pomodoros == 0:
            while total_time_in_seconds > 0:
                min, sec = divmod(total_time_in_seconds, 60)
                hour, min = divmod(min, 60)
                if sec < 10:
                    print(f'{hour}:{min}:0{sec}')
                else:
                    print(f'{hour}:{min}:{sec}')
                time.sleep(1)
                total_time_in_seconds -= 1
        else:
            time_gone = 0
            pomodoro_sessions = 1
            while total_time_in_seconds > 0:
                min, sec = divmod(total_time_in_seconds, 60)
                hour, min = divmod(min, 60)
                if time_gone % 1500 == 0 and time_gone != 0:
                    pomodoro_sessions += 1
                    if pomodoro_sessions % 4 == 0:
                        print("Time for BIG break!")
                        break_time = 0
                        while break_time < 1200:
                            min, sec = divmod(1200-break_time, 60)
                            if sec < 10:
                                print(f'{min}:0{sec}')
                            else:
                                print(f'{min}:{sec}')
                            time.sleep(1)
                            total_time_in_seconds -= 1
                            break_time += 1
                        print("Time to learn again!")
                    if pomodoro_sessions > 0 and pomodoro_sessions % 4 != 0:
                        print("Time for break!")
                        break_time = 0
                        while break_time < 300:
                            min, sec = divmod(300-break_time, 60)
                            if sec < 10:
                                print(f'{min}:0{sec}')
                            else:
                                print(f'{min}:{sec}')
                            time.sleep(1)
                            total_time_in_seconds += 1
                            break_time += 1
                        print("Time to learn again!")
                if sec < 10:
                    print(f'{hour}:{min}:0{sec}')
                else:
                    print(f'{hour}:{min}:{sec}')
                time.sleep(1)
                total_time_in_seconds -= 1
                time_gone += 1
        self.running = False
    

# pt = PomodoroTimer(0,25,5)
# pt.pomodoro_timer()