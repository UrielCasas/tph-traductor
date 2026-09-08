import os
import asyncio
import uuid
import glob
import threading
from flask import Flask, request, jsonify, render_template
import edge_tts
from deep_translator import GoogleTranslator, MyMemoryTranslator

app = Flask(__name__, template_folder='.')

STATIC_DIR = 'static'
os.makedirs(STATIC_DIR, exist_ok=True)

VOICE_MAPPING = {
    'en': {'name': 'Inglés', 'male': 'en-US-BrianNeural', 'female': 'en-US-EmmaNeural', 'mymemory_code': 'en-US'},
    'es': {'name': 'Español', 'male': 'es-AR-TomasNeural', 'female': 'es-MX-DaliaNeural', 'mymemory_code': 'es-AR'},
    'fr': {'name': 'Francés', 'male': 'fr-FR-RemyNeural', 'female': 'fr-FR-DeniseNeural', 'mymemory_code': 'fr-FR'},
    'de': {'name': 'Alemán', 'male': 'de-DE-ConradNeural', 'female': 'de-DE-AmalaNeural', 'mymemory_code': 'de-DE'},
    'pt': {'name': 'Portugués', 'male': 'pt-BR-AntonioNeural', 'female': 'pt-BR-FranciscaNeural', 'mymemory_code': 'pt-PT'},
    'it': {'name': 'Italiano', 'male': 'it-IT-DiegoNeural', 'female': 'it-IT-ElsaNeural', 'mymemory_code': 'it-IT'}
}

# Configuración segura de asyncio para servidores WSGI (Gunicorn)
loop = asyncio.new_event_loop()
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

threading.Thread(target=start_loop, args=(loop,), daemon=True).start()

async def generate_audio(text, voice_id, output_file):
    communicate = edge_tts.Communicate(text, voice_id)
    await communicate.save(output_file)

def cleanup_old_audios():
    try:
        files = glob.glob(os.path.join(STATIC_DIR, "traduccion_*.mp3"))
        for f in files:
            os.remove(f)
    except Exception as e:
        print(f"Error al limpiar audios viejos: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def process_query():
    data = request.json or {}
    user_query = data.get('query', '').strip()
    source_lang = data.get('source_lang', 'auto')
    target_lang = data.get('target_lang', 'en')       
    voice_gender = data.get('gender', 'female')
    translator_type = data.get('translator', 'google').lower() 
    
    if not user_query:
        return jsonify({'error': 'El texto está vacío.'}), 400
        
    if target_lang not in VOICE_MAPPING:
        return jsonify({'error': 'Idioma de destino no soportado.'}), 400
        
    try:
        cleanup_old_audios()

        if translator_type == 'mymemory':
            mm_source = VOICE_MAPPING[source_lang]['mymemory_code'] if source_lang in VOICE_MAPPING else source_lang
            mm_target = VOICE_MAPPING[target_lang]['mymemory_code']
            translated_text = MyMemoryTranslator(source=mm_source, target=mm_target).translate(user_query)
        else:
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(user_query)
        
        selected_voice = VOICE_MAPPING[target_lang][voice_gender]
        
        unique_id = uuid.uuid4().hex[:6]
        audio_filename = f"traduccion_{unique_id}.mp3"
        audio_path = os.path.join(STATIC_DIR, audio_filename)
        
        # Ejecución asíncrona segura en hilo dedicado
        future = asyncio.run_coroutine_threadsafe(generate_audio(translated_text, selected_voice, audio_path), loop)
        future.result(timeout=15) # Espera un máximo de 15 segundos
        
        return jsonify({
            'translated': translated_text,
            'audio_url': f"/static/{audio_filename}"
        })
        
    except Exception as e:
        return jsonify({'error': f"Error en el proceso: {str(e)}"}), 500

if __name__ == '__main__':
    # app.run(debug=True, port=5000)
    app.run()
