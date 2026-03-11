def two_sum(target, list):
  for i in range(len(list)):
    for j in range(len(list)):
      if list[i] + list[j] == target and i != j:
        return [i,j]
    
print(two_sum(10, [5,2,5]))