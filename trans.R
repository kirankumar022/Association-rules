library(readr)
library(arules)
trans=read.csv(file.choose())

summary(trans)
arules=apriori(trans,parameter = list(support=0.004,confidence=0.07,minlen=3))
arules
inspect(head(sort(arules,by='lift')))
head(quality(arules))
plot(quality(arules))
library(arulesViz)
plot(arules)
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph")
