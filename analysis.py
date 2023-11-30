import pandas as pd
import numpy as np
from unidecode import unidecode
from bidi.algorithm import get_display
import jdatetime
from datetime import datetime
pd.set_option('display.encoding', 'utf-8')


df = pd.read_csv(
    'houseData.csv',
    index_col=[0]
)


def persianDigitToEnglish(value):
    return unidecode(value)


numeric_columns = ['Area', 'YearBuilt', 'Rooms', 'Price', 'Floor']
text_column = 'Location'    

df[numeric_columns] = df[numeric_columns].applymap(persianDigitToEnglish)
df[text_column] = df[text_column].map(lambda x: get_display(x))

df['Area'] = df['Area'].astype(np.uint16)
df['YearBuilt'] = df['YearBuilt'].astype(np.uint16)
df['Rooms'] = df['Rooms'].astype(np.uint8)
df['Price'] = df['Price'].astype(np.uint64)
df['Floor'] = df['Floor'].astype(np.uint8)

print(df.info())


def calculate_age(year):
    today_date = datetime.now()
    persian_date = jdatetime.GregorianToJalali(gyear=today_date.year, gmonth=today_date.month, gday=today_date.day)
    return persian_date.jyear - year

df['BuildingAge'] = df['YearBuilt'].map(calculate_age)



print(df.head())



