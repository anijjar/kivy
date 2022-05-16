from kivy.uix.widget import Widget
from kivy.properties import (
    StringProperty, OptionProperty
)
from kivy.storage.jsonstore import JsonStore

class InfoWidget(Widget):
    """ Parent class for the widget """
    FirstName = StringProperty('')
    LastName = StringProperty('')
    EmergencyName = StringProperty('')
    EmergencyContact = StringProperty('')
    BloodType = OptionProperty('AB','B','A','O')
        


if __name__ == '__main__':
    """
    This module describes the user's info
    """
    print("This module describes the user's info")