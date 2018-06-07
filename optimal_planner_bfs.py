import numpy as np

def search(world_state, robot_pose, goal_pose):
	if world_state[robot_pose[0]][robot_pose[1]]==1:
		return None
	if world_state[goal_pose[0]][goal_pose[1]]==1:
		return None

	dir_x = [-1, 1, 0, 0]
	dir_y = [0, 0, -1, 1]
	length = len(world_state[0])-1
	width = len(world_state)-1
	path = []
	bfs_que = [robot_pose]
	visted_pose = [robot_pose]
	distance_dict = {robot_pose:0}
	lastnode_dict = {}

	while bfs_que:
		#print(bfs_que)
		robot_pose_old = bfs_que.pop(0)

		for i in xrange(4):
			robot_pose_next = (robot_pose_old[0]+dir_x[i], robot_pose_old[1]+dir_y[i])
			if robot_pose_next == goal_pose:
				path.append(goal_pose)
				while robot_pose_old != robot_pose:
					path.append(robot_pose_old)
					robot_pose_old = lastnode_dict[robot_pose_old]
				path.append(robot_pose)
				path.reverse()
				return path
			elif robot_pose_next[0]>=0 and robot_pose_next[0]<=width and robot_pose_next[1]>=0 and robot_pose_next[1]<=length and \
			world_state[robot_pose_next[0]][robot_pose_next[1]]==0 and robot_pose_next not in visted_pose:
				bfs_que.append(robot_pose_next)
				visted_pose.append(robot_pose_next)
				distance_dict[robot_pose_next] = distance_dict[robot_pose_old] + 1
				lastnode_dict[robot_pose_next] = robot_pose_old
	return None

if __name__ == '__main__':
	ws = [[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,0,0,1,0],[0,0,0,0,1,0],[0,0,1,1,1,0],[0,0,0,0,0,0]]
	rp = (2,0)
	gp = (5,5)
	result = search(ws, rp, gp)
	print(result)
