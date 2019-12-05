flag = False
N = int (input ())
for i in range (N):
	x = int (input ())
	flag = (x % 10 == 0) or flag
print (flag)