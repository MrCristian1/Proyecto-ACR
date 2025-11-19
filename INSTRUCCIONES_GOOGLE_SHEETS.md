# 📝 Configuración de Google Sheets para Consecutivos

## Paso 1: Crear Google Sheet

1. Ve a https://sheets.google.com
2. Crea una nueva hoja de cálculo
3. Nómbrala: **"ACR_Consecutivos"**
4. En la celda **A1** escribe: `consecutivo`
5. En la celda **A2** escribe: `26` (valor inicial)

## Paso 2: Obtener Credenciales de Google Cloud

### 2.1 Crear Proyecto en Google Cloud
1. Ve a https://console.cloud.google.com/
2. Crea un nuevo proyecto o selecciona uno existente
3. Nombre sugerido: "ACR-Manager"

### 2.2 Habilitar APIs necesarias
1. Ve a "APIs & Services" → "Library"
2. Busca y habilita:
   - **Google Sheets API**
   - **Google Drive API**

### 2.3 Crear Service Account
1. Ve a "APIs & Services" → "Credentials"
2. Click en "Create Credentials" → "Service Account"
3. Nombre: `acr-service-account`
4. Rol: `Editor`
5. Click en "Done"

### 2.4 Generar Clave JSON
1. Click en el Service Account creado
2. Ve a la pestaña "Keys"
3. Click "Add Key" → "Create new key"
4. Selecciona **JSON**
5. Se descargará un archivo JSON (ejemplo: `acr-manager-123456-abcdef.json`)

## Paso 3: Compartir Google Sheet con Service Account

1. Abre el archivo JSON descargado
2. Busca el campo `"client_email"` (ejemplo: `acr-service-account@acr-manager.iam.gserviceaccount.com`)
3. Copia ese email
4. Ve a tu Google Sheet "ACR_Consecutivos"
5. Click en "Compartir" (botón verde)
6. Pega el email del service account
7. Dale permisos de **Editor**
8. Click en "Enviar"

## Paso 4: Configurar Variables en Streamlit Cloud

Cuando despliegues en Streamlit Cloud, agrega estos secretos en formato TOML:

```toml
# Secrets de Streamlit Cloud
GEMINI_API_KEY = "TU_API_KEY_DE_GEMINI"
SMTP_USER = "tu_email@gmail.com"
SMTP_PASS = "tu_app_password"
DESTINATARIO = "destinatario@empresa.com"

# Google Sheets - Copia TODO el contenido del archivo JSON
[gcp_service_account]
type = "service_account"
project_id = "acr-manager-123456"
private_key_id = "abc123..."
private_key = "-----BEGIN PRIVATE KEY-----\nTU_CLAVE_PRIVADA_AQUI\n-----END PRIVATE KEY-----\n"
client_email = "acr-service-account@acr-manager.iam.gserviceaccount.com"
client_id = "123456789"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."

GOOGLE_SHEET_NAME = "ACR_Consecutivos"
```

## Paso 5: Para desarrollo local

1. Guarda el archivo JSON descargado en la carpeta del proyecto
2. Nómbralo: `google_credentials.json`
3. Asegúrate de que esté en `.gitignore`
4. Actualiza tu archivo `.env`:

```env
GOOGLE_SHEET_NAME=ACR_Consecutivos
GOOGLE_APPLICATION_CREDENTIALS=google_credentials.json
```

## ✅ Verificación

Una vez configurado, la app:
- Leerá el consecutivo desde Google Sheets
- Lo incrementará automáticamente después de cada generación
- Todos los usuarios verán el mismo consecutivo actualizado
- El historial quedará registrado en la hoja

## 🔒 Seguridad

- ⚠️ **NUNCA** subas `google_credentials.json` a GitHub
- Asegúrate de que esté en `.gitignore`
- En producción, usa solo los Secrets de Streamlit Cloud
