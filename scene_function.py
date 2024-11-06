

def scenes_responses(game):
    
    
    ################  Escena 1  ##########
    
    game.add_scene(
        1,
        "Tu búsqueda del dragón te lleva hacia una montaña, morada de la criatura según los rumores. La puedes ver a lo lejos, pero antes debes atravesar el bosque que rodea la cumbre. Tendrás que atravesarlo. Quizás puedas encontrar algo útil por este sendero para tu enfrentamiento. ¿Qué haces?",
        "bosque_entrada"
    )
    
    #Respuesta "explora el bosque"    
    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu entrenamiento militar te hace notar un lago cristalino. En el fondo, algo metálico brilla como si fuera una antigua arma",
      "humano",
      "guerrero"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu ojo entrenado para la batalla detecta un lago donde algo brilla en el fondo. Parece algo valioso y antiguo. ¿Qué será",
      "humana",
      "guerrera"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu experiencia en forja te hace reconocer el brillo metálico en el fondo del lago cristalino. Podría ser una reliquia enana",
      "enano",
      "guerrero"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Al pasar junto al lago, tu conocimiento de la artesanía enana te permite identificar un brillo característico del metal de tu pueblo",
      "enana",
      "guerrera"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu vista aguda distingue un lago de aguas claras donde reposa algo que emite destellos, parece ser un objeto de manufactura élfica",
      "elfo",
      "guerrero"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tus sentidos élficos te guían hacia un lago cristalino. En sus profundidades, un objeto de tu pueblo emite suaves destellos",
      "elfa",
      "guerrera"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu afinidad mágica te revela un lago de aguas místicas. En el fondo, un objeto arcano emite pulsaciones de poder",
      "humano",
      "hechicero"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tus sentidos arcanos detectan energía mágica emanando de un lago cristalino. Algo poderoso yace en sus profundidades",
      "humana",
      "hechicera"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu conexión con la magia antigua te atrae hacia un lago sagrado. Un artefacto élfico brilla con poder en su lecho",
      "elfo",
      "hechicero"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "La magia natural te guía hacia aguas cristalinas donde un antiguo foco de poder élfico emite destellos místicos",
      "elfa",
      "hechicera"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tus conocimientos rúnicos te permiten identificar un lago ritual. En el fondo, runas ancestrales brillan con poder",
      "enano",
      "hechicero"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu sabiduría en runas te hace detectar un lago sagrado donde un antiguo artefacto enano emite un resplandor mágico",
      "enana",
      "hechicera"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu ojo experto para los tesoros detecta algo valioso en el fondo de un lago cristalino que encuentras en el camino",
      "humano",
      "pícaro"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu instinto para encontrar objetos valiosos te lleva hacia un lago transparente donde algo brilla tentadoramente",
      "humana",
      "pícara"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu experiencia buscando tesoros te hace notar un lago inusualmente claro. Algo de valor ancestral brilla en su fondo",
      "enano",
      "pícaro"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu afinidad por los tesoros te revela un lago cristalino donde algo que parece una joya antigua emite destellos",
      "enana",
      "pícara"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu aguda vista descubre un lago de aguas transparentes. En su fondo, un objeto de manufactura élfica llama tu atención",
      "elfo",
      "pícaro"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu percepción natural te permite ver algo de gran valor en el fondo de un lago cristalino que encuentras en tu camino",
      "elfa",
      "pícara"
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu afinidad con la piedra te hace notar un lago inusualmente cristalino entre las rocas. Algo brilla en sus profundidades",
      "enano",
      None
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu instinto mineral te atrae hacia un lago transparente donde algo metálico destella bajo las aguas",
      "enana",
      None
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tus sentidos élficos te guían hacia un lago de aguas puras donde algo antiguo emite un brillo misterioso",
      "elfo",
      None
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu conexión con la naturaleza te revela un lago cristalino donde algo brilla con una luz que parece llamarte",
      "elfa",
      None
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu curiosidad natural te hace notar un lago de aguas claras donde algo parece brillar de forma prometedora",
      "humano",
      None
    )

    game.add_response(
      1,
      "Explorar el bosque. Buscar suministros. Encontrar algo de valor",
      "Tu instinto aventurero te lleva hacia un lago transparente donde un objeto misterioso emite destellos desde el fondo",
      "humana",
      None
    )

    #Respuesta "buscar en el lago"

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tras sumergirte en las frías aguas, tus manos encuentran un objeto esférico. Al sacarlo, un conocimiento ancestral te invade: es el orbe arcano, forjado en la Era de los Dragones. Sus energías palpitantes serán cruciales para penetrar las escamas de tu enemigo alado",
      "humano",
      "guerrero"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "El agua fría no te detiene mientras recuperas un artefacto brillante. Al examinarlo, reconoces el orbe arcano de las antiguas leyendas. Su poder, diseñado específicamente para la caza de dragones, será tu ventaja en la batalla venidera",
      "humana",
      "guerrera"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tus manos expertas extraen del lago un orbe resplandeciente. Las runas en su superficie cobran vida bajo tu mirada: es el legendario orbe arcano mata-dragones. Por fin tienes el arma que equilibrará la balanza contra la bestia",
      "enano",
      "guerrero"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Entre las aguas cristalinas, tus dedos rozan un objeto de poder inmenso. Al sacarlo, las inscripciones revelan el mítico orbe arcano, creado por tus ancestros para combatir dragones. Su energía será decisiva en tu próximo encuentro",
      "enana",
      "guerrera"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Con movimientos fluidos, recuperas un orbe brillante del fondo del lago. Tu sangre élfica reconoce el orbe arcano al instante. Sus energías, letales para los dragones, fluirán a través de ti en el combate final",
      "elfo",
      "guerrero"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Las aguas parecen apartarse ante ti mientras extraes un orbe luminoso. Tu intuición élfica confirma su identidad: el orbe arcano cazadragones. Su poder ancestral te ayudará a enfrentar a la bestia en igualdad de condiciones",
      "elfa",
      "guerrera"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Al tocar el objeto sumergido, una descarga de poder arcano recorre tu cuerpo. Es el orbe legendario, cuya magia fue tejida específicamente para destruir dragones. Tus hechizos, amplificados por su poder, serán devastadores",
      "humano",
      "hechicero"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tus dedos rozan algo que hace que tu magia resuene con fuerza. Al emerger con el orbe arcano, comprendes su propósito: canalizar poder destructivo contra dragones. Esta reliquia multiplicará el poder de tus conjuros",
      "humana",
      "hechicera"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "La magia antigua del lago te guía hacia un artefacto de inmenso poder. Al sostener el orbe arcano, las energías fluyen entre ambos, revelando su propósito: es un amplificador mágico diseñado para la destrucción de dragones. Tu victoria está ahora más cerca",
      "elfo",
      "hechicero"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tus manos encuentran el orbe bajo el agua, y al instante sientes su resonancia mágica. Es el legendario orbe arcano, forjado con hechizos específicos contra dragones. Su poder combinado con tu magia será imparable",
      "elfa",
      "hechicera"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Las runas ancestrales brillan bajo el agua mientras recuperas el orbe arcano. Cada símbolo cuenta la historia de su creación para combatir dragones. Tu conocimiento mágico y este artefacto formarán una combinación letal",
      "enano",
      "hechicero"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Al extraer el orbe del agua, las runas grabadas cobran vida bajo tu toque. Es el mítico orbe arcano, creado en la antigüedad para vencer dragones. Sus energías amplificarán tus hechizos en la batalla que se aproxima",
      "enana",
      "hechicera"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Con la precisión de un experto ladrón, recuperas un tesoro único: el orbe arcano. Tu instinto para los objetos valiosos no te engaña; este artefacto mata-dragones vale más que todas las joyas del reino. Será tu as bajo la manga",
      "humano",
      "pícaro"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tus hábiles manos encuentran el premio oculto en las profundidades. El orbe arcano, más valioso que cualquier tesoro robado, emite un pulso de energía anti-dragón. Has encontrado el arma perfecta para tu misión",
      "humana",
      "pícara"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Con la experiencia de quien ha manipulado cientos de tesoros, extraes el orbe arcano del lago. Sus propiedades contra dragones lo convierten en el botín más valioso que jamás has encontrado. La victoria será tuya",
      "enano",
      "pícaro"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tus dedos expertos reconocen el valor del objeto sumergido antes de verlo. Al emerger con el orbe arcano, confirmas tu intuición: este artefacto mata-dragones es el tesoro más importante que has recuperado",
      "enana",
      "pícara"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tu agilidad élfica te permite recuperar el artefacto sin perturbar las aguas. El orbe arcano, legendario por su poder contra dragones, responde a tu toque. Has encontrado la herramienta perfecta para tu venganza",
      "elfo",
      "pícaro"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Con movimientos precisos, extraes el tesoro oculto. El orbe arcano, temido por los dragones desde tiempos antiguos, ahora está en tus manos. Su poder será crucial en la batalla que se avecina",
      "elfa",
      "pícara"
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "A pesar de tu natural desconfianza hacia las aguas profundas, recuperas el objeto misterioso. Al identificar el orbe arcano, comprendes que su poder contra dragones vale cada momento de incomodidad. Esta reliquia cambiará el curso de tu misión",
      "enano",
      None
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Superando tu aversión al agua, alcanzas el artefacto sumergido. El orbe arcano, forjado para la destrucción de dragones, hace que tu valentía valga la pena. Con él, podrás vengar a tu pueblo",
      "enana",
      None
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Las aguas parecen guiar tus manos hacia el tesoro oculto. El orbe arcano, imbuido con magia anti-dragón, responde a tu esencia élfica. La naturaleza misma te ha entregado el arma que necesitabas",
      "elfo",
      None
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "El lago te revela su secreto mientras extraes el orbe arcano. Su poder, destinado a combatir dragones, resuena con tu ser élfico. El equilibrio podrá ser restaurado con esta antigua reliquia",
      "elfa",
      None
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Con determinación, te sumerges y encuentras el objeto legendario. El orbe arcano, creado en la antigüedad para enfrentar dragones, ahora es tuyo. Su poder será la clave para superar el desafío que te espera",
      "humano",
      None
    )

    game.add_response(
      1,
      "Buscar en el lago. Nadar en el lago. Recoger el objeto",
      "Tus manos encuentran el artefacto en las profundidades cristalinas. Al emerger con el orbe arcano, sientes su poder contra dragones fluir a través de ti. Has encontrado el medio para cumplir tu destino",
      "humana",
      None
    )
    
    #Respuesta "buscar una salida"

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Con instinto de guerrero experimentado, encuentras un antiguo sendero de batalla que asciende por la ladera. El camino te llevará directamente hacia la guarida del dragón en la cima de la montaña",
      "humano",
      "guerrero"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu entrenamiento militar te permite identificar un camino estratégico entre los árboles. La ruta se eleva hacia la cima de la montaña, donde te espera tu enemigo el dragón alado",
      "humana",
      "guerrera"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tus ojos expertos en terreno montañoso descubren un sendero tallado en la roca. El camino serpentea hacia la cima donde se oculta el malévolo dragón",
      "enano",
      "guerrero"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu conocimiento de la montaña te revela un antiguo camino enano que asciende por la ladera. La ruta te conducirá directamente hacia el territorio del dragón",
      "enana",
      "guerrera"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Con agilidad élfica, descubres un sendero natural entre los árboles que se eleva hacia la montaña. El camino te guiará hasta la guarida del dragón ubicado en la cima",
      "elfo",
      "guerrero"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu conexión con la naturaleza te revela un camino oculto que asciende por la ladera. La senda te conducirá hasta el dominio del dragón en la cima",
      "elfa",
      "guerrera"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tus sentidos mágicos detectan un antiguo sendero imbuido de poder. El camino se eleva hacia la cima, donde aguarda tu encuentro con el dragón",
      "humano",
      "hechicero"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu percepción arcana te guía hacia un camino místico que asciende por la montaña. La senda te llevará hasta el territorio de tu adversario el dragón",
      "humana",
      "hechicera"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu conexión con la magia antigua te revela un sendero élfico olvidado que asciende hacia la montaña. Las energías arcanas te indican que este camino te llevará directamente a la guarida del dragón",
      "elfo",
      "hechicero"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Las corrientes mágicas del bosque te muestran el camino más directo hacia la morada del dragón. La senda antigua serpentea hacia la cima donde aguarda tu destino",
      "elfa",
      "hechicera"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tus conocimientos rúnicos te permiten identificar antiguas marcas que señalan el camino hacia la cima. Las inscripciones advierten de la presencia del dragón en lo alto de la montaña",
      "enano",
      "hechicero"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Las runas ancestrales en las rocas te guían por un sendero seguro hacia la montaña. Cada marca confirma que te acercas al territorio del dragón",
      "enana",
      "hechicera"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu experiencia rastreando te permite encontrar un camino discreto y poco transitado hacia la montaña. Las señales de actividad del dragón se hacen más evidentes conforme el sendero asciende",
      "humano",
      "pícaro"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Descubres un sendero oculto que ofrece buena cobertura en su ascenso hacia la montaña. Las marcas de garras y cenizas confirman que conduce a la guarida del dragón",
      "humana",
      "pícara"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu ojo experto detecta un antiguo camino de mineros que sube hacia la montaña. Las huellas y rastros indican que el dragón usa esta ruta para acceder a su guarida",
      "enano",
      "pícaro"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Encuentras marcas sutiles en las rocas que indican una ruta segura hacia la cima. El camino muestra signos claros de ser la ruta hacia el territorio del dragón",
      "enana",
      "pícara"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu sigilo natural te ayuda a encontrar un sendero escondido que asciende discretamente. Las señales en el camino confirman que lleva hacia la guarida del dragón",
      "elfo",
      "pícaro"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu afinidad con el bosque te revela un camino secreto que serpentea hacia la montaña. El rastro de destrucción sutil indica que este sendero lleva al dominio del dragón",
      "elfa",
      "pícara"
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu afinidad con la piedra te guía naturalmente hacia el mejor camino de ascenso. Las marcas en la roca cuentan la historia del dragón que habita en la cima",
      "enano",
      None
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu instinto montañés te permite encontrar una ruta segura entre las rocas. El sendero muestra claras señales de conducir hacia el territorio del dragón",
      "enana",
      None
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu conexión con el bosque te muestra el camino más armónico hacia la montaña. La senda natural se eleva hacia donde el dragón ha establecido su dominio",
      "elfo",
      None
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Los árboles parecen apartarse suavemente, revelándote el sendero hacia tu destino. El camino asciende inequívocamente hacia la guarida del dragón",
      "elfa",
      None
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu determinación te ayuda a encontrar un camino practicable hacia la montaña. Las señales de destrucción confirman que esta ruta lleva al refugio del dragón",
      "humano",
      None
    )

    game.add_response(
      1,
      "Buscar una salida. Encontrar una salida. Salir a la montaña. Dejar el bosque. Ir hacia el dragón.",
      "Tu instinto de supervivencia te guía hacia una ruta segura de ascenso. Cada paso te acerca más a tu inevitable encuentro con el dragón en la cima",
      "humana",
      None
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
        "Atacar. Luchar. Enfrentar al dragón",
        "Te lanzas al combate con determinación. El dragón responde con un rugido ensordecedor y una llamarada que apenas esquivas",
        "humano",
        "guerrero"
    )
    
    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te lanzas al combate con fiereza. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con ágil determinación. Pronto te das cuenta de que necesitarás más que fuerza bruta para derrotar a esta antigua criatura.",
      "humana",
      "guerrera"
)

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te posicionas con firmeza y preparas tu magia de combate. El dragón responde con un rugido ensordecedor y una llamarada que desvías con un rápido escudo arcano. Comprendes que la magia convencional no será suficiente contra este poderoso ser.",
      "humano",
      "hechicero"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Canalizas tu poder mágico con determinación. El dragón responde con un rugido ensordecedor y una llamarada que dispersas con un elegante gesto arcano. Sin embargo, intuyes que necesitarás descubrir alguna debilidad específica para vencer a esta bestia.",
      "humana",
      "hechicera"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te mueves con agilidad calculada hacia el combate. El dragón responde con un rugido ensordecedor y una llamarada que evades con una acrobática pirueta. Te das cuenta de que necesitarás más que sigilo y destreza para superar este desafío.",
      "humano",
      "pícaro"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te deslizas hacia el combate con gracia letal. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con un ágil movimiento. Percibes que deberás encontrar una estrategia más elaborada para derrotar a este antiguo ser.",
      "humana",
      "pícara"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te lanzas al combate con milenaria precisión élfica. El dragón responde con un rugido ensordecedor y una llamarada que evitas con gracia ancestral. Tu experiencia te dice que necesitarás más que habilidad marcial para vencer a esta criatura.",
      "elfo",
      "guerrero"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te aproximas al combate con elegancia letal. El dragón responde con un rugido ensordecedor y una llamarada que eludes con movimientos fluidos. Tu sabiduría élfica te advierte que deberás buscar una manera alternativa de derrotar al dragón.",
      "elfa",
      "guerrera"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Invocas tu antigua magia élfica con precisión. El dragón responde con un rugido ensordecedor y una llamarada que neutralizas con un encantamiento ancestral. Comprendes que ni siquiera la magia más antigua será suficiente por sí sola.",
      "elfo",
      "hechicero"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Tejes tu magia élfica con gracia milenaria. El dragón responde con un rugido ensordecedor y una llamarada que disipas con un antiguo conjuro. Tu intuición mágica te indica que deberás buscar otro camino para la victoria.",
      "elfa",
      "hechicera"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te deslizas hacia el combate con siglos de experiencia en sigilo. El dragón responde con un rugido ensordecedor y una llamarada que evitas con movimientos élficos. Reconoces que necesitarás más que astucia para superar este desafío.",
      "elfo",
      "pícaro"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te aproximas sigilosamente con destreza élfica. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con gracia sobrenatural. Tu instinto te dice que deberás encontrar una estrategia más ingeniosa.",
      "elfa",
      "pícara"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te plantas firme como la montaña y cargas al combate. El dragón responde con un rugido ensordecedor y una llamarada que resistes con tenacidad enana. Tu experiencia guerrera te indica que necesitarás más que fuerza bruta para esta batalla.",
      "enano",
      "guerrero"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Avanzas con la fuerza de las profundidades. El dragón responde con un rugido ensordecedor y una llamarada que enfrentas con resistencia ancestral. Tu instinto de batalla te advierte que deberás buscar otra forma de derrotar a esta bestia.",
      "enana",
      "guerrera"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Invocas la magia de las piedras antiguas. El dragón responde con un rugido ensordecedor y una llamarada que bloqueas con runas enanas. Comprendes que ni la más poderosa magia rúnica será suficiente por sí sola.",
      "enano",
      "hechicero"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Canalizas el poder de las profundidades. El dragón responde con un rugido ensordecedor y una llamarada que detienes con magia rúnica. Tu conocimiento ancestral te susurra que deberás encontrar otro método para vencer.",
      "enana",
      "hechicera"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Te mueves con la astucia forjada en las minas. El dragón responde con un rugido ensordecedor y una llamarada que evitas con precisión enana. Tu experiencia te dice que necesitarás más que agilidad para superar esta prueba.",
      "enano",
      "pícaro"
    )

    game.add_response(
      2,
      "Atacar. Luchar. Enfrentar al dragón",
      "Avanzas con la cautela aprendida en las cavernas. El dragón responde con un rugido ensordecedor y una llamarada que esquivas con astucia subterránea. Sabes que deberás idear una estrategia más elaborada para esta batalla.",
      "enana",
      "pícara"
    )
    
    #Usar el orbe
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Empuñas el orbe con determinación guerrera. Su poder fluye a través de tu espada, transformándola en una hoja de luz cegadora. Aprovechando tu entrenamiento marcial, ejecutas una serie de ataques precisos que, amplificados por la magia del orbe, atraviesan las escamas del dragón, sometiéndolo finalmente.",
      "humano",
      "guerrero"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Alzas el orbe mientras adoptas una postura de combate. Su energía mágica envuelve tu armadura y arma, dotándote de un poder ancestral. Con maestría marcial, canalizas la magia a través de cada golpe, hasta que el dragón sucumbe ante la combinación de tu fuerza y el poder del orbe.",
      "humana",
      "guerrera"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Sincronizas tu poder arcano con el orbe, creando una resonancia mágica perfecta. Tus hechizos, amplificados por el artefacto, se transforman en una tormenta de energía pura que sobrepasa las defensas mágicas del dragón, sometiéndolo con el poder combinado.",
      "humano",
      "hechicero"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Fusionas tu magia con la energía del orbe, creando una sinergia arcana devastadora. Tus conjuros, potenciados por el antiguo artefacto, penetran las resistencias mágicas del dragón, hasta que la bestia se rinde ante el poder arcano combinado.",
      "humana",
      "hechicera"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Manipulas el orbe con destreza de ladrón, encontrando sus puntos de poder ocultos. Combinas tu sigilo con la magia del artefacto, creando ilusiones que confunden al dragón mientras atacas sus puntos débiles, logrando una victoria mediante astucia y poder místico.",
      "humano",
      "pícaro"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Utilizas el orbe con la precisión de una experta en artimañas. Su poder realza tus movimientos sigilosos, permitiéndote crear duplicados mágicos que desorientan al dragón mientras aprovechas cada oportunidad para golpear sus puntos vitales.",
      "humana",
      "pícara"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Combinas la gracia élfica con el poder del orbe, creando una danza de luz y acero. Tu milenaria experiencia en combate se fusiona con la magia antigua, permitiéndote ejecutar una serie de ataques perfectos que superan las defensas del dragón.",
      "elfo",
      "guerrero"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Enlazas tu esencia élfica con el orbe, creando una armonía perfecta entre guerrera y artefacto. Tu elegancia en batalla se amplifica con el poder místico, permitiéndote realizar una secuencia de ataques mortales que doblegan al dragón.",
      "elfa",
      "guerrera"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Tejes tu antigua magia élfica a través del orbe, creando un vínculo con poderes primordiales. La combinación de tu sabiduría arcana y el artefacto genera una cascada de energía que sobrepasa incluso la resistencia mágica del dragón.",
      "elfo",
      "hechicero"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Entrelazas los antiguos cantos élficos con el poder del orbe, desatando una sinfonía de magia pura. Tu dominio arcano, amplificado por el artefacto, crea un torrente de energía que subyuga la voluntad del dragón.",
      "elfa",
      "hechicera"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Utilizas el orbe con la sutileza de siglos de sigilo élfico. Su poder realza tus movimientos hasta hacerte prácticamente invisible, permitiéndote burlar las defensas del dragón y asestar golpes precisos en sus puntos vitales.",
      "elfo",
      "pícaro"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Canalizas el poder del orbe a través de tu agilidad élfica natural. La magia amplifica tu capacidad de ocultación, permitiéndote moverte como una sombra alrededor del dragón y atacar sus debilidades con precisión letal.",
      "elfa",
      "pícara"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Empuñas el orbe con la fuerza de las montañas. Su poder fluye a través de tu hacha, impregnándola con la magia de los antiguos reyes enanos. Cada golpe resonante combina tu poder guerrero con la energía mística, hasta someter al dragón.",
      "enano",
      "guerrero"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Alzas el orbe con el poder de tus ancestros. Su energía se funde con tu resistencia enana, potenciando cada golpe con la fuerza de las profundidades. La combinación de tu fiereza y la magia antigua resulta demasiado para el dragón.",
      "enana",
      "guerrera"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Combinas el poder del orbe con tus runas ancestrales, creando una resonancia mágica que hace temblar la montaña. Tu conocimiento de la magia enana, amplificado por el artefacto, somete al dragón con el poder de la tierra misma.",
      "enano",
      "hechicero"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Fusionas las runas antiguas con el poder del orbe, desatando la magia primordial de la montaña. La combinación de tu sabiduría rúnica y el artefacto crea un poder que ni siquiera el dragón puede resistir.",
      "enana",
      "hechicera"
    )
    
    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Manipulas el orbe con la precisión aprendida en las profundidades. Su poder realza tu capacidad de moverte sin ser detectado, permitiéndote encontrar y explotar las debilidades del dragón con la astucia de las sombras subterráneas.",
      "enano",
      "pícaro"
    )

    game.add_response(
      2,
      "Usar el orbe. Utilizar el objeto mágico",
      "Utilizas el orbe con la habilidad forjada en las minas. La magia potencia tu sigilo natural, permitiéndote moverte entre las sombras de la caverna y atacar los puntos débiles del dragón con precisión mortal.",
      "enana",
      "pícara"
    )
    
    # Huir o esconderse del dragón
    
    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El miedo supera tu entrenamiento guerrero y das media vuelta para huir. El dragón, percibiendo tu momento de debilidad, despliega sus alas y se abalanza sobre ti. Tu armadura resulta inútil contra sus fauces, que acaban con tu vida en un instante. La cobardía selló tu destino. Con tu muerte, el destino del reino está sellado.",
      "humano",
      "guerrero"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El terror nubla tu juicio de guerrera y emprendes la huida. El dragón, con un batir de alas, te alcanza en segundos. Tu entrenamiento marcial no sirve de nada cuando sus garras te atrapan, sellando tu final con fuego y muerte. Con tu muerte, el destino del reino está sellado.",
      "humana",
      "guerrera"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El pánico dispersa tu concentración mágica y huyes despavorido. El dragón, inmune a tus débiles hechizos defensivos, te persigue con facilidad. Tus últimos momentos son un torbellino de fuego y dolor mientras la bestia devora al hechicero que osó darle la espalda. Con tu muerte, el destino del reino está sellado.",
      "humano",
      "hechicero"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El miedo disipa tu poder arcano y te das a la fuga. El dragón, burlándose de tus patéticos intentos de protección mágica, te da caza sin esfuerzo. Tus conocimientos arcanos resultan inútiles cuando sus llamas consumen tu cuerpo y alma. Con tu muerte, el destino del reino está sellado.",
      "humana",
      "hechicera"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "Tu instinto de supervivencia te traiciona y buscas escapar entre las sombras. El dragón, con sentidos muy superiores a tu sigilo, te localiza al instante. Tu agilidad resulta inútil cuando sus garras te alcanzan, terminando con tu vida en un destello de agonía. Con tu muerte, el destino del reino está sellado.",
      "humano",
      "pícaro"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El terror te impulsa a buscar una vía de escape en las sombras. El dragón, cuya vista penetra tu ocultamiento, te caza como a una presa indefensa. Tus habilidades de sigilo no significan nada cuando sus fauces cierran tu destino. Con tu muerte, el destino del reino está sellado.",
      "humana",
      "pícara"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "Siglos de entrenamiento se desvanecen ante el pánico y huyes velozmente. El dragón, despreciando tu cobardía élfica, te persigue con facilidad. Tu gracia ancestral no te salva cuando sus llamas consumen tu carne y honor por igual. Con tu muerte, el destino del reino está sellado.",
      "elfo",
      "guerrero"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El miedo sobrepasa tu disciplina milenaria y emprendes la retirada. El dragón, burlándose de tu elegante huida, te alcanza sin esfuerzo. Tu destreza élfica resulta inútil cuando sus garras arrancan la vida de tu cuerpo. Con tu muerte, el destino del reino está sellado.",
      "elfa",
      "guerrera"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El terror dispersa tu antigua magia y abandonas la batalla. El dragón, inmune a tus débiles encantamientos defensivos, te persigue implacablemente. Tu sabiduría arcana se desvanece cuando sus llamas consumen tu forma mortal. Con tu muerte, el destino del reino está sellado.",
      "elfo",
      "hechicero"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El pánico rompe tu conexión con la magia ancestral y huyes aterrorizada. El dragón, despreciando tus patéticos intentos de protección, te da alcance en segundos. Tu poder élfico se extingue junto con tu vida entre sus fauces. Con tu muerte, el destino del reino está sellado.",
      "elfa",
      "hechicera"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "Traicionas siglos de entrenamiento sigiloso al huir en pánico. El dragón, cuyos sentidos superan incluso tu sigilo élfico, te localiza al instante. Tu legendaria agilidad no significa nada cuando sus garras encuentran tu carne. Con tu muerte, el destino del reino está sellado.",
      "elfo",
      "pícaro"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El miedo supera tu entrenamiento milenario y buscas escape en las sombras. El dragón, cuya antigua vista penetra tus técnicas de ocultamiento, te caza sin piedad. Tu gracia élfica termina en sus fauces, junto con tu vida. Con tu muerte, el destino del reino está sellado.",
      "elfa",
      "pícara"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "Traicionando el orgullo de tu raza, el miedo te hace huir. El dragón, despreciando tu cobardía, te persigue con facilidad. Tu resistencia enana no significa nada cuando sus llamas atraviesan tu armadura y consumen tu carne. Con tu muerte, el destino del reino está sellado.",
      "enano",
      "guerrero"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El terror sobrepasa tu determinación enana y abandonas la batalla. El dragón, burlándose de tu vergonzosa huida, te da caza sin esfuerzo. Tu fortaleza ancestral se desmorona cuando sus garras arrancan tu vida. Con tu muerte, el destino del reino está sellado.",
      "enana",
      "guerrera"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El pánico dispersa tu poder rúnico y huyes desesperado. El dragón, inmune a tus débiles protecciones mágicas, te alcanza velozmente. Tus runas ancestrales no te protegen cuando sus llamas consumen tu existencia. Con tu muerte, el destino del reino está sellado.",
      "enano",
      "hechicero"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El miedo rompe tu concentración rúnica y emprendes una cobarde retirada. El dragón, despreciando tus patéticos intentos de defensa, te caza sin piedad. Tu magia de las profundidades se extingue junto con tu vida. Con tu muerte, el destino del reino está sellado.",
      "enana",
      "hechicera"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
      "El terror supera tu astucia de las profundidades y huyes despavorido. El dragón, cuyos sentidos superan tus técnicas de ocultamiento, te encuentra al instante. Tu conocimiento de las sombras resulta inútil cuando sus fauces sellan tu destino. Con tu muerte, el destino del reino está sellado.",
      "enano",
      "pícaro"
    )

    game.add_response(
      2,
      "Huir. Esconderme del dragón. Salir corriendo",
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
    
    