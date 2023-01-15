using System;

namespace Bai7
{
    class Program
    {
        static bool laNamNhuan(int n)
        {
            if ((n % 4 == 0 && n % 100 != 0) || n % 400 == 0)
                return true;
            return false;
        }
        static void Main(string[] args)
        {
            int n;
            Console.Write("Nhap n = ");
            n = Convert.ToInt32(Console.ReadLine());
            if (Program.laNamNhuan(n))
                Console.WriteLine("{0} la nam nhuan", n);
            else Console.WriteLine("{0} khong la nam nhuan", n);
            Console.ReadLine();
        }
    }
}
