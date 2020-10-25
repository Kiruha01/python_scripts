import requests
from bs4 import BeautifulSoup 
import re

r = requests.get('https://ru.wikipedia.org/wiki/Список_городов_России')
soup = BeautifulSoup(r.content, features="lxml")

tables = soup.find('table', 'standard sortable').tbody.contents[2:]
towns=[]
for town in tables:
	towns.append(town.contents[2].a.string)
word = input('>').capitalize()

towns.remove(word)


# while True:
# 	print()
# 	ans = input('> ').capitalize()
# 	if ans in towns and word[-1] == ans[0].lower():
# 		towns.remove(ans)
# 	else:
# 		print('!!!!')
# 		continue
# 	while ans[-1] == 'ь' or ans[-1] == 'ъ' or ans[-1] == 'ы' or ans[-1] == 'й':
# 		ans = ans[:-1]
# 	for i in towns:
# 		if i[0].lower() == ans[-1]:
# 			towns.remove(i)
# 			print(i)
# 			word = i
# 			break
# 	while word[-1] == 'ь' or word[-1] == 'ъ' or word[-1] == 'ы' or word[-1] == 'й':
# 		word = word[:-1]


# =============================


f = open('Игра в города {0}.txt'.format(word), 'w')
print(word, file=f)
while True:
	for i in towns:
		if i[0].lower() == word[-1]:
			towns.remove(i)
			print(i, file=f)
			word = i
			break
	else:
		break
	while word[-1] == 'ь' or word[-1] == 'ъ' or word[-1] == 'ы' or word[-1] == 'й':
		word = word[:-1]
f.close()