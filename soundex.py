def soundex(word: str) -> str:
    index = ''
    word = word.upper()
    first = word[:1]
    word = word[1:]
    word.replace('a', '')
    word.replace('e', '')
    word.replace('i', '')
    word.replace('o', '')
    word.replace('u', '')
    word.replace('y', '')
    word.replace('h', '')
    word.replace('w', '')

    numbers = [
        ['b', 'f', 'p', 'v'],
        ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
        ['d', 't'],
        ['l'],
        ['m', 'n'],
        ['r']
    ]

    for char in word:
        for n in enumerate(numbers):
            for x in n[1]:
                if char == x.upper():
                    index += str(n[0] + 1)
                    break
    
    e = True
    while e:
        e = False
        for x in range(1, 7):
            if (str(x) + str(x)) in index:
                e = True
                index = index.replace(str(x) + str(x), str(x))

    if len(index) > 3:
        index = index[:4]
    elif len(index) < 3:
        for x in range(3 - len(index)):
            index += str(0)
    index = first + index
    return index

if __name__ == "__main__":
    print(soundex('Noovák') == soundex('Novákkk'))