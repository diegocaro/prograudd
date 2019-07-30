def word_count(message):
    counts = dict()
    words = message.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


mambo = '''Desde lima vengo a mi machaguay
Desde Lima vengo a mi machaguay
A bailar el mambo de mi machaguay
A bailar el mambo de mi machaguay'''

print(word_count(mambo))