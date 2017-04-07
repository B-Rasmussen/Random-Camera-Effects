from picamera import PiCamera
from time import sleep
import random

camera = PiCamera()
camera.resolution = (640,480)

#camera effects
effect = ('negative','solarize','sketch','denoise','emboss','oilpaint','hatch','gpen',
          'pastle','watercolor','film','blur','saturation','colorswap','washedout','posterise',
          'colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2');

camera.image_effect = random.choice(tuple(effect))

camera.start_preview()
print('preview started')
print(camera.image_effect)
sleep(3)
camera.stop_preview()
