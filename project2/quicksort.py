

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q, r)
    return(A)


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return(i+1)


A = [9, 66, 7, 3, 88, 232, 4, 234, 34234, 343, 980]
quicksort(A, 0, len(A)-1)