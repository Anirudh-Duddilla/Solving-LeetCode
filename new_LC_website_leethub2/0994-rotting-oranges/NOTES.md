This problem should be done by bfs, because with the each minute the fruits adjacent horizontally/vertically to the rotten one gets rotten. So, if a rotten fruits has four fruits up/down and left/right, all those 4 will be rotten in the next minute. We pick a position check if it is a freah one or nothing and if it is a rotten we will mark the surrounding four rotten and move on to the next. if it is a freash fruit we will check for surroundings that has rotten.
​
q.add
​
[[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[0,1,1],[1,0,1]]
[[0,2]]
[[2,2],[1,1],[0,0],[2,0]]
​