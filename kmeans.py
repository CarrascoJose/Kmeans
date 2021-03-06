from calendar import c
import random
import matplotlib.pyplot as plt


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
    return [(random.randint(1,10), random.randint(1,10))
        for _ in range(K)]

def get_coords(cluster_points):
    x_axis = [cp[0] for cp in cluster_points]
    y_axis = [cp[1] for cp in cluster_points]
    return x_axis,y_axis

        


def main():
    K = 3
    data = 50
    center_points = generate_points(K)
    colors = ['blue','red','green']
    clusters = {n: Cluster(center,color) for n,center,color in zip(range(len(center_points)),center_points,colors)}
    data_points = generate_points(data)

    #Plot initial data points
    fig = plt.figure(figsize = (10, 5),)
    x_axis,y_axis = get_coords(data_points)

    plt.scatter(x_axis, y_axis, 
            linewidths = 2, 
            s = 50,c="grey")
    
    plt.pause(2)
    ###

    stop = False
    while stop == False:

        #Plot cluster centers
        xcenter_points = []
        ycenter_points = []
        for k,v in clusters.items():
            xcenter_points.append([v.center[0]])
            ycenter_points.append([v.center[1]])

        for x,y,color in zip(xcenter_points,ycenter_points,colors):
            plt.scatter(x,y,s=50,c=color,marker="x")

        #KMeans Algotithm
        stop = K_Means(clusters,data_points)
        readjust(clusters)
        ####

        plt.pause(2)

        ##Plot cluster points
        x = []
        y = []
        for k,v in clusters.items():
            x_axis,y_axis = get_coords(v.points)
            x.append(x_axis)
            y.append(y_axis)

        
        for xp,yp,color in zip(x,y,colors):
            plt.scatter(xp, yp, c =color,
        linewidths = 2, 
            s = 50)
    
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.pause(2)

        #Reescribimos los datos
        plt.clf()

        for xp,yp,color in zip(x,y,colors):
            plt.scatter(xp, yp, c =color,
        linewidths = 2, 
            s = 50)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        ###
    

if __name__ == '__main__':
    main()