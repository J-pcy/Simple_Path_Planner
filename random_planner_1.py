import numpy as np

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
		rand_num = np.random.randint(0,4)
		if rand_num==0:
			robot_pose_new = (robot_pose_old[0]-1, robot_pose_old[1])
		elif rand_num==1:
			robot_pose_new = (robot_pose_old[0]+1, robot_pose_old[1])
		elif rand_num==2:
			robot_pose_new = (robot_pose_old[0], robot_pose_old[1]-1)
		elif rand_num==3:
			robot_pose_new = (robot_pose_old[0], robot_pose_old[1]+1)

		if robot_pose_new[0]<0 or robot_pose_new[0]>len(world_state)-1 or robot_pose_new[1]<0 or robot_pose_new[1]>len(world_state[0])-1 or world_state[robot_pose_new[0]][robot_pose_new[1]]==1:
			robot_pose_new = robot_pose_old

		if robot_pose_new != robot_pose_old:
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
