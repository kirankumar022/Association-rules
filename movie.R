library(readr)
library(arules)
movie=read.csv(file.choose())

summary(movie)
arules=apriori(movie,parameter = list(support=0.007,confidence=0.095,minlen=5))
arules
inspect(head(sort(arules,by='lift')))
head(quality(arules))
plot(quality(arules))
library(arulesViz)
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph")

