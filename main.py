"""LiteBrowser: a lightweight HTTP/HTTPS link sink for Android.

When Android hands this app a web link, it intentionally does not open the
page or forward it to another browser; it exits. Opening the app from its icon
shows setup instructions instead.
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class LiteBrowserApp(App):
    def is_web_link_launch(self):
        """Return True only when Android launched us to handle an HTTP(S) link."""
        if platform != "android":
            return False

        try:
            from jnius import autoclass

            activity = autoclass("org.kivy.android.PythonActivity").mActivity
            intent = activity.getIntent()
            if intent is None or intent.getAction() != "android.intent.action.VIEW":
                return False

            data = intent.getData()
            if data is None:
                return False

            scheme = data.getScheme()
            return scheme is not None and scheme.lower() in ("http", "https")
        except Exception:
            # If Android intent inspection is unavailable, show help rather than
            # unexpectedly closing the app.
            return False

    def build(self):
        if self.is_web_link_launch():
            # Let Android finish delivering the link intent, then dismiss this
            # activity. The URL is deliberately neither opened nor forwarded.
            Clock.schedule_once(lambda _dt: self.stop(), 0.1)
            return Widget()

        layout = BoxLayout(orientation="vertical", padding=24, spacing=16)
        title = Label(
            text="LiteBrowser",
            font_size="24sp",
            size_hint_y=None,
            height="48dp",
        )
        instructions = Label(
            text=(
                "This app dismisses web links instead of opening a browser.\n\n"
                "To use it, choose LiteBrowser as your phone's default browser "
                "or select it when Android asks which app should open a link.\n\n"
                "It cannot stop apps that launch Chrome directly, and it does "
                "not block ads inside other apps or websites."
            ),
            halign="center",
            valign="middle",
        )
        instructions.bind(
            size=lambda label, size: setattr(label, "text_size", size)
        )
        close_button = Button(text="Close", size_hint_y=None, height="48dp")
        close_button.bind(on_press=lambda _button: self.stop())

        layout.add_widget(title)
        layout.add_widget(instructions)
        layout.add_widget(close_button)
        return layout


if __name__ == "__main__":
    LiteBrowserApp().run()
