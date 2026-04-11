# Data Pulse Pipeline 🚀

### Descripción
Este es un proyecto de **Data Engineering** que implementa un pipeline ETL (Extract, Transform, Load) modular. El objetivo es capturar datos de una API pública, procesarlos mediante reglas de negocio y almacenarlos en una base de datos relacional para su posterior análisis.

### 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Librerías de Datos:** Pandas (Transformación), SQLAlchemy (ORM).
* **Base de Datos:** SQLite (Persistencia local).
* **Entorno:** Docker (Opcional) / Venv.

### 🏗️ Arquitectura del Proyecto
El sistema se divide en tres capas principales para asegurar la escalabilidad:
1. **Extraction:** Consumo de datos crudos desde API REST.
2. **Transformation:** Limpieza, tipado y manejo de nulos con Pandas.
3. **Loading:** Persistencia en base de datos mediante SQLAlchemy.

---
