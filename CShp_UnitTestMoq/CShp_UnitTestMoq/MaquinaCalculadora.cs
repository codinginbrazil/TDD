namespace CShp_UnitTestMoq
{
    public class MaquinaCalculadora
    {
        private ICalculadora calc;

        public MaquinaCalculadora() : this(new Calculadora())
        {}

        public MaquinaCalculadora(ICalculadora obj)
        {
            this.calc = obj;
        }

        public (string operacao, double resultado) Calcular(string tipoOperacao, double a, double b)
        {
            return calc.Calcular(tipoOperacao, a, b);
        }
    }
}
