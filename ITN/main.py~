import kivy
kivy.require('1.7.2') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.image import Image

import os
from PIL import Image as PILImage

class AmnaApp(App):

    def build(self):
        #define the carousel
        carousel = Carousel(direction='right',loop='true')
        filenames = [filename for filename in os.listdir('.') if filename.endswith('.jpg') or filename.endswith('.jpeg')]
        for imagefile in filenames:
            #load pictures from images folder
            imgsize = PILImage.open(imagefile).size
            image = Image(source=imagefile,pos=(0,0), size=imgsize)
            carousel.add_widget(image)
        return carousel
        
    def on_pause(App):
        return True
        
    def on_resume(App):
        pass

if __name__ == '__main__':
    AmnaApp().run()
