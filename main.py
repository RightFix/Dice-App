from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from random import randint

class Screen1(MDScreen):
  pass
class Screen2(MDScreen):
   pass
        
class MainApp(MDApp):
    def build(self):
      return super().build()
      
    ran = randint
        
MainApp().run()