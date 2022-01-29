import random
import statistics

class Cluster():

    def __init__(self,center,color):
        self.center = center
        self.points = []
        self.color = color

    
def K_Means(clusters,data):
    for k,v in clusters.items():
        v.points.clear()

    for d in data:
        distances = {}
        for k,v in clusters.items():
            distance = euclidean_distance(d,v.center)
            distances[k] = distance
        
        fin_min = min(distances, key = distances.get)
        clusters[fin_min].points.append(d)

    not_equal = 0
    for k,v in clusters.items():
        new_mean = mean(v.points)
        if new_mean != v.center:
            not_equal+=1
    
    if not_equal==0:
        return True
    else:
        return False
    
def readjust(clusters):
    for k,v in clusters.items():
        if len(v.points)>1:
            v.center = mean(v.points)

def mean(points):
    x_sum = 0
    y_sum = 0
    for p in points:
        x_sum += p[0]
        y_sum += p[1]

    return (x_sum/len(points),y_sum/len(points))

def euclidean_distance(p1,p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def generate_points(K):
    return [(random.randint(0,10), random.randint(0,10))
        for _ in range(K)]


def main():
    K = 3
    data = 20
    center_points = generate_points(K)
    colors = ['blue','red','green']
    clusters = {n: Cluster(center,color) for n,center,color in zip(range(len(center_points)),center_points,colors)}
    data_points = generate_points(data)

    stop = False
    i = 0
    while stop == False:
        stop = K_Means(clusters,data_points)
        readjust(clusters)
        i+=1
        for k,v in clusters.items():
            print(v.points)
        print("\n")
    

if __name__ == '__main__':
    main()