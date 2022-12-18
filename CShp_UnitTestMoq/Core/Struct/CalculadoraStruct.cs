namespace Core.Struct;

public record struct CalculadoraStruct(string operacao, double resultado)
{
    public static implicit operator (string operacao, double resultado)(CalculadoraStruct value)
    {
        return (value.operacao, value.resultado);
    }

    public static implicit operator CalculadoraStruct((string operacao, double resultado) value)
    {
        return new CalculadoraStruct(value.operacao, value.resultado);
    }
}