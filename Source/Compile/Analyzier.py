import pandas as pd

words_df = pd.read_excel('../../Data/words_dictionary.xlsx')
words_df.columns = ['word', 'style']
words_df = words_df.groupby('word')['style'].sum().to_frame().reset_index()
words = words_df['word'].values
words_style = words_df['style'].values
Bigrams = pd.DataFrame.from_csv("../../Data/bigrams.csv").set_index('index').to_dict()
 
def AnalyzeWords(Array):
    Count = 1
    Sum = 0
    for word in Array:
        for i in range(len(words)):
            if word == words[i]:
                Sum+=words_style[i]
                Count+=1
    return Sum / Count

def AnalyzeNeutralBigrams(Array):
    Coeff = 0
    Array = list(set(Array))
    for num in range(len(Array)):
        for i in range(num+1, len(Array)):
            if Array[num] != Array[i]:
                try:
                    Coeff += Bigrams['neutral'][Array[num]+"#"+Array[i]]
                except:
                    continue
    return Coeff

def AnalyzePositiveBigrams(Array):
    Coeff = 0
    Array = list(set(Array))
    for num in range(len(Array)):
        for i in range(num+1, len(Array)):
            if Array[num] != Array[i]:
                try:
                    Coeff += Bigrams['positive'][Array[num]+"#"+Array[i]]
                except:
                    continue
    return Coeff

def AnalyzeNegativeBigrams(Array):
    Coeff = 0
    Array = list(set(Array))
    for num in range(len(Array)):
        for i in range(num+1, len(Array)):
            if Array[num] != Array[i]:
                try:
                    Coeff += Bigrams['negative'][Array[num]+"#"+Array[i]]
                except:
                    continue
    return Coeff

