"""
Closest pair problem - The closest pair of points problem or closest pair 
problem is a problem of computational geometry: given *n* points in metric space, 
find a pair of points with the smallest distance between them.
"""
#sort x and y cords
def closest_pair(pointList):
	Px = sorted(pointList, key=lambda x:x[0])
	Py = sorted(pointList, key=lambda y:y[1])
	return brute_force(Px)
#calculate eucledian distance
def eucledian_dist(pair):
	return (pair[0][0]-pair[1][0])**2+(pair[0][1]-pair[1][1])**2

#brute force algorithm O(n^2)
def brute_force(pointList):
	bestPair=(pointList[0],pointList[1])
	bestDist=eucledian_dist(bestPair)
	for i in range(len(pointList)):
		for j in range(i+1, len(pointList)):
			dist = eucledian_dist((pointList[i],pointList[j]))
			if dist < bestDist:
				bestDist = dist
				bestPair = (pointList[i],pointList[j])
	return bestPair


if __name__ == '__main__':
	pointList = [(0,0), (7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]
	print 'List of points: %s' %pointList
	print 'The closest pair: %s %s'  %closest_pair(pointList)
