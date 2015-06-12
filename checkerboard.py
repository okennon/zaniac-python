import turtle

turtle.showturtle()

WINDOW_WIDTH = turtle.window_width()
WINDOW_HEIGHT=turtle.window_height()

tile_width = WINDOW_WIDTH/10
tile_height = WINDOW_HEIGHT/10

turtle.up()

turtle.setx(-WINDOW_WIDTH/2)
turtle.sety(WINDOW_HEIGHT/2)

# draw vertical lines
turtle.setheading(270)
for x in range(-WINDOW_WIDTH/2, WINDOW_WIDTH/2):
	# draw a line every tile_height pixels
	if (x % tile_width)==0:
		# draw a horizontal line
		turtle.setx(x)
		turtle.down()
		turtle.forward(WINDOW_HEIGHT)
		turtle.up()
		turtle.sety(WINDOW_HEIGHT/2)

# draw horizontal lines
turtle.setheading(0)
for y in range(-WINDOW_HEIGHT/2, WINDOW_HEIGHT/2):
	# draw a line every tile_height pixels
	if (y % tile_height)==0:
		# draw a horizontal line
		turtle.sety(y)
		turtle.down()
		turtle.forward(WINDOW_WIDTH)
		turtle.up()
		turtle.setx(-WINDOW_WIDTH/2)

end = raw_input("Press enter to quit.")