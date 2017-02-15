import pandas as pd
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def DeletePunctuation(Sentence):
    Sentence = Sentence.replace(",", " ")
    Sentence = Sentence.replace(";", " ")
    Sentence = Sentence.replace("(", " ")
    Sentence = Sentence.replace(")", " ")
    Sentence = Sentence.replace("{", " ")
    Sentence = Sentence.replace("?", " ")
    Sentence = Sentence.replace(".", " ")
    Sentence = Sentence.replace("!", " ")
    Sentence = Sentence.replace("}", " ")
    Sentence = Sentence.replace("\"", " ")
    Sentence = Sentence.replace("'", " ")
    Sentence = Sentence.replace("=", " ")
    Sentence = Sentence.replace("+", " ")
    Sentence = Sentence.replace("–", " ")
    Sentence = Sentence.replace("»", " ")
    Sentence = Sentence.replace("--", " ")
    Sentence = Sentence.replace('--', " ")
    Sentence = Sentence.replace("«", " ")
    Sentence = Sentence.replace(":", " ")
    Sentence = Sentence.replace("…", " ")
    Sentence = Sentence.replace("...", " ")
    return Sentence

def DeleteArticles(Array):
    Articles = ["без", "безо", "аль", "бы", "же", "но", "не", "то", "так", "а", "ах","близ", "в", "во", "вместо", "вне", "для", "до", "за", "из", "изо", "из-за", "из-под", "к", "ко", "кроме", "между", "меж", "на", "над", "надо", "о", "об", "обо", "от", "ото", "перед", "передо", "пo", "под", "при", "про", "ради", "с", "со", "сквозь", "среди", "у", "через", "чрез", "что", "и"]
    for aritcle in Articles:
        Result = []
        for element in Array:
            if element not in Articles:
                Result.append(element)
    return Result

def DeleteNumbers(Array):
    Result = []
    for element in Array:
        if element.isdigit() is False:
            Result.append(element)
    return Result


def CountArticles(Sentence):
    Result = {"!": 0, "?": 0, ".":0}
    Result["!"] = Sentence.count("!")
    Result["."] = Sentence.count(".")
    Result["?"] = Sentence.count("?")
    return Result


def ParseSentence(Sentence):
    Sentence = Sentence.lower()
    Articles = CountArticles(Sentence)
    Sentence = DeletePunctuation(Sentence)
    Sentence = Sentence.split()
    #Sentence = DeleteArticles(Sentence)
    Sentence = DeleteNumbers(Sentence)
    Sentence = list(map(lambda x:morph.parse(x)[0].normal_form, Sentence))
    return [Sentence, Articles]

def ParseLabel(label):
    if label == "negative":
        return -1
    elif label == "positive":
        return 1
    else:
        return 0

