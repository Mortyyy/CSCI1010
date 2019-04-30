# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:50:10 2019

@author: Alex
"""
from PIL import Image

img = Image.open("Flower.jfif")

w = img.width
h = img.height

""" PART A """
#Shrinks the image to one-eighth of the original.
scaled = img.resize((w//8, h//8), resample=0)
scaled.show()


""" PART B """
newimg = img.resize((w//4, h//4), resample=0)
newimg.show()

blank = Image.new('RGB',(w,h))
blank.paste(newimg,(0,0))
blank.show()
blank.paste(newimg,(0, h//4))
blank.show()
blank.paste(newimg,(w//4, h//4))
blank.paste(newimg,(w//4, 0))
blank.show()
