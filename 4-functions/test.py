# -*- coding:utf8 -*-

import turtle 

# Is called when the program start 
def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    
    # draw square
    draw_square(dave)

    turtle.mainloop()
    
# Fundtion to draw a square
def draw_square(t):
    lenght = int(input('square size: '))

    for i in range(4):
        draw_line_and_turn(t, lenght)
         

# Function to draw a line and turn the turtle 
def draw_line_and_turn(t, lenght):
    t.forward(lenght)
    t.left(90)

if __name__ == '__main__':
     main()
