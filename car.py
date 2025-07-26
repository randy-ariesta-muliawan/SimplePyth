class Mobil:

	def __init__(self, buatan, model, tahun, warna='Hitam'):
		self.buatan = buatan
		self.model = model
		self.tahun = tahun
		self.warna = warna #default value dgn argument
		self.odometer = 0 #default value yg constant

	def tentang_mobil(self):
		print(f"Mobil ini buatan {self.buatan} dengan model {self.model} yang dirakit pada tahun {self.tahun} dan berwarna {self.warna}")

	def tampilkan_odometer(self):
		print(f"Mobil telah berjalan sejauh {self.odometer} KM")

	def ubah_odometer(self, jarak):
		if jarak < self.odometer :
			print("Akses ditolak")
		else:
			self.odometer = jarak
			print("Odometer berhasil diubah")

	def kenaikan_odometer(self):
		self.odometer += 1

	def mengisi_bensin(self):
		print("Mobil sedang diisi bensin")

my_toyota = Mobil('Toyota', 'Avanza', 2019)
my_toyota.tentang_mobil()
my_toyota.tampilkan_odometer()

my_brio = Mobil('Honda', 'Brio', 2020, 'Biru')
my_brio.tentang_mobil()
my_brio.tampilkan_odometer()

#Memodifikasi / mengubah nilai dari attribut secara langsung
my_toyota.odometer = 9
my_toyota.tampilkan_odometer()

#Memodifikasi / mengubah nilai dari attribut dengan method di dalam class
my_toyota.ubah_odometer(12)
my_toyota.tampilkan_odometer()


for i in range(100):
	my_toyota.kenaikan_odometer()

my_toyota.tampilkan_odometer()

class Baterai:

	def __init__(self, ukuran=75):
		self.kapasitas = kapasitas

	def tentang_baterai(self):
		print(f"Sisa kapasitas baterai saat ini : {self.kapasitas} % ")

	def estimasi_jarak_tempuh(self):
		pesan = "Estimasi jarak sekitar"
		if self.kapasitas > 75:
			print(pesan,"100 KM")
		elif self.kapasitas > 50:
			print(pesan,"50 KM")
		else:
			print(pesan,"25 KM")


class MobilListrik(Mobil):

	def __init__(self, buatan, model, tahun, warna='Hitam'):
		super().__init__(buatan, model, tahun, warna)
		self.baterai = Baterai(100)

	#Overriding Method dari Parent Class
	def mengisi_bensin(self):
		print("Mobil ini tidak perlu diisi bensin")


my_tesla = MobilListrik('Tesla', 'Model E', 2020, 'Merah')
my_tesla.tentang_mobil()
my_tesla.baterai.tentang_baterai()
my_tesla.mengisi_bensin()
my_tesla.baterai.estimasi_jarak_tempuh()