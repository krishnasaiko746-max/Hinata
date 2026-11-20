import os

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


class HinataApp(App):

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        root = FloatLayout()

        image_path = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "hinata_final.png"
        )

        background = Image(
            source=image_path,
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        root.add_widget(background)

        buttons = [
            ("🎙 Voice", 0.84),
            ("💬 Chat", 0.71),
            ("📷 Camera", 0.58),
            ("🧠 Memory", 0.45),
            ("📞 Phone", 0.32),
            ("📱 Apps", 0.19),
        ]

        for name, y in buttons:
            button = Button(
                text=name,
                font_size="13sp",
                size_hint=(0.29, 0.075),
                pos_hint={"center_x": 0.83, "center_y": y},
                background_normal="",
                background_color=(0.35, 0.15, 0.50, 0.48),
                color=(1, 1, 1, 1)
            )
            root.add_widget(button)

        waveform = Label(
            text="▂  ▄  ▆  █  ▆  ▄  ▂",
            font_size="25sp",
            color=(0.85, 0.65, 1, 1),
            size_hint=(0.65, 0.09),
            pos_hint={"center_x": 0.48, "center_y": 0.07}
        )
        root.add_widget(waveform)

        return root





if __name__ == "__main__":
    HinataApp().run()
