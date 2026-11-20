import os

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
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

        return root


HinataApp().run()
