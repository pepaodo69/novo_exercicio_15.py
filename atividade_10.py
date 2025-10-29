import random

def verificar_sensor(leitura_sensor: float) -> str:
    """
    Verifica se a leitura do sensor está na faixa operacional normal (1 a 100).
    
    Parâmetros:
      leitura_sensor (float): O valor lido pelo sensor.
      
    Retorna:
      str: O status do sensor ('Sensor OK' ou 'Sensor com problema').
    """
    
    VALOR_MIN = 1
    VALOR_MAX = 100

    # Condição para "Sensor OK" (valor entre 1 e 100, inclusive)
    if VALOR_MIN <= leitura_sensor <= VALOR_MAX:
        return "Sensor OK ✅"
    # Condição para "Sensor com problema" (fora da faixa)
    else:
        return "Sensor com problema ❌"

# --- SIMULAÇÃO DE USO ---
if __name__ == "__main__":
    print("\n--- 📡 Diagnóstico de Sensores IoT ---")
    
    # 1. Simulação de uma leitura normal (entre 1 e 100)
    leitura_a = random.uniform(5.0, 95.0) # Gera um float aleatório na faixa OK
    status_a = verificar_sensor(leitura_a)
    print(f"Leitura A (Normal): {leitura_a:.2f} -> {status_a}")
    
    # 2. Simulação de uma leitura fora da faixa (muito alta)
    leitura_b = random.uniform(100.1, 500.0)
    status_b = verificar_sensor(leitura_b)
    print(f"Leitura B (Alta):   {leitura_b:.2f} -> {status_b}")
    
    # 3. Simulação de uma leitura fora da faixa (muito baixa)
    leitura_c = random.uniform(-50.0, 0.99)
    status_c = verificar_sensor(leitura_c)
    print(f"Leitura C (Baixa):  {leitura_c:.2f} -> {status_c}")
    
    # 4. Exemplo de entrada manual
    leitura_d = 75.0
    status_d = verificar_sensor(leitura_d)
    print(f"Leitura D (Manual): {leitura_d:.2f} -> {status_d}")