library(arules)
library(readr)
phone=read.csv(file.choose())
arules2=apriori(phone,parameter = list(support=0.002,confidence=0.06,minlen=2))
arules2
inspect(head(sort(arules2,by='lift')))
head(quality(arules2))
library('arulesViz')
plot(arules2)
plot(arules2, method = "grouped")
plot(arules2[1:10], method = "graph") # for good visualization try plotting only few rules


