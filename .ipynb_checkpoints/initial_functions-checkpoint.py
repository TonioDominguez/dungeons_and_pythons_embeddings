import time
import pandas as pd


'''

Variables necesarias para crear el personaje

'''

races = ["humano", "humana", "elfo", "elfa", "enano", "enana"]
professions = ["guerrero", "hechicero", "pícaro", "guerrera", "hechicera", "pícara"]




'''

Funciones de presentación y creación de personaje

'''

def linebreaker(): #Se usa para separar visualmente episodios del juego
        time.sleep(1)
        print(" ")
        x = " *** "
        print(x*15)
        print(x*15)
        print(" ")
        
        

def introduction(): #Texto de narrativa: presentación de juego
    time.sleep(1.5)
    print("Las antiguas leyendas cobran vida mientras las sombras danzan en las paredes de piedra...")
    print(" ")
    time.sleep(2)
    print("¡Bienvenido, viajero, a Dungeons&Pythons! Una aventura en donde la magia y el peligro acechan en cada rincón.")
    print("Estás a punto de embarcarte en una gesta que pondrá a prueba tu valentía y astucia.")
    print(" ")
    time.sleep(2.5)
    print("En estas tierras olvidadas, donde antiguos dragones duermen bajo montañas de oro")
    print("y criaturas misteriosas acechan en la oscuridad, tu leyenda está a punto de comenzar.")
    print(" ")
    time.sleep(2)
    print("Como aventurero, tendrás la oportunidad de forjar tu destino, conquistar mazmorras")
    print("inexploradas y ganar renombre en una tierra donde solo los más valientes sobreviven.")
    print(" ")
    time.sleep(2.5)
    print("Pero antes de que tu historia pueda ser cantada por los bardos en las tabernas...")
    time.sleep(1)
    print("Antes de que tu nombre pueda ser susurrado con admiración en los reinos...")
    time.sleep(1)
    print("Debes revelarme quién eres, intrépido héroe...")
    print(" ")

def get_name(): #Dota al personaje de nombre
    name = input("¿Cuál es tu nombre?: ").capitalize()   
    return name

def get_race(races): #Dota al personaje de raza jugable. Según la raza cambia las opciones de juego(aunque en demo no implementa) 
    while True:
            race = input("Elige tu raza: human@, elf@, enan@: ").lower()
            if race in races:
                break
            else:
                print(f"No contemplamos {race} como raza jugable por ahora")
    return race

def get_profession(professions): #Dota a personaje de profesión jugable. Determina opciones de narrativa e inventario   
    while True:
        profession = input("Elige tu profesión: guerrer@, hechicer@, pícar@: ").lower()
        if profession in professions:
            break
        else:
            print(f"No contemplamos {profession} como profesión jugable por ahora")
    return profession

def get_weapon(profession): #Añade un arma en función a la professión seleccionada
    
    if profession == "guerrero" or profession == "guerrera":
        weapon = "espada"
    elif profession == "hechicero" or profession == "hechicera":
        weapon = "báculo"
    elif profession == "pícaro" or profession == "pícara":
        weapon = "arco y flechas"    
    return weapon

def presentation(c_sheet):
    text = ""
    if c_sheet["Raza"][0] == "humano" and c_sheet["Profesión"][0] == "guerrero":
        
        text = f"""Eres {c_sheet['Nombre'][0]}, un valiente guerrero de la capital del Reino. Tu determinación y maestría con la espada te han traído hasta aquí para enfrentar al dragón de la montaña. La fuerza de tus antepasados corre por tus venas, y el deber de proteger a tu pueblo te impulsa a seguir adelante.
        
        El dragón ha estado aterrorizando las aldeas cercanas, y solo tu espada podrá detener su reinado de terror..."""

    elif c_sheet["Raza"][0] == "humana" and c_sheet["Profesión"][0] == "guerrera":
        
        text = f"""Te llaman {c_sheet['Nombre'][0]}, la guerrera más temida de las tierras del norte. Tu llegada a estas tierras no es casualidad, el dragón de la montaña debe ser derrotado. Tu armadura porta las marcas de cien batallas, y tu espada anhela añadir una victoria más a tu leyenda.
        
        El dragón ancestral ha despertado de su letargo, y solo tú tienes el valor para enfrentarlo..."""

    elif c_sheet["Raza"][0] == "humano" and c_sheet["Profesión"][0] == "hechicero":
        
        text = f"""Como {c_sheet['Nombre'][0]}, has dedicado tu vida al estudio de las artes arcanas en la Torre de Cristal. Ahora, tus conocimientos serán puestos a prueba. Los antiguos grimorios te han preparado para este momento, y tu magia será la clave para salvar estas tierras.
        
        Las escamas del dragón son resistentes a las armas comunes, pero tu magia podría ser la clave para derrotarlo..."""

    elif c_sheet["Raza"][0] == "humana" and c_sheet["Profesión"][0] == "hechicera":
        
        text = f"""Eres {c_sheet['Nombre'][0]}, una poderosa hechicera formada en los secretos del Círculo Carmesí. Tu dominio de la magia te ha traído hasta estas tierras malditas. Los elementos bailan a tu voluntad, y tu sabiduría será fundamental en esta peligrosa misión.
        
        El aliento de fuego del dragón ha consumido pueblos enteros, pero tus hechizos podrían ser su perdición..."""

    elif c_sheet["Raza"][0] == "humano" and c_sheet["Profesión"][0] == "pícaro":
        
        text = f"""Te conocen como {c_sheet['Nombre'][0]}, el más astuto ladrón de los Barrios Bajos. Tu habilidad para moverte entre las sombras te ha llevado a esta peculiar aventura. Puede que no seas el héroe que todos esperaban, pero tus talentos serán cruciales en esta misión.")
        
        El dragón puede ser poderoso, pero incluso las bestias más temibles tienen puntos débiles que solo tú puedes encontrar..."""

    elif c_sheet["Raza"][0] == "humana" and c_sheet["Profesión"][0] == "pícara":
        
        text = f"""Te llaman {c_sheet['Nombre'][0]}, la sombra que todos temen en los callejones de la ciudad. Tu reputación como maestra del sigilo te precede. Las riquezas del dragón te han atraído hasta aquí, pero quizás encuentres algo más valioso en el camino."
        
        El dragón nunca esperará un ataque desde las sombras, y ese será su mayor error..."""

    elif c_sheet["Raza"][0] == "enano" and c_sheet["Profesión"][0] == "guerrero":
        
        text = f"""Como {c_sheet['Nombre'][0]}, hijo de las montañas de hierro, tu arma ha probado la sangre de cientos de enemigos. El dragón es solo otro nombre en tu lista. Tu honor de guerrero enano y el orgullo de tu clan te guían en esta noble empresa.
        
        El dragón ha profanado las antiguas minas de tu pueblo, y tu hacha clama por venganza..."""

    elif c_sheet["Raza"][0] == "enana" and c_sheet["Profesión"][0] == "guerrera":
        
        text = f"""Eres {c_sheet['Nombre'][0]}, guardiana de las puertas de piedra. Tu arma de guerra ha defendido los halls ancestrales durante décadas. La sangre de los antiguos reyes enanos corre por tus venas, y tu valentía no conoce límites.
        
        El dragón amenaza los tesoros ancestrales de tu pueblo, y tu deber es protegerlos a cualquier costo..."""

    elif c_sheet["Raza"][0] == "enano" and c_sheet["Profesión"][0] == "hechicero":
        
        text = f"""Te llaman {c_sheet['Nombre'][0]}, el forjador de runas. Tus conocimientos ancestrales combinan la magia con la artesanía de tu pueblo. Las runas brillan en tu piel, recordándote el poder que los antiguos maestros te confiaron.
        
        Las runas ancestrales hablan de la debilidad del dragón, y solo tú puedes descifrar sus secretos..."""

    elif c_sheet["Raza"][0] == "enana" and c_sheet["Profesión"][0] == "hechicera":
        
        text = f"""Como {c_sheet['Nombre'][0]}, guardiana de los secretos rúnicos, tu magia proviene de las profundidades de la tierra misma. Los cristales mágicos responden a tu llamada, y los espíritus de la montaña te guían.
        
        El dragón puede dominar los cielos, pero tu magia de la tierra será su perdición..."""

    elif c_sheet["Raza"][0] == "enano" and c_sheet["Profesión"][0] == "pícaro":
        
        text = f"""Eres {c_sheet['Nombre'][0]}, el maestro de los túneles olvidados. Tu conocimiento de las antiguas rutas secretas te ha convertido en una leyenda. Puede que no sigas los caminos tradicionales de tu gente, pero tu astucia honra a tus ancestros.
        
        Los túneles bajo la guarida del dragón guardan secretos que solo tú puedes explotar..."""

    elif c_sheet["Raza"][0] == "enana" and c_sheet["Profesión"][0] == "pícara":
        
        text = f"""Te conocen por {c_sheet['Nombre'][0]}, la sombra de las profundidades. Tu habilidad para moverte sin ser detectada en la oscuridad es legendaria. Los secretos de los antiguos túneles son tus aliados, y las sombras tu segundo hogar.
        
        Mientras el dragón vigila los cielos, tú te acercas sigilosamente desde las profundidades..."""

    elif c_sheet["Raza"][0] == "elfo" and c_sheet["Profesión"][0] == "guerrero":
        
        text = f"""Como {c_sheet['Nombre'][0]}, guardián del bosque eterno, tu espada canta con la gracia de mil veranos. Siglos de entrenamiento te han preparado para este momento, y la naturaleza misma te respalda.
        
        El dragón amenaza el equilibrio del bosque ancestral, y tu espada será el instrumento de su caída..."""

    elif c_sheet["Raza"][0] == "elfa" and c_sheet["Profesión"][0] == "guerrera":
        
        text =f"""Eres {c_sheet['Nombre'][0]}, protectora de los antiguos robles. Tu gracia en batalla es comparable solo con tu determinación. Las estrellas guían tu camino, y el viento susurra historias de tus victorias.
        
        Las llamas del dragón han marchitado el bosque sagrado, y tu hoja vengará esta profanación..."""

    elif c_sheet["Raza"][0] == "elfo" and c_sheet["Profesión"][0] == "hechicero":
        
        text = f"""Te llaman {c_sheet['Nombre'][0]}, tejedor de los hilos mágicos del bosque. Tu conexión con la magia antigua es profunda y poderosa. Los espíritus de la naturaleza son tus aliados, y su sabiduría fluye a través de ti.
        
        El dragón puede dominar el fuego, pero la antigua magia del bosque responde a tu llamado..."""

    elif c_sheet["Raza"][0] == "elfa" and c_sheet["Profesión"][0] == "hechicera":
        
        text = f"""Como {c_sheet['Nombre'][0]}, tu magia fluye con la misma gracia que los ríos eternos del bosque. Los elementos son tus compañeros. La luz de las estrellas potencia tus hechizos, y la sabiduría de los antiguos te guía.
        
        La magia del dragón es poderosa, pero la tuya fluye desde el corazón mismo del bosque..."""

    elif c_sheet["Raza"][0] == "elfo" and c_sheet["Profesión"][0] == "pícaro":
        
        text = f"""Eres {c_sheet['Nombre'][0]}, el susurro entre las hojas. Tu sigilo es legendario incluso entre los más ágiles de tu raza. Las sombras del bosque son tu refugio, y tu astucia es tan afilada como tu daga.
        
        El dragón puede ser formidable, pero incluso las bestias más poderosas tienen puntos ciegos..."""

    elif c_sheet["Raza"][0] == "elfa" and c_sheet["Profesión"][0] == "pícara":
        
        text = f"""Te conocen como {c_sheet['Nombre'][0]}, la danza de las sombras del bosque. Tu gracia y sigilo son incomparables. Te Mueves como la brisa entre las hojas, invisible para aquellos que no saben dónde mirar.
        
        El dragón nunca verá venir tu golpe mortal desde las sombras del bosque..."""
    
    return text

def create_character():
    name = get_name()
    race = get_race(races)
    profession = get_profession(professions)
    
    character = {
        "Nombre": name,
        "Raza": race,
        "Profesión": profession
    }
    
    c_sheet = pd.DataFrame([character])
    return c_sheet
    
def intro():
    introduction()
    c_sheet = create_character()    
    presentation(c_sheet)
    
    return c_sheet
        

        
    
    
    
        