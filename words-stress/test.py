import sqlite3
import random
import time


def strtofloat(string):
	return time.mktime(time.strptime(string, '%d %b %Y'))

def floattostr(number):
	return time.strftime('%d %b %Y', time.localtime(number))

def doingWork(words):
	fail = []
	success = []
	count = 0
	while words:
		print()
		word = random.choice(words)
		print(word[0]+'\n'+'01234567890123456789----------{0}'.format(len(words)))
		while True:
			try:
				if int(input()) == word[1]:
					success.append(word)
					print('ДА')
				else:
					print('Правильный ответ: ', word[0][:word[1]] + word[0][word[1]].upper() + word[0][word[1]+1:])
					fail.append(word)
				break
			except:
				print('!!!!!!!!')

		words.remove(word)
		count += 1
	return success, fail

def getMiddleOfDate(date1, date2):
	res = strtofloat(date2)-strtofloat(date1)
	if res < 80000:
		res = 86400
	return res
	

def createNewTable(words, today, offset=0):
	newDateSuc = strtofloat(today) + offset
	newTable = floattostr(newDateSuc)
	try:
		cursor.execute("CREATE TABLE '{0}' (word text, indexOfBeat integer)".format((newTable)))
	except sqlite3.OperationalError:
		pass
	cursor.execute("INSERT INTO '"+ newTable +"' VALUES ('" + today + "', -1)")
	cursor.executemany("INSERT INTO '"+ newTable +"' VALUES (?,?)", words)
	conn.commit()

today = time.strftime('%d %b %Y')
print(today)
groupsWhichShouldDoToday = []
toDeleted = []

conn = sqlite3.connect("Beats.db")
cursor = conn.cursor()

# Есть ли план на сегодня

cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
allTables = cursor.fetchall()
for table in allTables:
	if table[1] == today:
		groupsWhichShouldDoToday.append(table[1])
	try:
		if strtofloat(table[1]) < strtofloat(today):
			toDeleted.append(table)
	except:
		pass

for table in toDeleted:
	cursor.execute("DROP TABLE '"+ table[1] + "'")
conn.commit()


# Нет плана
if not groupsWhichShouldDoToday:
	print('На сегодня плана нет')
	cursor.execute("SELECT * FROM noun")
	success, fail = doingWork(cursor.fetchall())


	# success
	#newDateSuc = time.mktime(time.strptime(today, '%d %b %Y')) + 604800 # +7 дней
	if success:
		createNewTable(success, today, 172800)
	# Fail
	# newDateFail = time.mktime(time.strptime(today, '%d %b %Y')) + 302400 # +3 дней
	if fail:
		createNewTable(fail, today, 86400)

else:
	for table in groupsWhichShouldDoToday:
		cursor.execute("SELECT word FROM '" + table + "' WHERE indexOfBeat=-1")
		previousDates = cursor.fetchall()
		previousDate = max(previousDates, key=lambda a:strtofloat(a[0]))[0]
		print(previousDate)
		cursor.execute("SELECT * FROM '" + table + "' WHERE indexOfBeat>=0")
		success, fail = doingWork(cursor.fetchall())

		if success:
			date = floattostr(strtofloat(today) + getMiddleOfDate(previousDate, today)*2)
			createNewTable(success, today, getMiddleOfDate(previousDate, today)*2) 
			print(date)
		if fail:
			date = getMiddleOfDate(previousDate, today)
			if date != 86400:
				date = date // 2
			createNewTable(fail, today, date) 
			date = floattostr(strtofloat(today) + date)
			print(date)
