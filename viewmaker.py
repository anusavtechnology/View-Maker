from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from selenium import webdriver
import os
import time


#Window.size = (400, 520)

class View_Maker(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        kv = Builder.load_file("welcome_screen.kv")
        kv1 = Builder.load_file("main_screen.kv")
        self.theme_cls.primary_palette = "Green"
        screen_manager.add_widget(kv)
        screen_manager.add_widget(kv1)
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, dt):
        screen_manager.current="MainScreen"
    
    def close_username_dialogue(self,obj):
            self.dialog.dismiss()

    def started(self):
        url_youtube=screen_manager.get_screen('MainScreen').ids.window_opened.text
        refresht=screen_manager.get_screen('MainScreen').ids.refresh_rate.text
        url= screen_manager.get_screen('MainScreen').ids.youtube_link.text
       
        

        if url_youtube=='' or url=='' or refresht=='':
            cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Error',text = "Please enter all details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            time_to_refresh=int(screen_manager.get_screen('MainScreen').ids.refresh_rate.text)
            no_of_driver=int(screen_manager.get_screen('MainScreen').ids.window_opened.text)
            drivers=[]
            for i in range(no_of_driver):
                drivers.append(webdriver.Chrome("/home/anuragvats/Desktop/view-maker/chromedriver"))
                drivers[i].get(url)
            while True:
                time.sleep(time_to_refresh)
                for i in range(no_of_driver):
                    drivers[i].refresh()

View_Maker().run()