import numpy as np

arr1 = np.random.randint(1, 20, 100)

print(arr1)
unique, counts = np.unique(arr1, return_counts=True)
print(np.mean(counts))
print(np.median(counts))
arr2 = dict(zip(unique, counts))
print(arr2)