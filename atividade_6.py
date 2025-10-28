def simular_turno_producao(duracao_turno_horas: int = 8):
    """
    Simula um turno de produção, somando a produção de cada hora.

    Parâmetros:
      duracao_turno_horas (int): A duração total do turno em horas (padrão é 8).
    """
    
    producao_total = 0
    
    print("--- 🏭 Contador de Produção por Turno (8 Horas) 🏭 ---")
    print(f"O turno terá duração de {duracao_turno_horas} horas.")
    print("-------------------------------------------------------")

    
    for hora in range(1, duracao_turno_horas + 1):
        while True:
            try:
                
                entrada = input(f"▶️ Digite a produção da HORA {hora} (peças): ").strip()

                producao_hora = int(entrada)

                if producao_hora < 0:
                    print("⚠️ A produção não pode ser um valor negativo. Tente novamente.")
                    continue

                producao_total += producao_hora
                
                break
                
            except ValueError:
                print("❌ Entrada inválida. Por favor, digite um número inteiro.")
            except Exception as e:
                 print(f"❌ Erro inesperado: {e}")


    print("\n=======================================================")
    print("                 ✅ RESUMO DO TURNO ✅                ")
    print("=======================================================")
    print(f"| Horas trabalhadas: {duracao_turno_horas}")
    print(f"| Produção Total do Turno: **{producao_total} peças**")
    print("=======================================================")


if __name__ == "__main__":
    simular_turno_producao(duracao_turno_horas=8)