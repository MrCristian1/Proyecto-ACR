# Guía de Instalación en Servidor Propio

## 📋 Requisitos Previos

- Python 3.11 o superior
- Git
- Acceso al servidor vía SSH
- Credenciales de API (Gemini, Gmail, Google Sheets)

## 🚀 Pasos de Instalación

### 1. Clonar el Repositorio

```bash
cd /home/acr
git clone https://github.com/MrCristian1/Proyecto-ACR.git streamlit-app
cd streamlit-app
```

### 2. Crear Entorno Virtual

```bash
python3 -m venv env
source env/bin/activate  # En Linux/Mac
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Secrets

Crear el directorio `.streamlit` si no existe:

```bash
mkdir -p .streamlit
```

Crear el archivo `secrets.toml`:

```bash
nano .streamlit/secrets.toml
```

Copiar el contenido del archivo `.streamlit/secrets.toml.example` y reemplazar con tus credenciales reales.

**Estructura del archivo:**

```toml
[general]
GEMINI_API_KEY = "tu_api_key_aqui"
SMTP_USER = "tu_email@gmail.com"
SMTP_PASS = "tu_app_password"
DESTINATARIO = "destinatario@solutionsandpayroll.com"
GOOGLE_SHEET_NAME = "ACR_Consecutivos"

[gcp_service_account]
type = "service_account"
project_id = "acr-manager"
private_key_id = "tu_private_key_id"
private_key = "-----BEGIN PRIVATE KEY-----\ntu_clave_privada\n-----END PRIVATE KEY-----\n"
client_email = "tu-service-account@tu-project.iam.gserviceaccount.com"
client_id = "tu_client_id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/tu-service-account%40tu-project.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

### 5. Alternativa: Configuración Global

Si prefieres configurar los secrets a nivel de usuario (no de proyecto):

```bash
mkdir -p ~/.streamlit
nano ~/.streamlit/secrets.toml
```

Copiar el mismo contenido anterior.

### 6. Verificar Permisos

```bash
chmod 600 .streamlit/secrets.toml  # Solo lectura/escritura para el propietario
```

### 7. Ejecutar la Aplicación

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Para ejecutar en modo producción con systemd:

```bash
sudo nano /etc/systemd/system/acr-app.service
```

Contenido del archivo:

```ini
[Unit]
Description=ACR Streamlit Application
After=network.target

[Service]
Type=simple
User=acr
WorkingDirectory=/home/acr/streamlit-app
Environment="PATH=/home/acr/streamlit-app/env/bin"
ExecStart=/home/acr/streamlit-app/env/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

Habilitar y arrancar el servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable acr-app
sudo systemctl start acr-app
sudo systemctl status acr-app
```

## 🔍 Verificación

### Comprobar que la aplicación está corriendo:

```bash
curl http://localhost:8501
```

### Ver logs en tiempo real:

```bash
sudo journalctl -u acr-app -f
```

## 🔧 Solución de Problemas

### Error: "No secrets found"

- Verifica que el archivo `.streamlit/secrets.toml` existe
- Verifica que está en una de estas rutas:
  - `/home/acr/.streamlit/secrets.toml` (global)
  - `/home/acr/streamlit-app/.streamlit/secrets.toml` (proyecto)
- Verifica los permisos: `chmod 600 .streamlit/secrets.toml`

### Error: "ModuleNotFoundError"

```bash
source env/bin/activate
pip install -r requirements.txt
```

### Error: "Permission denied"

```bash
sudo chown -R acr:acr /home/acr/streamlit-app
```

## 🔒 Seguridad

1. **NUNCA** subir `secrets.toml` a Git (ya está en `.gitignore`)
2. Mantener permisos restrictivos: `chmod 600 secrets.toml`
3. Usar un usuario sin privilegios de root para ejecutar la app
4. Configurar firewall para limitar acceso al puerto 8501

## 📚 Recursos Adicionales

- [Documentación de Streamlit Secrets](https://docs.streamlit.io/library/advanced-features/secrets-management)
- [Documentación de systemd](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
