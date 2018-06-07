#Motion Planning: Discrete planner

Author: Peng-Chenyu

File include: README.txt
			  random_planner_1.py
			  random_planner_2.py
			  optimal_planner_bfs.py
			  optimal_planner_a*.py

Discussion: 
			random_planner_1.py and random_planner_2.py are for Random planner. random_planner_1.py doesn't have short memory. random_planner_2.py satisfies all requirements in question 1.
			
			optimal_planner_bfs.py and optimal_planner_a*.py are for Optimal planner. optimal_planner_bfs.py use BFS algorithm and optimal_planner_a*.py use A* algorithm to implement optimal planner.

			Depends on max_step_number and size of world_state, usually random planner is much faster than optimal planner. However, random planner cannot guarantee to find an optimal path even a path. If there exists an optimal path, both optimal planners are sure to find optimal path.

			In all these 4 files, I use simple example mentioned in your question description as test case. If we want more test case, we could use rp = (np.random.randint(len(ws)),np.random.randint(len(ws[0]))), gp = (np.random.randint(len(ws)),np.random.randint(len(ws[0]))) to generate random robot_pose and goal_pose.

			Complexity of random planner is O(1), it depends on max_step_number which is a constant.
			Complexity of optimal planner is O(length*width) where length of world_state and width of world_state.