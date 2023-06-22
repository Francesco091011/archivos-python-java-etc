from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest

class EncuentraTemperatura(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        Window.size=(360,640)
        self.window.add_widget(Image(source="logo.png"))

        self.input_texto = TextInput(
            size_hint=(1, 0.2),
            font_size ='20sp',
            padding_y='12sp',
            halign='center'
        )
        self.window.add_widget(self.input_texto)

        self.input_boton = Button(
            text="Enter",
            size_hint=(1, 0.2),
            bold=True,
            background_color='#0099ff'
        )
        self.window.add_widget(self.input_boton)

        self.input_boton.bind(on_press=self.encuentra_temp)
        self.input_etiqueta = Label(
            text="Busca una ciudad...",
            font_size='20sp',
            color="#007dd1"
        )
        self.window.add_widget(self.input_etiqueta)
        
        return self.window
    
    def encuentra_temp(self, instance):
        def edit_label(request, result):
            temp = result['main']['temp']
            self.input_etiqueta.text=f"Hoy a {self.input_texto.text} hace {temp} °C"
        link=f"https://api.openweathermap.org/data/2.5/weather?q={self.input_texto.text}&appid=ef6843615275f022d431cb04f5381b3d&units=metric"
        UrlRequest(link, edit_label)

if __name__ == "__main__":
    EncuentraTemperatura().run()
