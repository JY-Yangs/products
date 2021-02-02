products = [] # 先創一個空清單
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quite
		break
	price = input('請輸入商品價格: ') # 放在break下面是因為在商品名稱輸入"q"之後就要跳出迴圈了, 不用再問價格
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

# note1: 'abc' + '123' = 'abc123'
# note2: 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f:
# 電腦原先如果沒有products.txt就會產生此檔案, 有的話會覆蓋掉舊檔案
# 明確告訴電腦要用"utf-8"這個編碼就要加encoding = 'utf-8', 這樣如果要寫入中文比較不會出錯
# 這邊也要注意一下讀取檔案的程式也是要用'utf-8'編碼讀取才不會發生錯誤
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 這一行才是真正的開始寫入
		# 要把把資料寫入檔案f就要這樣寫: f.write()
		# \n是"換行符號"
