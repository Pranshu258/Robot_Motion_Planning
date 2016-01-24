from robot import *
from os import mkdir
import sys
from random import randint
import numpy as np
import math

if len(sys.argv) == 3:	
	image_type = int(sys.argv[1])
	inst = int(sys.argv[2])				# Instances of rotation
	if inst < 0:
		inst = 0

	# Try to make a directory in which we will save the captured images
	try:
		mkdir("img/trajectory_" + str(image_type))
	except:
		i = 0		# Dummy

	points = []

	# RANDOM TRAJECTORY WITH PLAIN ARENA
	if image_type == 0:
		# Position the Robot
		robot = Robot(0, 0, 0, 120)
		N = 0
		for i in xrange(inst+1):
			for j in xrange(10000/(inst+1)):
				# Put the robot and construct the arena
				screen.fill(BGCOLOR)
				draw_poly(room_coords)
				robot.draw(screen)
				# Take the images
				image_data = robot.take_picture(screen)
				filename = "img/trajectory_" + str(image_type) + "/" + str(N) + ".png"
				save_picture(image_data, filename)
				points.append([robot.x, robot.y, robot.theta])	
				robot.x = randint(-180,180)
				robot.y = randint(-180,180)
				N = N + 1
				pygame.display.flip()
			robot.theta = randint(0,360)
			print "Images: " + str(N)
		points = np.array(points)
		np.savetxt('capture_points/captured' + str(image_type) + '.csv', points, delimiter=',')

	# RANDOM TRAJECTORY WITH GRADIENT ARENA
	if image_type == 1:
		# Position the Robot
		robot = Robot(0, 0, 0, 120)
		N = 0
		for i in xrange(inst+1):
			for j in xrange(50000/(inst+1)):
				# Put the robot and construct the arena
				screen.fill(BGCOLOR)
				# Draw the textured background
				load_background('texture.jpg')
				robot.draw(screen)
				# Take the images
				image_data = robot.take_picture(screen)
				filename = "img/trajectory_" + str(image_type) + "/" + str(N) + ".png"
				save_picture(image_data, filename)
				points.append([robot.x, robot.y, robot.theta])	
				robot.x = randint(-180,180)
				robot.y = randint(-180,180)
				N = N + 1
				pygame.display.flip()
			robot.theta = randint(0,360)
			print "Images: " + str(N)
		points = np.array(points)
		np.savetxt('capture_points/captured' + str(image_type) + '.csv', points, delimiter=',')

	# ROTATION ALONG STRAIGHT LINE IN GRADIENT ARENA
	if image_type == 2:
		# Position the Robot
		robot = Robot(-180, -180, 0, 120)
		N = 0
		for i in xrange(inst+1):
			for j in xrange(10000/(inst+1)):
				# Put the robot and construct the arena
				screen.fill(BGCOLOR)
				# Draw the textured background
				load_background('texture.jpg')
				robot.draw(screen)
				# Take the images
				image_data = robot.take_picture(screen)
				filename = "img/trajectory_" + str(image_type) + "/" + str(N) + ".png"
				save_picture(image_data, filename)
				points.append([robot.x, robot.y, robot.theta])	
				robot.x = robot.x + 0.0360
				robot.y = robot.y + 0.0360
				N = N + 1
				pygame.display.flip()
			robot.theta = robot.theta + (0.0360)*inst
			print "Images: " + str(N)
		points = np.array(points)
		np.savetxt('capture_points/captured' + str(image_type) + '.csv', points, delimiter=',')

	# CIRCULAR TRAJECTORY
	if image_type == 3:
		# Position the Robot
		robot = Robot(100, 100, 0, 120)
		N = 0
		for i in xrange(inst+1):
			for j in xrange(10000/(inst+1)):
				# Put the robot and construct the arena
				screen.fill(BGCOLOR)
				# Draw the textured background
				load_background('texture.jpg')
				robot.draw(screen)
				# Take the images
				image_data = robot.take_picture(screen)
				filename = "img/trajectory_" + str(image_type) + "/" + str(N) + ".png"
				save_picture(image_data, filename)
				points.append([robot.x, robot.y, robot.theta])
				robot.theta = robot.theta + 0.0360	
				robot.x = 100 * math.cos(math.radians(robot.theta))
				robot.y = 100 * math.sin(math.radians(robot.theta))
				N = N + 1
				pygame.display.flip()
			print "Images: " + str(N)
		points = np.array(points)
		np.savetxt('capture_points/captured' + str(image_type) + '.csv', points, delimiter=',')

else:
	print "Please supply the trajectory type (0 for random) and number of rotation instances"