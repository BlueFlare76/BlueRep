import pandas as pd

def quan_rab(n, k):
    if n > 40 or k > 5:
        return "Введите n <= 40 и k <= 5"
    else:
        df = pd.DataFrame({'Months': range(1, n + 1), 
                           'Reproduction_rabbits': [None] * n, 
                           'Young_rabbits': [None] * n, 
                           'Total_rabbits': [None] * n})

        df.at[0, 'Reproduction_rabbits'] = 0
        df.at[0, 'Young_rabbits'] = 1

        for i in range(1, n):
            df.at[i, 'Reproduction_rabbits'] = df.at[i - 1, 'Reproduction_rabbits'] + df.at[i - 1, 'Young_rabbits']
            df.at[i, 'Young_rabbits'] = k * df.at[i - 1, 'Reproduction_rabbits']

        df['Total_rabbits'] = df['Reproduction_rabbits'] + df['Young_rabbits']

    return df.at[n - 1, 'Total_rabbits']

#вызов:
result = quan_rab(n=13, k=5)
print('result:', result)


#структура данных, класс, метод, обьект
