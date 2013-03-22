#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 Olly Hicks <olly@olly-laptop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import math
import random

import subprocess
import tempfile
 
import pyglet
from simulator import *

def main(fullscreen = True):
    
    screenshot = None
    
    if fullscreen:
        screenshot = get_screenshot()
        window = pyglet.window.Window(fullscreen=True)
        window.set_mouse_visible(False)
    else:
        window = pyglet.window.Window(visible=False, caption="Collision")
        
    sim = Simulator(window)
    
    # clear the window and draw the scene
    @window.event
    def on_draw():
        window.clear()
        if not screenshot == None:
            screenshot.blit(0, 0)
        sim.batch.draw()
        
    @window.event
    def on_key_press(symbol, modifiers):
        pyglet.app.exit()
    
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        pyglet.app.exit()
        
    def on_mouse_press(x, y, button, modifiers):
        pyglet.app.exit()
    
    # schedule the update function, 60 times per second
    pyglet.clock.schedule_interval(sim.update, 1.0/60.0)
    
    # clear and flip the window, otherwise we see junk in the buffer before the first frame
    window.clear()
    window.flip()
     
    # make the window visible at last
    window.set_visible(True)
     
    # finally, run the application
    pyglet.app.run()
    
    return 0

def get_screenshot():
    handle, path = tempfile.mkstemp('.png')
    subprocess.call(['import', '-window',  'root', path])
    return pyglet.image.load(path)

if __name__ == '__main__':
    main(True)
