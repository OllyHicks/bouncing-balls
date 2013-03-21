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
import itertools
 
import pyglet
from pyglet.gl import *


from ball import *

class Simulator:
    
    num_balls = 8
    dist_matrix = []
    
    
    def __init__(self, window):
        self.batch = pyglet.graphics.Batch()
        self.window = window
        
        
        max_radius = 20
        
        fitted = False
        while fitted == False:
            self.balls = []
            for n in range(0, self.num_balls):
                radius = int(max_radius * 0.8 *random.random() + max_radius * 0.2)
                
                radius = max_radius
                ball = Ball(self, radius)
                
                for i in range(100):
                    ball.x = int(radius + (self.window.width - 2 * radius) * random.random())
                    ball.y = int(radius + (self.window.height - 2 * radius) * random.random())
                    
                    fitted = not self.detect_collision(ball)
                    
                    if fitted:
                        break
                        
                if fitted:
                    self.balls.append(ball)
                else:
                    break
            
            if max_radius <= 10:
                raise Exception('Two many balls, not enough space')
            max_radius = int(max_radius * 0.8)
            
                
    def update(self, dt):
        for ball in self.balls:
            ball.update(dt)
        
        for collision in self.detect_all_collisions():
            self.simulat_ball_collision(collision[0], collision[1])
    
    
    def detect_collision(self, ball, other_balls=None):
        if other_balls == None:
            other_balls = self.balls
    
        for other_ball in other_balls:
            if not ball == other_ball:
                min_dist = ball.radius + other_ball.radius
                
                dist = math.sqrt((ball.x - other_ball.x)**2 + (ball.y - other_ball.y)**2)
                
                if dist <= min_dist:
                    return True
                    
        return False
        
    

    def detect_all_collisions(self):
        collisions = []
        
        combs = itertools.combinations(self.balls, 2)
        
        for ball_1, ball_2 in combs:
            if self.detect_collision(ball_1, [ball_2]):
                collisions.append((ball_1, ball_2))
                
        return collisions
    
    def simulat_ball_collision(self, ball_1, ball_2):
        ball_1.vx = ball_1.vy = 0
        ball_2.vx = ball_2.vy = 0
