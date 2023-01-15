using System;

namespace Bai1
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b, c;
            string a_chuoi, b_chuoi, c_chuoi;
            Console.WriteLine("Chuong trinh tim so nho nhat trong 3 so:");

            Console.Write("Nhap vao a: ");
            a_chuoi = Console.ReadLine();
            a = Convert.ToInt32(a_chuoi);

            Console.Write("Nhap vao b: ");
            b_chuoi = Console.ReadLine();
            b = Convert.ToInt32(b_chuoi);

            Console.Write("Nhap vao c: ");
            c_chuoi = Console.ReadLine();
            c = Convert.ToInt32(c_chuoi);

            int min = a;
            if (b < min) min = b;
            if (c < min) min = c;
            Console.Write("So nho nhat cua {0},{1},{2} la: {3}", a, b, c, min);
            Console.ReadLine();
        }
    }
}
