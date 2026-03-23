from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.dizionario = Dictionary()

    def printMenu(self):
        print("------------------------------")
        print("    Translator Alien-Italian")
        print("------------------------------")
        # 1. Aggiungi nuova parola
        print("1. Aggiungi nuova parola")
        # 2. Cerca una traduzione
        print("2. Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3. Cerca con wildcard")
        # 4. stampa tutto il dizionario
        print("4. Stampa tutto il Dizionario")
        # 5. Exit
        print("5. Exit")
        print("------------------------------")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r") as f:
            for riga in f:
                parti = riga.split()
                self.dizionario.addWord(parti[0], parti[1])
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parti = entry.split()
        self.dizionario.addWord(parti[0], parti[1])
    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        print(self.dizionario.translate(query))

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        print(self.dizionario.translateWordWildCard(query))