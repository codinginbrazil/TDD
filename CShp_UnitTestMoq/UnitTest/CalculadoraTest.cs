using CShp_UnitTestMoq;
using FluentAssertions;
using Xunit;

namespace CShp_XUnitTest;

[Trait("Aplication", "Calculador")]
public class CalculadoraTest
{
    [Theory(DisplayName = "Opera��o entre dois numeros tendo um resultado")]
    [InlineData("somar", 3.2, 4.5, 7.7)]
    [InlineData("subtrair", 3, 4, -1)]
    [InlineData("multiplicar", 3.2, 4.5, 14.4)]
    [InlineData("dividir", 6, 2, 3)]
    [InlineData("asd", 3, 4, 7)]
    public void Operacao_Dois_Numeros(string operacao, double p1, double p2, double resultado)
    {
        //Arrange
        var calc = new Calculadora();

        //Act
        var result = calc.Calcular(operacao, p1, p2);

        //Assert
        result.resultado.Should().Be(resultado);
        result.operacao.Should().Be(operacao);
    }
}