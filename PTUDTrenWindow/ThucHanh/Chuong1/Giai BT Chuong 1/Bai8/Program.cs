using System;

namespace Bai8
{
    class Program
    {
        static void Main(string[] args)
        {
            int n;
            Console.Write("Nhap n = ");
            n = Convert.ToInt32(Console.ReadLine());

            float S1 = 0, S2 = 0;
            for(int i = 1; i<=n; i++)
            {
                S1 += i;
                S2 += (float)1/i;
            }
            Console.WriteLine("S1 = {0:0.00} S2 = {1:0.00}", S1, S2);
            Console.ReadLine();
        }
    }
}
