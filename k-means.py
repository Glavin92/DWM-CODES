# Enter x-coordinates: 1.0 2.0 1.5 8.0 8.5 9.0
# Enter y-coordinates: 2.0 3.0 4.0 5.0 3.5 7.0
# Enter number of clusters: 2
def euclidean_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def calculate_mean(cluster):
    return tuple(sum(coord) / len(cluster) for coord in zip(*cluster))

def k_means(data, k):
    centroids = data[:k]
    iteration = 0
    while True:
        clusters = [[] for _ in range(k)]

        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest = distances.index(min(distances))
            clusters[closest].append(point)

        new_centroids = [calculate_mean(cluster) for cluster in clusters]
        iteration += 1
        print(f"\nIteration {iteration}:")

        for i, cluster in enumerate(clusters):
            print(f"Cluster {i + 1}:", cluster) 
        print("Mean of clusters:", new_centroids)

        if centroids == new_centroids:
            print("\nClusters stabilized. Final means:", new_centroids)
            break

        centroids = new_centroids

x_data = list(map(float, input("Enter x-coordinates: ").split()))
y_data = list(map(float, input("Enter y-coordinates: ").split()))
data = list(zip(x_data, y_data))
k = int(input("Enter number of clusters: "))
k_means(data, k)
