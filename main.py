import os

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window



class IconButton(Button):
    def __init__(self, icon_type, label_text, **kwargs):
        super().__init__(**kwargs)
        self.text = ""

        content = BoxLayout(
            orientation="horizontal",
            spacing=4,
            padding=(8, 0),
            size_hint=(1, 1)
        )

        icon_path = os.path.join(
            os.path.dirname(__file__),
            "assets",
            f"{icon_type}.png"
        )

        icon = Image(
            source=icon_path,
            size_hint=(0.32, 0.72),
            allow_stretch=True,
            keep_ratio=True
        )

        label = Label(
            text=label_text,
            font_size="13sp",
            color=(1, 1, 1, 1),
            halign="left",
            valign="middle",
            size_hint=(0.68, 1)
        )

        content.add_widget(icon)
        content.add_widget(label)
        self.add_widget(content)


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
            ("Voice", "voice", 0.84),
            ("Chat", "chat", 0.71),
            ("Camera", "camera", 0.58),
            ("Memory", "memory", 0.45),
            ("Phone", "phone", 0.32),
            ("Apps", "apps", 0.19),
        ]

        for name, icon_type, y in buttons:
            button = IconButton(
                icon_type=icon_type,
                label_text=name,
                font_size="13sp",
                size_hint=(0.29, 0.075),
                pos_hint={"center_x": 0.83, "center_y": y},
                background_normal="",
                background_color=(0.35, 0.15, 0.50, 0.48),
                color=(1, 1, 1, 1)
            )
            root.add_widget(button)

        waveform_path = os.path.join(
            os.path.dirname(__file__), "assets", "waveform.png"
        )
        waveform = Image(
            source=waveform_path,
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(0.65, 0.09),
            pos_hint={"center_x": 0.48, "center_y": 0.07}
        )
        root.add_widget(waveform)

        return root





if __name__ == "__main__":
    HinataApp().run()
