class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_so_hop_le(self):
        if self.mau_so == 0:
            return False
        else:
            return True
    
    def nhap_phan_so(self):
        tu_so = int(input("Nhập vào tử số là :"))
        mau_so = int(input("Nhập vào mẫu số là :"))
        self.tu_so = tu_so
        self.mau_so = mau_so
        
    def in_phan_so(self):
        if self.kiem_tra_so_hop_le():
            print(f"{self.tu_so}/{self.mau_so}")
        else:
            print("Phân số không hợp lệ")

# Sử dụng lớp PhanSo
ps = PhanSo(2, 2)
ps.in_phan_so()

ps.nhap_phan_so()
ps.in_phan_so()