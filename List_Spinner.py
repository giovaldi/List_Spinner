#logicnya mirip sama spin matrix yang menerima nilai inisiasi z ='' kemudian menggunakan loop untuk mencari iterasinya kemudian print z
def counterClockwise(list_awal): #fungsi def yang menerima satu argumen yaitu list awal
    puterr = [] #list kosong untuk menerima hasil iterasi dari list_awal
    for i in range(len(list_awal[0]), 0, -1):#for loop yang mengiterasi di range len(list_awal[0]) = 3, 0 sebagai exclussive, dan -1 sebagai stepnya
        rumusan = list(map(lambda x: x[i-1], list_awal)) #lambda yang menerima argumen x[i-1] untuk mendapatkan puterr contoh : x[3-1], x[2-1] di variabel list_awal
        puterr.append(rumusan) #menambahkan nilai rumusan ke puterr dengan.append()
    return puterr#mengembalikan nilai puterr

print(counterClockwise([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]))

for i in counterClockwise([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]):print(i)
