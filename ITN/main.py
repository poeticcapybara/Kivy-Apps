import kivy
kivy.require('1.7.2') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import os
from PIL import Image as PILImage
import webbrowser

class ITNApp(App):

    icon = 'icon.png'
    def build(self):
        #define the carousel
        carousel = Carousel(direction='right',loop='true')
        filenames = [filename for filename in os.listdir('.') if filename.endswith('.jpg') or filename.endswith('.jpeg')]
        for imagefile in filenames:
            if 'Strike' in imagefile:
                imgsize = PILImage.open(imagefile).size
                image = Image(source=imagefile,size_hint = (1,1))
                carousel.add_widget(image)
            else:
                layout = BoxLayout()
                #load pictures from images folder
                imgsize = PILImage.open(imagefile).size
                image = Image(source=imagefile,size_hint = (.5,1))
                text_esr = open('text_'+imagefile.split('.')[0]+'.txt').read()
                label = Label(text=str(text_esr), halign='left',markup=True)
                label.bind(on_ref_press=self.print_it)
                layout.add_widget(image)
                layout.add_widget(label)
                carousel.add_widget(layout)
        itn_text = open('text_itn.txt').read()
        label = Label(text=str(itn_text), halign='left',markup=True)
        carousel.add_widget(label)
        
        return carousel
        
    def print_it(self,instance,value):
        print('User clicked on',value)
        webbrowser.open(value)
        
    def on_pause(self):
        return True
        
    def on_resume(self):
        pass

if __name__ == '__main__':
    ITNApp().run()
