from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivymd.uix.dialog import MDDialog
import math


class HomeScreen(Screen):
    weight = NumericProperty(40)
    slider_value_txt = StringProperty('40')
    
    def getvalue(self):
        slider_height_value = self.ids.height_value
        # print(slider_height_value.value)

    def increase(self):
        self.weight = self.weight + 1
        
    def decrease(self):
        self.weight = self.weight - 1

    def calculate_bmi(self):
        height = round(self.ids.height_value.value) / 100
        height_squared = height * height
        bmi = self.weight / height_squared
        
        weight_range = 'normal'
        if bmi < 18.5:
            weight_range = 'under weight'
        elif bmi >= 18.5 and bmi <= 24.9:
            weight_range = 'normal'
        elif bmi >= 25 and bmi <= 29.9:
            weight_range = 'over weight'
        elif bmi > 30:
            weight_range = 'obese'
        # print(bmi)
        
        
        dialog = MDDialog(
            title='BMI',
            text=f'Your bmi is {round(bmi)}\n your category is {weight_range}',
            size_hint=[.8,.5]
        )
        dialog.open()
        
    
    def on_slider_value(self, widget):
        # print('slider ' + str(int(widget.value)))
        self.slider_value_txt = str(int(widget.value))
        self.slider_value_txt_foot = str(int(widget.value / 30.48) )
        

class BmiCalculatorApp(MDApp):
    def __init__(self):
        super().__init__()
        Window.size = (400, 600)

        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = '500' # 200
        self.theme_cls.theme_style = 'Dark'  # 'Light'

BmiCalculatorApp().run()