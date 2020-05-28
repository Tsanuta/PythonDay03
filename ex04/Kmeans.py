import sys
import numpy
from NumPyCreator import NumPyCreator
from csvreader import CsvReader
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x_points = X[:, 0]
        y_points = X[:, 1]
        z_points = X[:, 2]
        ax.scatter3D(x_points, y_points, z_points, color='black')

        def print_centroids(ax, centroids):
            plot = numpy.array(centroids)
            col = {0: 'orange', 1: 'green', 2: 'blue', 3: 'pink', 4: 'yellow'}
            for element in plot:
                x_pts = element[0]
                y_pts = element[1]
                z_pts = element[2]
                ax.scatter3D(x_pts, y_pts, z_pts, marker='*', color=col[x])
            # x_pts = plot[:,0]
            # y_pts = plot[:,1]
            # z_pts = plot[:,2]
            # ax.plot3D(x_pts, y_pts, z_pts, color='green')
            # x_pts = plot[2,:,0]
            # y_pts = plot[2,:,1]
            # z_pts = plot[2,:,2]
            # ax.plot3D(x_pts, y_pts, z_pts, color='blue')
            # x_pts = plot[3,:,0]
            # y_pts = plot[3,:,1]
            # z_pts = plot[3,:,2]
            # ax.plot3D(x_pts, y_pts, z_pts, color='pink')
            pass
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """

        def get_L1_dist(a, b):
            dist = numpy.zeros(len(b))
            for i in range(len(b)):
                dist[i] = abs(b[i][0] - a[0]) + abs(b[i][1] - a[1]) + abs(b[i][2] - a[2])
                # dist[i] = (pow(b[i][0] - a[0], 2) + pow(b[i][1] - a[1],2) + pow(b[i][2] - a[2],2))**(1./3.)
            return dist
        self.centroids = random.choices(X.tolist(), k=self.ncentroid)
        npc = NumPyCreator()
        self.centroids = npc.from_list(self.centroids, dtype=float)
        clusters = numpy.zeros(len(X), dtype=float)
        x = self.ncentroid										# nombre d'iterations
        while x > 0:
            # Pour chaque X[i] on attribue la distance minimum entre centroide et X[i] au clusters[i] correspondant a chaque centroides
            for i in range(len(X)):								# parcours le tableau X
                distances = get_L1_dist(X[i], self.centroids)	# Calcul la distance entre X[i] et chaques centroides donnant chques distances par rapport a chaque centroides
                clusters[i] = numpy.argmin(distances)			# Prend l'indice du centroid ayant la distance le plus petite pour le point i de cluster
            # pour chaque centroid[i] on cherche la moyenne des points les plus proches du centroide
            # print(clusters)
            for i in range(self.ncentroid):
                points = [X[j] for j in range(len(X)) if clusters[j] == i] # on prend le X[i] si l'indice du cluster correspond a l'indice du centroide
                # points = npc.from_list(points, dtype=float)
                self.centroids[i] = numpy.mean(points, axis=0, dtype=float)	# Moyenne des points pour calculer le nouveau centroide
            x -= 1
            print_centroids(ax, self.centroids)
        # plt.show()

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        # height, wieght, bonedensity
        # areas = []
        # for i in self.ncentroid:
            # areas[i] = ['The flying cities of Venus', 'United Nations of Earth', 'Mars Republic', 'The Asteroids’ Belt colonies']

        cent_cpy = numpy.copy(self.centroids)

        print(cent_cpy)
        Belt = numpy.where(cent_cpy[:,0] == numpy.amax(cent_cpy[:,0]))

        for i  in range(len(cent_cpy)):
            if (cent_cpy[i][3] != slender_min and cent_cpy[i][0] != height_max and
                ((cent_cpy[((i+1)%3)][3] < cent_cpy[i][3] and cent_cpy[((i+2)%3)][0] > cent_cpy[i][0]) or
                    (cent_cpy[((i+2)%3)][3] < cent_cpy[i][3] and cent_cpy[((i+1)%3)][0] > cent_cpy[i][0]))):
                        earth_height = cent_cpy[i][0]
                        cent_cpy.remove(cent_cpy[i])

        print("Belt", Belt)

        # centroids = numpy.delete(centroids, Belt[0], axis=0)
        # print(centroids)
        # Venus = numpy.where(centroids[:,1] == numpy.amin(centroids[:,1]))
        # print(Venus)
        # centroids = numpy.delete(centroids, Venus[0], axis=0)
        # Mars = numpy.where(centroids[:,0] == numpy.amax(centroids[:,0]))
        # centroids = numpy.delete(centroids, Mars[0], axis=0)


if __name__ == "__main__":
    kmean = KmeansClustering(ncentroid=4)
    with CsvReader('solar_system_census.csv', header=True) as file:
        data = file.getdata()
        npc = NumPyCreator()
        data_array = npc.from_list(data, dtype=float)
        # print(data_array)
        kmean.fit(data_array)
        kmean.predict(data_array)
    pass
