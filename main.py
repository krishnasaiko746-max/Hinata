
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


class HinataApp(App):

    def build(self):
        Window.clearcolor = (0.06, 0.07, 0.12, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=12
        )

        self.output = Label(
            text="Hello! ❤️ Main HINATA hoon.\nBatao, main tumhari kya help kar sakti hoon?",
            font_size=19,
            halign="center",
            valign="middle"
        )
        root.add_widget(self.output)

        self.msg = TextInput(
            hint_text="Yahan message likho...",
            multiline=False,
            size_hint_y=0.15
        )
        root.add_widget(self.msg)

        btn = Button(
            text="SEND",
            size_hint_y=0.15
        )
        btn.bind(on_press=self.reply)
        root.add_widget(btn)

        self.msg.bind(on_text_validate=self.reply)

        return root

    def reply(self, instance):
        message = self.msg.text.lower().strip()

        if not message:
            return

        if any(w in message for w in ["hello", "hi", "नमस्ते", "हेलो"]):
            answer = "Hello! ❤️ Kaise ho? Main yahin hoon!"

        elif any(w in message for w in ["your name", "naam", "नाम"]):
            answer = "Mera naam HINATA hai! 🤖"

        elif any(w in message for w in ["how are you", "kaisi ho", "कैसी हो", "कैसे हो"]):
            answer = "Main bilkul theek hoon! Tum kaise ho? 😊"

        elif any(w in message for w in ["time", "समय", "टाइम"]):
            answer = "Abhi ka time hai: " + datetime.now().strftime("%I:%M %p")

        elif any(w in message for w in ["date", "तारीख", "आज कौन सा दिन"]):
            answer = "Aaj ki date hai: " + datetime.now().strftime("%d-%m-%Y")

        elif any(w in message for w in ["thank", "धन्यवाद", "शुक्रिया"]):
            answer = "You're welcome! ❤️ Main hamesha help ke liye hoon."

        elif any(w in message for w in ["help", "मदद", "मदद करो"]):
            answer = "Bilkul! Batao, tumhe kis cheez mein help chahiye?"

        elif any(w in message for w in ["who made you", "kisne banaya", "तुम्हें किसने बनाया"]):
            answer = "Mujhe tum bana rahe ho! ❤️ Main HINATA hoon."

        elif any(w in message for w in ["bye", "good night", "अलविदा"]):
            answer = "Bye! Apna khayal rakhna. ❤️"

        else:
            answer = "Main tumhari baat samajhne ki koshish kar rahi hoon. Thoda aur batao? ❤️"

        self.output.text = answer
        self.msg.text = ""


HinataApp().run()

