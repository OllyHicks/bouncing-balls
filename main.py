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
 
import pyglet
from simulator import *

def main(fullscreen = True):
    window = pyglet.window.Window(visible=False, caption="Collision", fullscreen=fullscreen)
    
    sim = Simulator(window)
    
    # clear the window and draw the scene
    @window.event
    def on_draw():
        window.clear()
        
        sim.batch.draw()
    
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

if __name__ == '__main__':
    main(False)
