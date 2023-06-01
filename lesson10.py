import pandas as pd
import seaborn as sns

# Задача 1. Найдите, какая область центрального федерального округа имела наибольшую численность 
# студентов вечерней формы обучения в 2015 году.

df = pd.read_csv('data.csv', sep=';',encoding='cp1251')
slice1 = df.loc[2:19, ['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015']]
print(slice1.max())


# Задача 2. Постройте диаграмму с данными о численности студентов 
# дневной формы обучения южного федерального округа за 2017 год

slice2 = df.loc[33:40, ['Субъект РФ', 'Численность студентов, очная форма, человек, 2017']]
plot = sns.barplot(data=slice2, x='Субъект РФ', y='Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(plot.get_xticklabels(),rotation = 90)


# Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, 
# в которых общее количество студентов не превышает 10000 за данный год.

slice3 = df[df['Численность студентов заочная форма, человек, 2019'] < 10000]
plot = sns.barplot(data=slice3, x='Субъект РФ', y='Численность студентов заочная форма, человек, 2019')
plot.set_xticklabels(plot.get_xticklabels(),rotation = 90)