from bardapi import Bard
import os

bard = Bard(token='eQiv-1H49tdc6RkQdcX9kshEnBerDgV4Mpt1GbjFEl1L6s9-M075uFSQeNuJ0W3TSCuEbw.')
image = open('image.jpg', 'rb').read() # (jpeg, png, webp) are supported.
bard_answer = bard.ask_about_image('What is in the image?', image)
print(bard_answer['content'])