# Ejercicio 1 - Sistema de IA con Agentic

## Descripción
Este ejercicio implementa un sistema de 3 llamadas secuenciales al LLM de OpenAI para:
1. Elegir un área de negocio prometedora para IA con Agentic
2. Identificar un problema específico en esa industria
3. Proponer una solución de IA con Agentic

## Requisitos Previos
- Python 3.8 o superior
- Una API Key de OpenAI

## Instalación

### Paso 1: Instalar las dependencias
```bash
pip install -r requirements.txt
```

### Paso 2: Configurar la API Key
1. Abre el archivo `.env`
2. Reemplaza `"TU API KEY"` con tu API Key real de OpenAI:
```
OPENAI_API_KEY="sk-tu-api-key-aqui"
```

## Ejecución

Para ejecutar el ejercicio:
```bash
python Ejercicio_1.py
```

## Funcionamiento

El programa realiza 3 llamadas secuenciales al LLM:

### Llamada 1: Área de Negocio
El LLM selecciona un área de negocio prometedora para implementar IA con Agentic.

### Llamada 2: Problema Específico
Basándose en el área elegida, el LLM describe un problema desafiante que enfrenta esa industria.

### Llamada 3: Solución Propuesta
El LLM propone una solución detallada de IA con Agentic, explicando:
- Cómo funcionaría el sistema agéntico
- Qué agentes específicos se necesitarían
- Cómo trabajarían de forma autónoma
- Beneficios concretos de la solución

## Características del Código

- **Historial de conversación**: Mantiene el contexto entre llamadas
- **Función reutilizable**: `llamar_llm()` puede usarse con o sin contexto previo
- **Salida formateada**: Muestra claramente cada paso del proceso
- **Manejo de variables de entorno**: Usa `python-dotenv` para cargar la API Key de forma segura

## Notas
- El modelo usado es `gpt-4.1 mini`
- Temperatura configurada en 0.7 para respuestas creativas pero coherentes
- Máximo de 500 tokens por respuesta
