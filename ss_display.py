import numpy as np
import pygame


class display:
    def __init__(self,position = [400,400] ) -> None:
        self.position = np.array(position)
        self.size = 30
        self.on_color = (0,255,0)
        self.off_color = (0,75,0)
        

    def draw(self,pencere:pygame.surface.Surface,input_value:str):
        h,g,f,e,d,c,b,a = list(input_value)
        

        color = self.on_color if a == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position,self.position+np.array([self.size,0]),self.size//10)
        
        color = self.on_color if b == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position+np.array([self.size,0]),self.position+np.array([self.size,self.size]),self.size//10)
        
        color = self.on_color if c == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position+np.array([self.size,self.size]),self.position+np.array([self.size,self.size*2]),self.size//10)
        
        color = self.on_color if d == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position+np.array([0,2*self.size]),self.position+np.array([self.size,2*self.size]),self.size//10)
        
        color = self.on_color if e == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position+np.array([0,self.size]),self.position+np.array([0,2*self.size]),self.size//10)
        
        color = self.on_color if f == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position,self.position+np.array([0,self.size]),self.size//10)
        
        color = self.on_color if g == '1' else self.off_color
        pygame.draw.line(pencere,color,self.position+np.array([0,self.size]),self.position+np.array([self.size,self.size]),self.size//10)
        
        color = self.on_color if h == '1' else self.off_color
        pygame.draw.circle(pencere,color,self.position+np.array([self.size,self.size*2])*1.2,self.size//7)
        