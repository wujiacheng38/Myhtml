def merge(A,B):
    result = []
    i = j = 0
    while len(A) > i and len(B) > j:
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    result.extend(A[i:])
    result.extend(B[j:])
    return result
A= [2,3,4]
B= [1,6,7]
sorted_arr =merge(A,B)
print(sorted_arr)
