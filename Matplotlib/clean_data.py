import numpy as np
import pandas as pd
import csv
from collections import Counter 
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     language_counter = Counter() 
#     for rows in csv_reader:
#         language_counter.update(rows['LanguagesWorkedWith'].split(';'))
# languages = []
# counts = []
# for items in language_counter.most_common(15):
#     languages.append(items[0])
#     counts.append(items[1])
# plt.barh(languages,counts)
# plt.title('Most popular 15 languages of programmings')
# plt.xlabel('Numbers Count')
# plt.ylabel('Programming Languages')
# plt.tight_layout()
# plt.show()
print('Another Method for data Cleaning')
language_count = Counter()
rec = pd.read_csv('data.csv')
languages = rec['LanguagesWorkedWith']
for all_lang in languages:
    language_count.update(all_lang.split(';'))
language = []
number = []
for record in language_count.most_common(15):
    language.append(record[0])
    number.append(record[1])
language.reverse()
number.reverse()
plt.barh(language,number)
plt.title('Most Popular Languages')
plt.xlabel('Numberes')
plt.tight_layout()
plt.show()



