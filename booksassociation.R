library("arules")
library(readr)
books=read.csv(file.choose())
class(books)
View(books)
summary(books)
arules <- apriori(books, parameter = list(support = 0.002, confidence = 0., minlen = 2))
arules
inspect(head(sort(arules, by = "lift")))
# Overal quality 
head(quality(arules))
library("arulesViz") # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)
windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules
