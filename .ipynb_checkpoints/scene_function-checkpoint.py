

def scenes_responses(game):
    
    
    ################  Escena 1  ##########
    
    game.add_scene(
        1,
        "La caza del dragón negro te lleva hacia una montaña, en donde según rumores se encuentra la guarida de la temible criatura. Para escalar a la cumbre, primero tendrás que atravesar un bosque que la rodea. ¿Explorarás el lugar antes de escalar la montaña o no perderás tiempo y buscarás un sendero que te lleve a la cima?",
        "bosque_entrada"
    )
    
    #Respuesta "explora el bosque"    
    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu entrenamiento militar te hace notar un lago cristalino. En el fondo, algo metálico brilla como si fuera una antigua arma",
      "humano",
      "guerrero",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu ojo entrenado para la batalla detecta un lago donde algo brilla en el fondo. Parece algo valioso y antiguo. ¿Qué será",
      "humana",
      "guerrera",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu experiencia en forja te hace reconocer el brillo metálico en el fondo del lago cristalino. Podría ser una reliquia enana",
      "enano",
      "guerrero",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Al pasar junto al lago, tu conocimiento de la artesanía enana te permite identificar un brillo característico del metal de tu pueblo",
      "enana",
      "guerrera",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu vista aguda distingue un lago de aguas claras donde reposa algo que emite destellos, parece ser un objeto de manufactura élfica",
      "elfo",
      "guerrero",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tus sentidos élficos te guían hacia un lago cristalino. En sus profundidades, un objeto de tu pueblo emite suaves destellos",
      "elfa",
      "guerrera",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu afinidad mágica te revela un lago de aguas místicas. En el fondo, un objeto arcano emite pulsaciones de poder",
      "humano",
      "hechicero",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tus sentidos arcanos detectan energía mágica emanando de un lago cristalino. Algo poderoso yace en sus profundidades",
      "humana",
      "hechicera",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu conexión con la magia antigua te atrae hacia un lago sagrado. Un artefacto élfico brilla con poder en su lecho",
      "elfo",
      "hechicero",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "La magia natural te guía hacia aguas cristalinas donde un antiguo foco de poder élfico emite destellos místicos",
      "elfa",
      "hechicera",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tus conocimientos rúnicos te permiten identificar un lago ritual. En el fondo, runas ancestrales brillan con poder",
      "enano",
      "hechicero",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu sabiduría en runas te hace detectar un lago sagrado donde un antiguo artefacto enano emite un resplandor mágico",
      "enana",
      "hechicera",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu ojo experto para los tesoros detecta algo valioso en el fondo de un lago cristalino que encuentras en el camino",
      "humano",
      "pícaro",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu instinto para encontrar objetos valiosos te lleva hacia un lago transparente donde algo brilla tentadoramente",
      "humana",
      "pícara",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu experiencia buscando tesoros te hace notar un lago inusualmente claro. Algo de valor ancestral brilla en su fondo",
      "enano",
      "pícaro",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu afinidad por los tesoros te revela un lago cristalino donde algo que parece una joya antigua emite destellos",
      "enana",
      "pícara",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu aguda vista descubre un lago de aguas transparentes. En su fondo, un objeto de manufactura élfica llama tu atención",
      "elfo",
      "pícaro",
      "explorar bosque"
    )

    game.add_response(
      1,
      ["explorar bosque", "buscar suministros", "buscar algo", "explorar", "buscar", "investigar", "explorar alrededor"],
      "Tu percepción natural te permite ver algo de gran valor en el fondo de un lago cristalino que encuentras en tu camino",
      "elfa",
      "pícara",
      "explorar bosque"
    )

    #Respuesta "buscar en el lago"

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tras sumergirte en las frías aguas, tus manos encuentran un objeto esférico. Al sacarlo, un conocimiento ancestral te invade: es el orbe arcano, forjado en la Era de los Dragones. Sus energías palpitantes serán cruciales para penetrar las escamas de tu enemigo alado",
      "humano",
      "guerrero",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "El agua fría no te detiene mientras recuperas un artefacto brillante. Al examinarlo, reconoces el orbe arcano de las antiguas leyendas. Su poder, diseñado específicamente para la caza de dragones, será tu ventaja en la batalla venidera",
      "humana",
      "guerrera",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tus manos expertas extraen del lago un orbe resplandeciente. Las runas en su superficie cobran vida bajo tu mirada: es el legendario orbe arcano mata-dragones. Por fin tienes el arma que equilibrará la balanza contra la bestia",
      "enano",
      "guerrero",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Entre las aguas cristalinas, tus dedos rozan un objeto de poder inmenso. Al sacarlo, las inscripciones revelan el mítico orbe arcano, creado por tus ancestros para combatir dragones. Su energía será decisiva en tu próximo encuentro",
      "enana",
      "guerrera",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Con movimientos fluidos, recuperas un objeto brillante del fondo del lago. Tu sangre élfica reconoce el orbe arcano al instante. Sus energías, letales para los dragones, fluirán a través de ti en el combate final",
      "elfo",
      "guerrero",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Las aguas parecen apartarse ante ti mientras extraes un orbe luminoso. Tu intuición élfica confirma su identidad: el orbe arcano cazadragones. Su poder ancestral te ayudará a enfrentar a la bestia en igualdad de condiciones",
      "elfa",
      "guerrera",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Al tocar el objeto sumergido, una descarga de poder recorre tu cuerpo. Es el orbe arcano, cuya magia fue tejida específicamente para destruir dragones. Tus hechizos, amplificados por su poder, serán devastadores",
      "humano",
      "hechicero",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tus dedos rozan algo que hace que tu magia resuene con fuerza. Al emerger con el orbe arcano, comprendes su propósito: canalizar poder destructivo contra dragones. Esta reliquia multiplicará el poder de tus conjuros",
      "humana",
      "hechicera",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "La magia antigua del lago te guía hacia un artefacto de inmenso poder. Al sostener el orbe arcano, las energías fluyen entre ambos, revelando su propósito: es un amplificador mágico diseñado para la destrucción de dragones. Tu victoria está ahora más cerca",
      "elfo",
      "hechicero",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tus manos encuentran el orbe bajo el agua, y al instante sientes su resonancia mágica. Es el legendario orbe arcano, forjado con hechizos específicos contra dragones. Su poder combinado con tu magia será imparable",
      "elfa",
      "hechicera",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Las runas ancestrales brillan bajo el agua mientras recuperas el orbe arcano. Cada símbolo cuenta la historia de su creación para combatir dragones. Tu conocimiento mágico y este artefacto formarán una combinación letal",
      "enano",
      "hechicero",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Al extraer el orbe del agua, las runas grabadas cobran vida bajo tu toque. Es el mítico orbe arcano, creado en la antigüedad para vencer dragones. Sus energías amplificarán tus hechizos en la batalla que se aproxima",
      "enana",
      "hechicera",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Con la precisión de un experto ladrón, recuperas un tesoro único: el orbe arcano. Tu instinto para los objetos valiosos no te engaña; este artefacto mata-dragones vale más que todas las joyas del reino. Será tu as bajo la manga",
      "humano",
      "pícaro",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tus hábiles manos encuentran el premio oculto en las profundidades. El orbe arcano, más valioso que cualquier tesoro robado, emite un pulso de energía anti-dragón. Has encontrado el arma perfecta para tu misión",
      "humana",
      "pícara",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Con la experiencia de quien ha manipulado cientos de tesoros, extraes el orbe arcano del lago. Sus propiedades contra dragones lo convierten en el botín más valioso que jamás has encontrado. La victoria será tuya",
      "enano",
      "pícaro",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tus dedos expertos reconocen el valor del objeto sumergido antes de verlo. Al emerger con el orbe arcano, confirmas tu intuición: este artefacto mata-dragones es el tesoro más importante que has recuperado",
      "enana",
      "pícara",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Tu agilidad élfica te permite recuperar el artefacto sin perturbar las aguas. El orbe arcano, legendario por su poder contra dragones, responde a tu toque. Has encontrado la herramienta perfecta para tu venganza",
      "elfo",
      "pícaro",
      "explorar lago"
    )

    game.add_response(
      1,
       ["explorar lago", "nadar en lago", "coger objeto", "bucear", "seguir brillo", "alcanzar objeto brillante", "recuperar artefacto", "recoger tesoro"],
      "Con movimientos precisos, extraes el tesoro oculto. El orbe arcano, temido por los dragones desde tiempos antiguos, ahora está en tus manos. Su poder será crucial en la batalla que se avecina",
      "elfa",
      "pícara",
      "explorar lago"
    )
    
    #Respuesta "probar el orbe"
    
    # Guerreros/Guerreras
    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Al empuñar el orbe, sientes cómo su energía fluye por tu brazo. Tu entrenamiento guerrero te permite canalizar su poder hacia tu arma. Las runas brillan con un propósito claro: potenciar tu próximo golpe contra tu enemigo",
      "humano",
      "guerrero",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe responde a tu toque guerrero, enviando oleadas de energía a través de tu armadura. Su poder ancestral se fusiona con tu técnica de combate, preparándote para enfrentar las escamas de tu enemigo",
      "humana",
      "guerrera",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tus manos curtidas en batalla despiertan el poder del orbe. Las antiguas runas enanas brillan con mayor intensidad, reconociendo tu linaje. El artefacto potenciará cada golpe que asestes contra la bestia alada",
      "enano",
      "guerrero",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe vibra con energía al reconocer tu sangre enana. Sus runas ancestrales cobran vida bajo tu toque, prometiendo hacer tus golpes letales contra las escamas de la bestia alada",
      "enana",
      "guerrera",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tu gracia élfica se combina con el poder del orbe, creando una sincronía perfecta. La energía arcana fluye como música a través de tu ser, preparándote para una danza mortal con el monstruo",
      "elfo",
      "guerrero",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe resuena con tu esencia élfica, sus energías entrelazándose con tu gracilidad natural. Cada movimiento se vuelve más preciso, más letal, perfecto para penetrar las defensas del monstruo",
      "elfa",
      "guerrera",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tu poder mágico se amplifica exponencialmente al contacto con el orbe. Los hechizos fluyen con una potencia renovada, preparados para atravesar las defensas mágicas de la bestia",
      "humano",
      "hechicero",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe responde a tu magia con un destello cegador. Sientes cómo amplifica tus poderes arcanos, transformando tus hechizos en armas perfectas contra la resistencia mágica de la criatura alada",
      "humana",
      "hechicera",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Las runas del orbe brillan con intensidad bajo tu toque mágico. La sabiduría ancestral de los enanos se fusiona con tu poder arcano, prometiendo devastación para tu enemigo",
      "enano",
      "hechicero",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tu conocimiento de las runas ancestrales despierta el verdadero potencial del orbe. La magia fluye como un torrente, preparada para superar las defensas místicas del enemigo",
      "enana",
      "hechicera",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe reconoce tu afinidad élfica con la magia. Los hechizos se entrelazan con su poder ancestral, creando una sinfonía arcana capaz de devastar al monstruo",
      "elfo",
      "hechicero",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tu magia élfica encuentra una resonancia perfecta con el orbe. Las energías se fusionan en una danza de poder, preparando hechizos que penetrarán las defensas más fuertes de tu enemigo",
      "elfa",
      "hechicera",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tus hábiles manos descubren rápidamente cómo manipular el orbe. Su poder se adapta a tu estilo sigiloso, prometiendo golpes precisos que encontrarán los puntos débiles de la criatura",
      "humano",
      "pícaro",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe responde a tu toque experto, revelando secretos de su uso. Su energía potenciará tus ataques sorpresa, perfectos para explotar las vulnerabilidades de tu enemigo",
      "humana",
      "pícara",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tu astucia natural te permite descifrar rápidamente los secretos del orbe. Su poder se concentra en tus armas, prometiendo golpes certeros entre las escamas del monstruo alado",
      "enano",
      "pícaro",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tus dedos ágiles encuentran los puntos de poder del orbe. La energía arcana fluye sutilmente, preparándote para asestar golpes precisos en las debilidades de tu formidable enemigo",
      "enana",
      "pícara",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "Tu gracia élfica te permite sincronizarte perfectamente con el orbe. Su poder se funde con tu sigilo natural, prometiendo ataques letales e invisibles contra tu enemigo",
      "elfo",
      "pícaro",
      "probar orbe"
    )

    game.add_response(
      1,
      ["probar el orbe", "probar artefacto", "usar objeto mágico", "usar orbe"],
      "El orbe responde a tu toque élfico con sutileza. Su energía se entrelaza con tu agilidad innata, preparándote para golpes precisos que encontrarán las debilidades del monstruo",
      "elfa",
      "pícara",
      "probar orbe"
    )
    
    #Respuesta "buscar una salida"

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Con instinto de guerrero experimentado, encuentras un antiguo sendero de batalla que asciende por la ladera. El camino te llevará directamente hacia la guarida del dragón en la cima de la montaña",
      "humano",
      "guerrero"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu entrenamiento militar te permite identificar un camino estratégico entre los árboles. La ruta se eleva hacia la cima de la montaña, donde te espera tu enemigo el dragón alado",
      "humana",
      "guerrera"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tus ojos expertos en terreno montañoso descubren un sendero tallado en la roca. El camino serpentea hacia la cima donde se oculta el malévolo dragón",
      "enano",
      "guerrero"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu conocimiento de la montaña te revela un antiguo camino enano que asciende por la ladera. La ruta te conducirá directamente hacia el territorio del dragón",
      "enana",
      "guerrera"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Con agilidad élfica, descubres un sendero natural entre los árboles que se eleva hacia la montaña. El camino te guiará hasta la guarida del dragón ubicado en la cima",
      "elfo",
      "guerrero"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu conexión con la naturaleza te revela un camino oculto que asciende por la ladera. La senda te conducirá hasta el dominio del dragón en la cima",
      "elfa",
      "guerrera"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tus sentidos mágicos detectan un antiguo sendero imbuido de poder. El camino se eleva hacia la cima, donde aguarda tu encuentro con el dragón",
      "humano",
      "hechicero"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu percepción arcana te guía hacia un camino místico que asciende por la montaña. La senda te llevará hasta el territorio de tu adversario el dragón",
      "humana",
      "hechicera"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu conexión con la magia antigua te revela un sendero élfico olvidado que asciende hacia la montaña. Las energías arcanas te indican que este camino te llevará directamente a la guarida del dragón",
      "elfo",
      "hechicero"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Las corrientes mágicas del bosque te muestran el camino más directo hacia la morada del dragón. La senda antigua serpentea hacia la cima donde aguarda tu destino",
      "elfa",
      "hechicera"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tus conocimientos rúnicos te permiten identificar antiguas marcas que señalan el camino hacia la cima. Las inscripciones advierten de la presencia del dragón en lo alto de la montaña",
      "enano",
      "hechicero"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Las runas ancestrales en las rocas te guían por un sendero seguro hacia la montaña. Cada marca confirma que te acercas al territorio del dragón",
      "enana",
      "hechicera"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu experiencia rastreando te permite encontrar un camino discreto y poco transitado hacia la montaña. Las señales de actividad del dragón se hacen más evidentes conforme el sendero asciende",
      "humano",
      "pícaro"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Descubres un sendero oculto que ofrece buena cobertura en su ascenso hacia la montaña. Las marcas de garras y cenizas confirman que conduce a la guarida del dragón",
      "humana",
      "pícara"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu ojo experto detecta un antiguo camino de mineros que sube hacia la montaña. Las huellas y rastros indican que el dragón usa esta ruta para acceder a su guarida",
      "enano",
      "pícaro"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Encuentras marcas sutiles en las rocas que indican una ruta segura hacia la cima. El camino muestra signos claros de ser la ruta hacia el territorio del dragón",
      "enana",
      "pícara"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu sigilo natural te ayuda a encontrar un sendero escondido que asciende discretamente. Las señales en el camino confirman que lleva hacia la guarida del dragón",
      "elfo",
      "pícaro"
    )

    game.add_response(
      1,
      ["buscar salida", "escalar montaña", "salir del bosque", "encontrar camino", "ir hacia la montaña", "seguir búsqueda del dragón", "sendero hacia la cima"],
      "Tu afinidad con el bosque te revela un camino secreto que serpentea hacia la montaña. El rastro de destrucción sutil indica que este sendero lleva al dominio del dragón",
      "elfa",
      "pícara"
    )
    
    
    ################  Escena 2  ##########
    
    
    game.add_scene(
        2,
        "Tras ascender por el sendero, llegas a la cima de la montaña. Ante ti se alza una inmensa cueva, y el suelo está cubierto de huesos calcinados. Un rugido estremecedor resuena desde el interior, y una enorme figura emerge entre las sombras. El dragón, con escamas como acero negro y ojos de fuego, se alza ante ti. ¿Qué haces?",
        "encuentro_dragon"
    )
    
    #Respuesta "Ataca al dragón"
    
    game.add_response(
        2,
        ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
        "Te lanzas al combate con determinación. El dragón responde con un rugido ensordecedor y una llamarada que apenas esquivas. Intuyes que te va a hacer falta algo más que fuerta bruta para derrotar a la criatura",
        "humano",
        "guerrero"
    )
    
    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te lanzas al combate con fiereza. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con ágil determinación. Pronto te das cuenta de que necesitarás más que fuerza bruta para derrotar a esta antigua criatura.",
      "humana",
      "guerrera"
)

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te posicionas con firmeza y preparas tu magia de combate. El dragón responde con un rugido ensordecedor y una llamarada que desvías con un rápido escudo arcano. Comprendes que la magia convencional no será suficiente contra este poderoso ser.",
      "humano",
      "hechicero"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Canalizas tu poder mágico con determinación. El dragón responde con un rugido ensordecedor y una llamarada que dispersas con un elegante gesto arcano. Sin embargo, intuyes que necesitarás descubrir alguna debilidad específica para vencer a esta bestia.",
      "humana",
      "hechicera"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te mueves con agilidad calculada hacia el combate. El dragón responde con un rugido ensordecedor y una llamarada que evades con una acrobática pirueta. Te das cuenta de que necesitarás más que sigilo y destreza para superar este desafío.",
      "humano",
      "pícaro"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te deslizas hacia el combate con gracia letal. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con un ágil movimiento. Percibes que deberás encontrar una estrategia más elaborada para derrotar a este antiguo ser.",
      "humana",
      "pícara"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te lanzas al combate con milenaria precisión élfica. El dragón responde con un rugido ensordecedor y una llamarada que evitas con gracia ancestral. Tu experiencia te dice que necesitarás más que habilidad marcial para vencer a esta criatura.",
      "elfo",
      "guerrero"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te aproximas al combate con elegancia letal. El dragón responde con un rugido ensordecedor y una llamarada que eludes con movimientos fluidos. Tu sabiduría élfica te advierte que deberás buscar una manera alternativa de derrotar al dragón.",
      "elfa",
      "guerrera"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Invocas tu antigua magia élfica con precisión. El dragón responde con un rugido ensordecedor y una llamarada que neutralizas con un encantamiento ancestral. Comprendes que ni siquiera la magia más antigua será suficiente por sí sola.",
      "elfo",
      "hechicero"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Tejes tu magia élfica con gracia milenaria. El dragón responde con un rugido ensordecedor y una llamarada que disipas con un antiguo conjuro. Tu intuición mágica te indica que deberás buscar otro camino para la victoria.",
      "elfa",
      "hechicera"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te deslizas hacia el combate con siglos de experiencia en sigilo. El dragón responde con un rugido ensordecedor y una llamarada que evitas con movimientos élficos. Reconoces que necesitarás más que astucia para superar este desafío.",
      "elfo",
      "pícaro"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te aproximas sigilosamente con destreza élfica. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con gracia sobrenatural. Tu instinto te dice que deberás encontrar una estrategia más ingeniosa.",
      "elfa",
      "pícara"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te plantas firme como la montaña y cargas al combate. El dragón responde con un rugido ensordecedor y una llamarada que resistes con tenacidad enana. Tu experiencia guerrera te indica que necesitarás más que fuerza bruta para esta batalla.",
      "enano",
      "guerrero"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Avanzas con la fuerza de las profundidades. El dragón responde con un rugido ensordecedor y una llamarada que enfrentas con resistencia ancestral. Tu instinto de batalla te advierte que deberás buscar otra forma de derrotar a esta bestia.",
      "enana",
      "guerrera"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Invocas la magia de las piedras antiguas. El dragón responde con un rugido ensordecedor y una llamarada que bloqueas con runas enanas. Comprendes que ni la más poderosa magia rúnica será suficiente por sí sola.",
      "enano",
      "hechicero"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Canalizas el poder de las profundidades. El dragón responde con un rugido ensordecedor y una llamarada que detienes con magia rúnica. Tu conocimiento ancestral te susurra que deberás encontrar otro método para vencer.",
      "enana",
      "hechicera"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Te mueves con la astucia forjada en las minas. El dragón responde con un rugido ensordecedor y una llamarada que evitas con precisión enana. Tu experiencia te dice que necesitarás más que agilidad para superar esta prueba.",
      "enano",
      "pícaro"
    )

    game.add_response(
      2,
      ["atacar", "luchar", "enfrentar dragón", "hacer frente a la criatura"],
      "Avanzas con la cautela aprendida en las cavernas. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con astucia subterránea. Sabes que deberás idear una estrategia más elaborada para esta batalla.",
      "enana",
      "pícara"
    )
    
    #Usar el orbe
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Empuñas el orbe con determinación guerrera. Su poder fluye a través de tu espada, transformándola en una hoja de luz cegadora. Aprovechando tu entrenamiento marcial, ejecutas una serie de ataques precisos que, amplificados por la magia del orbe, atraviesan las escamas del dragón, sometiéndolo finalmente.",
      "humano",
      "guerrero"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Alzas el orbe mientras adoptas una postura de combate. Su energía mágica envuelve tu armadura y arma, dotándote de un poder ancestral. Con maestría marcial, canalizas la magia a través de cada golpe, hasta que el dragón sucumbe ante la combinación de tu fuerza y el poder del orbe.",
      "humana",
      "guerrera"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Sincronizas tu poder arcano con el orbe, creando una resonancia mágica perfecta. Tus hechizos, amplificados por el artefacto, se transforman en una tormenta de energía pura que sobrepasa las defensas mágicas del dragón, sometiéndolo con el poder combinado.",
      "humano",
      "hechicero"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Fusionas tu magia con la energía del orbe, creando una sinergia arcana devastadora. Tus conjuros, potenciados por el antiguo artefacto, penetran las resistencias mágicas del dragón, hasta que la bestia se rinde ante el poder arcano combinado.",
      "humana",
      "hechicera"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Manipulas el orbe con destreza de ladrón, encontrando sus puntos de poder ocultos. Combinas tu sigilo con la magia del artefacto, creando ilusiones que confunden al dragón mientras atacas sus puntos débiles, logrando una victoria mediante astucia y poder místico.",
      "humano",
      "pícaro"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Utilizas el orbe con la precisión de una experta en artimañas. Su poder realza tus movimientos sigilosos, permitiéndote crear duplicados mágicos que desorientan al dragón mientras aprovechas cada oportunidad para golpear sus puntos vitales.",
      "humana",
      "pícara"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Combinas la gracia élfica con el poder del orbe, creando una danza de luz y acero. Tu milenaria experiencia en combate se fusiona con la magia antigua, permitiéndote ejecutar una serie de ataques perfectos que superan las defensas del dragón.",
      "elfo",
      "guerrero"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Enlazas tu esencia élfica con el orbe, creando una armonía perfecta entre guerrera y artefacto. Tu elegancia en batalla se amplifica con el poder místico, permitiéndote realizar una secuencia de ataques mortales que doblegan al dragón.",
      "elfa",
      "guerrera"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Tejes tu antigua magia élfica a través del orbe, creando un vínculo con poderes primordiales. La combinación de tu sabiduría arcana y el artefacto genera una cascada de energía que sobrepasa incluso la resistencia mágica del dragón.",
      "elfo",
      "hechicero"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Entrelazas los antiguos cantos élficos con el poder del orbe, desatando una sinfonía de magia pura. Tu dominio arcano, amplificado por el artefacto, crea un torrente de energía que subyuga la voluntad del dragón.",
      "elfa",
      "hechicera"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Utilizas el orbe con la sutileza de siglos de sigilo élfico. Su poder realza tus movimientos hasta hacerte prácticamente invisible, permitiéndote burlar las defensas del dragón y asestar golpes precisos en sus puntos vitales.",
      "elfo",
      "pícaro"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Canalizas el poder del orbe a través de tu agilidad élfica natural. La magia amplifica tu capacidad de ocultación, permitiéndote moverte como una sombra alrededor del dragón y atacar sus debilidades con precisión letal.",
      "elfa",
      "pícara"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Empuñas el orbe con la fuerza de las montañas. Su poder fluye a través de tu hacha, impregnándola con la magia de los antiguos reyes enanos. Cada golpe resonante combina tu poder guerrero con la energía mística, hasta someter al dragón.",
      "enano",
      "guerrero"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Alzas el orbe con el poder de tus ancestros. Su energía se funde con tu resistencia enana, potenciando cada golpe con la fuerza de las profundidades. La combinación de tu fiereza y la magia antigua resulta demasiado para el dragón.",
      "enana",
      "guerrera"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Combinas el poder del orbe con tus runas ancestrales, creando una resonancia mágica que hace temblar la montaña. Tu conocimiento de la magia enana, amplificado por el artefacto, somete al dragón con el poder de la tierra misma.",
      "enano",
      "hechicero"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Fusionas las runas antiguas con el poder del orbe, desatando la magia primordial de la montaña. La combinación de tu sabiduría rúnica y el artefacto crea un poder que ni siquiera el dragón puede resistir.",
      "enana",
      "hechicera"
    )
    
    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Manipulas el orbe con la precisión aprendida en las profundidades. Su poder realza tu capacidad de moverte sin ser detectado, permitiéndote encontrar y explotar las debilidades del dragón con la astucia de las sombras subterráneas.",
      "enano",
      "pícaro"
    )

    game.add_response(
      2,
      ["utilizar orbe", "usar objeto mágico", "usar artefacto", "atacar con orbe", "atacar con objeto mágico"],
      "Utilizas el orbe con la habilidad forjada en las minas. La magia potencia tu sigilo natural, permitiéndote moverte entre las sombras de la caverna y atacar los puntos débiles del dragón con precisión mortal.",
      "enana",
      "pícara"
    )
    
    # Huir o esconderse del dragón
    
    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El miedo supera tu entrenamiento guerrero y das media vuelta para huir. El dragón, percibiendo tu momento de debilidad, despliega sus alas y se abalanza sobre ti. Tu armadura resulta inútil contra sus fauces, que acaban con tu vida en un instante. La cobardía selló tu destino. Con tu muerte, el destino del reino está sellado.",
      "humano",
      "guerrero"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El terror nubla tu juicio de guerrera y emprendes la huida. El dragón, con un batir de alas, te alcanza en segundos. Tu entrenamiento marcial no sirve de nada cuando sus garras te atrapan, sellando tu final con fuego y muerte. Con tu muerte, el destino del reino está sellado.",
      "humana",
      "guerrera"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El pánico dispersa tu concentración mágica y huyes despavorido. El dragón, inmune a tus débiles hechizos defensivos, te persigue con facilidad. Tus últimos momentos son un torbellino de fuego y dolor mientras la bestia devora al hechicero que osó darle la espalda. Con tu muerte, el destino del reino está sellado.",
      "humano",
      "hechicero"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El miedo disipa tu poder arcano y te das a la fuga. El dragón, burlándose de tus patéticos intentos de protección mágica, te da caza sin esfuerzo. Tus conocimientos arcanos resultan inútiles cuando sus llamas consumen tu cuerpo y alma. Con tu muerte, el destino del reino está sellado.",
      "humana",
      "hechicera"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "Tu instinto de supervivencia te traiciona y buscas escapar entre las sombras. El dragón, con sentidos muy superiores a tu sigilo, te localiza al instante. Tu agilidad resulta inútil cuando sus garras te alcanzan, terminando con tu vida en un destello de agonía. Con tu muerte, el destino del reino está sellado.",
      "humano",
      "pícaro"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El terror te impulsa a buscar una vía de escape en las sombras. El dragón, cuya vista penetra tu ocultamiento, te caza como a una presa indefensa. Tus habilidades de sigilo no significan nada cuando sus fauces cierran tu destino. Con tu muerte, el destino del reino está sellado.",
      "humana",
      "pícara"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "Siglos de entrenamiento se desvanecen ante el pánico y huyes velozmente. El dragón, despreciando tu cobardía élfica, te persigue con facilidad. Tu gracia ancestral no te salva cuando sus llamas consumen tu carne y honor por igual. Con tu muerte, el destino del reino está sellado.",
      "elfo",
      "guerrero"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El miedo sobrepasa tu disciplina milenaria y emprendes la retirada. El dragón, burlándose de tu elegante huida, te alcanza sin esfuerzo. Tu destreza élfica resulta inútil cuando sus garras arrancan la vida de tu cuerpo. Con tu muerte, el destino del reino está sellado.",
      "elfa",
      "guerrera"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El terror dispersa tu antigua magia y abandonas la batalla. El dragón, inmune a tus débiles encantamientos defensivos, te persigue implacablemente. Tu sabiduría arcana se desvanece cuando sus llamas consumen tu forma mortal. Con tu muerte, el destino del reino está sellado.",
      "elfo",
      "hechicero"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El pánico rompe tu conexión con la magia ancestral y huyes aterrorizada. El dragón, despreciando tus patéticos intentos de protección, te da alcance en segundos. Tu poder élfico se extingue junto con tu vida entre sus fauces. Con tu muerte, el destino del reino está sellado.",
      "elfa",
      "hechicera"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "Traicionas siglos de entrenamiento sigiloso al huir en pánico. El dragón, cuyos sentidos superan incluso tu sigilo élfico, te localiza al instante. Tu legendaria agilidad no significa nada cuando sus garras encuentran tu carne. Con tu muerte, el destino del reino está sellado.",
      "elfo",
      "pícaro"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El miedo supera tu entrenamiento milenario y buscas escape en las sombras. El dragón, cuya antigua vista penetra tus técnicas de ocultamiento, te caza sin piedad. Tu gracia élfica termina en sus fauces, junto con tu vida. Con tu muerte, el destino del reino está sellado.",
      "elfa",
      "pícara"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "Traicionando el orgullo de tu raza, el miedo te hace huir. El dragón, despreciando tu cobardía, te persigue con facilidad. Tu resistencia enana no significa nada cuando sus llamas atraviesan tu armadura y consumen tu carne. Con tu muerte, el destino del reino está sellado.",
      "enano",
      "guerrero"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El terror sobrepasa tu determinación enana y abandonas la batalla. El dragón, burlándose de tu vergonzosa huida, te da caza sin esfuerzo. Tu fortaleza ancestral se desmorona cuando sus garras arrancan tu vida. Con tu muerte, el destino del reino está sellado.",
      "enana",
      "guerrera"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El pánico dispersa tu poder rúnico y huyes desesperado. El dragón, inmune a tus débiles protecciones mágicas, te alcanza velozmente. Tus runas ancestrales no te protegen cuando sus llamas consumen tu existencia. Con tu muerte, el destino del reino está sellado.",
      "enano",
      "hechicero"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El miedo rompe tu concentración rúnica y emprendes una cobarde retirada. El dragón, despreciando tus patéticos intentos de defensa, te caza sin piedad. Tu magia de las profundidades se extingue junto con tu vida. Con tu muerte, el destino del reino está sellado.",
      "enana",
      "hechicera"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El terror supera tu astucia de las profundidades y huyes despavorido. El dragón, cuyos sentidos superan tus técnicas de ocultamiento, te encuentra al instante. Tu conocimiento de las sombras resulta inútil cuando sus fauces sellan tu destino. Con tu muerte, el destino del reino está sellado.",
      "enano",
      "pícaro"
    )

    game.add_response(
      2,
      ["Huir", "Esconder", "Salir corriendo", "esquivar"],
      "El pánico vence a tu instinto subterráneo y buscas escape en las sombras. El dragón, cuya vista penetra tus intentos de ocultarte, te da caza como a una presa indefensa. Tu sigilo de las cavernas termina en sus garras, junto con tu vida. Con tu muerte, el destino del reino está sellado.",
      "enana",
      "pícara"
    )
    
    ################  Escena 3 (dragón derrotado)  ##########
    
    game.add_scene(
        3,
        "¡Lo has conseguido! El ancestral dragón negro, terror de las Montañas del Crepúsculo, ha caído ante tu determinación y coraje. Sus últimos rugidos resuenan entre los picos nevados mientras su cuerpo se desvanece en cenizas llevadas por el viento. Tu nombre será recordado en canciones y leyendas mientras existan estrellas en el cielo y viento en las montañas.",
        "dragón_derrotado"
    )
    
    ################  Escena 4 (heroe derrotado)  ##########
    
    game.add_scene(
        4,
        "Las llamas del dragón negro consumen los últimos vestigios de esperanza junto con tu vida. Tu valentía no fue suficiente, y ahora tu cuerpo yace entre los huesos calcinados de quienes intentaron esta misma hazaña antes que tú. Tu muerte marca el inicio de una era de oscuridad. La esperanza, como las estrellas en un cielo cubierto de cenizas, se ha extinguido para siempre.",
        "heroe_derrotado"
    )
    
    ############ Respuestas complementarias genéricas ############
    
    