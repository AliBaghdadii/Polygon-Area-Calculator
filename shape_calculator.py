class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self) -> float:
        return self.width * self.height
    
    def get_primeter(self) -> float:
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self) -> str:
        if (self.width > 50 or self.height > 50):
            return 'Too big for picture.'
        else:
            picture = ''
            for row in range(0, self.height):
                picture += '*' * (self.width) + '\n'
            return picture
        
    def get_amount_inside(self, otherShape) -> int:
        return round((self.get_area()/otherShape.get_area())-0.5)
    
class Square(Rectangle):
    def __init__(self, side):
        self.height = self.width = side
        
    def __str__(self) -> str:
        return f'Square(side={self.width})'
    
    def set_width(self, side):
        self.width = self.height = side
        
    def set_height(self, side):
        self.width = self.height = side
        
    def set_side(self, side):
        self.width = self.height = side