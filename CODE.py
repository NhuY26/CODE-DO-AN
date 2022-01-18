class Nguoi:

    def __init__(self, ten, gioi_tinh, tuoi, dia_chi):
        self._ten = ten
        self._gioi_tinh = gioi_tinh
        self._tuoi = tuoi
        self._dia_chi = dia_chi

    def getTen(self):
        return self._ten

    def getDiaChi(self):
        return self._dia_chi

    def getTuoi(self):
        return self._tuoi

    def getGioiTinh(self):
        return self._gioi_tinh

    @classmethod
    def nhap(cls):
        ten = input("Nhap ten: ")
        gioi_tinh = input("Nhap gioi tinh: ")
        tuoi = input("Nhap tuoi: ")
        dia_chi = input("Nhap dia chi: ")
        return Nguoi(ten, gioi_tinh, tuoi, dia_chi)


class GiaoVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_gv, so_nam_kn, chuyen_mon, luong):
        super().__init__(ten, gioi_tinh, tuoi, dia_chi)
        self._ma_gv = ma_gv
        self._so_nam_kn = so_nam_kn
        self._chuyen_mon = chuyen_mon
        self._luong = luong


class SinhVien(Nguoi):
    def __init__(self, ten, gioi_tinh, tuoi, dia_chi, ma_sv, lop, chuyen_nganh):
        super().__init__(ten, gioi_tinh, tuoi, dia_chi)
        self._ma_sv = ma_sv
        self._lop = lop
        self._chuyen_nganh = chuyen_nganh

    def getMaSV(self):
        return self._ma_sv

    def getLop(self):
        return self._lop

    def getChuyenNganh(self):
        return self._chuyen_nganh


class MonHoc:

    def __init__(self, ma, ten, so_tin_chi):
        self._ma = ma
        self._ten = ten
        self._so_tin_chi = so_tin_chi

    def get_ma(self):
        return self._ma


class LopHoc:

    def __init__(self, ma, ten, so_sv, giao_vien, ds_sv, mon_hoc):
        self._ma = ma
        self._ten = ten
        self._so_sv = so_sv
        self._giao_vien = giao_vien
        self._ds_dv = ds_sv
        self._mon_hoc = mon_hoc


class BangDiem:

    def __init__(self, sinh_vien, mon_hoc, so_diem):
        self._sinh_vien = sinh_vien
        self._mon_hoc = mon_hoc
        self._so_diem = so_diem

    def get_sinh_vien(self):
        return self._sinh_vien

    def get_so_diem(self):
        return self._so_diem

    def __repr__(self) -> str:
        return f"Ten sinh vien: {self._sinh_vien.getTen()} - Diem: {self._so_diem}"

class QLSV:
    ds_sv = []
    ds_gv = []
    ds_mon = []
    ds_lop = []
    bang_diem = []

    # tìm sinh viên theo mã
    def tim_sv(self, ma_sv):
        result = None
        if (self.ds_sv.__len__() > 0):
            for sv in self.ds_sv:
                if (sv.get_ma() == ma_sv):
                    result = sv
        return result

    def nhap_sv(self):
        nguoi = Nguoi.nhap()
        ma_sv = input("Nhap ma sinh vien: ")
        lop = input("Nhap lop: ")
        chuyen_nganh = input("Nhap chuyen nganh: ")
        return SinhVien(nguoi.get_ten(), nguoi.get_gioi_tinh(), nguoi.get_tuoi(), nguoi.get_dia_chi(),
                        ma_sv, lop, chuyen_nganh)

    def them_sv(self):
        sinh_vien = self.nhap_sv()
        self.ds_sv.append(sinh_vien)

    def them_gv(self):
        nguoi = Nguoi.nhap()
        ma_gv = input("Nhap ma giao vien: ")
        so_nam_kn = input("Nhap so nam kinh nghiem: ")
        chuyen_mon = input("Nhap chuyen mon: ")
        luong = input("Nhap luong: ")
        giao_vien = GiaoVien(nguoi.get_ten(), nguoi.get_gioi_tinh(), nguoi.get_tuoi(), nguoi.get_dia_chi(),
                             ma_gv, so_nam_kn, chuyen_mon, luong)
        self.ds_gv.append(giao_vien)

    def tim_mon(self, ma_mon):
        result = None
        if (self.ds_mon.__len__() > 0):
            for mon in self.ds_mon:
                if (mon.get_ma() == ma_mon):
                    result = mon
        return result

    def them_mon(self):
        ma = input("Nhap ma mon hoc: ")
        ten = input("Nhap ten mon hoc: ")
        so_tin_chi = input("Nhap so tin chi: ")
        mon_hoc = MonHoc(ma, ten, so_tin_chi)
        self.ds_mon.append(mon_hoc)

    def them_lop(self):
        ma = input("Nhap ma lop hoc: ")
        ten = input("Nhap ten lop hoc: ")
        so_sv = input("Nhap so sinh vien: ")
        print("Nhap thong tin giao vien")
        giao_vien = GiaoVien.nhap()
        print("Nhap danh sach sinh vien")
        ds_sv_lop = []
        for i in range(int(so_sv)):
            sv = self.nhap_sv()
            ds_sv_lop.append(sv)
        print("NHAP MON HOC")
        mon_hoc = MonHoc.nhap()
        lop_hoc = LopHoc(ma, ten, so_sv, giao_vien, ds_sv_lop, mon_hoc)
        self.ds_lop.append(lop_hoc)

    def them_diem(self):
        ma_sv = input("Nhap ma sinh vien: ")
        ma_mon_hoc = input("Nhap ma mon hoc: ")
        sinh_vien = self.tim_sv(ma_sv)
        mon_hoc = self.tim_mon(ma_mon_hoc)
        so_diem = input("Nhap so diem: ")
        diem = BangDiem(sinh_vien, mon_hoc, so_diem)
        self.bang_diem.append(diem)

    def sap_xep_tang(self):
        for i in range(self.bang_diem.__len__()):
            for j in range(i + 1, self.bang_diem.__len__()):
                if (self.bang_diem[i].get_sinh_vien().get_ten() > self.bang_diem[j].get_sinh_vien().get_ten()):
                    self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
                elif self.bang_diem[i]._sinh_vien.get_ten() == self.bang_diem[j]._sinh_vien.get_ten():
                    if self.bang_diem[i].get_so_diem() > self.bang_diem[j].get_so_diem():
                        self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
        # viết vào file

        write_file = open('result.csv', 'w')
        write_file.write("Ma sinh vien,Ma mon hoc,Diem\n")
        for i in self.bang_diem:
            write_file.write(i.get_sinh_vien().get_ma() + "," +
                             i.get_mon_hoc().get_ma() + "," +
                             i.get_so_diem() + "\n")
        write_file.close()

        # đọc từ file ra

        read_file = open('result.csv', 'r')
        content = read_file.read()
        print(content)
        read_file.close()

    def sap_xep_giam(self):
        for i in range(self.bang_diem.__len__()):
            for j in range(i + 1, self.bang_diem.__len__()):
                if (self.bang_diem[i].get_sinh_vien().get_ten() < self.bang_diem[j].get_sinh_vien().get_ten()):
                    self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
                elif self.bang_diem[i]._sinh_vien.get_ten() == self.bang_diem[j]._sinh_vien.get_ten():
                    if self.bang_diem[i].get_so_diem() < self.bang_diem[j].get_so_diem():
                        self.bang_diem[i], self.bang_diem[j] = self.bang_diem[j], self.bang_diem[i]
        write_file = open('result.csv', 'w')
        write_file.write("Ma sinh vien,Ma mon hoc,Diem\n")
        for i in self.bang_diem:
            write_file.write(i.get_sinh_vien().get_ma() + "," +
                             i.get_mon_hoc().get_ma() + "," +
                             i.get_so_diem() + "\n")
        write_file.close()

        read_file = open('result.csv', 'r')
        content = read_file.read()
        print(content)
        read_file.close()

    def main(self):
        while (1 == 1):
            print("\nCHUONG TRINH QUAN LY SINH VIEN")
            print("*****************************MENU******************************")
            print("**  1. Them sinh vien.                                       **")
            print("**  2. Them giao vien.                                       **")
            print("**  3. Them mon hoc.                                         **")
            print("**  4. Them lop hoc.                                         **")
            print("**  5. Them diem.                                            **")
            print("**  6. Sap xep bang diem tang dan theo ten, sau do den diem. **")
            print("**  7. Sap xep bang diem giam dan theo ten, sau do den diem. **")
            print("**  8. Tim kiem theo ma sinh vien                           **")
            print("**  0. Thoat                                                 **")
            print("***************************************************************")

            key = int(input("Nhap tuy chon: "))
            if (key == 1):
                print("\n1. Them sinh vien.")
                self.them_sv()
                print("\nThem sinh vien thanh cong!")
            elif (key == 2):
                print("\n2. Them giao vien.")
                self.them_gv()
                print("\nThem giao vien thanh cong!")
            elif (key == 3):
                print("\n3. Them mon hoc.")
                self.them_mon()
                print("\nThem mon hoc thanh cong!")
            elif (key == 4):
                print("\n4. Them lop hoc.")
                self.them_lop()
                print("\nThem lop hoc thanh cong!")
            elif (key == 5):
                print("\n5. Them diem.")
                self.them_diem()
                print("\nThem diem thanh cong!")
            elif (key == 6):
                print("\n6. Sap xep bang diem tang dan theo ten, sau do den diem.")
                self.sap_xep_tang()
                print("\nSap xep tang dan thanh cong!")
            elif (key == 7):
                print("\n7. Sap xep bang diem giam dan theo ten, sau do den diem.")
                self.sap_xep_giam()
                print("\nSap xep giam dan thanh cong!")
            elif (key == 8):
                print("\n8. Tim  kiem theo ten sinh vien")
                ma = input("Nhap ma sinh vien can tim: ")
                sv = self.tim_sv(ma)
                if (sv):
                    print("Da tim thay sinh vien:")
                    print(sv)
                else:
                    print("Khong tim thay sinh vien nao")
            elif (key == 0):
                print("\nBan da chon thoat chuong trinh!")
                break
            else:
                print("\nKhong co chuc nang nay!")
                print("\nHay chon chuc nang trong hop menu.")


if __name__ == "__main__":
    qlsv = QLSV()
    qlsv.main()
