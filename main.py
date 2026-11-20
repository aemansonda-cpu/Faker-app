"""
LiteBrowser: a no-page browser handler.

When Android launches this app for an http/https link, it exits cleanly.
It does not load the URL, open another browser, or request internet access.
"""
from kivy.app import App
from kivy.clock import Clock


class LiteBrowserApp(App):
    def build(self):
        # Return a tiny empty root widget; quit after Android finishes launching us.
        from kivy.uix.widget import Widget
        Clock.schedule_once(lambda _dt: self.stop(), 0.15)
        return Widget()


if __name__ == "__main__":
    LiteBrowserApp().run()
