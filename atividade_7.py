def calcular_eficiencia(producao_real: float, producao_esperada: float) -> tuple[float, str]:
    """
    Calcula a eficiência percentual (real/esperada * 100) e classifica a performance.

    Regras de Classificação:
      - Excelente: >= 90%
      - Boa: 70% a 89%
      - Precisa melhorar: < 70%

    Parâmetros:
      producao_real (float): A produção efetivamente alcançada.
      producao_esperada (float): A meta de produção.

    Retorna:
      tuple[float, str]: Uma tupla contendo a eficiência percentual e a classificação.
    """

    if producao_esperada <= 0:
        return 0.0, "ERRO: A produção esperada deve ser maior que zero para o cálculo."
    
    if producao_real < 0:
        return 0.0, "ERRO: A produção real não pode ser negativa."

    
    eficiencia_percentual = (producao_real / producao_esperada) * 100

    if eficiencia_percentual >= 90.0:
        classificacao = "Excelente"
    elif eficiencia_percentual >= 70.0:
        classificacao = "Boa"
    else:
        classificacao = "Precisa melhorar"
        
    return eficiencia_percentual, classificacao

def rodar_calculo_eficiencia():
    """
    Função principal que interage com o usuário para obter dados e calcular a eficiência.
    """
    print("--- 📊 Sistema de Cálculo de Eficiência de Máquinas ---")

    while True:
        try:
            entrada_real = input("Digite a produção real alcançada (ou 'sair'): ").strip().lower()
            if entrada_real == 'sair':
                print("Programa de eficiência encerrado.")
                break
            producao_real = float(entrada_real)
            
            entrada_esperada = input("Digite a produção esperada (meta): ").strip()
            producao_esperada = float(entrada_esperada)

            eficiencia, classificacao = calcular_eficiencia(producao_real, producao_esperada)

            print("\n[ RESULTADO DA PERFORMANCE ]")
            print(f"Produção Real: {producao_real}")
            print(f"Produção Esperada: {producao_esperada}")
            
            if "ERRO" in classificacao:
                print(f"Status: **{classificacao}**")
            else:
                print(f"Eficiência Calculada: **{eficiencia:.2f}%**")
                print(f"Classificação: **{classificacao}**")
            
            print("-" * 35 + "\n")

        except ValueError:
            print("\n[ ERRO DE ENTRADA ] Por favor, digite valores numéricos válidos.\n")
        except Exception as e:
            print(f"\n[ ERRO INESPERADO ] Ocorreu um problema: {e}\n")

if __name__ == "__main__":
    rodar_calculo_eficiencia()