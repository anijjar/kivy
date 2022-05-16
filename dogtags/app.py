from kivy.app import App
from map import MapWidget
from info import InfoWidget

class DogTagsApp(App):
    """ Parent class to enter game """
    def build(self):
        # use app to build the app screen
        app = Widget()
        self.map = MapWidget()
        # bind this to a button.
        self.info = InfoWidget()
        return app


if __name__ == '__main__':
    """
    This module is the entry point for the app
    """
    DogTagsApp().run()