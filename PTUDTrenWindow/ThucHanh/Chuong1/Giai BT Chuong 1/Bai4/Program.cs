using System;

namespace Bai4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Chuong trinh giai phuong trinh bac 2: ");

            double a, b, c;
            double delta, x1, x2;

            Console.Write("Nhap a = "); a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Nhap b = "); b = Convert.ToDouble(Console.ReadLine());
            Console.Write("Nhap c = ");  c = Convert.ToDouble(Console.ReadLine());

            if (a == 0)
            { 
                if (b == 0)
                {
                    if (c == 0) Console.WriteLine("Phuong trinh co vo so nghiem!");
                    else Console.WriteLine("Phuong trinh vo nghiem!");
                }
                else Console.WriteLine("Phuong trinh co nghiem x = : {0}", -c / b);
            }    
            else
            {
                delta = b * b - a * a * c;
                if (delta == 0)
                    Console.WriteLine("Phuong trinh co nghiem kep x1=x2={0}", -b / (2 * a));
                else if (delta < 0)
                    Console.WriteLine("Phuong trinh vo nghiem!");
                else
                {
                    x1 = (-b - Math.Sqrt(delta)) / (2 * a);
                    x2 = (-b + Math.Sqrt(delta)) / (2 * a);
                    Console.WriteLine("Phuong trinh co 2 nghiem la: x1={0}; x2={1}", x1, x2);
                }
                Console.ReadLine();
            }
        }
    }
}
