from math import sqrt
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (32/255, 32/255, 32/255, 0.87)
font_size = 20


class Calculator(App):
    def build(self):
        Window.size = (400, 600)
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=4, spacing=5, size_hint=(1, .6))
        self.lbl = Label(text=self.formula, font_size=50, size_hint=(1, .4),padding=(10, 10), halign='right', valign='center', text_size=(400 - 50, 500 * .4 - 50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="%", font_size=font_size, on_press=self.add_operation))
        gl.add_widget(Button(text="x^2", font_size=font_size, on_press=self.add_operation))
        gl.add_widget(Button(text="√", font_size=font_size, on_press=self.add_operation))
        gl.add_widget(Button(text="C", font_size=font_size, on_press=self.add_operation))

        gl.add_widget(Button(text='7', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='8', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='9', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='*', font_size=font_size, on_press=self.add_operation))

        gl.add_widget(Button(text='4', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='5', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='6', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='-', font_size=font_size, on_press=self.add_operation))

        gl.add_widget(Button(text='1', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='2', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='3', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='+', font_size=font_size, on_press=self.add_operation))

        gl.add_widget(Button(text='CE', font_size=font_size, on_press=self.clear))
        gl.add_widget(Button(text='0', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='.', font_size=font_size, on_press=self.add_number))
        gl.add_widget(Button(text='=', font_size=font_size, on_press=self.calc_result))
        bl.add_widget(gl)
        return bl

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if (str(instance.text) == "%"):
            self.formula = str(float(self.formula) / 100)
        elif (str(instance.text) == "√"):
            self.formula = str(sqrt(float(self.formula)))
        elif (str(instance.text) == "x^2"):
            self.formula = str(float(self.formula) ** 2)
        elif (str(instance.text) == "C"):
            self.formula = self.formula[:-1]
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        result = str(eval(self.lbl.text))
        self.formula = result
        self.lbl.text = result

    def clear(self, instance):
        self.formula = "0"
        self.update_label()


if __name__ == '__main__':
    Calculator().run()
