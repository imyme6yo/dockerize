import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):

    def build(self):
        return Button(text='Hello world')

if __name__=='__main__':
    MyApp().run()
