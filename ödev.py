

points= [((1,2),(4,6)),
         ((1,1),(5,7)),
         ((3,3),(6,8))]

distances=[]

def euclideanDistance(x1,x2,y1,y2):
    d=pow((pow((x2-x1),2)+pow((y2-y1),2)),1/2)
    return d

for point in points:
     x1= point[0][0]
     x2= point[1][0]

     y1=point[0][1]
     y2= point[1][1]
     distances.append(euclideanDistance(x1,x2,y1,y2)) 
     
distances.sort()

print(distances)
print("en küçük mesafe: ",distances[0])



