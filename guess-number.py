import random

r = random.randint(1,100)
while True:
	num = int(input('请猜数字：'))# do casting
	if num == r:
		print('你猜中了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
		
