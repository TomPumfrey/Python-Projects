# myEtchASketch app

from Tkinter import *

##### Variables:
canvas_height = 400
canvas_width = 600
canvas_colour = "black"
p1_x = canvas_width/2
p1_y = canvas_height
p1_colour = "red"
line_width = 5
line_length = 5

##### Functions:

# player controls
def p1_move_N(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length
    
def p1_move_S(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length
    
def p1_move_E(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_length, fill=p1_colour)
    p1_x = p1_x + line_length
    
def p1_move_W(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_length, fill=p1_colour)
    p1_x = p1_x - line_length
    
def erase_all(event):
    canvas.delete(ALL)

def p1_line_len_inc(event):
    global line_width
    line_width += 5

def p1_line_len_dec(event):
    global line_width
    line_width -= 5

    
##### main:
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

# bind movement
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Right>", p1_move_E)
window.bind("<Left>", p1_move_W)
window.bind("u", erase_all)
window.bind("2", p1_line_len_inc)
window.bind("1", p1_line_len_dec)

window.mainloop()
