from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class HinataApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        root.add_widget(Label(
            text='HINATA AI',
            font_size=30,
            size_hint_y=0.2
        ))

        root.add_widget(Label(
            text='Hello! I am HINATA. How can I help you?',
            font_size=18
        ))

        self.msg = TextInput(
            hint_text='Type your message...',
            multiline=False,
            size_hint_y=0.15
        )

        root.add_widget(self.msg)

        btn = Button(
            text='SEND',
            size_hint_y=0.15
        )

        root.add_widget(btn)

        return root

HinataApp().run()
