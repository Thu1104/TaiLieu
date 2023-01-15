using System;

namespace Bai2
{
    class Program
    {
        static void Main(string[] args)
        {
            string HoTen;
            Console.Write("Nhap Ho va Ten: ");
            HoTen = Console.ReadLine();
            string HT = HoTen.ToUpper();

            double Diem;
            string d;
            Console.Write("Nhap diem: ");
            d = Console.ReadLine();
            Diem = Convert.ToDouble(d);

            string Loai;
            if (Diem >= 8)
                Loai = "Gioi";
            else if (Diem >= 6.5 && Diem < 8)
                Loai = "Kha";
            else if (Diem >= 5 && Diem < 6.5)
                Loai = "Trung binh";
            else Loai = "Yeu";

            Console.Write("Em {0} dat loai: {1}", HT, Loai);
            Console.ReadLine();

        }
    }
}
