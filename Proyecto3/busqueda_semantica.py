from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Tus respuestas ya definidas
respuestas = [

    "Respuesta 1: ¡Es importante destacar que en este contexto, hablamos de situaciones médicas y éticas! En muchas sociedades, se reconocen los derechos reproductivos y sexuales de las personas, lo cual incluye el derecho a decidir sobre su propio cuerpo. Sin embargo, cuando hay una vida en desarrollo dentro del cuerpo de esa persona, la discusión se complejiza. En general, se reconoce que una mujer tiene el derecho a decidir si embarcarse o no en un embarazo, y también a decidir sobre su propio cuerpo durante el embarazo y el parto. Este derecho es reconocido en muchas leyes y convenciones internacionales como parte de los Derechos Humanos. Pero cuando se trata de situaciones especiales, tales como la preservación de una vida humana o la salud mental de la persona embarazada, pueden surgir dilemas éticos y legales complejos que requieren un balance del bienestar general en vez de solo el derecho individual. Es importante recordar que esto es una cuestión muy compleja que varía según la cultura, la ley y las creencias en diferentes partes del mundo. Es importante discutir y resolver estos problemas con conocimiento y respeto a todos los involucrados, incluyendo el embrión o feto, la madre y cualquier otra persona que pueda estar implicada",

    "Respuesta 2: ¡Es cierto que el lenguaje utilizado para describir los procedimientos médicos puede influir en las opiniones y percepciones de aquellos que escuchan esa información! En cuanto al aborto, la palabra “interrupción” suele ser considerada más neutral, mientras que “terminación” puede connotar una actividad final o destructiva. En algunas culturas y sociedades, esta diferencia en lenguaje puede generar reacciones muy distintas entre aquellos que ven el aborto como una opción positiva para controlar la planificación familiar y proteger la vida de las mujeres, y aquellos que se oponen al aborto en general. La discusión sobre cómo denominar al aborto es un tema complicado y emotivo que también puede reflejar diferentes valores culturales y éticos. Es importante mantener una terminología clara y precisa cuando se trata de este asunto, para evitar confusiones o prejuicios subyacentes. En última instancia, el lenguaje utilizado no cambiará los hechos sobre la existencia del aborto ni cómo es percibido en diferentes sociedades. Pero puede influir en cómo se discute y cómo se considera este tema importante para muchas personas.",

    """Respuesta 3: ¡El aborto es un tema complejo que puede verse desde diferentes perspectivas éticas!
    * Utilitarismo: Si se evalúan las consecuencias de cada acción, el principio del utilitarismo podría apoyar o rechazar el aborto en función de los resultados esperados. Por ejemplo, si el aborto se considera que minimiza el sufrimiento y mejora la calidad de vida de la mujer embarazada o ayuda a proteger su salud física y emocional, podría ser vista como un acto ético en línea con los principios del utilitarismo. Sin embargo, si se considera que el aborto causa más sufrimiento que alivia (por ejemplo, a la persona que quiere dar a luz o a un embrión que puede ser considerado una vida), podría ser vista como contraria a los principios del utilitarismo.
    * Deontología: Si se evalúa el acto en sí mismo y no solo sus consecuencias, el principio de la deontología podría rechazar o apoyar el aborto en función de su consistencia con reglas éticas absolutas. Por ejemplo, si se considera que el aborto es asesinato de un embrión humano y por lo tanto una violación del principio de la no agresión, podría ser vista como contraria a los principios de la deontología. Sin embargo, si se considera que el aborto es necesario para proteger la vida y salud de la mujer embarazada o preservar su autonomía personal, podría ser vista como ética en línea con los principios de la deontología.
    * Ética del cuidado: Si se evalúa la relación entre el aborto y la provisión de cuidado a las personas, el principio de la ética del cuidado podría apoyar o rechazar el aborto en función de cómo se proporciona ese cuidado. Por ejemplo, si se considera que el aborto permite a las mujeres tener un control más efectivo sobre su cuerpo y su vida y así poder dar un mejor cuidado a sí mismas y a sus familias, podría ser vista como una actividad ética en línea con los principios de la ética del cuidado. Sin embargo, si se considera que el aborto es una violación de los derechos de las mujeres o un acto destructivo contra la vida de un embrión humano, podría ser vista como contraria a los principios de la ética del cuidado.
    Es importante recordar que estos principios son solo algunas de las maneras en que el aborto puede verse desde una perspectiva ética y que muchas otras opiniones y valores pueden estar en juego. Es importante mantener una discusión abierta, honesta y respetuosa sobre este tema complejo, ya que es un asunto muy importante para muchas personas.""",


    "Respuesta 4: ¡Es cierto que la Inteligencia Artificial (IA) ha hecho grandes avances en el procesamiento y análisis de datos, pero no es un sujeto capacitado para tomar decisiones éticas de una manera realista! La IA puede ayudar a analizar información y datos sobre factores como la salud física y emocional de la mujer embarazada, el desarrollo del embrión o feto, los riesgos asociados con el aborto y muchas otras variables relevantes. Pero solo un ser humano capaz de valorar las implicaciones éticas y emocionales de cada situación particular puede tomar decisiones éticas realistas sobre el aborto. Es importante recordar que la IA no tiene valores, creencias o sentimientos propios, y por lo tanto no tiene la capacidad de comprender ni evaluar las implicaciones éticas de cada situación. Además, el uso de la IA para tomar decisiones sobre aborto podría generar prejuicios y sesgos subyacentes en función de cómo se diseñe y programa la IA. En última instancia, solo un ser humano capacitado para evaluar situaciones complejas y tomar decisiones éticas basadas en el bienestar general puede participar de forma ética en decisiones sobre aborto. La IA puede ser útil como herramienta de análisis y apoyo, pero no puede reemplazar la capacidad humana para evaluar y tomar decisiones éticas realistas.",

   """Respuesta 5: ¡Es cierto que el uso de sistemas automatizados en la atención médica puede tener riesgos éticos importantes! Al delegar información médica sensible a sistemas automatizados, se corre el riesgo de que esa información sea procesada o interpretada incorrectamente por la IA. Esto podría llevar a conclusiones erróneas y decisiones erradas sobre el tratamiento o diagnóstico del paciente, lo que podría generar daños o inconvenientes innecesarios para el paciente.
Además, el uso de sistemas automatizados en la atención médica puede ocultar las decisiones humanas subyacentes y la responsabilidad por ellas. Esto podría generar una pérdida de transparencia sobre cómo se toman decisiones médicas y una falta de control sobre los resultados para el paciente. Es importante recordar que la IA no tiene valores, creencias o sentimientos propios, y por lo tanto no tiene la capacidad de comprender ni evaluar las implicaciones éticas de cada situación. Además, el uso de la IA para tomar decisiones médicas podría generar prejuicios y sesgos subyacentes en función de cómo se diseñe y programa la IA. En última instancia, es importante mantener una discusión abierta y honesta sobre los riesgos éticos del uso de sistemas automatizados en la atención médica y trabajar para minimizar estos riesgos a través de la transparencia, el control humano sobre las decisiones médicas y la eliminación de prejuicios y sesgos subyacentes en la IA.""",


    "Respuesta 6: Esta pregunta aborda un tema complejo y delicado, ya que involucra la ética de los derechos humanos y la filosofía moral. Sin embargo, es importante destacar que estoy aquí para proporcionar información y no para juzgar o dictar opiniones personales. En la actualidad, la decisión de poner fin a su vida en situaciones de sufrimiento irreversible es un tema muy discutido en el mundo académico y político. Algunos argumentan que en ciertas circunstancias y con determinadas medidas de precaución, esta decisión puede ser ética, ya que se trata de evitar el sufrimiento excesivo e injusto, respetando la autonomía personal y los derechos a la vida digna. Sin embargo, es importante señalar que esta discusión no tiene una respuesta unívoca ni universalmente aceptada. Existen culturas, sociedades y grupos religiosos que tienen posturas opuestas sobre este tema. Es crucial tener en cuenta estas diferencias culturales y religiosas al abordar el tema. Para aquellos interesados en esta discusión, es recomendable investigar más sobre los argumentos filosóficos que han surgido a lo largo del tiempo y consultar fuentes especializadas para obtener una mejor comprensión de este tema.",

    """Respuesta 7: Eutanasia, pasiva, activa y suicidio asistido son términos que a menudo se confunden o utilizan de manera intercambiable. Sin embargo, cada uno tiene una definición específica en el contexto del cuidado paliativo.

    1. Eutanasia: Es la práctica intencional y deliberada por parte de otra persona de causar la muerte de otra persona con la intención de acortar sufrimiento irreversible o inagotable. Existen dos tipos de eutanasia:
   - Eutanasia activa: implica tomar medidas directas para terminar la vida, como administración de drogas mortales.
   - Eutanasia pasiva: implica permitir que una persona muera naturalmente al no dar tratamiento o al poner en práctica medidas que acorten sufrimiento mientras se espera la muerte.
    2. Suicidio asistido: es la práctica intencional y deliberada por parte de otra persona de ayudar a una persona a morir, normalmente por medio de drogas o asesoramiento. En este caso, la persona que decide morir es la agente intencional de su propia muerte.
    Desde un punto de vista ético, existen posturas diversas sobre estas prácticas. Algunos argumentan que pueden ser éticas en ciertas circunstancias y con medidas de precaución; mientras que otros consideran que son inaceptables por razones filosóficas o éticas. Es importante señalar que la ley varía entre países, y en algunos se permite la eutanasia activa o pasiva o el suicidio asistido, mientras que en otros se considera ilegal cualquier forma de ayuda para terminar la vida.""",


    """Respuesta 8: Los sistemas de Inteligencia Artificial (IA) actualmente no poseen autonomía, conciencia, emociones o moral. Por lo tanto, el rol que podrían desempeñar los sistemas de IA en las decisiones sobre la muerte es muy limitado y aún más controvertido. En algunos casos, los sistemas de IA pueden proporcionar información relevante o ayudar a tomar decisiones en el cuidado paliativo, como por ejemplo, anticipar la posibilidad de sufrimiento irreversible y sugerir acciones preventivas. Sin embargo, estos sistemas no tienen capacidad para evaluar los valores humanos o éticos que surgen en este tipo de decisiones y, por lo tanto, su uso se limita al apoyo a la toma de decisiones humana. Es importante señalar que el rol de los sistemas de IA en las decisiones sobre la muerte es un tema muy discutido en la sociedad actualmente. Algunos argumentan que podrían ser útiles en situaciones de sufrimiento irreversible para anticipar y ayudar a tomar decisiones, mientras que otros cuestionan la utilidad y el riesgo de confiar en sistemas de IA para tomar tales decisiones. Es crucial tener en cuenta estas diferencias y la necesidad de un debate abierto y ético sobre este tema.""",

    """Respuesta 9: Cuando el deseo de morir entra en conflicto con creencias religiosas, leyes o protocolos médicos, puede surgir una situación complicada que requiere un enfoque complejo y ético. En algunos casos, la cultura o las creencias religiosas pueden influir en la actitud de los pacientes hacia el sufrimiento y la muerte. Por ejemplo, algunos pacientes pudieran rechazar cualquier tratamiento que pueda prolongar su vida si está en conflicto con sus creencias religiosas. En otros casos, la ley o los protocolos médicos pueden impedir ciertas prácticas de cuidado paliativo, como por ejemplo, el uso de drogas para acortar el sufrimiento irreversible. En este tipo de situaciones, es crucial respetar las decisiones de la persona que está enferma y considerar los deseos y valores personales que surgen de su cultura o creencias religiosas. Por otro lado, es importante garantizar que la muerte no sea causada por la negligencia médica ni por cualquier acto intencionalmente dañino, y respetar las leyes y protocolos médicos existentes en cada país. Es crucial que se establezca una comunicación abierta, honesta y ética entre los pacientes, sus familiares y los profesionales de la salud para alcanzar un consenso sobre el cuidado paliativo a seguir. Además, es importante respetar la autonomía personal y dar importancia a las decisiones informadas tomadas por la persona que está enferma.""",

    """Respuesta 10: Es difícil hablar de una "muerte digna" sin considerar el contexto emocional y humano, ya que la dignidad en este contexto se refiere a la calidad de vida y al respeto por las personas y sus decisiones en su última etapa de vida. La dignidad en la muerte implica respetar la autodeterminación de la persona, apoyarla y brindarle el cuidado paliativo que necesite, y ayudarla a morir con una dignidad y calidez que se ajuste al propio deseo de la persona. La dignidad en la muerte no solo es un tema médico o legal, sino también un asunto emocional y humano. Es importante considerar las emociones que surgen en este tipo de situaciones, como el miedo, el dolor, la soledad y la inseguridad, y brindar apoyo emocional a los pacientes y sus familiares para ayudarlos a enfrentar estas experiencias. En resumen, una "muerte digna" se refiere a una muerte que se alinea con los deseos y valores de la persona, brindando cuidado paliativo de calidad, respetando su autodeterminación y apoyándola en sus emociones."""
]

# 1. Carga el modelo
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Genera los embeddings y convierte a float32 (requisito de faiss)
embeddings = modelo.encode(respuestas)
embeddings = np.array(embeddings).astype('float32')

# 3. Crea el índice Faiss
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # Usa L2, que es compatible con Faiss

# 4. Añade los embeddings al índice
index.add(embeddings)

# Función para buscar la respuesta más similar dada una consulta
def buscar_respuesta(query, top_k=1, umbral=0.7):
    query_embedding = modelo.encode([query])
    query_embedding = np.array(query_embedding).astype('float32')
    
    distances, indices = index.search(query_embedding, top_k)
    
    distancia = distances[0][0]
    idx = indices[0][0]

    # En L2, menor distancia significa mayor similitud
    # Vamos a considerar como válidas solo respuestas con distancia menor al umbral
    if distancia < umbral:
        return [respuestas[idx]]
    else:
        return ["No tengo una respuesta válida para ese tema."]

# Loop de interacción
while True:
    pregunta = input("Escribe tu pregunta (o 'salir' para terminar): ")
    if pregunta.lower() == 'salir':
        break
    resultados = buscar_respuesta(pregunta)
    print("\nRespuesta más relevante:\n", resultados[0], "\n")
