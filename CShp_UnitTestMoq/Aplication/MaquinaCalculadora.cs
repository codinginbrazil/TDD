using Core.Interface;
using Core.Struct;

namespace CShp_UnitTestMoq;

public class MaquinaCalculadora
{
    private readonly ICalculadora Calc;

    public MaquinaCalculadora(ICalculadora obj)
    {
        Calc = obj;
    }

    public CalculadoraStruct Calcular(string tipoOperacao, double a, double b)
    {
        return Calc.Calcular(tipoOperacao, a, b);
    }
}