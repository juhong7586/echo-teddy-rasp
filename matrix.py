#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time


from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import ImageDraw




def draw_smiley(n):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=0)
    
    with canvas(device) as draw:
        # Draw eyes
        draw.point((2, 2), fill="white")
        draw.point((5, 2), fill="white")
        
        # Draw mouth (smile)
        draw.arc((1, 3, 6, 6), start=0, end=180, fill="white")
    
    time.sleep(3)

def draw_sad_face(n):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=0)
    
    with canvas(device) as draw:
        # Draw eyes
        draw.point((2, 2), fill="white")
        draw.point((5, 2), fill="white")
        
        # Draw mouth (sad)
        draw.arc((2, 5, 5, 8), start=180, end=360, fill="white")

    time.sleep(3)