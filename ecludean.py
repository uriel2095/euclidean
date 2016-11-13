from scipy.spatial import distance
a = (1,0,0,1)
b = (7,6,9,4)
dst = distance.euclidean(a,b)

print dst