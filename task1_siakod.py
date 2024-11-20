import random
import time
import numpy as np
start = time.time()
r = int(input("Введите размер массива: "))
arr1 = [random.randint(0,9) for _ in range(r)]
arr2 = [random.randint(0,9) for _ in range(r)]
arr3 = np.concatenate((arr1, arr2))
arr3.sort()
end = time.time() - start
print(arr3)
print(end)