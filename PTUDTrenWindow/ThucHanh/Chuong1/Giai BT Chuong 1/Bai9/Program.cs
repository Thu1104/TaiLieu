using System;

namespace Bai9
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            Console.Write("Nhap n = ");
            n = Convert.ToInt32(Console.ReadLine());
            Console.Write("Cac so nguyen tu 1 den {0} la: ", n);
            int tong = 0;
            for(int i = 1; i<=n; i++)
            {
                Console.Write("{0} ", i);
                tong += i;
            }
            Console.WriteLine();
            float tb = (float)tong / n;
            Console.WriteLine("Tong = {0:0.00} Trung binh cong = {1:0.00}", tong, tb);
            Console.ReadLine();

        }
    }
}
