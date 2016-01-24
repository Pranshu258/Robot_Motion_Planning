from robot import *
from random import randint
import math
import os

	# Generate the images
try:
	mkdir("test/img_random/")
	mkdir("test/img_radial/")
except:
	i = 0		# Dummy


# GENERATE RANDOM TEST IMAGES
points = []
robot = Robot(0, 0, 0, 120)
for i in xrange(1000):
	# Put the robot and construct the arena
	screen.fill(BGCOLOR)
	# Draw the textured background
	load_background('texture.jpg')
	robot.draw(screen)
	# Take the images
	image_data = robot.take_picture(screen)
	filename = "test/img_random/" + str(i) + ".png"
	save_picture(image_data, filename)
	points.append([robot.x, robot.y, robot.theta])	
	robot.x = randint(-180,180)
	robot.y = randint(-180,180)
	robot.theta = randint(0,360)
	pygame.display.flip()
points = np.array(points)
np.savetxt('test/random_points.csv', points, delimiter=',')

# GENERATE CIRCLE TEST IMAGES
points = []
robot = Robot(0, 0, 0, 120)
for i in xrange(1000):
	# Put the robot and construct the arena
	screen.fill(BGCOLOR)
	# Draw the textured background
	load_background('texture.jpg')
	robot.draw(screen)
	# Take the images
	image_data = robot.take_picture(screen)
	filename = "test/img_radial/" + str(i) + ".png"
	save_picture(image_data, filename)
	points.append([robot.x, robot.y, robot.theta])	
	robot.theta = randint(0,360)	
	robot.x = 100 * math.cos(math.radians(robot.theta))
	robot.y = 100 * math.sin(math.radians(robot.theta))
	pygame.display.flip()
points = np.array(points)
np.savetxt('test/radial_points.csv', points, delimiter=',')