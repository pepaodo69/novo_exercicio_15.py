def identificar_turno(hora_atual: int) -> str:
    """
    Identifica o turno de operação com base na hora atual (formato 24h).

    Regras:
      - Manhã: 6h a 12h (6 <= hora < 12)
      - Tarde: 12h a 18h (12 <= hora < 18)
      - Noite: 18h a 6h (18 <= hora < 24 OU 0 <= hora < 6)

    Parâmetros:
      hora_atual (int): A hora no formato 24 horas (0 a 23).

    Retorna:
      str: O turno ('Manhã', 'Tarde', 'Noite') ou uma mensagem de erro.
    """

    if not 0 <= hora_atual <= 23:
        return "ERRO: Hora inválida. Use um valor inteiro entre 0 e 23."

   
    if 6 <= hora_atual < 12:
        return "Manhã"
    
    elif 12 <= hora_atual < 18:
        return "Tarde"
        
    
    else:
        
        return "Noite"

def rodar_identificacao():
    """
    Função principal que interage com o usuário para identificar o turno.
    """
    print("--- Sistema de Identificação de Turnos ---")

    while True:
        try:
            entrada = input("Digite a hora atual (0 a 23) ou 'sair' para encerrar: ").strip().lower()

            if entrada == 'sair':
                print("Programa de turnos encerrado.")
                break

            hora = int(entrada)

            turno_final = identificar_turno(hora)

            print(f"\n[ RESULTADO ]")
            print(f"Hora Informada: {hora:02}h")
            print(f"O turno atual é: **{turno_final}**\n")

        except ValueError:
            print("\n[ ERRO DE ENTRADA ] Por favor, digite um número inteiro de 0 a 23 ou 'sair'.\n")
        except Exception as e:
            print(f"\n[ ERRO INESPERADO ] Ocorreu um problema: {e}\n")

if __name__ == "__main__":
    rodar_identificacao()

