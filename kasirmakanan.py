from os import system

def opsi_kasir():
	system("cls")
	opsi = """
APLIKASI PAYMENT MAKANAN
[A] - CEK MENU MAKANAN
[B] - CEK MEJA
[C] - CEK STOCK
[D] - TAMBAH PESANAN
[E] - PAYMENT
[Q] - KELUAR
	"""
	print(opsi)

def print_data_menu():
	for menu in data_menu:
		makanan = menu
		harga = data_menu[menu]["harga"]
		print(f"MAKANAN:{makanan}\t\tHARGA:{harga}")

def add_to_kasir():
	#tambah pesanan c
	print_header("MASUKAN PESANAN BARU")
	makanan = input("MAKANAN\t:")
	nama = input("NAMA\t:")
	nomor = input("NOMOR PESANAN\t:")
	total = input("TOTAL PESANAN\t:")
	
	user_ans = input("tekan Y untuk menyimpan(Y/N) : ")

	if verify_ans(user_ans):
		print("menyimpan data....")
		data_pesanan[nomor] = {
			"nama" : nama,
			"pesanan" : makanan,
			"total" : total
		}
		print("payment tersimpan")

	else:
		print("payment tidak tersimpan")
	input("tekan ENTER utk kembali ke MENU")

def cek_menu():
	print_header("SEMUA MENU")
	if len(data_menu) == 0:
		print("BELUM ADA MENU YANG DISIMPAN")
	else:
			print_data_menu()
	input("tekan ENTER untuk kembali MENU")

def cek_meja():
	print_header("CEK MEJA")
	meja = print("nomor meja yang dicari ? ")
	result = searching(input)
	input("tekan ENTER utk kembali ke MENU")

def cek_stock():
	makanan = input("Masukan makanan yang ingin di cek : ")
	if makanan in data_menu:
		stok = data_menu[makanan]["stok"]
		print(f"STOCK:{stok}\t")
	else:
		print("makanan tidak ditemukan")
	input("tekan ENTER utk kembali ke MENU")


def mau_bayar():
	print_header("PAYMENT")
	nomor = input("nomor \t:")
	if nomor in data_pesanan :
		nama = data_pesanan[nomor]["nama"]
		makan = data_pesanan[nomor]["pesanan"]
		total = data_pesanan[nomor]["total"]
		print(nama)
		print(makan)
		print(total)
	else:
		print("coba cek lagi.....")
	input("tekan ENTER untuk kembali MENU")


def searching(input):
	nomor = int(input())
	answer = nomor%2
	if answer == 0:
		print("meja tidak tersedia")
	else:
		print("meja tersedia")

def print_header(msg):
	system("cls")
	print(msg)

def verify_ans(char):
	char =  char.upper()
	if char == "Y" :
		return True
	else:
		return False

def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "A":
		cek_menu()
	elif char == "B":
		cek_meja()
	elif char == "C":
		cek_stock()
	elif char == "D":
		add_to_kasir()
	elif char == "E":
		mau_bayar()

data_menu = {
	"ayam loncat" : {
		"harga" : "23.000 ",
		"stok" : "23 porsi"
	},
	"ikan gejrot" : {
		"harga" :  "65.000",
		"stok" : "34 porsi"
	},
	"tahu goreng" : {
		"harga" : "13.000",
		"stok" : "20 porsi"
	}
}
stop = False

data_pesanan = {
	"068" : {
		"nama" : "budi",
		"pesanan" :  "ikan gejrot",
		"total" : "48.000"
	},

	"098" : {
		"nama" : "siti",
		"pesanan" : "tahu tempe goreng",
		"total" :"20.000"
	}

}

while not stop:
	opsi_kasir()
	user_input = input("pilihan....")
	user_input = user_input.upper()
	stop = check_input(user_input)