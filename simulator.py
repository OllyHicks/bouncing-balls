#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simulator.py
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
from pyglet.gl import *


from ball import *

class Simulator:
    
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        
        self.balls = []
        
        self.balls.append(Ball(self, 20))
                
    def update(self, dt):
        for ball in self.balls:
            ball.update(dt)
