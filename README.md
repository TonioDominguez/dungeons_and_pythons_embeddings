![Dungeons and Pythons](https://i.imgur.com/t0n8bOy.jpeg)

# Dungeons & Pythons (Embedding Edition)

## Resumen del proyecto

"Dungeons & Pythons: Embedding Edition" es una particular versión de los clásicos juegos RPG basados en texto (text-based RPG), donde la narrativa se desarrolla a través de las decisiones del
jugador.

Lo que distingue a esta versión es su sistema de interacción basado en NLP: las decisiones del jugador se realizan mediante texto libre que es transformado en vectores mediante tecnología de embeddings, permitiendo una interpretación precisa por parte del sistema.

El motor del juego analiza la similitud cosenoidal entre los vectores generados por el input del usuario y un conjunto de respuestas narrativas predefinidas, también vectorizadas. Por ejemplo, cuando un jugador introduce "Quiero echar un vistazo alrededor", el modelo de embeddings identifica la similitud semántica con la acción predefinida "explorar el bosque", permitiendo una progresión narrativa más natural.

"Dungeons & Pythons: Embedding Edition" es un proyecto bastante especial para mí, ya que es una idea que parte para mejorar mi primer proyecto de Python ["Dungeons & Pythons"](https://github.com/TonioDominguez/Dungeons_and_Pythons). Con "Dungeons & Dragons: Embedding Edition" incorporo tecnología de procesamientode lenguaje natural a la mecánica original para crear una experiencia más inmersiva.

## Contenido del Repositorio

```Contenido del Repositorio Dungeons & Pythons: Embedding Edition
│
├── images/                     # Imágenes utilizadas en el juego
│   ├── scene(n).jpg            # Diferentes escenas
│   └── [nombre_raza]_[nombre_profesión].jpg  # Combinación de personaje
│
├── notebook/                   # Contenedor prueba
│   └── test_game.ipynb         # Notebook tester
│
├── .gitattributes               # Atributos de Git
├── .gitignore                   # Archivo que ignora Git
├── README.md                    # Documentación del proyecto
├── app.py                       # Ejecutar la aplicación
├── game_engine.py               # Motor del juego
├── initial_functions.py         # Funciones creación personajes
├── main.py                      # Iniciar el juego en terminal
└── requirements.txt             # Dependencias del proyecto
└── scene_function.py            # Funciones con escenas y respuestas
```

## Características Principales

- Juego de Rol basado en texto
- Sistema de juego desarrollado con tecnología NLP (Embeddings)
- Creación de personaje con 18 combinaciones posibles (elección de género, profesión y raza)
- Historia interactiva. Narrativa personalizada para cada uno de los 18 personajes
- 4 escenarios, 126 respuestas y 2 finales predefinidos

## Características Técnicas

- Sistema NLP (Embeddings) para interpretar las acciones
- Sistema de estado de sesión para mantener el progreso
- Sistema de imágenes dinámico basado en contexto
- Gestión de estados y escenas del juego

## Modelo IA

- [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2): Modelo de embeddings
- Sistema de similitud semántica para interpretación el texto libre

## Estructura del juego

![estructura](https://i.imgur.com/Dn9ymiC.png)

- El jugador crea su personaje. El género, raza y profesión que elija marcan las condiciones para la aparición de respuestas durante su partida.
- El output de las escenas marcan el contexto narrativo que encuentra el jugador. A través de inputs de textos libres el usuario aporta información que el sistema NLP interpreta y asocia con una determinada respuesta.
- La estructura en árbol de las respuestas organizan el accesl a las diferentes escenas y finales. Ciertas respuestas detonan el acceso a los diferentes caminos.

##🏗️ README EN CONSTRUCCIÓN 🏗️
