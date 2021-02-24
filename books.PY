import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules




book = pd.read_csv("E://data//book.csv", header=0)
book.columns
book[:]=book[:].fillna("")
type(book)


#frequent item sets
frequent_itemsets = apriori(book, min_support = 0.006, max_len = 6, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

import matplotlib.pyplot as plt
plt.bar(x = list(range(0, 8)), height = frequent_itemsets.support[0:8], color ='rgmyk')
plt.xticks(list(range(0, 8)), frequent_itemsets.itemsets[0:8], rotation =80)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

