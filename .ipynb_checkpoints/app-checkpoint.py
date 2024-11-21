import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
from initial_functions import create_character, races, professions, introduction, presentation
from scene_function import scenes_responses
from PIL import Image
import os


# CONFIGURACIÓN DE LA PÁGINA

st.set_page_config(
  page_title="Dungeons & Pythons: Embedding Edition",
  page_icon="⚔️",
  layout="centered",
  initial_sidebar_state="expanded",
  menu_items={
      'Get Help': None,
      'Report a bug': None,
      'About': """
      # Dungeons & Pythons
      
      Un juego de rol narrativo desarrollado con Streamlit y embeddings.
      
      Versión: 1.0
      
      Desarrollado por: Antonio D. Ambunan (antonio.d.ambunan@gmail.com)
      
      ## Características:
      * Juego de rol basado en texto
      * Sistema de embeddings para procesamiento de lenguaje natural
      * Múltiples razas y clases de personajes
      * Historia interactiva
      """
  }
)

st.markdown("""
<style>
  .stApp {
      background: linear-gradient(
          rgba(0, 0, 0, 0.8), 
          rgba(0, 0, 0, 0.8)
      ),
      url("https://i.imgur.com/1Kb191g.jpeg");
      background-size: cover;
      background-position: center;
  }
  
  /* Texto más legible */
  .stMarkdown {
      color: #E8E8E8;
  }
  
  /* Encabezados del mismo color que el texto */
  .stMarkdown h2, .stMarkdown h3, .stMarkdown h1 {
      color: #E8E8E8 !important;
  }
  
  /* Botones estilo medieval */
  .stButton>button {
      background-color: #8B4513;
      color: #FFD700;
      border: 2px solid #DAA520;
  }
  
  /* Sidebar con tema oscuro */
  .css-1d391kg {
      background-color: rgba(14, 17, 23, 0.9);
  }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  /* Estilo general para todos los textos de etiquetas y encabezados */
  .stMarkdown h2, 
  .stMarkdown h3, 
  .css-qrbaxs,
  .css-1d0tddh,
  .css-1aqmucy,
  div[data-baseweb="select"] label,
  div[data-baseweb="input"] label,
  .streamlit-expanderHeader,
  label[data-baseweb="label"],
  .stSelectbox label,
  .stTextInput label {
      color: #E8E8E8 !important;
  }
  
  
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  /* Fondo del sidebar */
  [data-testid="stSidebar"] {
      background-color: #0E1117;
  }
  
  /* Color del texto en el sidebar */
  [data-testid="stSidebar"] .css-17lntkn {
      color: #E8E8E8;
  }
  
  /* Estilo para los radio buttons del sidebar */
  [data-testid="stSidebar"] .st-bw {
      color: #E8E8E8;
  }
  
  /* Título del sidebar */
  [data-testid="stSidebar"] .css-17lntkn h1 {
      color: #E8E8E8;
  }
  
  /* Elementos del radio button */
  .st-cc {
      color: #E8E8E8 !important;
  }
  
  /* Texto del menú lateral */
  .css-17lntkn {
      color: #E8E8E8 !important;
  }
  
  /* Fondo de los elementos seleccionados en el sidebar */
  [data-testid="stSidebar"] .st-dk {
      background-color: rgba(255, 255, 255, 0.1);
  }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  /* Color negro para el texto dentro de los selectbox */
  .stSelectbox select option {
      color: black !important;
  }
  
  /* Color negro para el texto seleccionado en los selectbox */
  .stSelectbox select {
      color: black !important;
  }
  
  /* Color negro para el texto en el input */
  .stTextInput input {
      color: black !important;
  }
  
  /* Para asegurar que el texto sea visible en el dropdown */
  div[data-baseweb="select"] ul {
      color: black !important;
  }
  
  div[data-baseweb="select"] div {
      color: black !important;
  }
  
  /* Para el texto seleccionado */
  .st-bd {
      color: black !important;
  }
  
  /* Para las opciones en el menú desplegable */
  .st-be {
      color: black !important;
  }
</style>
""", unsafe_allow_html=True)


#CONFIGURACIÓN: PÁGINA DE INICIO

def home_page():
    st.markdown(
      """
      <style>
      .banner {
          width: 100%;
          height: 300px; /* Ajusta la altura según necesites */
          object-fit: cover;
          margin-bottom: 2rem;
          border-radius: 10px; /* Bordes redondeados */
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra suave */
      }
      </style>
      """,
      unsafe_allow_html=True
    )
    
    st.markdown(
      f'<img src="https://i.imgur.com/Jr9Urvv.jpeg" class="banner">',
      unsafe_allow_html=True
    )
    
    st.markdown("<h1 style='text-align: center;'>Bienvenido/a a Dungeons & Pythons (Embedding Edition)</h1>", unsafe_allow_html=True)
  
    st.markdown('''
    ## ¡Una aventura épica con tecnología NLP!
  
    "Dungeons & Pythons: Embedding Edition" es una particular versión de los clásicos juegos RPG basados en texto (text-based RPG), donde la narrativa se desarrolla a través de las decisiones del     
    jugador. 
    
    Lo que distingue a esta versión es su sistema de interacción basado en NLP: las decisiones del jugador se realizan mediante texto libre que es transformado en vectores mediante tecnología 
    de embeddings, permitiendo una interpretación precisa por parte del sistema.

    El motor del juego analiza la similitud cosenoidal entre los vectores generados por el input del usuario y un conjunto de respuestas narrativas predefinidas, también vectorizadas. Por ejemplo, cuando un
    jugador introduce "Quiero echar un vistazo alrededor", el modelo de embeddings identifica la similitud semántica con la acción predefinida "explorar el bosque", permitiendo una progresión narrativa 
    más natural.
    
    "Dungeons & Pythons: Embedding Edition" es un proyecto bastante especial para mí, ya que es una idea que parte para mejorar mi primer proyecto de Python "Dungeons & Pythons". Con "Dungeons & Dragons: 
    Embedding Edition" incorporo tecnología de procesamientode lenguaje natural a la mecánica original para crear una experiencia más inmersiva.
  
    ### Características principales:
    - Juego de Rol basado en texto
    - Sistema de juego desarrollado con tecnología NLP (Embeddings)
    - Creación de personaje con 18 combinaciones posibles (elección de género, profesión y raza)
    - Historia interactiva. Narrativa personalizada para cada uno de los 18 personajes
    - 4 escenarios, 126 respuestas y 2 finales predefinidos
    
    ### Características Técnicas
    - Sistema NLP (Embeddings) para interpretar las acciones
    - Sistema de estado de sesión para mantener el progreso
    - Sistema de imágenes dinámico basado en contexto
    - Gestión de estados y escenas del juego
    
    ### Modelos de IA
    - **all-MiniLM-L6-v2**: Modelo de embeddings 
    - Sistema de similitud semántica para interpretación el texto libre
    
    ### Bibliotecas Python:
    - **Streamlit**: Framework principal para la interfaz web interactiva
    - **Sentence-Transformers**: Modelo NLP para entender las acciones del usuario
    - **Pandas**: Manejo de datos estructurados para la información del personaje
    - **NumPy**: Operaciones con vectores para el sistema de similitud
    - **Pillow (PIL)**: Procesamiento y visualización de imágenes
    
    ''')
    
    st.markdown('''
    ### Estructura
    ''')
    
    st.markdown(
      f'<img src="https://i.imgur.com/z19UtPR.png">',
      unsafe_allow_html=True
    )
    
    st.markdown('''
    
    1. La creación de personaje marca el tipo de respuesta que mostrará el sistema durante el juego (7 por tipo de personaje, 126 almacenadas en total) 
    2. El usuario interactúa con los escenarios a través de texto libre. Si no encuentra similitud con las respuestas almacenadas, informa que la acción no está disponible
  
    ''')
     
    st.markdown('''
    ### Apuntes adicionales
    
    "Dungeons & Pythons: Embedding Edition" es una versión que está lejos de ser la definitiva. Lanzo este prototipo como una demo que muestra el potencial que puede desarrollarse con más tiempo y dedicación. Hay 
    aspectos que me gustaría mejorar en un futuro, como son los de desarrollar un sistema de combate dinámico adaptado a NLP, construir una estructura más robusta para transicionar entre escenas o generar muchas 
    más opciones de respuesta.
    
    Si crees que puedes aportar a "Dungeons & Pythons: Embedding Edition" con una sugerencia de código o alguna idea, te animo a contactes conmigo a mi correo antonio.d.ambunan@gmail.com o me tires un Pull 
    Request a https://github.com/TonioDominguez
    ''')

    
    
#CONFIGURACIÓN: PÁGINA DE JUEGO

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
      
    def add_response(self, scene_id, input_patterns, response_text, race_mod=None, profession_mod=None, response_image=None):
        if isinstance(input_patterns, str):
            input_patterns = [input_patterns]
      
        response = {
            'pattern': input_patterns,
            'text': response_text,
            'race_modifier': race_mod,
            'profession_modifier': profession_mod,
            'image': response_image,
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
      
        if best_response:
            if current_scene_id == 1 and "orbe arcano" in best_response["text"].lower():
                self.orb_found = True
        
        if best_score >= 0.7:
            
            return best_response
        
        
        else:
            return "Tu acción no está contemplada por ahora en el juego. Sé más específico"
    
    def load_scenes(self):
        scenes_responses(self)

#Definir rutas de imágenes y función para escenas y presentación

IMAGES_PATH = "images"  
SCENE_IMAGES = {
  1: os.path.join(IMAGES_PATH, "scene1.jpg"),
  2: os.path.join(IMAGES_PATH, "scene2.jpg"),
  3: os.path.join(IMAGES_PATH, "scene3.jpg"),
  4: os.path.join(IMAGES_PATH, "scene4.jpg")
}

CHARACTER_IMAGES_PATH = "images"  
CHARACTER_IMAGES = {
  ("humano", "guerrero"): os.path.join(CHARACTER_IMAGES_PATH, "humano_guerrero.jpg"),
  ("humana", "guerrera"): os.path.join(CHARACTER_IMAGES_PATH, "humana_guerrera.jpg"),
  ("humano", "hechicero"): os.path.join(CHARACTER_IMAGES_PATH, "humano_hechicero.jpg"),
  ("humana", "hechicera"): os.path.join(CHARACTER_IMAGES_PATH, "humana_hechicera.jpg"),
  ("humano", "pícaro"): os.path.join(CHARACTER_IMAGES_PATH, "humano_picaro.jpg"),
  ("humana", "pícara"): os.path.join(CHARACTER_IMAGES_PATH, "humana_picara.jpg"),
  ("elfo", "guerrero"): os.path.join(CHARACTER_IMAGES_PATH, "elfo_guerrero.jpg"),
  ("elfa", "guerrera"): os.path.join(CHARACTER_IMAGES_PATH, "elfa_guerrera.jpg"),
  ("elfo", "hechicero"): os.path.join(CHARACTER_IMAGES_PATH, "elfo_hechicero.jpg"),
  ("elfa", "hechicera"): os.path.join(CHARACTER_IMAGES_PATH, "elfa_hechicera.jpg"),
  ("elfo", "pícaro"): os.path.join(CHARACTER_IMAGES_PATH, "elfo_picaro.jpg"),
  ("elfa", "pícara"): os.path.join(CHARACTER_IMAGES_PATH, "elfa_picara.jpg"),
  ("enano", "guerrero"): os.path.join(CHARACTER_IMAGES_PATH, "enano_guerrero.jpg"),
  ("enana", "guerrera"): os.path.join(CHARACTER_IMAGES_PATH, "enana_guerrera.jpg"),
  ("enano", "hechicero"): os.path.join(CHARACTER_IMAGES_PATH, "enano_hechicero.jpg"),
  ("enana", "hechicera"): os.path.join(CHARACTER_IMAGES_PATH, "enana_hechicera.jpg"),
  ("enano", "pícaro"): os.path.join(CHARACTER_IMAGES_PATH, "enano_picaro.jpg"),
  ("enana", "pícara"): os.path.join(CHARACTER_IMAGES_PATH, "enana_picara.jpg"),
}

RESPONSE_IMAGES_PATH = "images"
RESPONSE_IMAGES = {
    "explorar bosque": "lago.jpg",
    "explorar lago": "orbe.jpg"
}


# Funciones de implementación de imágenes (creador de personajes, escena y respuestas determinadas)

def show_scene_image(scene_id):    
    if scene_id in SCENE_IMAGES and os.path.exists(SCENE_IMAGES[scene_id]):        
        col1, col2, col3 = st.columns(3)        
        with col2:
            image = Image.open(SCENE_IMAGES[scene_id])
            st.image(image, width=300)

def show_character_image(race, profession):
    if (race, profession) in CHARACTER_IMAGES and os.path.exists(CHARACTER_IMAGES[(race, profession)]):
        col1, col2, col3 = st.columns(3)
        with col2:
            image = Image.open(CHARACTER_IMAGES[(race, profession)])
            st.image(image, width=300)            
            
def show_response_image(image_key, image_container):
      if image_key in RESPONSE_IMAGES:
            image_path = os.path.join(RESPONSE_IMAGES_PATH, RESPONSE_IMAGES[image_key])
            if os.path.exists(image_path):
                with image_container:
                    image = Image.open(image_path)
                    st.image(image, width=300)
            
        
#Función de la página de juego
        
def game_page():
        
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
    if 'orb_found' not in st.session_state:
        st.session_state.orb_found = False
    
    st.markdown(
      """
      <style>
      .banner {
          width: 100%;
          height: 300px; /* Ajusta la altura según necesites */
          object-fit: cover;
          margin-bottom: 2rem;
          border-radius: 10px; /* Bordes redondeados */
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra suave */
      }
      </style>
      """,
      unsafe_allow_html=True
    )
    
    st.markdown(
      f'<img src="https://i.imgur.com/Jr9Urvv.jpeg" class="banner">',
      unsafe_allow_html=True
    )

    # Title
    st.markdown("<h1 style='text-align: center;'>Dungeons & Pythons: Embedding Edition</h1>", unsafe_allow_html=True)

    # Contenedor principal para el log del juego
    main_container = st.empty()

    # Crea Personje
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

            show_character_image(
                st.session_state.game.character['Raza'].iloc[0],
                st.session_state.game.character['Profesión'].iloc[0]
            )

            # Mostrar introducción y presentación del personaje
            intro_text = """
            
            ¡Bienvenido/a a Dungeons&Pythons: Embedding Edition! Una aventura en donde la magia y el peligro acechan en cada rincón. Estás a punto de embarcarte en una gesta que pondrá a prueba tu valentía y 
            astucia.
            Un enorme y ancestral dragón negro está destruyendo todo a su paso. ¿Serás tú quién salve a los habitantes del Reino?
            
            """

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

        image_container = st.empty()

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
                    response_obj = st.session_state.game.find_best_response(user_input.lower(), st.session_state.current_scene_id)

                    response_text = ""

                    if isinstance (response_obj, dict):

                    # Se limpia la imagen anterior
                        image_container.empty()

                    # Condición que muestra la imagen si coincide el patron en respuesta

                        action_key = None
                        for pattern in response_obj['pattern']:
                            if pattern in RESPONSE_IMAGES:
                                action_key = pattern
                                break

                    #Muestra la respuesta concreta o la escena si no aplica

                        if action_key:
                            show_response_image(action_key, image_container)
                        else:
                            show_scene_image(st.session_state.current_scene_id)

                    # Actualizar el texto actual
                        response_text = response_obj["text"]
                        st.session_state.current_text = response_text

                    # Verificar si el orbe arcano fue encontrado en escena 1
                        if st.session_state.current_scene_id == 1 and "orbe arcano" in response_text.lower():
                            st.session_state.orb_found = True

                    # Verificar cambios de escena
                        new_scene = None
                        if st.session_state.current_scene_id == 1 and "dragón" in response_text.lower():
                            st.session_state.current_scene_id = 2
                            new_scene = st.session_state.game.scenes[2]["text"]
                            st.session_state.current_text = f"{response_text}\n\n{new_scene}"

                        elif st.session_state.current_scene_id == 2 and "orbe" in response_text.lower() and st.session_state.orb_found:
                            st.session_state.current_scene_id = 3
                            new_scene = st.session_state.game.scenes[3]["text"]
                            st.session_state.current_text = f"{response_text}\n\n{new_scene}\n\n ¡HAS GANADO! ¡ENHORABUENA POR DERROTAR AL DRAGÓN!"

                        elif st.session_state.current_scene_id == 2 and "con tu muerte" in response_text.lower():
                            st.session_state.current_scene_id = 4
                            new_scene = st.session_state.game.scenes[4]["text"]
                            st.session_state.current_text = f"{response_text}\n\n{new_scene}\n\n ¡HAS PERDIDO! ¡INTÉNTALO OTRA VEZ!"

                        else:
                            st.session_state.current_text = response_text

                    else: #Si no hay una respuesta que coincida
                        st.session_state.current_text = "No hay respuestas relacionadas con tu acción. Sé más específico"

                # Actualiza interfaz cuando termina todo el proceso embedding
                st.rerun()

        # Reset button
        if st.button("Reiniciar Juego"):
            st.session_state.clear()
            #st.experimental_rerun()
            st.rerun()

# MENÚ LATERAL

st.sidebar.image(
  "https://i.imgur.com/mnu0AWt.jpeg",  
  width=250
)
st.sidebar.title("Dungeons & Pythons (Embedding Edition)")
page = st.sidebar.radio("", ["Inicio","Jugar"])

#NAVEGACIÓN

if page == "Inicio":
    home_page()
else:
    game_page()
