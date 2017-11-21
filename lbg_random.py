import cv2
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
import scipy.misc


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
image_location = "Lenna.png"
image = cv2.imread(image_location, cv2.IMREAD_GRAYSCALE)
image_height = len(image)
image_width = len(image[0])

bits_per_codevector = 2

# dimension of the vector
block_width = 4
block_height = 4
vector_dimension = block_width*block_height

codebook_size = pow(2, bits_per_codevector)

image_vectors = []
for i in range(0, image_width, block_width):
    for j in range(0, image_height, block_height):
        image_vectors.append(np.reshape(image[i:i+block_width, j:j+block_height], vector_dimension))
image_vectors = np.asarray(image_vectors).astype(float)
number_of_image_vectors = image_vectors.shape[0]

centroids = 255 * np.random.rand(codebook_size, vector_dimension)

whitened = whiten(np.asarray(image_vectors))
reconstruction_values, distortion = kmeans(image_vectors, centroids)

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

output_image_name = "CB_size" + str(codebook_size) + ".png"
scipy.misc.imsave(output_image_name, image_after_compression)

print "Mean square error = " + str(mse(image, image_after_compression))
