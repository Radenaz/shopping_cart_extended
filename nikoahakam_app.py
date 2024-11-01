
# =================================================
# Graded Challenge 1

# Nama  : Niko Amrullah Hakam
# Batch : RMT-038

# Program sederhana ini mememungkinan user untuk menambah, menghapus, dan 
# melihat barang di keranjang belanja (cart) mereka. 
# Tiap barang memiliki informasi nama barang dan harganya. User juga bisa melihat total harga belanjanya.
# =================================================

class CartItem():
    """__init__ has 2 args.
    nama : any and
    harga : numerical
    """
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    
class ShoopingCart():
    """Creates an object shoppingcart with an empty kranjang attribute, initially.

    Methods
    -------
    method : tambah_barang()
    method : hapus_barang()
    method : display_kranjang()
    method : total_belanja()
    method : activate_it()
    """
    def __init__(self):
        self.kranjang = []
    
    def tambah_barang(self, nama, harga):
        """Takes in 2 args. Passes them to CartItem() object.

        Args:
            nama (any): product name
            harga (numerical): price
        """
        brang = CartItem(nama, harga)
        self.kranjang.append(brang)
        
    
    def hapus_barang(self, nama):
        """Removes item from self.kranjang. One arg.
        by looping through this class atr. If found, .remove().

        Args:
            nama (str): case sensitive. product name
        """
        for i in self.kranjang:
            if i.nama == nama:
                self.kranjang.remove(i)
                
                break
        # if nama not in self.kranjang:
        #         print(f"===== Barang {nama} tidak ditemukan di keranjang")
    
    def display_kranjang(self):
        """Display self.kranjang.
        If empty, prints a notif.
        Else, loop then prints each.
        """
        if self.kranjang == []:
            print("----------------")
            print("====== Kranjang masih kosong!")
            print("----------------")
            
        else:
            print("----------------")
            print(" Barang di keranjang :")
            print("---------------")
            for i in self.kranjang:
                print(f"    - {i.nama} : IDR {i.harga:,}")
            print("==================")

    def total_belanja(self):
        """Sums harga from self.kranjang.

        Returns:
            numeric: total price.
        """
        total = []
        for i in self.kranjang:
            total.append(i.harga)
        return sum(total)
    
    def activate_it(self):
        """Main activation method for this class.
        """
        switch_it = True
        while switch_it:
            print(":: MENU ::")
            print("1. Tambah Barang")
            print("2. Hapus Barang")
            print("3. Tampilkan barang di keranjang")
            print("4. Lihat Total belanja")
            print("5. Exit")
            menu_input = input("Pilih angka (1 - 5) :   ")
            
            if menu_input == "1":
                nama = input(":::::: Masukan nama barang :     ")
                try:
                    harga = input(":::::: Masukan harga barang :    ")
                    self.tambah_barang(nama, float(harga))
                    print('================================')
                    print(f"===== Barang {nama} berhasil dimasukkan ke keranjang!")
                    print('================================')
                except ValueError:
                    print("==================")
                    print("====== Bukan numeric")
                    print("====== Masukkan angka numeric.")
                    print("==================")
                                
                
            elif menu_input == "2":
                nama = input("::::: Masukan nama barang yang akan dihapus:    ")
                self.hapus_barang(nama)
                if nama not in self.kranjang:
                    print(f"===== Barang {nama} tidak ditemukan di keranjang")
                else:
                    print(f"Barang {nama} berhasil dihapus dari keranjang")
                
            elif menu_input == "3":
                self.display_kranjang()
                
            elif menu_input == "4":
                total_bayar = self.total_belanja()
                print(f"====== Total yang harus dibayar:   IDR {total_bayar:,}")
                print("==================")
                
            elif menu_input == "5":
                print(":: Bye! Terima kasih sudah belanja di Toko Koto.")
                print(" ---------------------------------Come again soon!")
                switch_it = False
                
            else:
                print("Input salah. \nMasukkan angka 1, 2, 3, 4, atau 5")
                

if __name__ == "__main__":
    keranjang_01 = ShoopingCart()
    keranjang_01.activate_it()
                
