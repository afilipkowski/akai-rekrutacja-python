# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
word_count = dict()

for sentence in range(len(sentences)):
    words = sentences[sentence].split()
    for w in words:
        if w.lower() in word_count:
            word_count[w.lower()] += 1
        if w.lower() not in word_count:
            word_count[w.lower()] = 1


count_sorted = sorted(word_count, key=word_count.get, reverse=True)

i = 1
for x in count_sorted:
    if i > 3:
        break
    else:
        print(i, ". " ,x, "-", word_count[x])
        i+=1

