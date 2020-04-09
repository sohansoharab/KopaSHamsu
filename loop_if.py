# for x in range(1,20+1):
# 	if x==4 or x==13:
# 		print(f"{x} is unlucky")
# 	elif x%2==0:
# 		print(f"{x} is even")
# 	elif x%2!=0:
# 		print(f"{x} is odd")

# x = "\u0001"
# num = 1
# while num<16:
# 	print(num*x)
# 	num = num+1

# for num in range(1,15):
# 	print(num*"\u0001")

msg = input(":")
while msg != "stop copying me":
	print(":" + msg)
	msg = input(":")
print(":Alright! You win")