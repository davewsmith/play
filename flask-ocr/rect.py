"""
Represent a Rect(angle), primarily to calculate intersections.

Note: Reuse at your own risk. This is minimal code, and isn't robust to garbage inputs.
"""
class Rect:
    __slots__ = ['x1', 'y1', 'x2', 'y2']

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __eq__(self, other):
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

    def __repr__(self):
        return "Rect({},{}:{},{})".format(self.x1, self.y1, self.x2, self.y2)

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def area(self):
        return self.width * self.height

    def intersect(self, other):
        """Returns intersecting rect, or None if no intersection"""

        if self.x1 >= other.x2 or other.x1 >= self.x2:
            return None
        if self.y1 >= other.y2 or other.y1 >= self.y2:
            return None

        return Rect(max(self.x1, other.x1),
                    max(self.y1, other.y1),
                    min(self.x2, other.x2),
                    min(self.y2, other.y2))
                    
