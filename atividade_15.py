# EXERCÍCIO 15: DASHBOARD DE PRODUÇÃO (Código Interativo)

def coletar_producao(num_linhas: int = 5):
    """
    Coleta a produção de cada linha, calcula o total e identifica a linha com maior produção.
    """
    
    producao_linhas = []
    producao_total = 0
    maior_producao = -1  # Usado para armazenar o valor máximo
    linha_maxima = 0     # Usado para armazenar o índice da linha com maior produção

    print("--- 📈 Dashboard de Produção da Fábrica (Entrada Manual) ---")
    print(f"Coletando dados de {num_linhas} linhas de produção.")
    print("----------------------------------------------------------")

    # 1. Coleta da produção (Usando FOR para iterar sobre as linhas)
    for i in range(1, num_linhas + 1):
        while True:
            try:
                # Solicita a produção da linha atual
                entrada = input(f"Linha {i}: Digite a produção de peças: ").strip()
                producao = int(entrada)
                
                if producao < 0:
                    print("⚠️ A produção não pode ser negativa. Tente novamente.")
                    continue
                
                producao_linhas.append(producao)
                break
                
            except ValueError:
                print("❌ Entrada inválida. Por favor, digite um número inteiro.")

    # 2. Processamento e Cálculo
    print("\n[ PROCESSANDO DADOS... ]")
    
    for i, prod in enumerate(producao_linhas, start=1):
        # Soma a produção total
        producao_total += prod
        
        # Identifica a linha com maior produção
        if prod > maior_producao:
            maior_producao = prod
            linha_maxima = i

    # 3. Exibição do Dashboard
    print("\n--- 📊 RELATÓRIO FINAL ---")
    for i, prod in enumerate(producao_linhas, start=1):
        print(f"| Linha {i}: {prod} peças")
        
    print("\n==============================================")
    print(f"Produção Total da Fábrica: **{producao_total} peças**")
    print(f"Linha de Melhor Performance: Linha **{linha_maxima}** com {maior_producao} peças.")
    print("==============================================")


# Inicia o dashboard interativo
if __name__ == "__main__":
    coletar_producao(num_linhas=5)