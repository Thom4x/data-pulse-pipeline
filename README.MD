# Cripto Data Pipeline 🚀

### Descripción
Este es un proyecto de **Data Engineering** que implementa un pipeline ETL (Extract, Transform, Load) modular. El objetivo es capturar datos de una API pública, procesarlos mediante reglas de negocio y almacenarlos en una base de datos relacional para su posterior análisis.

### 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Librerías de Datos:** Pandas (Transformación), SQLAlchemy (ORM).
* **Base de Datos:** SQLite (Persistencia local).
* **Entorno:** Docker (Opcional) / Venv.

## 📋 Estructura del Proyecto
* `src/extract.py`: Consumo de API con manejo de headers y seguridad.
* `src/transform.py`: Limpieza, tipado de datos (datetime) y normalización con Pandas.
* `src/load.py`: Carga eficiente en base de datos relacional.
* `main.py`: Orquestador del flujo completo.

## 🚀 Cómo ejecutar
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python main.py`
---
