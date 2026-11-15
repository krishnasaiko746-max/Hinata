from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class HinataApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        self.output = Label(
            text="Hello! I am HINATA ❤️\nNamaste! Main HINATA hoon.",
            font_size=20
        )
        root.add_widget(self.output)

        self.msg = TextInput(
            hint_text="Type in Hindi or English...",
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

        if any(word in message for word in ["hello", "hi", "नमस्ते", "हेलो"]):
            answer = "Hello! ❤️ Namaste! Kaise ho?"
        elif any(word in message for word in ["name", "naam", "नाम"]):
            answer = "My name is HINATA AI. Mera naam HINATA hai! 🤖"
        elif any(word in message for word in ["how are you", "kaisi ho", "कैसी हो", "कैसे हो"]):
            answer = "I am fine! Main bilkul theek hoon. 😊"
        elif any(word in message for word in ["thank", "धन्यवाद", "शुक्रिया"]):
            answer = "You're welcome! Koi baat nahi! ❤️"
        elif any(word in message for word in ["bye", "good night", "अलविदा"]):
            answer = "Goodbye! Phir milenge! ❤️"
        else:
            answer = "I am listening! Main sun rahi hoon. Aur batao! ❤️"

        self.output.text = answer
        self.msg.text = ""

HinataApp().run()
