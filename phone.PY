import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules

phone=pd.read_csv("E://data//myphonedata.csv")
phone1=phone.iloc[:,3:]

frequent_itemsets_p=apriori(phone1,min_support=0.0084,max_len=8,use_colnames=True)
frequent_itemsets_p.sort_values('support',ascending=False,inplace=True)
import matplotlib.pyplot as plt
plt.bar(x=list(range(0,15)),height=frequent_itemsets_p.support[0:15],color='rgmyk')
plt.xticks(list(range(0,15)),frequent_itemsets_p.itemsets[0:15],rotation=85)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules=association_rules(frequent_itemsets_p,metric='lift',min_threshold=1)
rules.head(20)
rules.sort_values('lift', ascending=False).head(15)

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