import discord 
import random
import os
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='/', intents=intents)
text = "Claro! Aquí tienes los comandos que puedes realizar: /datos -Muestra datos curiosos sobre el impacto ambiental ; /consejos -da consejos de como reducir basura ; /reciclaje -explica los colores de los botes de reciclaje ; /aprende -da lecciones simples de conceptos ecologicos" 


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ayuda(ctx):
    await ctx.send(text)

@bot.command()
async def datos(ctx):
    datos_impacto_ambiental = [
    # Impacto de los residuos plásticos
    "Una botella de plástico tarda hasta 500 años en descomponerse.",
    "Cada minuto se compran 1 millón de botellas plásticas en el mundo; menos del 30 porciento se recicla.",
    "El plástico ya ha llegado a los rincones más remotos del planeta, como el Ártico y la Fosa de las Marianas.",
    
    # Alimentos y desperdicio
    "El 30 porciento de los alimentos producidos en el mundo se desperdicia, equivalente a 1.300 millones de toneladas al año.",
    "Si el desperdicio de alimentos fuera un país, sería el tercero con más emisiones de CO₂, después de Estados Unidos y China.",
    "El pan es uno de los alimentos más desperdiciados, seguido por frutas y verduras.",
    
    # Impacto del transporte
    "Un automóvil promedio emite 4.6 toneladas de CO₂ al año, equivalente a talar 30 árboles maduros.",
    "El avión es el medio de transporte más contaminante. Un vuelo de ida y vuelta de Londres a Nueva York genera la misma cantidad de CO₂ que usar un automóvil durante un año.",
    
    # Agua y consumo
    "Se necesitan 2.700 litros de agua para producir una camiseta de algodón.",
    "Un grifo que gotea puede desperdiciar hasta 10.000 litros de agua al año.",
    "El 70 porciento del agua dulce del mundo se usa en la agricultura.",
    
    # Moda y textiles
    "La industria de la moda genera el 10 porciento de las emisiones de gases de efecto invernadero global.",
    "Se tiran más de 92 millones de toneladas de ropa al año, y la mayoría no es reciclable.",
    "Un par de jeans puede requerir hasta 7.500 litros de agua desde su producción hasta llegar a una tienda.",
    
    # Residuos electrónicos
    "En 2023 se generaron más de 50 millones de toneladas de residuos electrónicos; solo el 20 porciento se recicló adecuadamente.",
    "Un celular contiene hasta 60 metales diferentes, incluidos oro y cobalto, que son difíciles de extraer y reciclar.",
    "Los residuos electrónicos crecen a un ritmo de 3-4 porciento al año, lo que los convierte en la categoría de basura que más rápido aumenta.",
    
    # Energía y electricidad
    "Las luces LED usan hasta un 75% menos de energía que las bombillas incandescentes y duran 25 veces más.",
    "Dejar el cargador del celular enchufado consume electricidad, incluso si no está cargando un dispositivo ('carga fantasma').",
    
    # Océanos y biodiversidad
    "Cada año, 8 millones de toneladas de plástico llegan a los océanos, equivalente a un camión de basura lleno de plástico cada minuto.",
    "El 40 porciento de los arrecifes de coral ya han sido destruidos, en parte debido a la contaminación y el cambio climático.",
    "Las especies marinas ingieren hasta 24.000 toneladas de plástico al año.",
    
    # Deforestación
    "Se pierden 10 millones de hectáreas de bosques cada año, un área del tamaño de Islandia.",
    "El papel reciclado puede ahorrar hasta un 60 porciento de energía en comparación con fabricar papel nuevo a partir de árboles.",
    "Los bosques absorben aproximadamente 2.6 mil millones de toneladas de CO₂ al año, lo que los convierte en aliados clave contra el cambio climático."]
    dato = random.choice(datos_impacto_ambiental)
    await ctx.send(dato)


@bot.command()
async def consejos(ctx):
    consejos_para_reducir_basura = [
    # Reduce
    "Compra a granel para evitar empaques innecesarios.",
    "Lleva tu propia bolsa reutilizable al hacer compras.",
    "Evita los productos de un solo uso, como cubiertos y platos desechables.",
    "Compra solo lo necesario para evitar desperdiciar comida.",
    "Opta por productos con menos embalaje o que usen materiales reciclables.",
    
    # Reutiliza
    "Usa frascos de vidrio o recipientes reutilizables para almacenar alimentos.",
    "Reutiliza papel y sobres como borradores o para notas rápidas.",
    "Repara objetos dañados en lugar de desecharlos (ropa, muebles, etc.).",
    "Dona ropa y objetos en buen estado que ya no uses.",
    "Transforma envases de plástico en macetas o organizadores.",
    
    # Recicla
    "Clasifica tu basura y asegúrate de separar reciclables como papel, plástico, vidrio y metales.",
    "Lleva los residuos electrónicos a centros especializados para su reciclaje.",
    "Investiga los puntos de reciclaje en tu comunidad.",
    "Aprende a leer los símbolos de reciclaje en los productos que compras.",
    "Usa compostaje para restos de comida y desechos orgánicos.",
    
    # Evita desperdicios de comida
    "Planea tus comidas y haz listas de compras para evitar comprar de más.",
    "Congela alimentos que no vayas a consumir de inmediato.",
    "Usa las sobras de comida para preparar nuevas recetas.",
    "Compra frutas y verduras 'feas', que suelen ser descartadas pero están perfectamente bien para consumir.",
    "Aprende a almacenar correctamente los alimentos para que duren más tiempo.",
    
    # Adopta hábitos sostenibles
    "Lleva tu propia botella de agua reutilizable.",
    "Usa servilletas de tela en lugar de las de papel.",
    "Elige productos recargables, como baterías o detergentes concentrados.",
    "Haz tus propios productos de limpieza con ingredientes naturales.",
    "Participa en iniciativas locales para limpiar espacios públicos.",
    
    # Cambia hábitos de consumo
    "Compra productos de segunda mano, como ropa o muebles.",
    "Elige productos fabricados con materiales reciclados.",
    "Prefiere marcas que tengan políticas sostenibles y respetuosas con el medio ambiente.",
    "Suscríbete a servicios digitales en lugar de recibir correspondencia en papel.",
    "Piensa antes de comprar: ¿realmente lo necesitas?"]
    consejo = random.choice (consejos_para_reducir_basura)
    await ctx.send(consejo)

@bot.command()
async def reciclaje(ctx):
    with open('images/post_reciclaje.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
@bot.command()
async def aprende(ctx):
    conceptos_ecologicos = [
    {
        "concepto": "Huella de carbono",
        "descripcion": "Es la cantidad total de gases de efecto invernadero emitidos directa o indirectamente por las actividades humanas."
    },
    {
        "concepto": "Huella hídrica",
        "descripcion": "Es el volumen total de agua utilizada para producir bienes y servicios consumidos por una persona o comunidad."
    },
    {
        "concepto": "Sostenibilidad",
        "descripcion": "Es el uso responsable y equilibrado de los recursos naturales para satisfacer las necesidades actuales sin comprometer las de las futuras generaciones."
    },
    {
        "concepto": "Economía circular",
        "descripcion": "Es un modelo económico que busca reducir residuos al máximo mediante la reutilización, reciclaje y rediseño de productos y materiales."
    },
    {
        "concepto": "Cambio climático",
        "descripcion": "Es la alteración del clima global causada principalmente por la actividad humana, como la emisión de gases de efecto invernadero."
    },
    {
        "concepto": "Energías renovables",
        "descripcion": "Son fuentes de energía que se obtienen de recursos naturales inagotables, como el sol, el viento y el agua."
    },
    {
        "concepto": "Biodiversidad",
        "descripcion": "Es la variedad de especies animales, vegetales y microorganismos en un ecosistema o en todo el planeta."
    },
    {
        "concepto": "Compostaje",
        "descripcion": "Es el proceso de descomposición natural de residuos orgánicos para crear un abono rico en nutrientes para las plantas."
    },
    {
        "concepto": "Deforestación",
        "descripcion": "Es la eliminación de bosques debido a actividades humanas como la agricultura, la ganadería o la urbanización."
    },
    {
        "concepto": "Reciclaje",
        "descripcion": "Es el proceso de recolectar y transformar materiales usados para fabricar nuevos productos y reducir la basura."
    },
    {
        "concepto": "Efecto invernadero",
        "descripcion": "Es un fenómeno natural en el que gases en la atmósfera atrapan el calor del sol, pero se intensifica por actividades humanas."
    },
    {
        "concepto": "Sobrepesca",
        "descripcion": "Es la explotación excesiva de recursos pesqueros que amenaza la biodiversidad marina y la sostenibilidad del ecosistema."
    },
    {
        "concepto": "Microplásticos",
        "descripcion": "Son pequeñas partículas de plástico de menos de 5 mm que contaminan el agua, el suelo y los alimentos."
    },
    {
        "concepto": "Eficiencia energética",
        "descripcion": "Es el uso inteligente de la energía para realizar actividades con el menor consumo posible, reduciendo el desperdicio."
    },
    {
        "concepto": "Agricultura ecológica",
        "descripcion": "Es un sistema de producción agrícola que evita el uso de productos químicos sintéticos y promueve la biodiversidad."
    },
    {
        "concepto": "Residuos electrónicos",
        "descripcion": "Son desechos de dispositivos electrónicos como celulares, computadoras y electrodomésticos, que requieren tratamiento especial."
    },
    {
        "concepto": "Capa de ozono",
        "descripcion": "Es una capa de gas ozono en la atmósfera que protege la Tierra de la radiación ultravioleta del sol."
    },
    {
        "concepto": "Calentamiento global",
        "descripcion": "Es el aumento de la temperatura promedio de la Tierra debido al aumento de gases de efecto invernadero."
    },
    {
        "concepto": "Consumo responsable",
        "descripcion": "Es un enfoque de consumo que considera el impacto ambiental, social y ético de los productos y servicios adquiridos."
    },
    {
        "concepto": "Reserva natural",
        "descripcion": "Es un área protegida destinada a la conservación de ecosistemas, flora y fauna en su estado natural."
    }]

    aprender = random.choice(conceptos_ecologicos)
    await ctx.send(aprender)   


bot.run("")










