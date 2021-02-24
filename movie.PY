import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules


movie=pd.read_csv("E://data//my_movies.csv")
movie=movie.iloc[:,5:]
frequent_itemsets_m=apriori(movie,min_support=0.0094,max_len=6,use_colnames=True)
frequent_itemsets_m.sort_values('support',ascending=False,inplace=True)
import matplotlib.pyplot as plt
plt.bar(x=list(range(0,10)),height=frequent_itemsets_m.support[0:10],color='rgmyk')
plt.xticks(list(range(0,10)),frequent_itemsets_m.itemsets[0:10],rotation=85)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()
rules = association_rules(frequent_itemsets_m, metric = "lift", min_threshold = 1)
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