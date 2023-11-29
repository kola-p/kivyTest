from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder


Window.size = (250, 200)
Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class MyApp(App):
    def write_to_file(self, *_):
        if self.filepath.text:
            file = self.filepath.text
            try:
                with open(file, 'a') as file:
                    file.write(self.to_write.text + '\n')
                    self.label.text = "Writing to the file was successful"
            except Exception as e:
                print(e)
        else:
            self.label.text = 'Enter path to file'

    def create_file(self, *_):
        if self.filepath.text:
            file = self.filepath.text
            try:
                open(file, 'w').close()
                self.label.text = "File created"
            except Exception as e:
                print(e)
        else:
            self.label.text = 'Enter path to file'

    def read_file(self, *_):
        if self.filepath.text:
            file = self.filepath.text
            try:
                with open(file, 'r') as file:
                    self.label.text = str(file.read())
            except Exception as e:
                self.label.text = str(e)
        else:
            self.label.text = 'Enter path to file'

    def __init__(self):
        super().__init__()
        self.label = ScrollableLabel(text="")
        self.create_button = Button(text='Create file')
        self.read_button = Button(text="Read file")
        self.write_button = Button(text='Write to file')
        self.filepath = TextInput(hint_text="Path to file")
        self.to_write = TextInput(hint_text="Write something")

        self.read_button.bind(on_press=self.read_file)
        self.create_button.bind(on_press=self.create_file)
        self.write_button.bind(on_press=self.write_to_file)

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.filepath)
        box.add_widget(self.create_button)
        box.add_widget(self.read_button)
        box.add_widget(self.write_button)
        box.add_widget(self.to_write)
        box.add_widget(self.label)
        return box


if __name__ == "__main__":
    MyApp().run()
