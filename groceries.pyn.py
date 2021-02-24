import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
groceries=[]
with open('E://data//groceries.csv')as f:
    groceries=f.read()
    
groceries=groceries.split('\n')    

groceries_list=[]
for i in groceries:
    groceries_list.append(i.split(","))

all_groceries=[i for item in groceries_list for i in item]    
from collections import Counter
item_freq=Counter(all_groceries)

item_freq=sorted(item_freq.items(),key= lambda x:x[1])

freq = list(reversed([i[1] for i in item_freq]))
items = list(reversed([i[0] for i in item_freq]))

import matplotlib.pyplot as plt
plt.bar(height = freq[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11],rotation=80)
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

groceries_series=pd.DataFrame(pd.Series(groceries_list))
groceries_series=groceries_series.iloc[0:9835,:]
groceries_series.columns = ["transactions"]
X = groceries_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')
frequent_purchases=apriori(X,min_support=0.008,max_len=4,use_colnames=True)

plt.bar(x = list(range(0, 11)), height = frequent_purchases.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_purchases.itemsets[0:11],rotation=80)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_purchases, metric = "lift", min_threshold = 1)
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
