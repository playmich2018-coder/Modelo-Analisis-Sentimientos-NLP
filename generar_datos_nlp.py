import pandas as pd
import random

# 1. Definir patrones de texto para simular el lenguaje natural
reseñas_positivas = [
    "Excelente producto, muy recomendado.",
    "Me encantó, superó todas mis expectativas.",
    "Muy buena calidad y entrega rápida.",
    "La mejor compra que he hecho, estoy muy feliz.",
    "Todo perfecto, funciona de maravilla."
]

reseñas_neutras = [
    "El producto está bien, cumple su función.",
    "Llegó a tiempo, pero el empaque estaba algo golpeado.",
    "Es normal, nada fuera de lo común.",
    "Por el precio está aceptable, ni bien ni mal.",
    "No está mal, pero los materiales podrían mejorar."
]

reseñas_negativas = [
    "Pésima experiencia, no lo recomiendo para nada.",
    "El producto llegó roto y la atención fue horrible.",
    "Muy mala calidad, se dañó al primer uso.",
    "No sirve, quiero un reembolso de mi dinero ya.",
    "Definitivamente una pérdida de tiempo y plata."
]

# 2. Generar 500 reseñas aleatorias con distribución realista
datos = []
random.seed(42)

for _ in range(500):
    # Simulamos que la mayoría de clientes están satisfechos
    categoria = random.choices(
        ['Positivo', 'Neutro', 'Negativo'], 
        weights=[0.5, 0.3, 0.2]
    )[0]
    
    if categoria == 'Positivo':
        texto = random.choice(reseñas_positivas)
    elif categoria == 'Neutro':
        texto = random.choice(reseñas_neutras)
    else:
        texto = random.choice(reseñas_negativas)
        
    datos.append({'Texto': texto, 'Sentimiento_Real': categoria})

# 3. Exportar el conjunto de datos
df_reseñas = pd.DataFrame(datos)
df_reseñas.to_csv('dataset_resenas.csv', index=False, encoding='utf-8')

print("✅ Éxito: Base de datos 'dataset_resenas.csv' generada con 500 opiniones.")
print("\nMuestra aleatoria de los datos creados:")
print(df_reseñas.sample(5))