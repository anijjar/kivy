from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivymd.app import MDApp
from kivy_garden.mapview import MapView

class MapWidget(Widget):
    """ Parent class for the widget """
    pass


if __name__ == '__main__':
    """
    This module describes the map for location tracking
    
    basically, we want a button to save the location then using the gps, record their steps into a csv file, until the button is depressed.

    finally, a report is generated with all their nearby hotspots. 
    """
    print("This module describes the map widget")