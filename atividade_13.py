# EXERCÍCIO 13: CONTROLE DE VELOCIDADE (Código com Escolha/Interativo)

def ajustar_velocidade(tipo_produto: str) -> str:
    """
    Ajusta a velocidade da esteira com base no tipo de produto.
    
    Regras:
      A: Velocidade 1 (Lenta)
      B: Velocidade 2 (Média)
      C: Velocidade 3 (Rápida)
    """
    
    tipo_produto = tipo_produto.strip().upper() # Padroniza para A, B ou C

    if tipo_produto == 'A':
        velocidade = "Velocidade 1 (Lenta)"
    elif tipo_produto == 'B':
        velocidade = "Velocidade 2 (Média)"
    elif tipo_produto == 'C':
        velocidade = "Velocidade 3 (Rápida)"
    else:
        velocidade = "ERRO: Tipo de Produto Não Identificado."
        
    return f"Ajuste da Esteira: **{velocidade}**"

def rodar_controle_velocidade():
    """
    Função interativa que solicita o tipo de produto ao usuário e exibe o ajuste.
    """
    print("--- ⏱️ Controle de Velocidade da Esteira ---")
    
    while True:
        # Solicita a entrada do usuário
        entrada = input("\nDigite o TIPO DE PRODUTO (A, B, C) ou 'sair' para encerrar: ").strip().lower()
        
        if entrada == 'sair':
            print("Programa de controle de velocidade encerrado.")
            break
            
        if len(entrada) == 1 and entrada.upper() in ['A', 'B', 'C']:
            # Tipo de produto válido
            ajuste = ajustar_velocidade(entrada)
            print(f"\n[ RESULTADO DO AJUSTE PARA PRODUTO {entrada.upper()} ]")
            print(ajuste)
            
        else:
            # Entrada inválida (que não seja A, B, C ou 'sair')
            print("\n❌ Entrada inválida. Por favor, digite apenas 'A', 'B' ou 'C'.")


# --- Execução do Código ---
if __name__ == "__main__":
    # Opção A: Rodar o sistema interativo
    rodar_controle_velocidade()

    # Opção B: Testes Rápidos (como no seu código original - descomente para testar)
    # print("\n--- Testes Rápidos da Função Original ---")
    # print(ajustar_velocidade('A'))
    # print(ajustar_velocidade('b'))
    # print(ajustar_velocidade('C'))
    # print(ajustar_velocidade('D'))