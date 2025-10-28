import time 
def simular_manutencao(limite_horas: int = 500, incremento_horas: int = 10):
    """
    Simula o tempo de operação de uma máquina até o limite de manutenção.
    """
    
    horas_operadas = 0       
    print("--- 🔔 Alerta de Manutenção Preventiva ---")
    print(f"Máquina programada para manutenção a cada {limite_horas} horas.")
    print(f"Simulando em incrementos de {incremento_horas} horas.")
    print("--------------------------------------------------")

    while horas_operadas < limite_horas:
        
        if horas_operadas + incremento_horas >= limite_horas:
            horas_operadas = limite_horas
        else:
            horas_operadas += incremento_horas

        print(f"| Horas operadas: {horas_operadas}h")
        
        time.sleep(0.1) 
        
        if horas_operadas >= limite_horas:
            print("\n==============================================")
            print(f"🚨 ALERTA DE MANUTENÇÃO! ({limite_horas} HORAS ATINGIDAS) 🚨")
            print("A simulação de operação foi PARADA.")
            print("==============================================")
            break 

if __name__ == "__main__":
    simular_manutencao(limite_horas=500, incremento_horas=10)