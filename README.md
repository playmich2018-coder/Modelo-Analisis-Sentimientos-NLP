# 📝 Modelo de Análisis de Sentimientos (NLP)

## 📖 ¿Para qué sirve y por qué utilizarlo?
El análisis de sentimientos mediante Procesamiento de Lenguaje Natural (NLP) permite a las computadoras "leer" e interpretar texto humano no estructurado. 

En un entorno de inteligencia de negocios, su implementación es fundamental para:
1. **Medición de Satisfacción a Escala:** Permite procesar miles de reseñas, correos o comentarios en redes sociales en segundos, sin intervención humana.
2. **Detección de Crisis:** Ayuda a identificar picos de inconformidad en tiempo real, permitiendo a las áreas de servicio al cliente reaccionar de forma proactiva.
3. **Análisis Cualitativo Cuantificado:** Transforma opiniones subjetivas (texto) en métricas duras (porcentajes de aprobación) para su integración en dashboards gerenciales.

## 🎯 Objetivo del Proyecto
Entrenar un modelo de Machine Learning capaz de analizar comentarios de usuarios y clasificarlos automáticamente en tres categorías de satisfacción: Positivo, Neutro y Negativo.

## 🛠 Metodología y Tecnologías
Se construyó un pipeline de NLP para transformar lenguaje humano en matrices matemáticas operables.
* **Vectorización:** TF-IDF (Term Frequency-Inverse Document Frequency) para asignar pesos relativos a las palabras según su importancia.
* **Modelo Analítico:** Clasificador Naive Bayes (MultinomialNB), ideal para cálculo de probabilidades probabilísticas en texto.
* **Librerías:** Pandas, Scikit-Learn.

## 🧠 Resultados y Aplicación de Negocio
El algoritmo demostró capacidad para interpretar contextos mixtos. En pruebas en vivo, logró diagnosticar correctamente opiniones donde existían elementos positivos ("el envío fue rápido") pero que concluían en un estado de insatisfacción ("producto roto"), categorizándolo exitosamente como 'Negativo'. 

Este desarrollo está listo para ser acoplado a flujos de web scraping o bases de datos de encuestas NPS para automatizar el monitoreo de la experiencia del cliente.