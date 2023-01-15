using System;

namespace Bai3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Chuong trinh giai phuong trinh bac 1: bx + c = 0");
            
            double b, c;

            Console.Write("Nhap b: "); b = Convert.ToDouble(Console.ReadLine());
            Console.Write("Nhap c: "); c = Convert.ToDouble(Console.ReadLine());

            if (b == 0)
            {
                if (c == 0) Console.WriteLine("Phuong trinh co vo so nghiem!");
                else Console.WriteLine("Phuong trinh vo nghiem!");
            }
            else Console.WriteLine("Phuong trinh co nghiem x = : {0}", -c / b);
            
            Console.ReadLine();
        }
    }
}
