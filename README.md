# CSE4082 Project 2 - Artificial Intelligence for 2048 Game 

## Aim of the Project
This project aims to implement 6 different uninformed and informed search strategies. These strategies include;
1. Depth-First Search
2. Breadth-First Search
3. Iterative Deepening
4. Uniform Cost Search
5. Greedy Best First Search
6. A* HeuristicSearch

## Maze
<img src="https://i.ibb.co/TwRcbFJ/image.png" data-canonical-src="https://i.ibb.co/TwRcbFJ/image.png" width="400" />

### Comparison of the Searching Algorithms
![](https://i.ibb.co/ZWrxH3M/image.png)

### Solution Paths

#### DFS
**Solution Path:** (2,3) - (2,4) - (3,4) - (3,5) - (3,6) - (2,6) - (1,6) - (1,5) - (1,4) - (1,3) - (1,2) - (1,1) - (2,1) - (2,2) - (3,2) - (4,2) - (4,3) - (5,3) - (6,3) - (7,3)
#### BFS
**Solution Path:**  (2,3) - (1,3) - (1,2) - (1,1) - (2,1) - (2,2) - (3,2) - (4,2) - (4,3) - (5,3) - (6,3) - (7,3)
#### ITERATIVE DEEPENING 
**Solution Path:** (2,3) - (1,3) - (1,2) - (1,1) - (2,1) - (2,2) - (3,2) - (4,2) - (4,3) - (5,3) - (6,3) - (7,3)
#### UNIFORM COST
**Solution Path:** (2,3) - (1,3) - (1,2) - (1,1) - (2,1) - (2,2) - (3,2) - (3,1) - (4,1) - (5,1) - (6,1) - (7,1) - (8,1) - (8,2) - (8,3) - (8,4) - (8,5) - (8,6) - (7,6)
#### GREEDY BEST FIRST
**Solution Path:** (2,3) - (1,3) - (1,2) - (1,1) - (2,1) - (2,2) - (3,2) - (4,2) - (4,3) - (5,3) - (6,3) - (7,3)
#### A*
**Solution Path:** (2,3) - (1,3) - (1,2) - (1,1) - (2,1) - (2,2) - (3,2) - (3,1) - (4,1) - (5,1) - (6,1) - (7,1) - (8,1) - (8,2) - (8,3) - (8,4) - (8,5) - (8,6) - (7,6)

## Our Designed Maze
<img src="https://i.ibb.co/ckk4D69/image.png" data-canonical-src="https://i.ibb.co/ckk4D69/image.png" width="400" />

### Comparison of the Searching Algorithms
![](https://i.ibb.co/DCgDrTQ/image.png)

### Solution Paths

#### DFS
**Solution Path:** (1,1) - (1,2) - (1,3) - (2,3) - (3,3) - (4,3) - (5,3) - (6,3) - (7,3) - (8,3) - (8,4) - (8,5) - (8,6) - (8,7) - (7,7) - (6,7) - (6,8) - (7,8) - (8,8)
#### BFS
**Solution Path:** (1,1) - (1,2) - (1,3) - (1,4) - (1,5) - (2,5) - (2,4) - (3,4)
#### ITERATIVE DEEPENING 
**Solution Path:** (1,1) - (1,2) - (1,3) - (1,4) - (1,5) - (2,5) - (2,4) - (3,4)
#### UNIFORM COST
**Solution Path:** (1,1) - (1,2) - (1,3) - (2,3) - (3,3) - (4,3) - (4,4) - (4,5) - (3,5) - (2,5) - (2,4) - (3,4)
#### GREEDY BEST FIRST
**Solution Path:** (1,1) - (1,2) - (1,3) - (2,3) - (3,3) - (4,3) - (4,4) - (4,5) - (3,5) - (2,5) - (2,4) - (3,4)
#### A*
**Solution Path:** (1,1) - (1,2) - (1,3) - (2,3) - (3,3) - (4,3) - (4,4) - (4,5) - (3,5) - (2,5) - (2,4) - (3,4)
