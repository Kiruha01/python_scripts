from random import choice


def genSecuence(word, minNum=0, maxNum=100):
	for i in range(minNum, maxNum):
		yield str(word) % str(i)

words = ['photo_%s.png', 'image_%s.jpg', 'C://Program Files/Windows/datebase_%s.db', 'sound_%s.wav', 'music_%s.mp3', 'source_%s.vbs',
'C://Windows/Users/Alluser/SecretKey%s..qt', 'Program/files%s.cpp']

dlllist = ['C://Users/user', 'data', 'C://windows/Win32', 'C://windows/Hall', 'Done', 'C://windows/BIOS', 'C://windows/HardDisk', 'mouse', 'zip', 'ValeriyaTimakova', 'Hole', 
'Google', 'Win64', 'mic', 'Kernel32', 'C://windows/Newdev', 'C://Users/Msv1_0', 'C://windows/Msgina', 'batarey', 'putin']

def getDLL(count):
	for i in range(count):
		yield choice(dlllist) + '.dll'