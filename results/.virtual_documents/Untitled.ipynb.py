import pandas as pd


df = pd.read_csv('radiologists_evaluation_results.csv', sep=',')


df['subject'] = df.patient.apply(lambda X: X.split('_')[0])


len(set(df.loc[df.label == 1].subject.values))


len(set(df.loc[df.label == 0].subject.values))



