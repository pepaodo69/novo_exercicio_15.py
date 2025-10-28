META_DIARIA = 1000 

def verificar_producao():
    """
    Recebe a quantidade produzida, compara com a meta e informa o status.
    """
    print("--- Sistema de Controle de Produção Diária ---")
    print(f"** Meta Diária a ser atingida: {META_DIARIA} unidades **")

    try:
        producao_str = input("Digite a quantidade de unidades produzidas hoje: ")
        producao = int(producao_str) 
        if producao < 0:
            print("\n❌ ERRO: A produção não pode ser um número negativo.")
            return

        
        if producao >= META_DIARIA:
            unidades_a_mais = producao - META_DIARIA
            print("\n✅ META ATINGIDA! ✅")
            
            if unidades_a_mais > 0:
                print(f"Parabéns! Você produziu **{producao} unidades**, superando a meta em **{unidades_a_mais} unidades**.")
            else:
                 print(f"Meta atingida com **{producao} unidades** produzidas.")

        else:
            unidades_faltantes = META_DIARIA - producao
            print("\n⚠️ META NÃO ATINGIDA! ⚠️")
            print(f"Você produziu **{producao} unidades**.")
            print(f"Faltaram **{unidades_faltantes} unidades** para atingir a meta diária de {META_DIARIA}.")

    except ValueError:
        print("\n❌ ERRO DE ENTRADA ❌")
        print("Por favor, digite um valor numérico inteiro válido para a produção.")

verificar_producao()