import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

fuelcostFin = ""


class Widget(GridLayout):
    def __init__(self, **kwargs):
        super(Widget, self) .__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Best Lap Time(Format: mins:secs/0:00):"))
        self.laptime = TextInput(multiline=False,)
        self.add_widget(self.laptime)

        self.add_widget(Label(text="Fuel used by the car on one lap(format: 1.3, 2.77)"))
        self.fueluse = TextInput(multiline=False)
        self.add_widget(self.fueluse)

        self.add_widget(Label(text="Race length in minutes"))
        self.race = TextInput(multiline=False)
        self.add_widget(self.race)

        btn1 = Button(text="Calculate:")
        btn1.bind(on_press=self.buttonClicked)
        self.add_widget(btn1)


    def buttonClicked(self, btn):
        bestlap=self.laptime.text
        racelength=self.race.text
        fuelCons = self.fueluse.text
        bestlapSEC = get_sec_lap(bestlap)
        if bestlapSEC == False:
            return
        racelengthSEC = get_sec_race(racelength)
        if racelengthSEC == False:
            return
        good_test = False
        if get_fuel(fuelCons) != False:
            fuelConsTEST = get_fuel(fuelCons)
            good_test = True
        else:
            popup = Popup(title='Badfuel', content=Label(text='The input fuel is invalid. please follow the instructions'),size_hint=(None, None), size=(400, 100))
            popup.open()
        if good_test == True:
            lapcount = racelengthSEC/bestlapSEC
            fuelinliter = lapcount * fuelConsTEST
            fuelinliter= round(fuelinliter,2)
            safefuel = fuelinliter + 3
            str_fin = 'The needed fuel for the race(risky) = '+str(fuelinliter)+' l\n' + 'The safe amount of fuel is = '+ str(safefuel)+' l'
            popup = Popup(title='Finnished Calculations', content=Label(text=str_fin),size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title='Tests failed', content=Label(text='some tests failed. please try again'),size_hint=(None, None), size=(400, 200))
            popup.open()


def get_sec_lap(time_str):
    if ':' in time_str:
        split_str = time_str.split(':')
        good_calc = False
        m = split_str[0]
        s = split_str[1]
        good_calc = True
        if good_calc == True:
            if m.isnumeric() and s.isnumeric():
                return int(m) * 60 + int(s)
            else:
                popup = Popup(title='innerBadLap', content=Label(text='The input laptime is invalid. please follow the instructions'),size_hint=(None, None), size=(400, 100))
                popup.open()
                return False
        else:
            popup = Popup(title='innerBadLap', content=Label(text='Calculations failed. Please try again'),size_hint=(None, None), size=(400, 100))
            popup.open()
            return False
    else:
        popup = Popup(title='OuterBadLap', content=Label(text='The input laptime is invalid. please follow the instructions'),size_hint=(None, None), size=(400, 100))
        popup.open()
        return False

def get_sec_race(time_str):
    if time_str.isnumeric():
        i = int(time_str)
        return i*60
    else:
        popup = Popup(title='OuterBadrace', content=Label(text='The input racetime is invalid. please follow the instructions'),size_hint=(None, None), size=(450, 100))
        popup.open()
        return False

def get_fuel(fuel_str):
    try:
        float(fuel_str)
        return float(fuel_str)
    except ValueError:
        return False

class TestApp(App):
    def build(self):
        return Widget()

if __name__ == '__main__':
    TestApp().run()
