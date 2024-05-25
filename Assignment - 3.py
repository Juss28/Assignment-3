import numpy as np

# Example 1: Saving data to a text file
data_to_save = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

np.savetxt('saved_data.txt', data_to_save)

# Example 2: Saving data to a binary file
np.save('saved_data.npy', data_to_save)

import numpy as np

# Example 1: Loading data from a text file
loaded_text_data = np.loadtxt('saved_data.txt')
print("Loaded Text Data:\n", loaded_text_data)

# Example 2: Loading data from a binary file
loaded_binary_data = np.load('saved_data.npy')
print("Loaded Binary Data:\n", loaded_binary_data)

import numpy as np

# Example 1: Saving data to a CSV file
data_to_save = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

np.savetxt('saved_data.csv', data_to_save, delimiter=',')

# Example 2: Loading data from a CSV file
loaded_csv_data = np.genfromtxt('saved_data.csv', delimiter=',')
print("Loaded CSV Data:\n", loaded_csv_data)

import numpy as np

# Example 1: Saving data to a text file
data_to_save = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

np.savetxt('saved_data.txt', data_to_save)

# Example 2: Loading data from a text file
loaded_text_data = np.loadtxt('saved_data.txt')
print("Loaded Text Data:\n", loaded_text_data)

import numpy as np

# Example 1: Saving data to a binary file
data_to_save = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

np.save('saved_data.npy', data_to_save)

# Example 2: Loading data from a binary file
loaded_binary_data = np.load('saved_data.npy')
print("Loaded Binary Data:\n", loaded_binary_data)
