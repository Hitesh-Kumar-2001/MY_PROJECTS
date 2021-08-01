menu= {1: 3.50, 2: 2.50, 3: 4.00, 4: 3.50, 5: 1.75, 6: 1.50, 7: 2.25, 8: 3.75, 9: 1.25}
dish= {1: 'Chicken Strips 	', 2: 'French Fries 	', 3: 'Hamburger 	', 4: 'Hotdog		', 5: 'Large Drink 	', 6: 'Medium Drink	', 7: 'Milk Shake 	', 8: 'Salad		', 9: 'Small Drink 	'}
while 2:
	print("\t---------------------------MENU-------------------------------")
	print("1. Chicken Strips @ $3.50/pc")
	print("2. French Fries @ $2.50/pc")
	print("3. Hamburger @ $4.00/pc")
	print("4. Hotdog @ $3.50/pc")
	print("5. Large Drink  @ $1.75/pc")
	print("6. Medium Drink @ $1.50/pc")
	print("7. Milk Shake @ $2.25/pc")
	print("8. Salad @ $3.75/pc")
	print("9. Small Drink @ $1.25/pc")
	print("Please press 0 to exit the program if your order is complete")
	ans=0
	order={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	s=input("Please enter the order string\n")
	if s=='0':
		break
	for i in range(len(s)):
		x=ord(s[i])-ord('0')
		ans+=menu[x]
		order[x]+=1
	print("Order Details:-")
	print("Item\t\tQuantity")
	for i in range(1,10,1):
		if order[i]!=0:
			print(dish[i],order[i])
	print('The total order cost is $',end='')
	print('%.3f'%ans)

