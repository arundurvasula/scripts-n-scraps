#####
# This file contains code to count the number of contigs for each virus in a sample.
# Data must be in .csv, and excel files with multiple sheets must be split up
# To run this script, type in "Rscript countViruses.r <filename>" (no quotes and replace <filename> without the brackets)
# If this script is run without a filename, it will attempt to use some default filename. If these don't exist it will return an error
####

if("stringr" %in% rownames(installed.packages()) == FALSE) {install.packages("stringr")}
require(stringr)

# column should be 5 for CLCbio files, 13 for local blast
column <- 13

getCounts <- function(file)
{
  #df <- read.csv(file)
  fields <- max(count.fields(file, sep = ','), na.rm = TRUE)
  df <- read.csv(file, header=FALSE, col.names = paste0("V", seq_len(fields)), fill = TRUE)
  if(length(grep("\\[", df[[1,column]])) == 0)
  {
    #this means there's no brackets in virus name
    str_extract(df[[57,column]], "^(.*?)virus\\s.?")
    counts <- data.frame(table(str_extract(tolower(df[[column]]), "^(.*?)virus\\s.?")))
  }
  else
  {
    #counts <- data.frame(table(str_extract(tolower(df[,column]), "\\[(.*?)\\]")))
    counts <- countColumn(14)#sapply(column, countColumn(), column)
  }
  counts$Var1 <- gsub("\\[|\\]", "", counts$Var1)
  write.csv(counts, file = paste(file, "counts", sep="."))
}
countColumn <- function(local.column)
{
  local.counts <- data.frame(table(str_extract(tolower(df[,local.column]), "\\[(.*?)\\]")))
  return(local.counts)
}
file <- commandArgs(TRUE)
if(length(file) == 0) 
{
  files = c("LV98-2.csv", "LR106.csv", "LR127.csv", "LV94-4.csv", "ToRSV100.csv", "LV91-1.csv", "LR102.csv", "CB100.csv", "CB120.csv")
  sapply(files, getCounts)
} else if(length(file) > 0)
{
  getCounts(file[1])
}