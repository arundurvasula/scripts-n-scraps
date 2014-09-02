#!/usr/bin/env Rscript
#This script will get the family names for all species in the 3rd column of a file
# use like cat ../results/P3/blast/P3-clean-blast.csv | ./taxize.r ../results/P3/blast/P3-virus-summary
# You need to provide a file name as an argument to the script
# You also might need to chmod +x the file
require("taxize")
require("ggplot2")
d <- read.csv(file="stdin", header=FALSE)
ca <- commandArgs(trailingOnly=TRUE)

d$V3 <- gsub(".*\\[(.*)\\].*", "\\1", d$V3)
d.virus = subset(d, grepl("virus", V3))
families <- tax_name(query=d.virus$V3,get='family', db='ncbi')
d.virus["V4"] <- families

d.new <- data.frame(d.virus$V1, d.virus$V2, d.virus$V3, families)

write.table(d.new, file=paste(ca[1], "-families.csv", sep=""), row.names=FALSE, sep=",", col.names=c("Contig name", "Length", "Virus name", "Virus family"))

png(file=ca[1], width=1000, height=500)

vir.families <- table(d.virus$V4)
df.vir.families <- data.frame(vir.families)
if (length(df.vir.families$Var1) > 7) { # if there are more than 7 families
  df.vir.families <- subset(df.vir.families, Freq > 5)
}
ggplot(df.vir.families, aes(x=Var1, y=Freq, fill=Var1, title="Virus Families")) + labs(x="Family", y="Number of contigs", fill="Families") + geom_bar(stat="identity", xlab="Families", ylab="Number of contigs")

dev.off()