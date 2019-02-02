string_kalimat = 'You can can imagine cans '

daftar_kata = string_kalimat.split() # mendapatkan daftar kata

freq_kata = []
for w in daftar_kata:
    freq_kata.append(daftar_kata.count(w)) # menghitung frekuensi kata setiap anggota daftar kata

print("Kalimat\n" + string_kalimat +"\n")
print("Daftar Kata\n" + str(daftar_kata) + "\n")
print("Frekuensi\n" + str(freq_kata) + "\n")
print("Frekuensi, Kata\n" + str(zip(daftar_kata, freq_kata)))