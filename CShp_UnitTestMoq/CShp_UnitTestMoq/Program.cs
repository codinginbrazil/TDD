using System;

namespace CShp_UnitTestMoq
{
    class Program
    {
        static void Main(string[] args)
        {
            Calculadora calc = new Calculadora();

            (string op, double res) resultado = calc.Calcular("som", 1, 4);
            Console.WriteLine($"{resultado.op} de 1 com 4 é igual a {resultado.res}" );
            Console.ReadLine();
        }
    }
}
