import random
import math
from tkinter import *

# GENERATE MAZE WITH Randomized Prim's algorithm

size = 25
windowsize = 400
wallsize = windowsize / size
maze = {}
visited = {}
walls = []

for i in range(size*size):
	visited[i] = False
	# Northern wall
	if i-size >= 0:
		maze[i-size, i] = 1
	# Southern wall
	if i+size < size*size-size:
		maze[i, i+size] = 1
	# Eastern wall
	if not (i + 1) % size == 0:
		maze[i, i+1] = 1
	# Western wall
	if not i % size == 0:
		maze[i-1, i] = 1

# Start in left corner.
cell = 0
visited[0] = True

# Add walls from cell to walls list.
walls = walls + [[0,x] for x in range(size*size) if (0,x) in maze.keys()]

while not len(walls) == 0:
	random.shuffle(walls)
	wall = walls.pop()
	if visited[wall[0]] and not visited[wall[1]]:
		maze.pop((wall[0],wall[1]), None)
		maze.pop((wall[1],wall[0]), None)
		visited[wall[1]] = True
		walls = walls + [[wall[1],x] for x in range(size*size) if ((wall[1],x) in maze.keys()) or ((x,wall[1]) in maze.keys())]
	if visited[wall[1]] and not visited[wall[0]]:
		maze.pop((wall[0],wall[1]), None)
		maze.pop((wall[1],wall[0]), None)
		visited[wall[0]] = True
		walls = walls + [[wall[0],x] for x in range(size*size) if ((wall[0],x) in maze.keys()) or ((x,wall[0]) in maze.keys())]

# Draw maze
# Blank image size*size
# Walls all around
# Walls where specified
# Draw entrance and exit TODO
master = Tk()
w = Canvas(master, width=windowsize, height=windowsize)
w.pack()
w.create_rectangle(0,0,windowsize,windowsize,fill="black")
w.create_rectangle(3,3,windowsize-3,windowsize-3,fill="white")
for wall in maze:
	wall_from = min(wall)
	wall_to = max(wall)
	wall_from_x = wall_from % size
	wall_to_x = wall_to % size
	wall_from_y = math.floor(min(wall_from / size, wall_to / size))
	wall_to_y = math.floor(max(wall_to / size, wall_from / size))
	if wall_from_x == wall_to_x:
		rect_x_from = wall_from_x * wallsize
		rect_x_to = wall_from_x * wallsize + wallsize
		rect_y_from = wall_from_y*wallsize + wallsize - 1
		rect_y_to = wall_from_y*wallsize + wallsize + 1
		w.create_rectangle(rect_x_from, rect_y_from, rect_x_to, rect_y_to, fill="black")
	if wall_from_y == wall_to_y:
		rect_y_from = wall_from_y * wallsize
		rect_y_to = wall_from_y * wallsize + wallsize
		rect_x_from = wall_from_x*wallsize + wallsize - 1
		rect_x_to = wall_from_x*wallsize + wallsize + 1
		w.create_rectangle(rect_x_from, rect_y_from, rect_x_to, rect_y_to, fill="black")
w.create_rectangle(0,4,3,wallsize+3,fill="yellow",outline="white")
w.create_rectangle(windowsize-4,windowsize-wallsize,windowsize,windowsize-4,fill="green",outline="white")
mainloop()
