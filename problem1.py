taste_case = int(input())
for j in range(0,taste_case):
	total_tastes = int(input())
	tastes = list(map(int,input().split()))
	c=[]
	result =[]
	for i in range(0,len(tastes)):
		if int(tastes[i])<0:
			c.append(-1)
		else:
			c.append(0)
		if -1 in c:
			result.append("No")
		else:
			result.append("Yes")
# for r in range(0,len(result)):
# 	print(result[r])
# print(result)
for r in result:
	print(r)