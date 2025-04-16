#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:33:34 2025

@author: juan
"""

import streamlit as st
def recomendar_vino(plato):
    vinos = {
        "Gazpacho andaluz": {
            "vino": "Pazo de Señoráns Albariño - Rías Baixas",
            "uva": "Albariño",
            "cosecha": "2020",
            "region": "Rías Baixas, Galicia",
            "copa": 3.5,
            "botella": 25.0,
            "explicacion": "Un Albariño joven y vibrante que con su frescura cítrica y notas florales potencia la acidez natural del gazpacho.",
            "vino_premium": {
                "vino": "Do Ferreiro Cepas Vellas - Rías Baixas",
                "uva": "Albariño",
                "cosecha": "2021",
                "region": "Rías Baixas",
                "copa": 6.0,
                "botella": 45.0,
                "explicacion": "Una interpretación más compleja del Albariño, con carácter mineral y una textura envolvente."
            }
        },
        "Tortilla española": {
            "vino": "Marqués de Murrieta Rioja Reserva - Rioja",
            "uva": "Tempranillo, Mazuelo, Graciano",
            "cosecha": "2018",
            "region": "Rioja",
            "copa": 5.0,
            "botella": 35.0,
            "explicacion": "Un tinto equilibrado que resalta los sabores suaves de la tortilla y su textura melosa.",
            "vino_premium": {
                "vino": "Marqués de Murrieta Gran Reserva - Rioja",
                "uva": "Tempranillo, Garnacha",
                "cosecha": "2016",
                "region": "Rioja",
                "copa": 7.0,
                "botella": 55.0,
                "explicacion": "Con elegancia y una madurez exquisita, aporta complejidad y redondez al plato tradicional."
            }
        },
        "Ensaladilla rusa": {
            "vino": "Bodegas Valdesil Godello - Valdeorras",
            "uva": "Godello",
            "cosecha": "2021",
            "region": "Galicia",
            "copa": 4.0,
            "botella": 27.0,
            "explicacion": "Su acidez equilibrada y su frescura limpian el paladar tras la cremosidad de la ensaladilla.",
            "vino_premium": {
                "vino": "As Sortes - Rafael Palacios",
                "uva": "Godello",
                "cosecha": "2021",
                "region": "Valdeorras",
                "copa": 7.5,
                "botella": 60.0,
                "explicacion": "Un Godello de parcela con cuerpo y elegancia, perfecto para elevar la experiencia."
            }
        },
        "Almejas a la marinera": {
            "vino": "Albariño Martín Códax - Rías Baixas",
            "uva": "Albariño",
            "cosecha": "2020",
            "region": "Rías Baixas",
            "copa": 2.5,
            "botella": 22.0,
            "explicacion": "Su perfil salino y floral armoniza con el yodo del molusco y el toque de la salsa.",
            "vino_premium": {
                "vino": "Pazo de Barrantes - Rías Baixas",
                "uva": "Albariño",
                "cosecha": "2021",
                "region": "Rías Baixas",
                "copa": 6.0,
                "botella": 45.0,
                "explicacion": "Con más volumen y complejidad, ofrece un maridaje refinado para sabores marinos."
            }
        },
        "Pimientos de padrón": {
            "vino": "Cava Freixenet Cordon Negro - Cataluña",
            "uva": "Macabeo, Xarel·lo, Parellada",
            "cosecha": "NV",
            "region": "Cataluña",
            "copa": 3.0,
            "botella": 36.0,
            "explicacion": "Las burbujas del cava refrescan el paladar y suavizan el picor del padrón.",
            "vino_premium": {
                "vino": "Gramona Imperial Gran Reserva - Cataluña",
                "uva": "Xarel·lo, Macabeo, Chardonnay",
                "cosecha": "2017",
                "region": "Cataluña",
                "copa": 6.5,
                "botella": 50.0,
                "explicacion": "Un espumoso de gran finura, ideal para contrastes y platos con chispa."
            }
        },
        "Paella Valenciana": {
            "vino": "Protos Crianza - Ribera del Duero",
            "uva": "Tempranillo",
            "cosecha": "2018",
            "region": "Castilla y León",
            "copa": 3.1,
            "botella": 26.0,
            "explicacion": "Un tinto de taninos suaves que se adapta al carácter complejo de la paella tradicional.",
            "vino_premium": {
                "vino": "Pago de Carraovejas Crianza",
                "uva": "Tempranillo, Cabernet Sauvignon, Merlot",
                "cosecha": "2020",
                "region": "Ribera del Duero",
                "copa": 7.0,
                "botella": 55.0,
                "explicacion": "Su estructura elegante y notas de fruta madura realzan cada matiz del arroz."
            }
        },
        "Cordero asado al horno": {
            "vino": "Pesquera Crianza - Ribera del Duero",
            "uva": "Tempranillo",
            "cosecha": "2017",
            "region": "Ribera del Duero",
            "copa": 3.7,
            "botella": 40.0,
            "explicacion": "Potente y especiado, este tinto acompaña de forma ideal la intensidad del cordero asado.",
            "vino_premium": {
                "vino": "Aalto - Ribera del Duero",
                "uva": "Tempranillo",
                "cosecha": "2020",
                "region": "Ribera del Duero",
                "copa": 8.5,
                "botella": 75.0,
                "explicacion": "Un vino de autor que eleva el maridaje a una experiencia intensa y memorable."
            }
        },
        "Merluza a la gallega": {
            "vino": "Albariño Martín Códax - Rías Baixas",
            "uva": "Albariño",
            "cosecha": "2020",
            "region": "Rías Baixas",
            "copa": 2.9,
            "botella": 21.0,
            "explicacion": "Ligero y fresco, perfecto para realzar la sutileza de la merluza a la gallega.",
            "vino_premium": {
                "vino": "Albamar Finca O Pereiro",
                "uva": "Albariño",
                "cosecha": "2021",
                "region": "Rías Baixas",
                "copa": 6.0,
                "botella": 42.0,
                "explicacion": "Ofrece notas minerales y profundidad que elevan este plato tradicional."
            }
        },
        "Croquetas de jamón ibérico": {
            "vino": "Cava Freixenet Cordon Negro - Cataluña",
            "uva": "Macabeo, Xarel·lo, Parellada",
            "cosecha": "NV",
            "region": "Cataluña",
            "copa": 3.0,
            "botella": 40.0,
            "explicacion": "El cava limpia y contrasta con la cremosidad del interior de las croquetas.",
            "vino_premium": {
                "vino": "Recaredo Terrers Brut Nature",
                "uva": "Xarel·lo, Macabeo, Parellada",
                "cosecha": "2018",
                "region": "Cataluña",
                "copa": 6.0,
                "botella": 52.0,
                "explicacion": "Burbuja elegante y expresiva que acompaña con sofisticación el jamón curado."
            }
        },
        "Pollo al ajillo": {
            "vino": "Marqués de Cáceres Crianza - Rioja",
            "uva": "Tempranillo, Garnacha",
            "cosecha": "2019",
            "region": "Rioja",
            "copa": 3.7,
            "botella": 39.0,
            "explicacion": "Con notas especiadas y fruta madura, armoniza con el ajo y el dorado del pollo.",
            "vino_premium": {
                "vino": "Viña Ardanza Reserva - La Rioja Alta",
                "uva": "Tempranillo, Garnacha",
                "cosecha": "2016",
                "region": "Rioja",
                "copa": 7.0,
                "botella": 58.0,
                "explicacion": "Clásico y refinado, potencia los sabores rústicos con un toque elegante."
            }
        }
    }

    platos_precio = {
        "Gazpacho andaluz": 9.0,
        "Tortilla española": 7.5,
        "Ensaladilla rusa": 6.5,
        "Almejas a la marinera": 12.0,
        "Pimientos de padrón": 8.0,
        "Paella Valenciana": 18.0,
        "Cordero asado al horno": 22.0,
        "Merluza a la gallega": 16.0,
        "Croquetas de jamón ibérico": 9.0,
        "Pollo al ajillo": 14.0
    }

    return vinos.get(plato), platos_precio.get(plato, 0)

def main():
    print("Bienvenido/a a Chin Chin, tu sumiller virtual.\n")

    try:
        edad = int(input("¿Cuál es tu edad? "))
        if edad < 18:
            print("\nLo siento, este servicio solo está disponible para mayores de edad.")
            return
    except ValueError:
        print("Edad no válida. Por favor, introduce un número.")
        return

    genero = input("¿Cuál es tu género? (Masculino / Femenino / Otro): ")
    region_vinicola = input("¿Cuál es tu región vinícola favorita? (Rioja, Ribera del Duero, Rías Baixas, Bierzo, Priorat, Jerez): ")

    print("\nGracias por tus respuestas. Ahora, elige tu comida de la siguiente lista:\n")

    platos = [
        "Gazpacho andaluz",
        "Tortilla española",
        "Ensaladilla rusa",
        "Almejas a la marinera",
        "Pimientos de padrón",
        "Paella Valenciana",
        "Cordero asado al horno",
        "Merluza a la gallega",
        "Croquetas de jamón ibérico",
        "Pollo al ajillo"
    ]

    for i, plato in enumerate(platos, 1):
        print(f"{i}. {plato}")

    try:
        eleccion = int(input("\nElige el número de tu plato: "))
        if 1 <= eleccion <= len(platos):
            plato_elegido = platos[eleccion - 1]
            vino_info, precio_plato = recomendar_vino(plato_elegido)

            print(f"\nHas elegido: {plato_elegido}")
            print(f"Precio del plato: {precio_plato}€\n")

            print("🍷 Vino recomendado:")
            print(f"- {vino_info['vino']} ({vino_info['copa']}€/copa - {vino_info['botella']}€/botella)")
            print(f"  👉 {vino_info['explicacion']}\n")

            print("🥂 Vino premium recomendado:")
            premium = vino_info['vino_premium']
            print(f"- {premium['vino']} ({premium['copa']}€/copa - {premium['botella']}€/botella)")
            print(f"  ⭐ {premium['explicacion']}")
        else:
            print("Opción inválida. Por favor, elige un número válido.")
    except ValueError:
        print("Entrada inválida. Introduce un número para seleccionar el plato.")


if __name__ == "__main__":
    main()

# Configuración de la app
st.set_page_config(page_title="Sumiller Virtual", page_icon="🍷")
st.title("🍷 Chin Chin: Tu Sumiller Virtual")

st.markdown("Bienvenido a tu recomendador de vinos personalizado. Elige tus preferencias y te sugerimos el mejor vino para tu plato.")

# Inputs del usuario
edad = st.number_input("¿Qué edad tienes?", min_value=0, max_value=120, step=1)
genero = st.selectbox("¿Cuál es tu género?", ["masculino", "femenino", "otro"])
region_favorita = st.selectbox("¿Cuál es tu región vinícola favorita?", ["Rías Baixas", "Rioja", "Valdeorras", "Cataluña", "Ribera del Duero"])

platos_disponibles = [
    "Gazpacho andaluz", "Tortilla española", "Ensaladilla rusa", "Almejas a la marinera",
    "Pimientos de padrón", "Paella Valenciana", "Cordero asado al horno",
    "Merluza a la gallega", "Croquetas de jamón ibérico", "Pollo al ajillo"
]

plato_elegido = st.selectbox("¿Qué plato vas a comer?", platos_disponibles)

# Función de recomendación adaptada para Streamlit
def recomendar_vino_streamlit(plato):
    vino_info, precio_plato = recomendar_vino(plato)
    if edad < 18:
        return {"mensaje": "Lo siento, este servicio está disponible solo para mayores de edad."}, precio_plato
    else:
        return vino_info, precio_plato

# Botón para mostrar la recomendación
if st.button("🍽️ Recomendar vino"):
    vino_info, precio_plato = recomendar_vino_streamlit(plato_elegido)

    if "mensaje" in vino_info:
        st.warning(vino_info["mensaje"])
    else:
        st.success(f"Has elegido **{plato_elegido}** (Precio: {precio_plato}€)")
        st.markdown(f"### 🥂 Recomendación de vino: **{vino_info['vino']}**")
        st.markdown(f"- **Uva:** {vino_info['uva']}")
        st.markdown(f"- **Cosecha:** {vino_info['cosecha']}")
        st.markdown(f"- **Región:** {vino_info['region']}")
        st.markdown(f"- **Precio por copa:** {vino_info['copa']}€")
        st.markdown(f"- **Precio por botella:** {vino_info['botella']}€")
        st.info(vino_info["explicacion"])

        if "vino_premium" in vino_info:
            st.markdown("---")
            st.markdown(f"### 🍾 Recomendación premium: **{vino_info['vino_premium']['vino']}**")
            st.markdown(f"- **Uva:** {vino_info['vino_premium']['uva']}")
            st.markdown(f"- **Cosecha:** {vino_info['vino_premium']['cosecha']}")
            st.markdown(f"- **Región:** {vino_info['vino_premium']['region']}")
            st.markdown(f"- **Precio por copa:** {vino_info['vino_premium']['copa']}€")
            st.markdown(f"- **Precio por botella:** {vino_info['vino_premium']['botella']}€")
            st.info(vino_info['vino_premium']['explicacion'])