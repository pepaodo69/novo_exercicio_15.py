def classificar_peca(peso):
    try:
        p = float(peso)
    except ValueError:
        return "Erro: Entrada inválida. Por favor, insira um valor numérico para o peso (em kg)."
    
    if p <= 0.5:
        return f"Peso: {p}kg - CLASSIFICAÇÃO: Leve"
    elif p<= 2.0:
        return f"Peso {p}kg - CLASSIFICAÇÃO: Média"
    elif p <= 5.0:
        return f"Peso {p}kg - CLASSIFICAÇÃO: Pesada"

    else:
        return f"Peso {p}kg - CLASSIFICAÇÃO: Muito pesada"
    
entrada = input("Insira o peso da peça em kg: ")
resultado = classificar_peca(entrada)
print(resultado)