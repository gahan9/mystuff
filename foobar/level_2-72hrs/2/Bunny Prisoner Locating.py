def answer(x, y):
	row_result = 0
	for rows in range(1, x+1):
		row_result += rows
	col_result = row_result
	if y==1:
		return str(col_result)
	elif x==y==1:
		return "1"
	else:
		count = 0
		for cols in range(0,y-1):
			count +=1
			col_result = x + cols + col_result
		return str(col_result)


print(answer(5,10))
print(answer(9,10))
# print(answer(1,1))
print(answer(1,3))
print(answer(2,3))
print(answer(3,3))
print(answer(3,2))
# print(answer(100000,55555))