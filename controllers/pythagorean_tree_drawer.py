import turtle


class TreeDrawer:
    def __init__(self, size, angle, thickness):
        self.size = size
        self.angle = angle
        self.thickness = thickness
        self.t = turtle.Turtle()
        self.t.left(90)
        self.t.speed(20)

    def draw_tree(self, level):
        self.__draw_tree(self.t, self.size, self.angle, level, self.thickness)

    def __draw_tree(self, t, size, angle, level, thickness):
        if level > 0:
            turtle.colormode(255)
            t.pencolor(0, 255 // level, 0)
            t.pensize(thickness)
            t.forward(size)
            t.right(angle)

            self.__draw_tree(t, 0.8 * size, angle, level - 1, thickness * 0.8)
            t.pencolor(0, 255 // level, 0)
            t.left(2 * angle)

            self.__draw_tree(t, 0.8 * size, angle, level - 1, thickness * 0.8)
            t.pencolor(0, 255 // level, 0)
            t.right(angle)

            t.forward(-size)


def draw_pythagorean_tree_task():
    recursion_level = int(input("Enter the recursion depth ==> "))
    angle = 30
    branch_length = 130
    window = turtle.Screen()
    try:
        tree_drawer = TreeDrawer(branch_length, angle, 8)
        tree_drawer.draw_tree(recursion_level)
        window.mainloop()
    except:
        print("The window was closed before the recursion finished.")
