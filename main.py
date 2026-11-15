from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class HinataApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        self.output = Label(
            text="Hello! I am HINATA ❤️\nHow can I help you?",
            font_size=20
        )
        root.add_widget(self.output)

        self.msg = TextInput(
            hint_text="Type your message...",
            multiline=False,
            size_hint_y=0.15
        )
        root.add_widget(self.msg)

        btn = Button(text="SEND", size_hint_y=0.15)
        btn.bind(on_press=self.reply)
        root.add_widget(btn)

        return root

    def reply(self, instance):
        message = self.msg.text.lower().strip()

        if "hello" in message or "hi" in message:
            answer = "Hello! ❤️ I am HINATA."
        elif "name" in message:
            answer = "My name is HINATA AI. 🤖"
        elif "how are you" in message:
            answer = "I am fine! How are you? 😊"
        else:
            answer = "I am listening! Tell me more. ❤️"

        self.output.text = answer
        self.msg.text = ""

HinataApp().run()
