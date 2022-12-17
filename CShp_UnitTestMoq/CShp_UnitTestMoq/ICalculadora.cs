namespace CShp_UnitTestMoq
{
    public interface ICalculadora
    {
        (string operacao, double resultado) Calcular(string operacao, double a, double b);
    }
}
