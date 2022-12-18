using System;

namespace CShp_UnitTestMoq;

public static class Program
{
    public static void Main()
    {
        Calculadora calc = new();

        var resultado = calc.Calcular("soma", 1, 4);
        Console.WriteLine($"{resultado.operacao} de 1 com 4 é igual a {resultado.resultado}");
        Console.ReadLine();
    }
}