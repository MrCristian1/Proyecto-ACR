# Aplicativo Interactivo - Acciones de Mejora (ACR)

Una aplicación web desarrollada con Streamlit para automatizar el proceso de Análisis de Causa Raíz (ACR) utilizando la metodología de los 5 porqués con integración de IA.

## 🚀 Características

- **Formulario interactivo**: Captura toda la información necesaria para un ACR
- **Análisis automático con IA**: Genera los 5 porqués usando la API de Gemini
- **Generación de Excel**: Crea archivos Excel descargables con los datos del ACR
- **Gestión de archivos**: Permite cargar ACR existentes y transferirlos a un Excel maestro
- **Interfaz intuitiva**: Desarrollado con Streamlit para una experiencia de usuario fluida

## 📋 Requisitos

- Python 3.8 o superior
- API Key de Google Gemini

## 🛠️ Instalación

1. Clona o descarga este proyecto
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura tu API Key de Gemini:
   - Crea un archivo `.env` en la raíz del proyecto
   - Agrega tu API Key: `GEMINI_API_KEY=tu_api_key_aqui`

## 🚀 Uso

1. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```
2. Abre tu navegador en `http://localhost:8501`
3. Selecciona entre crear una nueva ACR o cargar archivos existentes

## 📊 Funcionalidades

### Crear Nueva ACR
- Completa el formulario con los detalles del problema
- Usa la IA para generar automáticamente los 5 porqués
- Descarga el archivo Excel con toda la información

### Cargar ACR Existente
- Sube un archivo Excel de ACR
- Sube el Excel maestro con el historial
- Transfiere automáticamente los datos al historial

## 🔧 Configuración

### Variables de Entorno
Crea un archivo `.env` con las siguientes variables:
```
GEMINI_API_KEY=tu_api_key_de_gemini
```

## 📁 Estructura del Proyecto

```
aplicativo-acr/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
├── .env               # Variables de entorno (crear)
└── README.md          # Este archivo
```

## 🤝 Contribuciones

Este proyecto está en desarrollo activo. Las sugerencias y mejoras son bienvenidas.

## 📄 Licencia

Proyecto interno de la empresa.