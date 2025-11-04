"""
EJERCICIO 2: Agente de Información de Países con API Pública

ENUNCIADO:
----------
Crear un agente inteligente que:

1. Reciba consultas en lenguaje natural sobre países del mundo
   Ejemplo: "¿Cuál es la capital de Francia?"
   Ejemplo: "Dime la población y moneda de Argentina"

2. Use el LLM de OpenAI para:
   - Extraer el nombre del país de la consulta del usuario
   - Interpretar qué información específica se está solicitando

3. Consulte la API REST Countries (https://restcountries.com/v3.1/name/{pais})
   para obtener datos reales del país

4. Use nuevamente el LLM para:
   - Formatear la respuesta de la API en lenguaje natural
   - Presentar la información de forma conversacional al usuario

OBJETIVO:
---------
Implementar un agente que integre:
- LLM para procesamiento de lenguaje natural
- API externa para obtener datos reales
- Flujo de trabajo agéntico (percepción → acción → respuesta)

API A UTILIZAR:
---------------
REST Countries API v3.1
- URL base: https://restcountries.com/v3.1
- Endpoint: /name/{nombre_pais}
- No requiere API key
- Documentación: https://restcountries.com

DATOS DISPONIBLES:
------------------
- Capital, población, área
- Idiomas oficiales, monedas
- Región, subregión
- Países fronterizos
- Bandera (emoji y URL)
- Zona horaria, código de llamada
"""

import os
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

# TODO: Cargar las variables de entorno
# Pista: load_dotenv()


# TODO: Inicializar el cliente de OpenAI
# Pista: client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extraer_pais(consulta_usuario):
    """
    Usa el LLM para extraer el nombre del país de la consulta del usuario.
    
    Args:
        consulta_usuario: La pregunta del usuario en lenguaje natural
    
    Returns:
        El nombre del país en inglés (para la API)
    """
    # TODO: Crear un prompt que le pida al LLM extraer el nombre del país
    # El prompt debe:
    # - Indicar que debe extraer solo el nombre del país
    # - Pedir que responda SOLO con el nombre en inglés
    # - Sin explicaciones adicionales
    
    prompt = """
    # Escribe aquí tu prompt
    """
    
    # TODO: Hacer la llamada al LLM
    # Usa client.chat.completions.create()
    # model: "gpt-4o-mini"
    # messages: [{"role": "user", "content": prompt}]
    # temperature: 0.3 (baja para respuestas más precisas)
    
    
    # TODO: Retornar el nombre del país extraído
    # Pista: response.choices[0].message.content.strip()
    

def consultar_api_paises(nombre_pais):
    """
    Consulta la API de REST Countries para obtener información del país.
    
    Args:
        nombre_pais: Nombre del país en inglés
    
    Returns:
        Diccionario con los datos del país o None si hay error
    """
    # TODO: Construir la URL de la API
    # URL base: https://restcountries.com/v3.1/name/
    # Agregar el nombre del país al final
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
    
    try:
        # TODO: Hacer la petición GET a la API
        # Pista: response = requests.get(url)
        
        
        # TODO: Verificar si la respuesta fue exitosa
        # Pista: response.status_code == 200
        
        
        # TODO: Convertir la respuesta JSON a diccionario Python
        # Pista: datos = response.json()
        # La API devuelve una lista, toma el primer elemento [0]
        
        
        # TODO: Retornar los datos del país
        pass
        
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return None


def formatear_respuesta(consulta_usuario, datos_pais):
    """
    Usa el LLM para formatear los datos del país en una respuesta natural.
    
    Args:
        consulta_usuario: La pregunta original del usuario
        datos_pais: Diccionario con los datos del país de la API
    
    Returns:
        Respuesta formateada en lenguaje natural
    """
    # TODO: Extraer información relevante de los datos del país
    # Algunos campos útiles:
    # - datos_pais['name']['common']: Nombre común
    # - datos_pais['capital'][0]: Capital
    # - datos_pais['population']: Población
    # - datos_pais['region']: Región
    # - datos_pais['subregion']: Subregión
    # - datos_pais['languages']: Idiomas (diccionario)
    # - datos_pais['currencies']: Monedas (diccionario)
    # - datos_pais['area']: Área en km²
    # - datos_pais['flag']: Emoji de la bandera
    
    # Convertir los datos a un formato legible para el LLM
    info_pais = f"""
    Nombre: {datos_pais.get('name', {}).get('common', 'N/A')}
    Capital: {datos_pais.get('capital', ['N/A'])[0] if datos_pais.get('capital') else 'N/A'}
    Población: {datos_pais.get('population', 'N/A'):,}
    Región: {datos_pais.get('region', 'N/A')}
    Subregión: {datos_pais.get('subregion', 'N/A')}
    Área: {datos_pais.get('area', 'N/A'):,} km²
    Bandera: {datos_pais.get('flag', '')}
    """
    
    # TODO: Agregar idiomas si existen
    # Pista: datos_pais.get('languages', {}).values()
    
    
    # TODO: Agregar monedas si existen
    # Pista: datos_pais.get('currencies', {})
    
    
    # TODO: Crear un prompt que le pida al LLM formatear la respuesta
    # El prompt debe:
    # - Incluir la consulta original del usuario
    # - Incluir la información del país
    # - Pedir una respuesta natural y conversacional
    # - Responder específicamente a lo que el usuario preguntó
    
    prompt = f"""
    # Escribe aquí tu prompt
    # Incluye:
    # - La consulta del usuario: {consulta_usuario}
    # - La información del país: {info_pais}
    """
    
    # TODO: Hacer la llamada al LLM
    # Usa client.chat.completions.create()
    # temperature: 0.7 (para respuestas más naturales)
    
    
    # TODO: Retornar la respuesta formateada
    


def agente_paises(consulta_usuario):
    """
    Función principal del agente que orquesta todo el flujo.
    
    Args:
        consulta_usuario: La pregunta del usuario
    
    Returns:
        Respuesta final del agente
    """
    print(f"\n🤖 Agente: Procesando tu consulta...\n")
    
    # PASO 1: Extraer el país de la consulta
    print("📍 Paso 1: Identificando el país...")
    # TODO: Llamar a la función extraer_pais()
    pais = None  # Reemplaza con la llamada real
    
    if not pais:
        return "❌ No pude identificar el país en tu consulta. ¿Podrías reformularla?"
    
    print(f"   ✓ País identificado: {pais}")
    
    # PASO 2: Consultar la API
    print("🌍 Paso 2: Consultando información del país...")
    # TODO: Llamar a la función consultar_api_paises()
    datos = None  # Reemplaza con la llamada real
    
    if not datos:
        return f"❌ No encontré información sobre '{pais}'. Verifica el nombre del país."
    
    print(f"   ✓ Datos obtenidos de la API")
    
    # PASO 3: Formatear la respuesta
    print("💬 Paso 3: Generando respuesta natural...\n")
    # TODO: Llamar a la función formatear_respuesta()
    respuesta = None  # Reemplaza con la llamada real
    
    return respuesta


def main():
    print("=" * 80)
    print("🌎 AGENTE DE INFORMACIÓN DE PAÍSES")
    print("=" * 80)
    print("\nEste agente puede responder preguntas sobre países del mundo.")
    print("Ejemplos:")
    print("  - ¿Cuál es la capital de Francia?")
    print("  - Dime la población de Japón")
    print("  - ¿Qué moneda usa Argentina?")
    print("  - Información sobre Italia")
    print("\nEscribe 'salir' para terminar.")
    print("=" * 80)
    
    while True:
        # TODO: Solicitar la consulta del usuario
        consulta = input("\n👤 Tu consulta: ").strip()
        
        # TODO: Verificar si el usuario quiere salir
        if consulta.lower() in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Hasta luego!")
            break
        
        # TODO: Verificar que la consulta no esté vacía
        if not consulta:
            print("⚠️  Por favor, escribe una consulta.")
            continue
        
        # TODO: Llamar al agente con la consulta
        # respuesta = agente_paises(consulta)
        
        # TODO: Mostrar la respuesta
        # print(f"\n🤖 Agente: {respuesta}")
        print("\n" + "-" * 80)


if __name__ == "__main__":
    main()


"""
TIPS PARA COMPLETAR EL EJERCICIO:
----------------------------------

1. EXTRACCIÓN DEL PAÍS:
   - Usa un prompt claro y específico
   - Pide al LLM que responda SOLO con el nombre del país
   - Usa temperature baja (0.3) para respuestas precisas

2. CONSULTA A LA API:
   - La API devuelve una lista, usa [0] para el primer resultado
   - Maneja errores con try/except
   - Verifica el status_code antes de procesar

3. FORMATEO DE RESPUESTA:
   - Incluye la consulta original en el prompt
   - Proporciona todos los datos relevantes al LLM
   - Usa temperature más alta (0.7) para respuestas naturales

4. MANEJO DE DATOS:
   - Usa .get() para acceder a campos que pueden no existir
   - Los idiomas y monedas son diccionarios anidados
   - Formatea números grandes con comas para legibilidad

5. FLUJO DEL AGENTE:
   Usuario → LLM (extrae país) → API → LLM (formatea) → Usuario

¡Buena suerte! 🚀
"""
