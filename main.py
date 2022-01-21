import kivy
kivy.require("1.0.6")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class Widget(GridLayout):
    def __init__(self, **kwargs):
        super(Widget, self) .__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Best Lap Time(Format: mins:secs/0:00):"))
        self.laptime = TextInput(multiline=False)
        self.add_widget(self.laptime)

        self.add_widget(Label(text="Fuel used by the car on one lap"))
        self.fueluse = TextInput(multiline=False)
        self.add_widget(self.fueluse)

        self.add_widget(Label(text="Race length in minutes"))
        self.race = TextInput(multiline=False)
        self.add_widget(self.race)

        btn1 = Button(text="Calculate:")
        btn1.bind(on_press=self.buttonClicked)
        self.add_widget(btn1)


    def buttonClicked(self, btn):
        #texts = self.rpm.text.split()
        #if len(texts) == 2:
         #   try:
          #      x, y = map(float, texts)
           #     res = x/y
            #    popup = Popup(title='Result', content=Label(text=str(res)), size_hint=(None, None), size=(500, 90))
             #   popup.open()
            #except (ValueError, ZeroDivisionError):
            #    print("error")
        bestlap=self.laptime.text
        racelength=self.race.text
        fuelCons = self.fueluse.text
        bestlapSEC = get_sec_lap(bestlap)
        racelengthSEC = get_sec_race(racelength)

def get_sec_lap(time_str):
    if ':' in time_str:
        m, s = time_str.split(':')
        if m.isnumeric() and s.isnumeric():
            return int(m) * 60 + int(s)
        else:
            popup = Popup(title='innerBadLap', content=Label(text='The input laptime is invalid. please follow the instructions'),size_hint=(None, None), size=(400, 100))
            popup.open()
    else:
        popup = Popup(title='OuterBadLap', content=Label(text='The input laptime is invalid. please follow the instructions'),size_hint=(None, None), size=(400, 100))
        popup.open()

def get_sec_race(time_str):
    if time_str.isnumeric():
        i = int(time_str)
        return i*60
    else:
        popup = Popup(title='OuterBadrace', content=Label(text='The input racetime is invalid. please follow the instructions'),size_hint=(None, None), size=(450, 100))
        popup.open()

class TestApp(App):
    def build(self):
        return Widget()

if __name__ == '__main__':
    TestApp().run()
