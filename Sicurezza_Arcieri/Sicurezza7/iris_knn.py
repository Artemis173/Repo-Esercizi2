import Levenshtein
import re


testo="""
Las weak, I visitted a musuem that exhebits artefacts from anchient civilasations. The expereance was incrediblle, but som of the descripshons were dificult to undrestand becose of the olden stile of writting. I noteced that som historicle detales were exagerrated, espeshally about the Midle Ege kings who were portraiyed as infallibel.
A tour guied explaind the orrigin of certain relics, but he mispronunce som names, which confuzed me. One of the most intresting artefacts was a gilden statue of a Mithologicol creture that resembeled a griffen, but with unussualy large wings.
After the tour, I went to a libary to reserch more about anchient architechture and the technics used to construct massiv monumments like the Pyramides and the Colossium. I found a manuskript from the 17th sentury that detalied the metalls used in medeviel weaponry, but it was writen in an arkaic dialect, making it extremly complex to interpret.
I desided to barrow a book about linguistics to undrestand how languges evlove over time. One chapther expained the diffirences betwen Latin and its derivitives, but the exampels were poorly formated, making the comparisons uncler.
Overall, it was an edducational but chalenging day, and I realy apperciate how our knowlege of history continuasly expands through new discoveries and reserch."""

# Split the text into words
# Remove special characters and split the text into words
cleaned_text = re.sub(r'[^\w\s]', '', testo)
words = cleaned_text.split()
print(words)

# Per ogni parola più lunga di due caratteri calcola la distanza di Levenshtein con le parole del dizionario
with open('/usr/share/dict/british-english', 'r') as correct:
    correct_words = correct.readlines()
    for word in words:
        if len(word) >= 2:
            minlvd=1000 #tanto una distanza di 1000 non è ottenibile
            bestwd=""
            for c_word in correct_words:
                c_word = c_word.strip()
                lvd1 = Levenshtein.distance(word, c_word)
                lvd2 = Levenshtein.distance(word.lower(), c_word)
                minlv = min(lvd1, lvd2)
                if minlv < minlvd:
                    bestwd=c_word
                    minlvd=minlv
                
            if minlvd == 0:
                print(f"Word: {word} is correct")
            elif minlvd <= 2:
                print(f"Word: {word} - Correct word: {bestwd}")
            else:
                print(f"Word: {word} is too strange ({minlvd} - {bestwd})")
