import json
from notifypy import Notify
import PySimpleGUI as sg
import os
class ErrorsHandling():
    """Class containing error-handling mathods."""
    def handling_negatives(value: int, max_value: int):
        """

        Args:
            value (int): input value
            max_value (int): max value to choose

        Returns:
            int: value
        """
        
        if value > max_value:
            return 0
        
        if value < 0:
            return max_value
        return value


    def handling_popups_empty_value(value: str, message: str):
        """Handling empty value and not numeric input

        Args:
            value (str): input value
            message (str): error message

        Returns:
            bool: bool if value is correct
        """
        if not value:
            return True, sg.popup(message)
        if not value.isnumeric():
            return True, sg.popup("Please insert numeric value...")
        return False


    def handling_popups_empty_value_title(value: str, message: str):
        """Handling empty value input

        Args:
            value (str): input value
            message (str): error message

        Returns:
            bool: bool if value is correct
        """
        if not value:
            return True, sg.popup(message)
        return False


    def file_existence(path: str):
        """Handling file doesn't exist error

        Args:
            path (str): file path

        Returns:
            bool: if file exist or not
        """
        if os.path.exists(path):
            return True
        sg.popup(f"File {path} doesn't exist, automatically creating one...")
        return False

  


def notify(t, m):
    """Sends system notification

    Args:
        t (str): title of notification
        m (str): message
    """
    print(os.getcwd())
    os.chdir('assets')
    n = Notify()
    n.title = t
    n.message = m
    n.icon = 'icon.png'
    n.application_name = 'Pomodoro-App'
    n.send()
    os.chdir('..')

def saving_defaults_to_file(data: list, destination: str):
    """Saves default values to json file

    Args:
        data (list): list of data that has to be saved
        destination (str): file path
    """
    object = json.dumps(data, indent=2)
    with open(destination, "w") as f:
        f.write(object)


def reading_defaults_from_file(destination: str):
    """Reads defaults from json file

    Args:
        destination (str): file path

    Returns:
        list: return list of defaults
    """
    with open(destination, "r") as f:
        object = json.load(f)
    return object
