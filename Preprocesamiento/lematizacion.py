import stanza

def lematizacion():
    #Abrir archivo pinocho
    with open("Preprocesamiento\pinocho.txt", "r", encoding="utf-8") as f:
        pinocho = f.read()

    #Crear el pipeline 
    ##lang = es(español)
    ##processors = tokenize(tokenizar), mwt(palabras compuestas), pos(etiquetado gramatical), lemma(lematizar)

    nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

    doc = nlp(pinocho)

    #Guardar el nuvo archivo con los tokens
    with open("Preprocesamiento\pinocho_tokens.txt", "w", encoding="utf-8") as f:
        for sent in doc.sentences:
            f.write("Oracion " + str(sent.index + 1) + "\n")
            for word in sent.words:
                f.write("\tId: {" + str(word.id) + "} \t")
                f.write("Texto: {" + word.text + "}\t->\t")
                f.write("Lexema: {" + word.lemma + "}\n")
                pass
            f.write("\n")
    pass

if __name__ == "__main__":
    lematizacion()
    pass