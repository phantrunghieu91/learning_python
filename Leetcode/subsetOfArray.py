def subsetOf(arr):
  if(len(arr) == 0): return []
  result = [[]]
  for i in range(len(arr)):
    n = len(result)
    for j in range(n):
      result.append(result[j] + [arr[i]])
  return result;

# Test cases
print(subsetOf([1, 2, 3])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(subsetOf([1])) # [[], [1]]