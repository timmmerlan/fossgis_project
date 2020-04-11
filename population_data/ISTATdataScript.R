# script for cleaning the "raw" table of the population data from ISTAT

rm(list = ls())
setwd("C:/Users/jnlpu/Documents/Studium/Geographie/5. Semester/FOSSGIS/Abschlussprojekt")

# load table
TabelleUnbereinigt <- read.csv(file = "Censimento_2011_Indicatori_famiglie_per_Comuni_nella_regione_SICILIA.csv",
                                 header = T, sep = ";")

# load package for select function; would also be possible with rename function of the same package only (had some issues with it though, possibly because of the original column names or because of spaces)
library(dplyr)

# select only necessary columns
TabelleBereinigt <- select(TabelleUnbereinigt, ??..CodiceIstat, Nome, Ampiezza.demografica, Densit??..di.popolazione)

# renaming the columns
colnames(TabelleBereinigt)[1] <- "Postal Code"
colnames(TabelleBereinigt)[2] <- "Name"
colnames(TabelleBereinigt)[3] <- "Population"
colnames(TabelleBereinigt)[4] <- "Population Density"

# checking whether everythings fine down there
sum(is.na(TabelleBereinigt))

# export as .csv
write.table(TabelleBereinigt, file = "ISTATdata.csv", sep = ";", row.names = F)
