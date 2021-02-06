from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

class myApp(App):
    def build(self):
        Al=AnchorLayout()
        bl = BoxLayout(orientation ='vertical', padding = [200], spacing = 15)
        bl.add_widget(Button(
            text="Жми!!!",
            font_size=14,
            on_press=self.btn_press,
            background_color=[0,0,1,1],
            background_normal='',
        ))
        bl.add_widget(Button(
            text="Не трогай меня",
            font_size=14,
            on_press=self.btn_press2,
            background_color=[0,1,0,1],
            background_normal='',
        ))
        Al.add_widget(bl)
        return Al
    def btn_press(self, instance):        
        instance.text='Спасибо'

    def btn_press2(self, instance):        
        instance.text='Я же просила'
       
        
if __name__=="__main__":
    myApp().run()
