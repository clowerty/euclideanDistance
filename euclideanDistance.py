import math
points=[(10,44),(4,6),(7,10),(12,3),(12,27)]
def euclideanDistance(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
distances=[]
for i in range (len(points)):
    for j in range (i+1,len(points)):
        distance_main=euclideanDistance(points[i], points[j])
        distances.append(distance_main)
print("Noktalar arasındaki mesafeler:")
for i, distance in enumerate(distances, start=1):
    print(f"Mesafe {i}: {distance}")


    
