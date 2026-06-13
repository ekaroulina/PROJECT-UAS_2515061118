# eka118.py 
def tambah(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kurang(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kali(A, B):
    br, bk, kl = len(A), len(B[0]), len(A[0])
    return [[sum(A[i][k] * B[k][j] for k in range(kl)) for j in range(bk)] for i in range(br)]

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

def determinan(A):
    n = len(A)
    if n == 1: return A[0][0]
    if n == 2: return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    return sum((1 if j%2==0 else -1) * A[0][j] * determinan(
        [row[:j] + row[j+1:] for row in A[1:]]
    ) for j in range(n))

def invers(A):
    det = determinan(A)
    if det == 0: raise ValueError("Matriks singular")
    n = len(A)
    # Matriks kofaktor
    kof = [[((1 if (i+j)%2==0 else -1)) * determinan(
        [row[:j] + row[j+1:] for row in (A[:i] + A[i+1:])]
    ) for j in range(n)] for i in range(n)]
    return [[kof[j][i] / det for j in range(n)] for i in range(n)]

def kali_matriks_3x3(A, B):
    if len(A)!=3 or len(A[0])!=3 or len(B)!=3 or len(B[0])!=3:
        raise ValueError("Harus matriks 3x3")
    return kali(A, B)
