import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os

# Verificar si existe el archivo
if not os.path.exists('dataset_resenas.csv'):
    print("⚠️ Faltan los datos. Ejecuta primero: python generar_datos_nlp.py")
else:
    # 1. Cargar el histórico de reseñas
    df = pd.read_csv('dataset_resenas.csv')

    # 2. Separar el texto (X) y la categoría real (y)
    X = df['Texto']
    y = df['Sentimiento_Real']

    # 3. Dividir los datos: 80% para que la IA estudie, 20% para examinarla
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Magia NLP: Transformar palabras en matrices matemáticas (TF-IDF)
    vectorizador = TfidfVectorizer()
    X_train_vect = vectorizador.fit_transform(X_train)
    X_test_vect = vectorizador.transform(X_test)

    # 5. Entrenar el modelo clasificador (Naive Bayes)
    print("🧠 Entrenando el motor de Procesamiento de Lenguaje Natural...")
    modelo = MultinomialNB()
    modelo.fit(X_train_vect, y_train)

    # 6. Evaluar qué tan inteligente se volvió el modelo
    predicciones = modelo.predict(X_test_vect)
    precision = accuracy_score(y_test, predicciones)
    print(f"📊 Nivel de precisión del algoritmo: {precision * 100:.1f}%\n")

    # 7. Prueba de fuego: Clasificar opiniones completamente nuevas
    print("🔮 PRUEBA EN VIVO: CLASIFICANDO NUEVOS COMENTARIOS 🔮")
    print("-" * 65)
    
    nuevas_resenas = [
        "El envío fue rápido, pero el producto llegó totalmente roto.",
        "¡Me fascina! Lo volvería a comprar mil veces más, recomendado.",
        "Es un artículo promedio, hace su trabajo sin destacar."
    ]

    # Convertimos los nuevos textos a números y predecimos
    nuevas_resenas_vect = vectorizador.transform(nuevas_resenas)
    predicciones_nuevas = modelo.predict(nuevas_resenas_vect)

    for texto, sentimiento in zip(nuevas_resenas, predicciones_nuevas):
        print(f"📝 Cliente: '{texto}'")
        print(f"   -> Diagnóstico IA: {sentimiento}\n")
    print("-" * 65)