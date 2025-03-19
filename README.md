# 🤖 Asistente Virtual de Perfiles Laborales

Este proyecto es un **asistente virtual local** que ayuda a las personas a construir y mejorar su **perfil laboral** y **hoja de vida**, utilizando un modelo de lenguaje ejecutado en tu propio equipo (sin conexión a Internet).

Utiliza **LLaMA 3.2** a través de **Ollama** y está construido con **FastAPI**, permitiendo consumirlo vía herramientas como **Postman** o integrarlo a otros sistemas.

---

## 🚀 Características

- Corre **100% local**, sin costos ni API externas.
- Utiliza **LLaMA 3.2** para respuestas avanzadas y naturales.
- Mantiene **contexto conversacional**.
- Permite consumirlo vía **Postman** o integrarlo a apps.
- Clasificado como **Asistente Virtual Especializado**.

---

## ⚙️ Tecnologías

- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [Ollama](https://ollama.com/) (modelo local)
- Postman (para pruebas)
- LLaMA 3.2

---

## 🛠️ Instalación y Ejecución

### 1. Clona el repositorio
``
git clone https://github.com/mauromarsiglia/talentotech.git
``

``
cd talentotech
``

### 2. Instalar dependencias
``
pip install fastapi uvicorn ollama
``

### 3. Descarga el modelo en Ollama
``
ollama pull llama3.2
``

### 4. Ejecuta la API
``
uvicorn app:app --port 8000 --workers 2
``

## 📬 Uso con Postman
Método: POST
URL: http://127.0.0.1:8000/consultar
Headers: Content-Type: application/json
Body (raw JSON):

``
{
  "pregunta": "¿Cómo puedo mejorar mi perfil como analista de datos?"
}
``

Respuesta esperada:

``
{
  "respuesta": "Excelente pregunta! Como analista de datos, deberías destacar tus habilidades en...",
  "tiempo_respuesta_seg": 14.65
}
``


## 📄 Créditos
Desarrollado por Mauro Marsiglia
Clase de Chatbots – [Talento Tech].

## 📜 Licencia

---

## ⚡ ¿Listo para compartirlo?  
Este proyecto es de uso educativo y personal. Licencia [MIT].
