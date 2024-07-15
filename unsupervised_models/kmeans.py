import csv
import math
import numpy as np
from random import *

def compute_euclidean_distance(point , centroid):
    x = float(point[0]) - centroid[0]
    y = float(point[1]) - centroid[1]
    return math.sqrt(x**2 + y**2)

def assign_label_cluster(distance, data_point, centroids):
    iMinimum = min(distance, key=distance.get)
    return [iMinimum, data_point, centroids[iMinimum]]

def compute_new_centroids(cluster_label, centroids):
    x = float(cluster_label[0]) + float(centroids[0])
    y = float(cluster_label[1]) + float(centroids[1])
    return [x/2 , y/2]
    
def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    
    for iteration in range(0, total_iteration):
        for point in data_points:
            distance = {}
            for j in range(0, k):
                distance[j] = compute_euclidean_distance(point, centroids[j])
            label = assign_label_cluster(distance, point, centroids)
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])
            
            if iteration == (total_iteration - 1):
                cluster_label.append(label)

    return [cluster_label, centroids]
    
def initialize_centroids(data_points,k):
    centroids = []
    for i in range(0 , k):
        r = randint(1, len(data_points))
        centroids.append([float(data_points[r][0]) , float(data_points[r][1])])
    return np.array(centroids)

def print_label_data(result):
    print("Result of k-Means Clustering: ")
    for data in result[0]:
        print("data point: ",data[1])
        print("cluster number: ",data[0])
    print('New centroids position: ',result[1])
                    
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data_points = list(reader)
    
k = input("Enter K-Value: ")
centroids = initialize_centroids(data_points,k)
total_iteration = 100

[cluster_label, new_centroids] = iterate_k_means(data_points, centroids, total_iteration)

print_label_data([cluster_label, new_centroids])
