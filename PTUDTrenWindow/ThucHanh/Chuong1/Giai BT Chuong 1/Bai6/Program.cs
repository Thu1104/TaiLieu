using System;

namespace Bai6
{
    class Program
    {
        static bool laSoNguyenTo(int n)
        {
            int found = 0;
            if (n <= 1) return false;
            for(int i=2; i <= Math.Sqrt(n); i++)
            {
                if (n % i == 0)
                {
                    found = 1; break;
                }
            }
            return found == 0;
        }
        static void Main(string[] args)
        {
            int n;
            Console.Write("Nhap so n = ");
            n = Convert.ToInt32(Console.ReadLine());
            //Program a = new Program();
            if (Program.laSoNguyenTo(n)) Console.WriteLine("{0} la so nguyen to", n);
            else Console.WriteLine("{0} khong la so nguyen to", n);
            Console.ReadLine();
        }
    }
}
