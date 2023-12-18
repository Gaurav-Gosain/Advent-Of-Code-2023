# Day 18, lava 🎅

f = open(0).read().strip().split("\n")

def solution(part_1: bool):
    m = {"R": (0,1), "L": (0,-1), "U": (-1,0), "D": (1,0)}
    path = []
    pos = (0,0)

    d = {"0": "R", "1": "D", "2": "L", "3": "U"}
    pathlen = 0

    for i in range(len(f)):
        row = f[i].split()
        
        if part_1:
            dir = row[0]
            dist = int(row[1])
        else:
            hex = row[2][2:-1]
            dist = int(hex[:5], 16)
            dir = d[hex[-1]]

        move = (m[dir][0]*dist, m[dir][1]*dist)
        pathlen += dist
        pos = (pos[0] + move[0], pos[1] + move[1])
        path.append(pos)
    
    def shoelace_theorem(path):  # computes the area of a polygon given its lattice point coordinates
        area = 0
        fullpath = [path[-1]] + path
        for i in range(len(fullpath)-1):
            one = fullpath[i]
            two = fullpath[i+1]
            area += (0.5*(one[0]+two[0])*(one[1]-two[1]))
        return abs(area)

    def picks_theorem(area, boundary_pts):  # computes the number of interior lattice points of a polygon given its area and the number of boundary lattice points 
        return area + 1 - (boundary_pts)/2

    area = shoelace_theorem(path)
    interior_points = picks_theorem(area, pathlen)
    return int(interior_points + pathlen)

        
print("Part 1:", solution(part_1=True))
print("Part 2:", solution(part_1=False))