import numpy as np

# membaca file txt
file = open('a.txt', 'r')
book = file.read()

# membagi kalimat menjadi kata dalam array
def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None

# menyimpan satu kata di setiap kalimat tanpa dobel
def type(tokens):
    final_token = []

    for tok in tokens:
        if tok not in final_token:
            final_token.append(tok)
    return final_token

# menghitung frekuensi dari setiap kata yang difilter oleh fungsi type
def final_count():
    freq = []
    total_count = 0

    for word in token:
        freq.append(count_word(words, word))
    return freq

# menghitung frekuensi
def count_word(tokens, token):
    count = 0

    for word in tokens:
        if word == token:
            count += 1
    return count

# Tokenize kalimat di file
words = tokenize()
# mencari kata tanpa dobel
token = type(words)
# menghitung frekuensi
freq = final_count()
# print kalimat awal
print('Sentence: ',book)
# print banyak tipe
print('Type: ', len(token))
# print perbaris
row = np.column_stack((token,freq))
print("Word, Frequency : \n", row)
# rata-rata freq
avg = np.sum(freq) / len(token)
print("Average Freq: \n", avg)