import streamlit as st
import requests
import os
from dotenv import load_dotenv

st.title("🧪 Test de API Gemini")

# Cargar variables de entorno
load_dotenv()

if st.button("Probar API de Gemini"):
    st.write("Iniciando test...")
    
    # Obtener API key
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.error("No se encontró API key")
        st.stop()
    
    if len(api_key) != 39:
        # Leer directamente del archivo
        try:
            with open('.env', 'r') as f:
                content = f.read()
                for line in content.split('\n'):
                    if line.startswith('GEMINI_API_KEY='):
                        api_key = line.split('=', 1)[1].strip()
                        break
        except Exception as e:
            st.error(f"Error leyendo .env: {e}")
            st.stop()
    
    st.write(f"API Key: {len(api_key)} caracteres")
    st.write(f"Primeros 10: {api_key[:10]}")
    
    # Preparar petición
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{
                "text": "Responde brevemente: ¿Cómo estás?"
            }]
        }]
    }
    
    st.write("Enviando petición...")
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        st.write(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            st.success("¡API funcionando!")
            if 'candidates' in result and len(result['candidates']) > 0:
                respuesta = result['candidates'][0]['content']['parts'][0]['text']
                st.write(f"Respuesta: {respuesta}")
            else:
                st.write("Respuesta vacía")
                st.json(result)
        else:
            st.error(f"Error {response.status_code}")
            st.write(response.text)
            
    except requests.exceptions.Timeout:
        st.error("Timeout - La petición tardó más de 30 segundos")
    except requests.exceptions.ConnectionError:
        st.error("Error de conexión")
    except Exception as e:
        st.error(f"Error: {e}")
        import traceback
        st.code(traceback.format_exc())