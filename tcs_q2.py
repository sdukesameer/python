'''End 99 98 S(7) 96 95 94 93 92 91
81 82 L(99) 84 L(98) 86 87 88 89 90
80 79 78 77 76 75 74 73 72 71
61 S(22) 63 64 65 66 67 68 69 70
60 59 58 S(14) 56 55 54 53 52 51
41 42 43 44 45 46 L(80) 48 49 50
40 39 38 37 36 35 34 33 32 31
21 22 23 L(63) 25 26 27 28 29 30
20 19 S(2) 17 16 15 14 13 12 11
Start 2 3 4 5 6 7 8 9 10
7 3 5 2 2 4 1 5'''
arr, c = [], 1
for i in range(10):
	col = []
	for j in range(10):
		col.append(c)
		c = c + 1
	arr.append(col)

for i in range(9, -1, -1):
	if i % 2 == 0:
		str, j = input(), 0
		for k in str.split(" "):
			#print(k)
			if k.startswith('S(') or k.startswith('L('):
				#print(k[2:-1])
				if k[2:-1]=='Start':
					arr[i][j] = 1
				elif k[2:-1] == 'End':
					arr[i][j] = 0
				else:
					arr[i][j] = int(k[2:-1])
			j = j + 1
	else:
		str, j = input(), 9
		for k in str.split(" "):
			#print(k)
			if k.startswith('S(') or k.startswith('L('):
				#print(k[2:-1])
				if k[2:-1] == 'Start':
					arr[i][j] = 1
				elif k[2:-1] == 'End':
					arr[i][j] = 0
				else:
					arr[i][j] = int(k[2:-1])
			j = j - 1

p, s, l = 0, 0, 0
inp = input().split(" ")
for k in inp:
	if p + int(k) < 101:
		p += int(k)
		t=p
		if p%10==0:
			p = arr[int(p/10)-1][9]
		else:
			p=arr[int(p/10)][int(p%10)-1]
		if t<p:
			l+=1
		elif t>p:
			s+=1
		if p == 100:
			break
if p==100:
	print("Possible", s, l, end='\n')
else:
    print("Not Possible", s, l, p, end='\n')
