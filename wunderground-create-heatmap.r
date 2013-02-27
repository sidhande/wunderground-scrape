# requires plyr and reshape packages
# should be run after running the scrape-wunderground.py script

weather <- read.csv(file="wunder-data.csv", sep=",", header=FALSE)
weather <- rename(weather, c('V1'='city','V2'='year.month','V3'='high.max','V4'='avg.max','V5'='low.max','V6'='high.mean','V7'='avg.mean','V8'='low.mean','V9'='high.min','V10'='avg.min','V11'='low.min'))
weather2 <- data.frame('city'=weather$city,'date'=weather$year.month,'avg.temp'=weather$avg.mean)
weathermelt <- melt(weather2, id=c('city','date'))
weatherfinal <- cast(weathermelt, city~date)
row.names(weatherfinal) <- weatherfinal$city
weatherfinal <- weatherfinal[,2:13]
weathermatrix <- data.matrix(weatherfinal)
weatherheatmap <- heatmap(weathermatrix, Rowv=NA, Colv=NA, col = cm.colors(256), scale="column", margins=c(5,10), main='Heatmap of Avg Temps in 2012', xlab='Year-Month', ylab='City')
