
A = [9,3,9,3,9,9,7]
B = []
count = 0
for i in range(len(A)):
    for y in range(len(A)):
        if i != y:
            if A[i] == A[y]:
                count += 1
    if count % 2 == 0:
        if not B.__contains__(A[i]):
            B.append(A[i])
    count = 0

print(B)
            

