using System;
using System.Collections.Generic;
using System.Linq;

namespace BiquadraticEquation
{
    class Program
    {
        static void Main(string[] args)
        {
            double a, b, c;
            if (args.Length == 3)
            {
                if (double.TryParse(args[0], out a) && double.TryParse(args[1], out b) && double.TryParse(args[2], out c))
                {
                    Console.WriteLine("Коэффициенты из аргументов командной строки:");
                    Console.WriteLine($"A = {a}, B = {b}, C = {c}");
                }
                else
                {
                    Console.WriteLine("Введите коэффициенты вручную:");
                    GetCoefficientsFromKeyboard(out a, out b, out c);
                }
            }
            else
            {
                GetCoefficientsFromKeyboard(out a, out b, out c);
            }
            double D = b * b - 4 * a * c;
            List<double> roots = new List<double>();

            if (D > 0)
            {
                double temp_root1 = (-b + Math.Sqrt(D)) / (2 * a);
                double temp_root2 = (-b - Math.Sqrt(D)) / (2 * a);

                if (temp_root1 >= 0)
                {
                    roots.Add(Math.Sqrt(temp_root1));
                    roots.Add(-Math.Sqrt(temp_root1));
                }
                if (temp_root2 >= 0)
                {
                    roots.Add(Math.Sqrt(temp_root2));
                    roots.Add(-Math.Sqrt(temp_root2));
                }
            }
            else if (D == 0)
            {
                double temp_root = -b / (2 * a);
                if (temp_root >= 0)
                {
                    roots.Add(Math.Sqrt(temp_root));
                    roots.Add(-Math.Sqrt(temp_root));
                }
            }
            roots = roots.Distinct().ToList();
            if (roots.Count == 0)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Нет действительных корней!");
                Console.ResetColor();
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Корни:");
                foreach (double root in roots)
                {
                    Console.WriteLine($"x = {root}");
                }

                Console.ResetColor();
            }

            // Ожидание ввода перед закрытием окна
            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadKey();
        }

        static void GetCoefficientsFromKeyboard(out double a, out double b, out double c)
        {
            Console.Write("Введите A: ");
            while (!double.TryParse(Console.ReadLine(), out a))
            {
                Console.Write("Введите заново A: ");
            }

            Console.Write("Введите B: ");
            while (!double.TryParse(Console.ReadLine(), out b))
            {
                Console.Write("Введите заново B: ");
            }

            Console.Write("Введите C: ");
            while (!double.TryParse(Console.ReadLine(), out c))
            {
                Console.Write("Введите заново C: ");
            }
        }
    }
}