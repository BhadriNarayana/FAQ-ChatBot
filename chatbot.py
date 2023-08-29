from kivymd.app import MDApp

from kivymd.uix.screen import Screen

class MyScreen(Screen):
    pass


class ChatBotApp(MDApp):
    def build(self):
        return MyScreen()


ChatBotApp().run()
        