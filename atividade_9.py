NUM_MAQUINAS = 5
consumo_total_fabrica = 0.0

print("\n--- 💡 Cálculo de Consumo Energético da Fábrica ---")

for i in range(1, NUM_MAQUINAS + 1):
    while True:
        try:
            entrada = input(f"Máquina {i}/{NUM_MAQUINAS}: Digite o consumo em kWh: ").strip()
            consumo_maquina = float(entrada)
            
            if consumo_maquina < 0:
                print("⚠️ O consumo deve ser um valor não-negativo.")
                continue

            consumo_total_fabrica += consumo_maquina
            break
            
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número (ex: 150.5).")


print("\n==============================================")
print("             RELATÓRIO DE CONSUMO             ")
print("==============================================")
print(f"Máquinas monitoradas: {NUM_MAQUINAS}")
print(f"Consumo Total da Fábrica: **{consumo_total_fabrica:.2f} kWh**")
print("==============================================")