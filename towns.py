import requests
import sys
from bs4 import BeautifulSoup


def removeExtraLetters(word: str) -> str:
    new_word = word
    while new_word[-1] == 'ь' or new_word[-1] == 'ъ' or new_word[-1] == 'ы' or new_word[-1] == 'й':
        new_word = new_word[:-1]
    return new_word


r = requests.get('https://ru.wikipedia.org/wiki/Список_городов_России')
soup = BeautifulSoup(r.content, features="lxml")

townRaw = soup.find('table', 'standard sortable').tbody.contents[2:]
townsOfRussia = []
for town in townRaw:
    town = town.contents[2].a.string.lower()
    # delete "-"
    town.replace("-", " ")
    townsOfRussia.append(town)

if len(sys.argv) > 1:
    if sys.argv[1] == '-f':
        # filemod
        word = input('>').capitalize()
        townsOfRussia.remove(word)

        f = open('Игра в города {0}.txt'.format(word), 'w')
        print(word, file=f)

        while True:
            word = removeExtraLetters(word) # remove Ь Ъ Ы Й
            for newTown in townsOfRussia:
                if newTown[0] == word[-1]:
                    townsOfRussia.remove(newTown)
                    print(newTown.capitalize(), file=f)
                    word = newTown
                    break
            else:  # if don't break
                break
        f.close()

    elif sys.argv[1] != '-i':
        print("Error! Invalid param.")
        exit(1)
else:
    newTown = None
    while True:
        ans = input('> ').lower()
        if ans not in townsOfRussia:
            print("Town have to exist!")
            continue

        if newTown and newTown[-1] != ans[0]:
            print("Follow the riles!")
            continue
        ans = removeExtraLetters(ans)

        for newTown in townsOfRussia:
            if newTown[0] == ans[-1]:
                townsOfRussia.remove(newTown)
                print(newTown.capitalize())
                break
        else:
            print("You win!")
            exit(0)
        newTown = removeExtraLetters(newTown)
