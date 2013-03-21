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
    
    num_balls = 3
    dist_matrix = []
    
    _prev_collisions = []
    
    def __init__(self, window):
        self.batch = pyglet.graphics.Batch()
        self.window = window
        
        self.balls = [
            Ball(self, 100, 200, 200),
            Ball(self, 50, 400, 400),
            Ball(self, 20, 30, 30)
        ]
        
        return 
        
        
        max_radius = 100
        
        fitted = False
        while fitted == False:
            self.balls = []
            for n in range(0, self.num_balls):
                radius = int(max_radius * 0.8 *random.random() + max_radius * 0.2)
                
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
        
        collisions = self.detect_all_collisions()
        
        for collision in collisions:
            if not collision in self._prev_collisions:
                self.simulat_ball_collision(collision[0], collision[1])
            
        self._prev_collisions = collisions
    
    
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
        #ball_1.vx = ball_1.vy = 0
        #ball_2.vx = ball_2.vy = 0
        
        normal_line = math.atan((ball_2.y - ball_1.y)/(1.0*(ball_2.x- ball_1.x)))
        
        print
        print 'angle:', normal_line
        print 'pos:', ball_1.x, ball_1.y
        print 'vel (x,y):', ball_1.vx, ball_1.vy
        
        # Rotate direction
        ball_1_vn = ball_1.vx * math.cos(-normal_line) - ball_1.vy * math.sin(-normal_line)
        ball_1_vt = ball_1.vy * math.cos(-normal_line) + ball_1.vx * math.sin(-normal_line)
        
        ball_2_vn = ball_2.vx * math.cos(-normal_line) - ball_2.vy * math.sin(-normal_line)
        ball_2_vt = ball_2.vy * math.cos(-normal_line) + ball_2.vx * math.sin(-normal_line)
        
        print 'vel (n,t):', ball_1_vn, ball_1_vt
        print 
        
        # Do collision
        #ball_1_vn = -1 * ball_1_vn
        #ball_2_vn = -1 * ball_2_vn
        ball_1_vn, ball_2_vn = ball_2_vn, ball_1_vn
        
        # Rotate back
        ball_1.vx = ball_1_vn * math.cos(normal_line) - ball_1_vt * math.sin(normal_line)
        ball_1.vy = ball_1_vt * math.cos(normal_line) + ball_1_vn * math.sin(normal_line)
        
        ball_2.vx = ball_2_vn * math.cos(normal_line) - ball_2_vt * math.sin(normal_line)
        ball_2.vy = ball_2_vt * math.cos(normal_line) + ball_2_vn * math.sin(normal_line)

        #pyglet.clock.unschedule(self.update)
