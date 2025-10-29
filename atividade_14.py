def classificar_produto_final(peso: float, num_defeitos: int) -> str:
    """
    Classifica um produto final com base no peso e no número de defeitos.

    Regras:
      - Premium: peso ideal (9.8-10.2) E sem defeitos.
      - Rejeitado: >= 3 defeitos OU peso fora da faixa aceitável (< 9.0 ou > 11.0).
      - Standard: O que sobrou (pequenas variações aceitáveis).

    Parâmetros:
      peso (float): O peso da peça.
      num_defeitos (int): O número de defeitos.

    Retorna:
      str: A classificação ('Premium', 'Standard' ou 'Rejeitado').
    """
    
    PESO_IDEAL_MIN = 9.8
    PESO_IDEAL_MAX = 10.2

    # 1. Condição para REJEITADO (Mais crítica)
    if num_defeitos >= 3 or peso < 9.0 or peso > 11.0:
        return "**Rejeitado ❌** (Fora dos padrões estritos de qualidade ou peso.)"
    
    # 2. Condição para PREMIUM
    elif PESO_IDEAL_MIN <= peso <= PESO_IDEAL_MAX and num_defeitos == 0:
        return "**Premium ✨** (Peso ideal e sem defeitos.)"
        
    # 3. Condição para STANDARD (O que sobrou, com 0, 1 ou 2 defeitos e peso aceitável)
    else:
        return "**Standard ⭐** (Pequenas variações aceitáveis.)"

def rodar_classificacao_interativa():
    """
    Função interativa que solicita os dados do produto ao usuário e exibe a classificação.
    """
    print("--- 🌟 Sistema Interativo de Classificação de Produtos Finais ---")
    
    while True:
        try:
            # 1. Entrada de Peso
            entrada_peso = input("\nDigite o peso do produto (em kg) ou 'sair': ").strip().lower()
            if entrada_peso == 'sair':
                print("Sistema de classificação encerrado.")
                break
            
            peso = float(entrada_peso)

            # 2. Entrada de Defeitos
            entrada_defeitos = input("Digite o número de defeitos encontrados: ").strip()
            num_defeitos = int(entrada_defeitos)
            
            if num_defeitos < 0 or peso < 0:
                print("⚠️ Valores de peso e defeitos devem ser não-negativos.")
                continue

            # 3. Classifica e exibe o resultado
            classificacao = classificar_produto_final(peso, num_defeitos)
            
            print(f"\n[ RESULTADO DA INSPEÇÃO ]")
            print(f"Peso: {peso:.2f} kg | Defeitos: {num_defeitos}")
            print(f"Classificação Final: {classificacao}")
            
        except ValueError:
            print("\n❌ Entrada inválida. Certifique-se de digitar números válidos para peso e defeitos.")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")


# --- Execução do Código ---
if __name__ == "__main__":
    # Opção A: Rodar o sistema interativo
    rodar_classificacao_interativa()

    # Opção B: Testes Rápidos (como no seu código original - descomente para testar)
    # print("\n--- Testes Rápidos da Função Original ---")
    # print(classificar_produto_final(peso=10.05, num_defeitos=0))
    # print(classificar_produto_final(peso=10.5, num_defeitos=1))
    # print(classificar_produto_final(peso=12.0, num_defeitos=0))
    # print(classificar_produto_final(peso=9.9, num_defeitos=3))