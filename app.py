from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import time

app = FastAPI()

MODELO = 'llama3.2'

contexto = [
    {'role': 'system', 'content': 
     'Eres un asesor profesional experto en perfiles laborales y desarrollo de carrera. Ayuda al usuario a crear y mejorar su perfil laboral, hoja de vida y resumen profesional. Responde 	siempre en español, con ejemplos y claridad.'
	}
]

@app.on_event("startup")
def precargar_modelo():
    print("⏳ Precargando modelo llama3.2...")
    _ = ollama.chat(model=MODELO, messages=[{'role': 'user', 'content': 'Hola'}], options={'num_predict': 10})
    print("✅ Modelo listo.")

class Consulta(BaseModel):
    pregunta: str

@app.post("/consultar")
def consultar(consulta: Consulta):
    pregunta = consulta.pregunta
    contexto.append({'role': 'user', 'content': pregunta})

    if len(contexto) > 10:
        contexto[:] = contexto[-10:]

    try:
        inicio = time.time()

        # Acumulador de respuesta
        respuesta_final = ""

        # Llamada inicial
        respuesta = ollama.chat(
            model=MODELO,
            messages=contexto,
            options={
                'num_predict': 1000,
                'temperature': 0.6,
                'top_p': 0.9
            }
        )

        mensaje_bot = respuesta['message']['content'].strip()
        respuesta_final += mensaje_bot
        contexto.append({'role': 'assistant', 'content': mensaje_bot})

        # Bucle de continuación: máximo 3
        for i in range(3):
            if not respuesta_final.strip().endswith(('.', '!', '?')):
                contexto.append({'role': 'user', 'content': 'Continúa.'})
                respuesta_cont = ollama.chat(
                    model=MODELO,
                    messages=contexto,
                    options={
                        'num_predict': 500,
                        'temperature': 0.6,
                        'top_p': 0.9
                    }
                )
                mensaje_extra = respuesta_cont['message']['content'].strip()
                respuesta_final += " " + mensaje_extra
                contexto.append({'role': 'assistant', 'content': mensaje_extra})
            else:
                break  # Respuesta completa

        tiempo_total = time.time() - inicio
        print(f"⏱️ Tiempo total: {tiempo_total:.2f} segundos")

        return {
            "respuesta": respuesta_final,
            "tiempo_respuesta_seg": round(tiempo_total, 2)
        }

    except Exception as e:
        return {"error": str(e)}
