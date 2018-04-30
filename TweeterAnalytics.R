install.packages("twitteR")
install.packages("wordcloud")
install.packages("plyr")
install.packages("dplyr")
install.packages("stringr")
install.packages("ggplot2")
install.packages("tm")
install.packages("devtools")
install.packages("stringr")


library(plyr)
library(dplyr)
library(stringr)
library(ggplot2)
library(reshape2)
library(twitteR)
library(wordcloud)


require(devtools)
install_url("http://cran.r-project.org/src/contrib/Archive/sentiment/sentiment_0.2.tar.gz")
require(sentiment)
ls("package:sentiment")

tweets.df <- read.csv("C://Users/India/Documents/GitHub/Tweeter Analytics/demonetization-local.csv")
str(tweets.df)