// O Resumo da Orientação a Objetos em Código

/**
 * CLASSE ABSTRATA: Um molde parcialmente pronto que não pode ser instanciado diretamente.
 * Usada para estabelecer a ABSTRAÇÃO e a relação "é um"[cite: 128, 130].
 *
 * Neste exemplo, 'ContaBancaria' é a base que define os atributos (dados) essenciais
 * e comportamentos comuns (métodos) de qualquer conta[cite: 190, 191].
 */
public abstract class ContaBancaria {

    // ---------------------------------------------------------------------------------
    // | PILAR 2: ENCAPSULAMENTO (Pág. 7) |
    // ---------------------------------------------------------------------------------

    // Atributos privados: Protegem o acesso direto aos dados[cite: 78, 162].
    // São agrupados com comportamentos (métodos) dentro da "cápsula" do objeto[cite: 69].
    private String titular;
    private String numeroConta;
    private double saldo;

    // Construtor: Inicializa a conta[cite: 199].
    public ContaBancaria(String titular, String numeroConta) {
        this.titular = titular; // [cite: 202]
        this.numeroConta = numeroConta; // [cite: 203]
        this.saldo = 0.0; // [cite: 204]
    }

    // Métodos (Comportamentos): O acesso ao 'saldo' é controlado por métodos públicos.
    public void depositar(double valor) {
        if (valor > 0) { // Garante a integridade dos dados (Validação) [cite: 196, 207]
            this.saldo += valor;
            System.out.println("Depósito de " + valor + " realizado com sucesso.");
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }

    // Método 'sacar' na classe base. Será sobreposto (Overriding) pelas subclasses.
    public boolean sacar(double valor) {
        if (valor > 0 && valor <= saldo) { // Regra padrão: só saca se tiver saldo. [cite: 264]
            this.saldo -= valor; // [cite: 223]
            System.out.println("Saque de " + valor + " realizado com sucesso.");
            return true;
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
            return false;
        }
    }

    // Getters: Expõem os dados de forma controlada (Encapsulamento)[cite: 81, 193].
    public double getSaldo() {
        return saldo; // [cite: 237]
    }
    public String getTitular() {
        return titular; // [cite: 231]
    }

    // Setter protegido para uso interno das subclasses (ex: ContaCorrente, Poupanca)
    // Não é fornecido um setter público para prevenir a alteração direta do saldo[cite: 239].
    protected void setSaldo(double saldo) {
        this.saldo = saldo;
    }


    // ---------------------------------------------------------------------------------
    // | HERANÇA E POLIMORFISMO EM AÇÃO (Pág. 8 e 9) |
    // ---------------------------------------------------------------------------------

    /**
     * SUBCLASSE: ContaCorrente
     * PILAR 3: HERANÇA: 'extends ContaBancaria' reutiliza o código e estabelece a relação "é um"[cite: 85, 87].
     */
    public static class ContaCorrente extends ContaBancaria {
        private double limiteChequeEspecial;

        public ContaCorrente(String titular, String numeroConta, double limiteChequeEspecial) {
            super(titular, numeroConta); // Usa 'super' para chamar o construtor da classe pai [cite: 87, 300]
            this.limiteChequeEspecial = limiteChequeEspecial; // Atributo especializado
        }

        /**
         * PILAR 4: POLIMORFISMO (Sobreposição/Overriding):
         * O mesmo método 'sacar' tem um comportamento diferente aqui (Muitas Formas)[cite: 98, 102].
         * Ele considera o limite do cheque especial, além do saldo[cite: 253, 292].
         */
        @Override
        public boolean sacar(double valor) {
            double saldoDisponivel = getSaldo() + limiteChequeEspecial; // Cálculo especializado
            if (valor > 0 && valor <= saldoDisponivel) { // Verifica limite disponível [cite: 303]
                setSaldo(getSaldo() - valor); // Atualiza saldo [cite: 304]
                System.out.println("Saque C/C de " + valor + " realizado. Saldo atualizado.");
                return true; // [cite: 305]
            } else {
                System.out.println("Saque C/C inválido: Limite indisponível."); // [cite: 309]
                return false;
            }
        }
    }

    /**
     * SUBCLASSE: ContaPoupanca
     * PILAR 3: HERANÇA: Adiciona funcionalidades específicas (Especialização)[cite: 89].
     */
    public static class ContaPoupanca extends ContaBancaria {
        private double taxaRendimento = 0.005; // Exemplo de taxa

        public ContaPoupanca(String titular, String numeroConta) {
            super(titular, numeroConta);
        }

        public void aplicarRendimento() {
            double rendimento = getSaldo() * taxaRendimento;
            depositar(rendimento); // Reutiliza o método 'depositar' da classe pai
            System.out.println("Rendimento de " + rendimento + " aplicado.");
        }

        // O método 'sacar' da ContaPoupanca não é sobreposto, ele mantém o comportamento da classe pai.
    }


    // ---------------------------------------------------------------------------------
    // | DEMONSTRAÇÃO DO POLIMORFISMO (Pág. 9) |
    // ---------------------------------------------------------------------------------

    public static void main(String[] args) {
        // Criação de objetos: Instâncias concretas da classe (Planta -> Casa) [cite: 31, 35]
        ContaBancaria contaPadrao = new ContaCorrente("João", "100-1", 0.0); // Polimorfismo por referência
        ContaCorrente contaCC = new ContaCorrente("Ana", "101-2", 500.0);
        ContaPoupanca contaCP = new ContaPoupanca("Pedro", "102-3");

        System.out.println("--- PILAR 4: POLIMORFISMO (Método Sacar) ---");

        contaCC.depositar(100.0);
        System.out.print("Conta Corrente (saldo 100, limite 500): ");
        // O saque C/C consegue usar o limite! (Comportamento especializado)
        contaCC.sacar(400.0); // Saque bem-sucedido (saldo -300)

        System.out.print("\nConta Poupança (saldo 0): ");
        // O saque C/P usa o comportamento original (Não sobreposto)
        contaCP.sacar(400.0); // Saque falha (Saldo insuficiente)

        System.out.println("\nConta Poupança aplica rendimento:");
        contaCP.depositar(2000.0);
        contaCP.aplicarRendimento(); // Comportamento especializado
        System.out.println("Saldo final C/P: " + contaCP.getSaldo());

        // Para aprofundar: Próximos Passos
        System.out.println("\n--- PRÓXIMOS PASSOS (Pág. 10 e 15) ---");
        System.out.println("- Interfaces: Contrato de comportamento ('sabe fazer')[cite: 141, 143].");
        System.out.println("- Pratique: Crie seus próprios projetos para solidificar os 4 pilares[cite: 334, 335].");
    }
}