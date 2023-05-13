import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set("graphics", "width", 600)
Config.set("graphics", "height", 400)

class Bandera_Italiana(BoxLayout):
    None

class main2App(App):
    title = "Bandera Italiana"
    def build(self):
        return Bandera_Italiana()
    
if __name__ == "__main__":
    main2App().run()