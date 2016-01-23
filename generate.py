# Generate images by rotating the robot at a given point and storing them in an appropriate folder

from robot import *
from os import mkdir
import sys

if len(sys.argv) == 4:
	x = float(sys.argv[1])			# The x co-ordinate
	y = float(sys.argv[2])			# The y co-ordinate
	N = int(sys.argv[3])			# Number of images to capture

	# Try to make a directory in which we will save the captured images
	try:
		mkdir("img/part1/" + str(x) + "_" + str(y))
	except:
		i = 0		# Dummy

	robot = Robot(x, y, 0, 120)
	for i in xrange(N):
		# Put the robot and construct the arena
		screen.fill(BGCOLOR)
		# Draw the textured background
		load_background('texture.jpg')
		#draw_poly(room_coords)
		robot.draw(screen)
		# Take the images
		image_data = robot.take_picture(screen)
		filename = "img/part1/" + str(x) + "_" + str(y) + "/" + str(i) + ".png"
		save_picture(image_data, filename)	
		robot.theta = robot.theta + 360/float(N)
		pygame.display.flip()
else:
	print "Please supply x_coord y_coord and Number of Images"