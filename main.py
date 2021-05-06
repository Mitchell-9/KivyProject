from kivy.app import App
import structure
import config

class WormApp(App):
    def build(self):
        self.config = config.Config()
        self.form = structure.Form(self.config)
        return self.form

    def on_start(self):
        self.form.start()


if __name__ == '__main__':
    WormApp().run()