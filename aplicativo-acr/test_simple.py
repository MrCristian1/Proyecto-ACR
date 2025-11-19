import requests
import os
from dotenv import load_dotenv

def test_gemini_simple():
    """Prueba simple de la API de Gemini"""
    # Cargar variables de entorno
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"API Key length: {len(api_key) if api_key else 'None'}")
    
    if not api_key:
        # Leer del archivo .env directamente
        try:
            with open('.env', 'r') as f:
                content = f.read()
                for line in content.split('\n'):
                    if line.startswith('GEMINI_API_KEY='):
                        api_key = line.split('=', 1)[1].strip()
                        break
        except Exception as e:
            print(f"Error leyendo .env: {e}")
            return None
    
    if not api_key:
        print("❌ No se pudo obtener API key")
        return None
    
    print(f"✅ API Key obtenida: {api_key[:10]}...")
    
    # Prompt de prueba
    prompt = "Explica brevemente qué son los 5 porqués en español."
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    print("🚀 Enviando petición...")
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        print(f"📡 Status code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                texto = result['candidates'][0]['content']['parts'][0]['text']
                print(f"✅ Respuesta recibida: {len(texto)} caracteres")
                print(f"📝 Texto: {texto[:200]}...")
                return texto
            else:
                print("❌ No hay candidates en la respuesta")
                print(f"Respuesta completa: {result}")
                return None
        else:
            print(f"❌ Error HTTP: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    resultado = test_gemini_simple()
    if resultado:
        print("🎉 Test exitoso!")
    else:
        print("💥 Test falló")