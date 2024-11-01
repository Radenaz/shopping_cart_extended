# =================================================
# Graded Challenge 1

# Nama  : Niko Amrullah Hakam
# Batch : RMT-038

# Program ini dibuat untuk melakukan unittest nikoahakam_app.py 
# Ada 3 kategori unittest : 
#   1. Penambahan barang ke cart
#   2. Penghapusan barang dari cart
#   3. Perhitungan total belanja
# =================================================

import unittest
from nikoahakam_app import ShoopingCart, CartItem

class TestShoopingCart(unittest.TestCase):
    def setUp(self):
        self.carts = ShoopingCart()
    
    def test_tambah_barang(self):
        """create test object, assert item in object.kranjang
        [[nama, harga]] .
        
        """
        self.carts.tambah_barang("Ayam", 50_000)
        self.assertEqual(self.carts.kranjang[0].nama, "Ayam")
        self.assertEqual(self.carts.kranjang[0].harga, 50_000)
    
    def test_hapus_barang(self):
        self.carts.tambah_barang("Ayam", 50_000)
        self.carts.tambah_barang("Apple", 20_000)
        
        self.carts.hapus_barang("Ayam")
        self.assertEqual(self.carts.kranjang[0].nama, "Apple")
    
    def test_total_belanja(self):
        pass
    
    
if __name__ == "__main__":
    unittest.main()