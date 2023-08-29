from kivymd.app import MDApp

from kivymd.uix.screen import Screen

from kivy.uix.textinput import TextInput


import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = joblib.load('data/vectorizer.pkl')
data = pd.read_csv('data/Mental_Health_FAQ.csv')
data.drop(columns = ['Question_ID'], inplace = True)
data['col'] = data['Questions'] + data['Answers']

x = vectorizer.transform(data['col'])


class MyScreen(Screen):
    def ask(self):
        container = self.ids.container
        q_content = self.ids.qry.text 
        q_w = TextInput(text = q_content, size_hint_y = None)

        container.add_widget(q_w)
        self.ids.qry.text = ""

        transformed_q = vectorizer.transform([q_content])

        similarities = cosine_similarity(transformed_q, x)
        maxarg = np.argmax(similarities, axis = 1)

        a_content = data['Answers'].iloc[maxarg].values[0]
        a_w = TextInput(text = a_content, size_hint_y = None)

        container.add_widget(a_w)


class ChatBotApp(MDApp):
    def build(self):
        return MyScreen()


ChatBotApp().run()
        