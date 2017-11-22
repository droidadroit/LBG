# LBG by splitting technique

import cv2
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
from math import log
import scipy.misc
import sys


def mse(image_a, image_b):
    # calculate mean square error between two images
    err = np.sum((image_a.astype(float) - image_b.astype(float)) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])

    return err


def get_centroids(c, p):
    # double the centroids after each iteration
    final_centroids = np.copy(c)
    for centroid in c:
        final_centroids = np.vstack((final_centroids, np.add(centroid, p)))
    return final_centroids


# source image
image_location = sys.argv[1]
image = cv2.imread(image_location, cv2.IMREAD_GRAYSCALE)
image_height = len(image)
image_width = len(image[0])

# dimensions of an image block
block_width = int(sys.argv[3])
block_height = int(sys.argv[4])
vector_dimension = block_width*block_height

bits_per_codevector = int(sys.argv[2])
codebook_size = pow(2, bits_per_codevector)
perturbation_vector = np.full(vector_dimension, 10)

image_vectors = []
for i in range(0, image_width, block_width):
    for j in range(0, image_height, block_height):
        image_vectors.append(np.reshape(image[i:i+block_width, j:j+block_height], vector_dimension))
image_vectors = np.asarray(image_vectors).astype(float)
number_of_image_vectors = image_vectors.shape[0]

centroid_vector = np.mean(image_vectors, axis=0)
centroids = np.vstack((centroid_vector, np.add(centroid_vector, perturbation_vector)))
whitened = whiten(np.asarray(image_vectors))
reconstruction_values, distortion = kmeans(image_vectors, centroids)

for i in range(0, int(log(codebook_size/2, 2)), 1):
    reconstruction_values = get_centroids(reconstruction_values, perturbation_vector)
    reconstruction_values, distortion = kmeans(image_vectors, reconstruction_values)

image_vector_indices, distance = vq(image_vectors, reconstruction_values)

image_after_compression = np.zeros([image_width, image_height], dtype="uint8")
for index, image_vector in enumerate(image_vectors):
    start_row = int(index / (image_width/block_width)) * block_height
    end_row = start_row + block_height
    start_column = (index*block_width) % image_width
    end_column = start_column + block_width
    image_after_compression[start_row:end_row, start_column:end_column] = \
        np.reshape(reconstruction_values[image_vector_indices[index]],
                   (block_width, block_height))

output_image_name = "CB_size=" + str(codebook_size) + ".png"
scipy.misc.imsave(output_image_name, image_after_compression)

print "Mean square error = " + str(mse(image, image_after_compression))
