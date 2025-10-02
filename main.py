from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput

class StickerBoardApp(App):

    def build(self):
        self.main_layout = FloatLayout()
        self.title = 'Stickerboard'

        add_btn = Button(text="Add Sticker", size_hint=(0.15,0.08), pos_hint={'x':0.05,'y':0.88})
        add_btn.bind(on_press = self.add_sticker)
        self.main_layout.add_widget(add_btn)

        save_btn = Button(text="Save Board", size_hint=(0.15,0.08), pos_hint={'x':0.22,'y':0.88})
        save_btn.bind(on_press = self.save_board)
        self.main_layout.add_widget(save_btn)

        self.board = FloatLayout(size_hint=(0.9, 0.8), pos_hint={'x':0.05, 'y':0.05})
        self.main_layout.add_widget(self.board)

        return self.main_layout
    
    def add_sticker(self, instance):

        box = BoxLayout(orientation='vertical')

        chooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'], multiselect=True)
        box.add_widget(chooser)

        def select_image(instance):
            selected = chooser.selection
            if selected:
                for file in selected:
                    # Create image widget
                    scatter = Scatter(size_hint=(None, None),size=(150,150),pos = (200,200))
                    img = Image(source=file)
                    scatter.add_widget(img)
                    self.board.add_widget(scatter)
                popup.dismiss()

        select_btn = Button(text="Select", size_hint=(1, 0.1))
        select_btn.bind(on_press=select_image)
        box.add_widget(select_btn)
        
        popup = Popup(title='Select Image(s)', content= box, size_hint=(0.9, 0.9))
        popup.open()

    def save_board(self,instance):
        
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)

        name_input = TextInput(hint_text='Enter file name', multiline=False)
        box.add_widget(name_input)

        def save_image_to_folder(instance):
            
            name = name_input.text.strip()

            if name:
                if not name.endswith('.png'):
                    name += '.png'

                    self.board.export_to_png(name)
                    popup.dismiss()

        save_image = Button(text="Save", size_hint=(1, 0.3))
        save_image.bind(on_press=save_image_to_folder)
        box.add_widget(save_image)

        popup = Popup(title='Save Sticker Board', content=box, size_hint=(0.5, 0.4))
        popup.open()



        

StickerBoardApp().run()


