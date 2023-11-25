n = int(input())
synonims = {}

for _ in range(n):
    word = input()
    synonim = input()

    if word in synonims:
        synonims[word].append(synonim)
    else:
        synonims[word] = [synonim]

for word, synonym_list in synonims.items():
    synonym_string = ', '.join(synonym_list)
    print(f'{word} - {synonym_string}')
