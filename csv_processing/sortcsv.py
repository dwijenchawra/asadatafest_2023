# sort a tsv by the Id column

import pandas as pd

DELIMITER = '`'

df = pd.read_csv('../data/cleanedquestions.txt', sep=DELIMITER, error_bad_lines=False)

print(df.shape)
print(df.columns)
print(df.describe())
print(df.dtypes)
df.sort_values(by=['Id'], inplace=True)
df.to_csv('../data/cleanedquestionssorted.txt', sep=DELIMITER, index=False)
