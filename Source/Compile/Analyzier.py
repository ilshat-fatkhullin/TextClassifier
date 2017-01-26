import pandas as pd

words_df = pd.read_excel('../../Data/words_dictionary.xlsx')
words_df.columns = ['word', 'style']
words_df = words_df.groupby('word')['style'].sum().to_frame().reset_index()
words = words_df['word'].values
words_style = words_df['style'].values
 
def AnalyzeWords(Array):
    Count = 1
    Sum = 0
    for word in Array:
        for i in range(len(words)):
            if word == words[i]:
                Sum+=words_style[i]
                Count+=1
    return Sum / Count



