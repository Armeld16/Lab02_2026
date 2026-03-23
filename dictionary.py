class Dictionary:
    def __init__(self):
        self.word = {}

    def addWord(self, parolaAliena, traduzione):
        self.word[parolaAliena] = traduzione

    def translate(self, parolaAliena):
        if parolaAliena in self.word:
            return self.word[parolaAliena]
        else:
            return "La Parola cercata non esiste"


    def translateWordWildCard(self, query):
        for parola in self.word:
            if len(query) == len(parola):
                for c1, c2 in zip(query, parola):  # zip prende due sequenze e le "unisce" in coppie, elemento per elemento. paragona la prima lettera per la prima lettera
                    if c1 == "?" or c1 == c2:
                        pass
                    else:
                        break
                else:
                    return self.word[parola]
