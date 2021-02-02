products = [] # 先創一個空清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quite
		break
	price = input('請輸入商品價格: ') # 放在break下面是因為在商品名稱輸入"q"之後就要跳出迴圈了, 不用再問價格
	# sub_list_p = []
	# sub_list_p.append(name)
	# sub_list_p.append(price)
	sub_list_p = [name, price] # 7 - 9 行可以直接這樣寫:
	products.append(sub_list_p) # 把一個清單裝進另一個清單裡面(二維清單)
	
	# products.append([name, price]) 7 - 11行都不寫，直接寫13行也行
print(products)

# 二維清單的存取方式: product[0][0] => ex: products = [[a0,b0],[c1,d1]]
# 左邊的0: 大清單的位置 => [a0,b0]
# 右邊的0: 子清單的位置 => a0

print(products[0][0]) # 印出來確認

for p in products: # 確認2為清單用for loop印出來是什麼
	print(p)

for p in products:
	print(p[0], '的價格是', p[1])