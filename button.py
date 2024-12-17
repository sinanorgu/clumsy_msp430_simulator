from text import *
class button():
    def __init__(self,string="Button",x=50,y=5,len_x=100,len_y=50):
        self.x=x
        self.y=y
        self.len_x=len_x
        self.len_y=len_y
        self.on_mouse_color=(0,255,0)
        self.out_mouse_color=(0,0,255)
        self.color=self.out_mouse_color
        self.string=string
        self.text_render=text.print_text(self.string)
        self.clicked=False
        self.margins = [10,15]

    def is_on_mouse(self):
        x,y=pygame.mouse.get_pos()
        if self.x<x<self.x+self.len_x and self.y<y<self.y+self.len_y:
            return True
        else:
            False

    def draw(self,pencere):
        if self.is_on_mouse():
            self.color=self.on_mouse_color
        else:
            self.color=self.out_mouse_color
        if self.color is not None:
            pygame.draw.rect(pencere,self.color,(self.x,self.y,self.len_x,self.len_y),0)
        pencere.blit(self.text_render, (self.x +self.margins[0], self.y + self.margins[1]))

    def is_click(self):
        if pygame.mouse.get_pressed()[0] and self.is_on_mouse():
            if self.clicked==False:
                self.clicked=True
                return True
        else:
            self.clicked=False
        return False
    def update_string(self,string):
        self.string = string
        self.text_render=text.print_text(self.string)
