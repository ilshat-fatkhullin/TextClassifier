
# coding: utf-8

# In[11]:

import pandas as pd


# In[12]:

Sentences = pd.DataFrame.from_csv("../Data/sentences.csv")
Sentences = Sentences.reset_index()


# In[63]:

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
    Sentence = Sentence.replace("«", " ")
    Sentence = Sentence.replace(":", " ")
    Sentence = Sentence.replace("…", " ")
    Sentence = Sentence.replace("...", " ")
    return Sentence


# In[77]:

def DeleteArticles(Array):
    Articles = ["без", "безо", "аль", "бы", "же", "но", "не", "то", "так", "а", "ах","близ", "в", "во", "вместо", "вне", "для", "до", "за", "из", "изо", "из-за", "из-под", "к", "ко", "кроме", "между", "меж", "на", "над", "надо", "о", "об", "обо", "от", "ото", "перед", "передо", "пo", "под", "при", "про", "ради", "с", "со", "сквозь", "среди", "у", "через", "чрез", "что", "и"]
    for aritcle in Articles:
        Result = []
        for element in Array:
            if element not in Articles:
                Result.append(element)
    return Result


# In[78]:

def DeleteNumbers(Array):
    Result = []
    for element in Array:
        if element.isdigit() is False:
            Result.append(element)
    return Result


# In[79]:

def CountArticles(Sentence):
    Result = {"!": 0, "?": 0, ".":0}
    Result["!"] = Sentence.count("!")
    Result["."] = Sentence.count(".")
    Result["?"] = Sentence.count("?")
    return Result


# In[82]:

def ParseSentence(Sentence):
    Sentence = Sentence.lower()
    Articles = CountArticles(Sentence)
    Sentence = DeletePunctuation(Sentence)
    Sentence = Sentence.split()
    Sentence = DeleteArticles(Sentence)
    Sentence = DeleteNumbers(Sentence)
    Sentence.append(Articles)
    return Sentence


# In[81]:

Sentences["Предложение"].apply(ParseSentence)


# In[ ]:



