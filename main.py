import os
from datetime import datetime

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle


class HinataApp(App):

    def build(self):
        Window.clearcolor = (0.12, 0.06, 0.18, 1)
        root = FloatLayout()

        image_path = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "hinata_ui.jpg"
        )

        background = Image(
            source=image_path,
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        root.add_widget(background)

        self.reply_label = Label(
            text="",
            font_size="16sp",
            color=(1, 1, 1, 1),
            size_hint=(0.8, 0.07),
            pos_hint={"center_x": 0.5, "center_y": 0.48}
        )
        root.add_widget(self.reply_label)

        def make_button(text, x, y, w, h, callback):
            button = Button(
                text=text,
                font_size="15sp",
                background_normal="",
                background_color=(0.25, 0.05, 0.35, 0.12),
                color=(1, 1, 1, 1),
                size_hint=(w, h),
                pos_hint={"center_x": x, "center_y": y}
            )
            button.bind(on_release=callback)
            root.add_widget(button)

        make_button("🎙️", 0.50, 0.30, 0.22, 0.13, self.voice)
        make_button("⌨️", 0.25, 0.30, 0.20, 0.08, self.keyboard)
        make_button("📷", 0.75, 0.30, 0.20, 0.08, self.camera)

        make_button("Memory", 0.16, 0.14, 0.21, 0.10, self.memory)
        make_button("AI Chat", 0.39, 0.14, 0.21, 0.10, self.chat)
        make_button("Phone\nControl", 0.62, 0.14, 0.21, 0.10, self.phone)
        make_button("Apps", 0.85, 0.14, 0.20, 0.10, self.apps)

        self.message = TextInput(
            hint_text="यहाँ संदेश लिखें...",
            multiline=False,
            size_hint=(0.70, 0.055),
            pos_hint={"x": 0.16, "y": 0.035},
            background_color=(0.20, 0.08, 0.28, 0.75),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 0.6, 1, 1),
            hint_text_color=(0.85, 0.7, 0.9, 1),
            font_size="16sp"
        )
        root.add_widget(self.message)

        send = Button(
            text="➤",
            font_size="25sp",
            background_normal="",
            background_color=(0.45, 0.12, 0.55, 0.8),
            size_hint=(0.12, 0.055),
            pos_hint={"right": 0.97, "y": 0.035}
        )
        send.bind(on_release=self.send_message)
        root.add_widget(send)
        self.message.bind(on_text_validate=self.send_message)

        return root

    def send_message(self, instance):
        message = self.message.text.strip().lower()
        if not message:
            return

        if "hello" in message or "hi" in message:
            answer = "Hello! ❤️ Kaise ho? Main HINATA hoon!"
        elif "naam" in message or "name" in message:
            answer = "Mera naam HINATA hai! 🌸"
        elif "time" in message or "समय" in message:
            answer = datetime.now().strftime("Abhi %I:%M %p ho rahe hain.")
        elif "date" in message or "तारीख" in message:
            answer = datetime.now().strftime("Aaj %d-%m-%Y hai.")
        else:
            answer = "Main sun rahi hoon! ❤️ Abhi mera AI brain jodna baaki hai."

        self.reply_label.text = answer
        self.message.text = ""

    def voice(self, instance):
        self.reply_label.text = "Voice feature jald jodega! 🎙️"

    def keyboard(self, instance):
        self.message.focus = True

    def camera(self, instance):
        self.reply_label.text = "Camera feature abhi jodna baaki hai. 📷"

    def memory(self, instance):
        self.reply_label.text = "HINATA Memory feature abhi taiyar ho raha hai. 🧠"

    def chat(self, instance):
        self.reply_label.text = "HINATA AI Chat mein swagat hai! ❤️"

    def phone(self, instance):
        self.reply_label.text = "Phone Control abhi jodna baaki hai. 📱"

    def apps(self, instance):
        self.reply_label.text = "Apps section abhi taiyar ho raha hai. 🌸"


HinataApp().run()
