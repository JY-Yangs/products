import os # operating system, "os"為"標準函式庫"裡面就有的東西可以直接import進來"這個模組"
# Refactor 重構, 重新把架構都寫成funcion, 和有一個main() function程式的進入點
# 讀取檔案
def read_file(filename): # 把檔名設成參數比較靈活, 可讀別的檔案
	products = [] # 先創一個空清單
	with open(filename, 'r', encoding = 'utf-8') as f: #之前寫得檔案用utf-8寫, 所以讀取也要用utf-8才讀的到
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
	return products #讀完資料要回傳products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q': #quite
			break
		price = input('請輸入商品價格: ') # 放在break下面是因為在商品名稱輸入"q"之後就要跳出迴圈了, 不用再問價格
		products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# note1: 'abc' + '123' = 'abc123'
# note2: 'abc' * 3 = 'abcabcabc'

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
	# 電腦原先如果沒有products.txt就會產生此檔案, 有的話會覆蓋掉舊檔案
	# 明確告訴電腦要用"utf-8"這個編碼就要加encoding = 'utf-8', 這樣如果要寫入中文比較不會出錯
	# 這邊也要注意一下讀取檔案的程式也是要用'utf-8'編碼讀取才不會發生錯誤
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') # 這一行才是真正的開始寫入
			# 要把把資料寫入檔案f就要這樣寫: f.write()
			# \n是"換行符號"



def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在
		# os這個模組裡面"的"path模組裡面"的"isfile()這個功能 的意思
		# isfile()這個功能可以檢查檔案在不在
		# isfile('products.csv')這個寫法可確定在跟"這個pythont程式"相同資料夾內有沒有要找的那個檔案(相對路徑)
		# isfile()如果要確定別的地方的檔案在不在, 就要填"絕對路徑"
		print('yeah! 找到檔案了!')
		products = read_file(filename)
		print(products)
	else:
		print('找不到檔案.....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()