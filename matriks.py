import eka118

# Definisikan dua matriks 3x3
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]

# Perkalian matriks 3x3 
print("Perkalian Matriks 3x3")
hasil_kali = eka118.kali_matriks_3x3(A, B)
for row in hasil_kali:
    print(row)

# Penjumlahan
print("\nPenjumlahan Matriks")
hasil_tambah = eka118.tambah(A, B)
for row in hasil_tambah:
    print(row)

# Determinan
print("\nDeterminan Matriks A")
det_A = eka118.determinan(A)
print(det_A)

#Transpose
print("\nTranspose Matriks A")
trans_A = eka118.transpose(A)
print(trans_A)

# Invers
C = [[4, 7, 2],
    [3, 6, 1],
    [2, 5, 3]]
print("\nInvers Matriks C")
inv_C = eka118.invers(C)
for row in inv_C:
    print([round(x, 2) for x in row]) 
