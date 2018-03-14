from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#add_circle(edges, 200, 200, 0, 200, 360)
#add_bezier(edges, 0, 0, 200, 400, 400, 200, 500, 500)
#add_hermite(edges, 0, 0, 300, 100, 100, 0)
clear_screen(screen)
draw_lines(edges, screen, color)
display(screen)

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

#parse_file( 'script', edges, transform, screen, color )
