// O Resumo da Introdução ao Java em Código

/**
 * Esta classe encapsula os conceitos fundamentais de Java e Programação Orientada a Objetos (POO),
 * conforme apresentado no material de introdução.
 */
public class ResumoIntroducaoJava {

    // ---------------------------------------------------------------------------------
    // | VARIÁVEIS E TIPOS (Pág. 5 e 6) |
    // ---------------------------------------------------------------------------------

    // Tipos Primitivos (exemplos)
    int anoCriacao = 1995; // Sun Microsystems [cite: 32]
    double pi = 3.14;      // 'double' armazena números com casas decimais [cite: 67]
    boolean isOrientadaAObjetos = true; // 'boolean' só aceita 'true' ou 'false' [cite: 67, 32]

    // Inferência de Tipo com 'var' (Java 10+)
    // O compilador infere o tipo automaticamente, mantendo-o estático [cite: 91, 101, 102]
    var nomeLinguagem = "Java"; // inferido como String [cite: 92, 76]
    var versaoLTS = 21;         // inferido como int (exemplo moderno) [cite: 258]

    // Outros Tipos Não-Primitivos (Essenciais) [cite: 75]
    String mantra = "Write Once, Run Anywhere"; // [cite: 31]
    // Arrays, Classes, Interfaces (vistos mais adiante no curso) [cite: 77, 78, 79]


    // ---------------------------------------------------------------------------------
    // | PONTO DE ENTRADA DO PROGRAMA (Pág. 4) |
    // ---------------------------------------------------------------------------------

    /**
     * O Método Main é o ponto de partida do seu programa Java.
     * Sem ele, a JVM (Java Virtual Machine) não sabe por onde começar a execução. [cite: 56, 57]
     * A aplicação é compilada em Bytecode para rodar na JVM, garantindo a
     * independência de plataforma. [cite: 33, 34, 41]
     */
    public static void main(String[] args) {
        // Saída de Dados: Imprime o texto no console [cite: 58, 59]
        System.out.println("--- Conceitos Fundamentais de Java ---");
        System.out.println("Java é um ecossistema, robusto e seguro. [cite: 11, 234]");
        System.out.println("+90% das Fortune 500 usam Java. [cite: 13]");
        System.out.println("Foco: Backend, Android, Big Data e Aplicações Corporativas. [cite: 19, 21, 24, 16]");
        System.out.println("Mundo OO em Ação:");

        // Criação de um Objeto (Instância da Classe 'Carro') [cite: 211, 220]
        Carro meuCarro = new Carro();
        meuCarro.modelo = "Sedan Corporativo";
        meuCarro.ligar();

        // Demonstração de Controle de Fluxo
        System.out.println("\n--- Controle de Fluxo (Decisão e Repetição) ---");
        ControladorDeFluxo.tomarDecisoes(7.5);
        ControladorDeFluxo.realizarRepeticoes();
        ControladorDeFluxo.usarSwitchExpression('B');
    }


    // ---------------------------------------------------------------------------------
    // | PROGRAMAÇÃO ORIENTADA A OBJETOS - POO (Pág. 11) |
    // ---------------------------------------------------------------------------------

    /**
     * Classe: A "planta" ou modelo básico para criar objetos. [cite: 209, 54]
     */
    static class Carro { // Usamos 'static' só para simplificar o exemplo no main
        // Atributos (Dados/Características) [cite: 215]
        String modelo;
        int ano;

        /**
         * Método (Comportamento) [cite: 216]
         */
        void ligar() {
            System.out.println("O " + modelo + " está ligando!"); // Exemplo de uso de atributo [cite: 219]
        }
    }


    // ---------------------------------------------------------------------------------
    // | OPERADORES E CONTROLE DE FLUXO (Pág. 7, 8, 9, 10) |
    // ---------------------------------------------------------------------------------

    /**
     * Classe utilitária para demonstrar Operadores e Estruturas de Controle.
     */
    static class ControladorDeFluxo {

        static void tomarDecisoes(double nota) {
            // Operadores Relacionais (>=) e Lógicos (!, &&) [cite: 144, 137, 131]
            boolean aprovado = nota >= 7.0;

            // Estrutura if/else (Tomada de Decisão) [cite: 160]
            if (aprovado) {
                System.out.println("Nota " + nota + ": Aprovado!"); // [cite: 163]
            } else if (nota >= 5.0) { // Utiliza Operador Relacional [cite: 164]
                System.out.println("Nota " + nota + ": Recuperação"); // [cite: 165]
            } else {
                System.out.println("Nota " + nota + ": Reprovado"); // [cite: 168]
            }
        }

        static void realizarRepeticoes() {
            System.out.println(">> Loop For:");
            // Loop for (Repetição) [cite: 170]
            for (int i = 0; i < 2; i++) {
                System.out.println("Iteração: " + i); // [cite: 172]
            }
            // Loop while (Outra forma de repetição) [cite: 174]
            // ... (O código do 'while' foi omitido para concisão)
        }
        
        static void usarSwitchExpression(char nota) {
            // Switch Expression (Java Moderno) - Mais conciso, não precisa de 'break', e retorna valor [cite: 194, 201, 202, 204]
            String feedback = switch (nota) {
                case 'A' -> "Excelente!";
                case 'B' -> "Bom"; // [cite: 197]
                default -> "Pode melhorar"; // [cite: 198]
            };
            System.out.println(">> Switch Expression ('" + nota + "'): " + feedback); // [cite: 199]
        }
    }
}