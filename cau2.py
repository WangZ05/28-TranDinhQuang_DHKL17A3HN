class TS:
    def __init__(self, ten, diem_toan, diem_ly, diem_hoa):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

# Initialize an empty list to store the candidates
candidates = []

# Nhập dữ liệu của thí sinh
def nhap_thong_tin():
    ten = input("Nhập họ tên của thí sinh: ")
    diem_toan = float(input("Nhập điểm môn Toán: "))
    diem_ly = float(input("Nhập điểm môn Lý: "))
    diem_hoa = float(input("Nhập điểm môn Hóa: "))
    candidate = TS(ten, diem_toan, diem_ly, diem_hoa)
    candidates.append(candidate)

# In ra danh sách thì sinh trúng tuyển
def in_thong_tin_trung_tuyen():
    print("Danh sách thí sinh trúng tuyển:")
    print("-------------------------------")
    for candidate in candidates:
        if candidate.tinh_tong_diem() >= 20:
            print(f"Họ tên: {candidate.ten}, Tổng điểm: {candidate.tinh_tong_diem()}")

# Nhập vào số lượng thí sinh
so_thi_sinh = int(input("Nhập số lượng thí sinh: "))
for _ in range(so_thi_sinh):
    nhap_thong_tin()

# In ra danh sách thi sinh trúng tuyển
in_thong_tin_trung_tuyen()

