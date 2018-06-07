import numpy as np
import random

max_step_number = 100

def search(world_state, robot_pose, goal_pose):
	if world_state[robot_pose[0]][robot_pose[1]]==1:
		return None
	if world_state[goal_pose[0]][goal_pose[1]]==1:
		return None
	path = [robot_pose]
	short_memory = [robot_pose]
	while len(path)<=max_step_number:
		robot_pose_old = path[-1]
		next_pose = []
		next_pose_new = []
		pose_in_memory = {}
		if robot_pose_old[0]-1 >=0 and world_state[robot_pose_old[0]-1][robot_pose_old[1]]!=1:
			next_pose.append((robot_pose_old[0]-1, robot_pose_old[1]))
		if robot_pose_old[0]+1 <=len(world_state)-1 and world_state[robot_pose_old[0]+1][robot_pose_old[1]]!=1:
			next_pose.append((robot_pose_old[0]+1, robot_pose_old[1]))
		if robot_pose_old[1]-1 >=0 and world_state[robot_pose_old[0]][robot_pose_old[1]-1]!=1:
			next_pose.append((robot_pose_old[0], robot_pose_old[1]-1))
		if robot_pose_old[1]+1 <=len(world_state[0])-1 and world_state[robot_pose_old[0]][robot_pose_old[1]+1]!=1:
			next_pose.append((robot_pose_old[0], robot_pose_old[1]+1))

		if len(next_pose) ==0:
			return None
		else:
			for pose in next_pose:
				flag = 0
				for i in xrange(len(short_memory)):
					if pose == short_memory[i]:
						flag = 1
						pose_in_memory[pose] = i
				if flag ==0:
					next_pose_new.append(pose)

			if len(next_pose_new) > 0:
				robot_pose_new = random.sample(next_pose_new,1)[0]
			else:
				robot_pose_new = min(pose_in_memory, key=pose_in_memory.get)

		path.append(robot_pose_new)
		short_memory.append(robot_pose_new)
		if len(short_memory) > np.sqrt(max_step_number):
			short_memory.pop(0)

		if robot_pose_new == goal_pose:
			return path
	return None

if __name__ == '__main__':
	ws = [[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,0,0,1,0],[0,0,0,0,1,0],[0,0,1,1,1,0],[0,0,0,0,0,0]]
	rp = (2,0)
	gp = (5,5)
	result = search(ws, rp, gp)
	print(result)
