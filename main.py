from copy import deepcopy

#A* Caroling Lab
#Ella Mohanram
#February 10, 2023

#finds the best path to all the dorms for senior caroling
class AStarCaroling:
    #1D array of all building names
    dorm_names = ["Main", "Watson", "Flinn", "Redlich", "Edelman", "Wieler", "Memo", "Buehler", "Coy", "Tinker", "V-S", "Garland", "Dana"]

    #2D array containing distances to each building from each building
    distances = [
        [0, 5.5, -1, 4.0, 8.5, 7.0, 5.0, 5.5, 5.7, 5.2, 7.2, 9.5, 9.3],
        [5.5, 0, 3.7, 2.2, -1, -1, -1, -1, -1, -1, -1, -1, 11.5],
        [-1, 3.7, 0, 4.0, 3.8, -1, -1, -1, -1, -1, -1, -1, -1],
        [4.0, 2.2, 4.0, 0, 5.5, 6.5, 7.0, -1, -1, -1, -1, -1, -1],
        [8.5, -1, 3.8, 5.5, 0, 5.0, -1, -1, -1, -1, -1, -1, -1],
        [7.0, -1, -1, 6.5, 5.0, 0, 4.0, -1, -1, -1, -1, -1, -1],
        [5.0, -1, -1, 7.0, -1, 4.0, 0, 2.5, -1, 6.0, -1, -1, -1],
        [5.5, -1, -1, -1, -1, -1, 2.5, 0, 2.2, -1, -1, -1, -1],
        [5.7, -1, -1, -1, -1, -1, -1, 2.2, 0, 2.0, -1, -1, -1],
        [5.2, -1, -1, -1, -1, -1, 6.0, -1, 2.0, 0, 3.3, -1, 9.0],
        [7.2, -1, -1, -1, -1, -1, -1, -1, -1, 3.3, 0, 3.3, 6.5],
        [9.5, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3.3, 0, 4.2],
        [9.3, 11.5, -1, -1, -1, -1, -1, -1, -1, 9.0, 6.5, 4.2, 0]
    ]

    #initializes main building
    main_building = 0

    #constructor function that initializes class attributes
    def __init__(self):
        self.count_paths = 0
        self.priority_queue = []

    #finds the best path from start to end including all nodes, and counts how many nodes visited
    #param: start_dorm: dorm at start of path
    #param: end_dorm: dorm at end of path 
    #return: optimal path if possible, else empty path
    def find_best_path(self, start_dorm, end_dorm):
        self.priority_queue.append([0, [start_dorm]])

        while len(self.priority_queue) > 0:
            current_path = self.priority_queue[0]
            self.priority_queue.pop(0)

            end_node = current_path[-1][-1]
            end_node_paths = self.distances[end_node]

            for i in range(len(end_node_paths)):
                distance = end_node_paths[i]
                if distance > 0 and i not in current_path[1]:
                    current_path_copy = deepcopy(current_path)
                    current_path_copy[0] += distance
                    current_path_copy[1].append(i)

                    self.count_paths += 1
                    print("D: " + str(current_path_copy[0]) + ", P: " + str(current_path_copy[1]))

                    if len(current_path_copy[1]) == len(AStarCaroling.distances) and i == end_dorm:
                        return current_path_copy
                    else:
                        if self.count_paths == 1:
                            self.priority_queue.append(current_path_copy)
                        else:
                            done = False
                            index = 0
                            while (done == False) and (index < len(self.priority_queue)):
                                temp_path = self.priority_queue[index]
                                if current_path_copy[0] < temp_path[0]:
                                    done = True
                                else:
                                    index += 1
                            self.priority_queue.insert(index, current_path_copy)
        return []

    #takes user input and returns best path and number of nodes visited
    #returns: best path, number of nodes visited
    def run(self):
        start_dorm = int(input("Enter starting dorm: "))
        solution = self.find_best_path(start_dorm, AStarCaroling.main_building)

        path = []
        for number in solution[1]:
            path.append(AStarCaroling.dorm_names[number])

        print("Found solution after " + str(self.count_paths) + " paths")
        print("The best path from " + AStarCaroling.dorm_names[start_dorm] + " is D: " + str(solution[0]) + ", P: " + str(path))

astar = AStarCaroling()
astar.run()

