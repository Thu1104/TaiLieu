using System;

namespace Bai5
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            do
            {
                Console.Write("Nhap n = "); 
                n = Convert.ToInt32(Console.ReadLine());
            } while (n <= 0);
            Console.ReadLine();
        }
    }
}
