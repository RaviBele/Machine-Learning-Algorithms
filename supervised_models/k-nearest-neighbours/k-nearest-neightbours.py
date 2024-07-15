import math

def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nearest_neighbors = find_k_nearest_neighbors(examples, features, k)
    
    count_is_intrusive = 0
    count_is_not_intrusive = 0
    for neighbor in k_nearest_neighbors:
        if examples[neighbor][label_key] == 1:
            count_is_intrusive += 1
        else:
            count_is_not_intrusive += 1
    
    return 1 if count_is_intrusive > count_is_not_intrusive else 0

def find_k_nearest_neighbors(examples, features, k):
    #Find Euclidean distance

    sorted_distances = find_euclidean_distance(examples, features, k)

    return sorted_distances[:k]

def find_euclidean_distance(examples, features, k):
    distances = {}
    for example_key, example_value in examples.items():
        distance = 0
        for feature, example in zip(features, example_value["features"]):
            distance += (feature - example)**2
        distances[example_key] = (math.sqrt(distance), example_value["is_intrusive"])

    return list(dict(sorted(distances.items(), key=lambda x:x[1][0])).keys())[:k]