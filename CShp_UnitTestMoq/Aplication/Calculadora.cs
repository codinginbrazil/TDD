using System;
using Core.Interface;
using Core.Struct;

namespace CShp_UnitTestMoq;

public class Calculadora : ICalculadora
{
    public CalculadoraStruct Calcular(string operacao, double a, double b)
    {
        CalculadoraStruct resultadoOperacao;
        double c;
        switch (operacao)
        {
            case "somar":
                c = a + b;
                break;
            case "subtrair":
                c = a - b;
                break;
            case "multiplicar":
                c = a * b;
                break;
            case "dividir":
                c = Math.Round(a / b, 2);
                break;
            default:
                c = a + b;
                break;
        }

        resultadoOperacao = (operacao, c);
        return resultadoOperacao;
    }
}