meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GL HF": "Buena suerte, diviertete!",
            "GG": "Para felicitar a los jugadores con un BUEN JUEGO!",
            "AESTHETIC": "Para denotar que algo es estético o bonito visualmente",
            "PINKY": "Para denotar que alguien es muy amiga tuya, generalmente usado entre mujeres",
            "CARRY": "Persona que ayuda a otra a conseguir su objetivo"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("no se encuentra la palabra")
