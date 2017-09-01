# Defines two classes, Point() and NonVerticalLine().
# An object for the second class is created by passing named arguments,
# point_1 and point_2, to its constructor.
# Such an object can be modified by changing one point or both points thanks to the
# function change_point_or_points().
# At any stage, the object maintains correct values for slope and intersect.
#
# Written by Mingkai Ma and Eric Martin for COMP9021


class Point():
    def __init__(self, x = None, y = None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        elif x == None or y == None:
            print('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y


class NonVerticalLine:
    def __init__(self, *, point_1, point_2):
        if not self._check_and_initialise(point_1, point_2):
            print('Incorrect input, line not created.')
            return

    def change_point_or_points(self, *, point_1 = None, point_2 = None):
        if not self._change_point_or_points(point_1, point_2):
            print('Could not perform this change.')
            return

    def _check_and_initialise(self, p1, p2):
        if p1.x == p2.x:
            return False
        else:
            self.p1 = p1
            self.p2 = p2
            self._slope()
            self._intercept()
            return True
        
    def _change_point_or_points(self, p1, p2):
        if p1 is not None and p2 is not None:
            if p1.x == p2.x:
                return False
            else:
                self.p1 = p1
                self.p2 = p2
                self._slope()
                self._intercept()
                return True
        elif p1 is None and p2 is not None:
            if self.p1.x == p2.x:
                return False
            else:
                self.p2 = p2
                self._slope()
                self._intercept()
                return True
        elif p1 is not None and p2 is None:
            if self.p2.x == p1.x:
                return False
            else:
                self.p1 = p1
                self._slope()
                self._intercept()
                return True
        elif p1 is None and p2 is None:
            self._slope()
            self._intercept()
            return True

    def _slope(self):
        self.slope = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def _intercept(self):
        self.intercept = self.p1.y - self.slope * self.p1.x
        
