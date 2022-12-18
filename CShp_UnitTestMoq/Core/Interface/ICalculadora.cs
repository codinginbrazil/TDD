using Core.Struct;

namespace Core.Interface;

public interface ICalculadora
{
    CalculadoraStruct Calcular(string operacao, double a, double b);
}