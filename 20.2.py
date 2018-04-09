from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

n = 0

end2rus = dict()
end2rus["table"] = "стол"

def isRight(t, n):
    if end2rus["table"] == t:
        return ("Bravo!")
    else:
        return("try again" +  " осталось " + str(20 - n) + " попыток")


class Translate(FloatLayout):
    def __init__(self, **kwargs):
        super(Translate, self).__init__(**kwargs)

        self.n = -1

        self.title = Label(text = "Translate the word 'table':", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.75})
        self.add_widget(self.title)
        
        self.input = TextInput(multiline = False, text = "0", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.6})
        self.add_widget(self.input)


        self.output = Label(text = "0", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.5})
        self.update_output()
        self.add_widget(self.output)

        self.convert = Button(text = "Translate", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.4})
        self.convert.bind(on_press = self.convert_press)
        
        self.add_widget(self.convert)

        self.quit = Button(text = "Quit", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.25})
        self.quit.bind(on_press = self.quit_press)

        self.add_widget(self.quit)

    def update_output(self):
        try:
            i = self.input.text
        except:
            i = 0
            self.input.text = str(0)
        self.n = self.n + 1

        self.output.text = str(isRight(i,self.n))

    def convert_press(self, a):
        self.update_output()


    def quit_press():
        sys.exit()

class TranslatorApp(App):
    def build(self):
        return Translate()

if __name__ == '__main__':
    TranslatorApp().run()