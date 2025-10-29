
import random

def inspecionar_lote():
    """
    Inspeciona um lote, contando peças boas e parando após 5 falhas seguidas.
    """
    LIMITE_DEFEITOS = 5
    peças_boas = 0
    defeitos_seguidos = 0
    total_inspecionado = 0

    print("--- 🔬 Inspeção de Lote (Parada após 5 falhas seguidas) ---")

    while defeitos_seguidos < LIMITE_DEFEITOS:
        total_inspecionado += 1
        
        status_peca = random.choices([1, 0], weights=[0.6, 0.4], k=1)[0]
        
        if status_peca == 1:
            peças_boas += 1
            defeitos_seguidos = 0  
            print(f"| Peça {total_inspecionado}: OK. ✅")
            
        else:
            
            defeitos_seguidos += 1
            print(f"| Peça {total_inspecionado}: FALHA! ({defeitos_seguidos}/{LIMITE_DEFEITOS} falhas seguidas) ❌")

    
    print("\n==============================================")
    print("        LOTE INTERROMPIDO POR FALHAS          ")
    print("==============================================")
    print(f"Total de Peças Inspecionadas: {total_inspecionado}")
    print(f"Total de Peças Boas no Lote: **{peças_boas}**")
    print("==============================================")

if __name__ == "__main__":
    inspecionar_lote()