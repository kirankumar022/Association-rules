


import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

tra = pd.read_csv("E://data//transactions_retail1.csv", header=None)
tran=tra.iloc[:,:]
tran[:]=tra[:].fillna("")


tr = []


tr=tran.to_string()

tr = tr.split("\n")

tr_list = []
for i in tr:
    tr_list.append(i.split(","))

all_tr_list = [i for item in tr_list for i in item]

from collections import Counter # ,OrderedDict

item_frequencies = Counter(all_tr_list)

# after sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 
import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11], rotation='vertical')
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

