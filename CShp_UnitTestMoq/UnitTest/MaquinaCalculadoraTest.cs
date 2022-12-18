using Core.Interface;
using CShp_UnitTestMoq;
using FluentAssertions;
using Moq;
using Moq.AutoMock;
using Xunit;

namespace UnitTest;

[Trait("Aplication", "MaquinaCalculadora")]
public class MaquinaCalculadoraTest
{
    [Theory(DisplayName = "Valida as operações entre dois numeros tendo resultado")]
    [InlineData("somar", 3.2, 4.5, 7.7)]
    [InlineData("subtrair", 3.2, 4.5, -1.3)]
    [InlineData("multiplicar", 3.2, 4.5, 14.4)]
    [InlineData("dividir", 3.2, 4.5, 0.71)]
    [InlineData("asd", 3, 4, 9)]
    public void Validade_Operacoes(string operacao, double p1, double p2, double resultado)
    {
        // Arrange
        var mock = new Mock<ICalculadora>();
        mock.Setup(x => x.Calcular(It.IsAny<string>(), It.IsAny<double>(), It.IsAny<double>()))
            .Returns((operacao, resultado));

        var maqCalc = new MaquinaCalculadora(mock.Object);

        // Act
        var op = maqCalc.Calcular(operacao, p1, p2);

        // Assert
        op.operacao.Should().Be(operacao);
        op.resultado.Should().Be(resultado);

        mock.Verify(x => x.Calcular(operacao, p1, p2), Times.Once, "Nunca chamado");
    }

    [Theory(DisplayName = "Operação entre dois numeros tendo um resultado")]
    [InlineData("somar", 3.2, 4.5, 7.7)]
    [InlineData("subtrair", 3.2, 4.5, -1.3)]
    [InlineData("multiplicar", 3.2, 4.5, 14.4)]
    [InlineData("dividir", 3.2, 4.5, 0.71)]
    [InlineData("asd", 3, 4, 9)]
    public void Operacao_Dois_Numeros_AutoMock(string operacao, double p1, double p2, double resultado)
    {
        // Arrange
        var mocker = new AutoMocker();
        var maqCalc = mocker.CreateInstance<MaquinaCalculadora>();

        mocker.GetMock<ICalculadora>()
            .Setup(x => x.Calcular(It.IsAny<string>(), It.IsAny<double>(), It.IsAny<double>()))
            .Returns((operacao, resultado));

        // Act
        var op = maqCalc.Calcular(operacao, p1, p2);

        // Assert
        op.operacao.Should().Be(operacao);
        op.resultado.Should().Be(resultado);

        mocker.GetMock<ICalculadora>().Verify(x => x.Calcular(operacao, p1, p2), Times.Once, "Nunca chamado");
    }
}