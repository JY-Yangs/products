# 在寫一個讀取檔案的動作
products = [] # 先創一個空清單
with open('products.csv', 'r', encoding = 'utf-8') as f: #之前寫得檔案用utf-8寫, 所以讀取也要用utf-8才讀的到
	for line in f: # 讀取檔案f, 會一行一行讀取, 把暫時變數稱作"line"(任意名稱都可)
		if '商品,價格' in line:
			continue # 功能是"直接跳到下一迴"然後繼續 ; break是直接跳出迴圈
		name, price = line.strip().split(',') # 先strip掉換行符號\n, 再用','去切割
		# 由左至右: line先strip()在split()
		# split()這個函式可以用來切割東西
		# split()裡面填"字串", 則依照"填的那個字串"做切割
		# split()切割完的結果是"清單"
		# 因為已經知道切完的結果會有"左右兩塊"(去看讀取的檔案就知), 所以等號左邊的暫時變數可以這樣設定" name, price "
		# strip()可以把換行符號(\n)、空白去掉
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quite
		break
	price = input('請輸入商品價格: ') # 放在break下面是因為在商品名稱輸入"q"之後就要跳出迴圈了, 不用再問價格
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# note1: 'abc' + '123' = 'abc123'
# note2: 'abc' * 3 = 'abcabcabc'

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
# 電腦原先如果沒有products.txt就會產生此檔案, 有的話會覆蓋掉舊檔案
# 明確告訴電腦要用"utf-8"這個編碼就要加encoding = 'utf-8', 這樣如果要寫入中文比較不會出錯
# 這邊也要注意一下讀取檔案的程式也是要用'utf-8'編碼讀取才不會發生錯誤
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 這一行才是真正的開始寫入
		# 要把把資料寫入檔案f就要這樣寫: f.write()
		# \n是"換行符號"
