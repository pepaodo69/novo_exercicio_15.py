def verificar_estoque(nome_produto: str, estoque_atual: int, limite_minimo: int = 50):
    """
    Monitora o estoque de um produto, emite alerta se estiver abaixo do limite
    e sugere um pedido de reposição.
    """
    
    print("\n--- 📦 Gerenciamento de Estoque de Matéria-Prima ---")
    print(f"Produto Monitorado: {nome_produto}")
    print(f"Estoque Atual: {estoque_atual} unidades")
    print(f"Limite Mínimo para Alerta: {limite_minimo} unidades")
    print("--------------------------------------------------")

    if estoque_atual < limite_minimo:
        unidades_faltantes = limite_minimo - estoque_atual
        
        # Sugestão de pedido: Cobrir o que falta + uma margem de segurança de 100 unidades
        pedido_sugerido = unidades_faltantes + 100
        
        print("🚨 **ALERTA: ESTOQUE BAIXO!**")
        print(f"O estoque está abaixo do limite em {unidades_faltantes} unidades.")
        print(f"📢 Sugestão de Reposição: Pedir **{pedido_sugerido} unidades** de {nome_produto} imediatamente.")
        
    else:
        print("✅ **Estoque em Nível OK.** Não é necessário reposição imediata.")

def rodar_sistema_estoque():
    """
    Função para rodar o sistema de estoque interativamente.
    """
    NOME_DO_PRODUTO = "Peça de Montagem XPTO"
    LIMITE = 50
    
    print("\n##### Sistema Interativo de Verificação de Estoque #####")
    print(f"Produto padrão: {NOME_DO_PRODUTO}. Alerta: {LIMITE} unidades.")

    while True:
        try:
            entrada = input("\nDigite o estoque atual do produto (ou 'sair'): ").strip().lower()

            if entrada == 'sair':
                print("Sistema encerrado.")
                break

            estoque = int(entrada)
            
            if estoque < 0:
                print("⚠️ O estoque não pode ser negativo. Tente novamente.")
                continue

            # Chama a função principal com a entrada do usuário
            verificar_estoque(NOME_DO_PRODUTO, estoque, LIMITE)

        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número inteiro de unidades.")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")


# Execução do código
if __name__ == "__main__":
    # Opção A: Rodar testes diretos (como no seu código original)
    print("--- Testes Rápidos da Função Original ---")
    verificar_estoque(nome_produto="Parafuso M8", estoque_atual=35)
    verificar_estoque(nome_produto="Chapa de Aço 3mm", estoque_atual=75)
    verificar_estoque(nome_produto="Fio de Cobre", estoque_atual=50) 
    
    # Opção B: Rodar o sistema interativo (descomente para usar)
    # rodar_sistema_estoque()
