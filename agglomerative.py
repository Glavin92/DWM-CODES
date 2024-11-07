# Enter the number of data points: 6
# Enter data point 1: 18
# Enter data point 2: 22
# Enter data point 3: 24
# Enter data point 4: 27
# Enter data point 5: 43
# Enter data point 6: 42
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

# Function to compute the distance matrix using single linkage
def compute_distance_matrix(points):
    return squareform(pdist(points, metric='euclidean'))

# Function to print the distance matrix
def print_distance_matrix(matrix, step):
    print(f"\nDistance matrix after step {step}:")
    print(matrix)

# Main program
def hac_clustering():
    # Input from the user
    num_points = int(input("Enter the number of data points: "))
    data_points = np.array([int(input(f"Enter data point {i + 1}: ")) for i in range(num_points)]).reshape(-1, 1)
    num_clusters = 1

    print("\nNumber of data points: ", len(data_points))
    print("Data points: ", data_points.flatten())

    # Compute initial distance matrix
    distance_matrix = compute_distance_matrix(data_points)
    print("\nInitial Distance Matrix:")
    print(distance_matrix)

    # Create a list to track current clusters
    clusters = data_points.copy()
    cluster_labels = list(range(num_points))

    # Print distance matrix after each step
    for step in range(num_points - num_clusters):
        # Extract cluster indices and distance from the linkage matrix
        min_dist = np.inf
        cluster1, cluster2 = -1, -1

        # Find the two closest clusters
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if distance_matrix[i, j] < min_dist:
                    min_dist = distance_matrix[i, j]
                    cluster1, cluster2 = i, j

        # Merge clusters
        label1 = cluster_labels[cluster1]
        label2 = cluster_labels[cluster2]

        # Create a new array for the clusters
        new_clusters = []
        for i in range(len(clusters)):
            if i != cluster1 and i != cluster2:
                new_clusters.append(clusters[i])

        # Merge the two clusters using the minimum value
        new_cluster = np.min([clusters[cluster1], clusters[cluster2]], axis=0)
        new_clusters.append(new_cluster)
        clusters = np.array(new_clusters)

        # Update cluster labels
        new_label = f'Cluster {len(cluster_labels)}'
        cluster_labels = [label for idx, label in enumerate(cluster_labels) if idx != cluster1 and idx != cluster2] + [new_label]

        # Recompute the distance matrix for the new clusters
        new_distance_matrix = np.zeros((len(clusters), len(clusters)))

        # Fill in the new distance matrix
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if i < len(new_clusters) and j < len(new_clusters):
                    new_distance_matrix[i, j] = compute_distance_matrix(np.array([clusters[i], clusters[j]]))[0, 1]
                    new_distance_matrix[j, i] = new_distance_matrix[i, j]

        distance_matrix = new_distance_matrix

        # Print the merging description before showing the distance matrix
        print(f"\nStep {step + 1}: Merging clusters {label1} and {label2} with distance {min_dist:.2f}")
        print_distance_matrix(distance_matrix, step + 1)

    # Final distance matrix
    print("\nFinal Distance Matrix:")
    print(distance_matrix)

    # Plotting the dendrogram with actual data point values
    plt.figure(figsize=(10, 5))
    dendrogram(linkage(data_points, method='single'), labels=data_points.flatten())
    plt.title('Dendrogram')
    plt.xlabel('Data points')
    plt.ylabel('Distance')
    plt.show()

# Run the clustering
hac_clustering()