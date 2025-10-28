def inspecionar_peca(numero_defeitos: int) -> str:
    """
    Inspeciona uma peça com base no número de defeitos encontrados.

    Regras:
      - Aprovada: 0, 1 ou 2 defeitos (até 2)
      - Reprovada: Mais de 2 defeitos

    Parâmetros:
      numero_defeitos (int): O total de defeitos na peça.

    Retorna:
      str: O status de aprovação da peça ('APROVADA' ou 'REPROVADA').
    """

    if numero_defeitos < 0:
        return "ERRO: O número de defeitos não pode ser negativo."

    if numero_defeitos <= 2:
        return "APROVADA"
    else:
        return "REPROVADA"

def rodar_inspecao():
    """
    Função principal que interage com o usuário para inspecionar peças.
    """
    print("--- Sistema de Inspeção Automática de Qualidade ---")

    while True:
        try:
            entrada = input("Digite o número de defeitos encontrados (ex: 3) ou 'sair' para encerrar: ").strip().lower()

            if entrada == 'sair':
                print("Programa de inspeção encerrado. Qualidade garantida!")
                break

            num_defeitos = int(entrada)

            status_final = inspecionar_peca(num_defeitos)

            print(f"\n[ RESULTADO DA INSPEÇÃO ]")
            print(f"Defeitos encontrados: {num_defeitos}")

            if status_final == "APROVADA":
                print(f"Status Final: **PEÇA APROVADA** ✅\n")
            elif status_final == "REPROVADA":
                 print(f"Status Final: **PEÇA REPROVADA** ❌\n")
            else:
                 print(f"Status Final: {status_final}\n")
        except ValueError:
            print("\n[ ERRO DE ENTRADA ] Por favor, digite um número inteiro não-negativo de defeitos ou 'sair'.\n")

if __name__ == "__main__":
    rodar_inspecao()

