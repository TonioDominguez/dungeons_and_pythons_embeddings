import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import time
from initial_functions import create_character, races, professions, introduction, presentation
from scene_function import scenes_responses
from PIL import Image
import os

# Funciones necesarias

def type_text(text, container):
    placeholder = container.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(displayed_text)
        time.sleep(0.01)
    return displayed_text

class GameEngine:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.character = None
        self.scenes = {}
        self.responses = {}
        self.similarity_threshold = 0.3
      
    def set_character(self, c_sheet):
        self.character = c_sheet
      
    def add_scene(self, scene_id, scene_text, context=None, required_race=None, required_profession=None):    
        self.scenes[scene_id] = {
            'text': scene_text,
            'context': context,
            'required_race': required_race,
            'required_profession': required_profession,
            'embedding': self.model.encode(scene_text)
        }    
        if scene_id not in self.responses:
            self.responses[scene_id] = []
      
    def add_response(self, scene_id, input_patterns, response_text, race_mod=None, profession_mod=None):
        if isinstance(input_patterns, str):
            input_patterns = [input_patterns]
      
        response = {
            'pattern': input_patterns,
            'text': response_text,
            'race_modifier': race_mod,
            'profession_modifier': profession_mod,
            'embeddings': [self.model.encode(pattern) for pattern in input_patterns]
        }
        self.responses[scene_id].append(response)
      
    def find_best_response(self, user_input, current_scene_id):
        if current_scene_id not in self.responses:
            return "No hay respuestas disponibles para esta escena."    
      
        user_embedding = self.model.encode(user_input)
        best_score = -1
        best_response = None
      
        for response in self.responses[current_scene_id]:
            similarities = [np.dot(user_embedding, pattern_embeding)
                          for pattern_embeding in response['embeddings']]
            max_similarity = max(similarities)
          
            if response['race_modifier'] == self.character['Raza'].iloc[0]:
                max_similarity += 0.1
            if response['profession_modifier'] == self.character['Profesión'].iloc[0]:
                max_similarity += 0.1
          
            if max_similarity > best_score:
                best_score = max_similarity
                best_response = response
      
        if best_score >= 0.7:
            return best_response["text"]
        else:
            return "Tu acción no está contemplada por ahora en el juego. Sé más específico"
  
    def load_scenes(self):
        scenes_responses(self)

#Definir rutas de imágenes y función para escenas

IMAGES_PATH = "images"  
SCENE_IMAGES = {
  1: os.path.join(IMAGES_PATH, "scene1.jpg"),
  2: os.path.join(IMAGES_PATH, "scene2.jpg"),
  3: os.path.join(IMAGES_PATH, "scene3.jpg"),
  4: os.path.join(IMAGES_PATH, "scene4.jpg")
}

def show_scene_image(scene_id):
    
    if scene_id in SCENE_IMAGES and os.path.exists(SCENE_IMAGES[scene_id]):
        
        col1, col2, col3 = st.columns(3)
        
        with col2:
            image = Image.open(SCENE_IMAGES[scene_id])
            st.image(image, width=300)

        
# Initialize session state
if 'game' not in st.session_state:
    st.session_state.game = GameEngine()
if 'current_scene_id' not in st.session_state:
    st.session_state.current_scene_id = 1
if 'character_created' not in st.session_state:
    st.session_state.character_created = False
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'current_text' not in st.session_state:
    st.session_state.current_text = ""
if 'introduction_shown' not in st.session_state:
    st.session_state.introduction_shown = False

# Title
st.markdown("<h1 style='text-align: center;'>Dungeons & Pythons</h1>", unsafe_allow_html=True)

# Contenedor principal para el log del juego
main_container = st.empty()

# Character Creation Section
if not st.session_state.character_created:
    st.markdown("<h2 style='text-align: center;'>Crea tu personaje</h1>", unsafe_allow_html=True)
  
    col1, col2 = st.columns(2)
    with col1:
        race = st.selectbox("Elige tu raza:", races)
    with col2:
        profession = st.selectbox("Elige tu profesión:", professions)
  
    name = st.text_input("Introduce tu nombre:")
  
    if st.button("Crear Personaje"):
        if name:
            character = {
                "Nombre": name,
                "Raza": race,
                "Profesión": profession
            }
            c_sheet = pd.DataFrame([character])
            st.session_state.game.set_character(c_sheet)
            st.session_state.character_created = True
            st.session_state.game.load_scenes()
            st.experimental_rerun()
        else:
            st.error("Por favor, introduce un nombre para tu personaje.")

# Game Section
elif not st.session_state.game_started:
    if not st.session_state.introduction_shown:
        
        show_scene_image(1)
        
        # Mostrar introducción y presentación del personaje
        intro_text = """¡Bienvenido/a a Dungeons&Pythons! Una aventura en donde la magia y el peligro acechan en cada rincón.
Estás a punto de embarcarte en una gesta que pondrá a prueba tu valentía y astucia.

¡El destino del reino está en tus manos! ¿Serás tú quién salve al reino?."""

        # Obtener la presentación del personaje basada en el c_sheet
        character_presentation = presentation(st.session_state.game.character)
        
        # Combinar introducción y presentación
        complete_intro = f"{intro_text}\n\n{character_presentation}"
        
        st.markdown(complete_intro)
        st.session_state.introduction_shown = True
        
    main_container.markdown(st.session_state.current_text)
    
    if st.button("Comenzar Aventura"):
        st.session_state.game_started = True
        st.session_state.current_text = st.session_state.game.scenes[st.session_state.current_scene_id]['text']
        st.session_state.text_type = "scene"
        st.experimental_rerun()

else:
    
    show_scene_image(st.session_state.current_scene_id)
    
    # Mostrar el texto actual
    main_container.markdown(st.session_state.current_text)
    
    # Input section at the bottom
    user_input = st.text_input("¿Qué quieres hacer?", key="action_input")
  
    if st.button("Ejecutar Acción"):
        if user_input:
            # Mostrar spinner mientras se procesa
            with st.spinner('Procesando tu acción...'):
            
                # Obtener respuesta
                response = st.session_state.game.find_best_response(user_input.lower(), st.session_state.current_scene_id)
            
                # Actualizar el texto actual
                st.session_state.current_text = response
            
                # Verificar cambios de escena
                new_scene = None
                if st.session_state.current_scene_id == 1 and "dragón" in response.lower():
                    st.session_state.current_scene_id = 2
                    new_scene = st.session_state.game.scenes[2]["text"]
                    st.session_state.current_text = f"{response}\n\n{new_scene}"
          
                elif st.session_state.current_scene_id == 2 and "orbe" in response.lower():
                    st.session_state.current_scene_id = 3
                    new_scene = st.session_state.game.scenes[3]["text"]
                    st.session_state.current_text = f"{response}\n\n{new_scene}\n\n ¡HAS GANADO!"
          
                elif st.session_state.current_scene_id == 2 and "con tu muerte" in response.lower():
                    st.session_state.current_scene_id = 4
                    new_scene = st.session_state.game.scenes[4]["text"]
                    st.session_state.current_text = f"{response}\n\n{new_scene}\n\n ¡HAS PERDIDO! ¡INTENTALO OTRA VEZ"
          
                else:
                    st.session_state.current_text = response
            
            # Actualiza interfaz cuando termina todo el proceso embedding
            st.experimental_rerun()

    # Reset button
    if st.button("Reiniciar Juego"):
        st.session_state.clear()
        st.experimental_rerun()
