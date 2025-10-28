def monitorar_temperatura():
    """
    Recebe a temperatura atual e exibe o status (Crítico, Elevado ou Normal).
    """
    print("--- Sistema de Monitoramento de Refrigeração ---")

    try:
        temperatura_str = input("Digite a temperatura atual em °C: ")
        temperatura = float(temperatura_str)

        if temperatura > 80:
            print("\n🚨 ALERTA CRÍTICO! 🚨")
            print(f"Temperatura de {temperatura}°C é **ACIMA DO LIMITE CRÍTICO (80°C)**.")
            print("Ação sugerida: VERIFICAR imediatamente o sistema de refrigeração.")

        elif temperatura >= 60 and temperatura <= 80:
            print("\n⚠️ AVISO: TEMPERATURA ELEVADA! ⚠️")
            print(f"Temperatura de {temperatura}°C está entre 60°C e 80°C.")
            print("Ação sugerida: Monitorar a tendência e ajustar a capacidade de refrigeração.")

        elif temperatura < 60:
            print("\n✅ STATUS NORMAL ✅")
            print(f"Temperatura de {temperatura}°C está abaixo de 60°C.")
            print("Ação sugerida: Não requer ação imediata; sistema operando em faixa segura.")
            
        
    except ValueError:
        print("\n❌ ERRO DE ENTRADA ❌")
        print("Por favor, digite um valor numérico válido para a temperatura.")

monitorar_temperatura()