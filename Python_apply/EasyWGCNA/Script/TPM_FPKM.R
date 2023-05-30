install.packages('xlsx')
library(xlsx)

YourCountsData <- read.table('YourFinalCounts.txt')
rowname <- YourCountsData$V1
rowname <- rowname[2:nrow(YourCountsData)]
colname <- YourCountsData[1,]
colname <- colname[2:length(colname)]
#读取数据

YourCountsData <- as.data.frame(lapply(YourCountsData[2:nrow(YourCountsData),2:ncol(YourCountsData)],as.numeric))
#将数据都转换为数值型

colnames(YourCountsData) <- colname
#整理好列名

rownames(YourCountsData) <- rowname
#整理好行名

YourCountsDataFilter <- YourCountsData[rowSums(YourCountsData)>0,]
#删除在不同样本中表达量都为0的基因

#TPM计算如下
Li <- nrow(YourCountsData)/1000
Ni_to_Li <- YourCountsDataFilter/Li
TPM <- t(t(Ni_to_Li)/colSums(Ni_to_Li)*10^6)
write.xlsx(TPM, file = 'YourFinalTPM.xls')


#FPKM计算如下：
FPKM <- t(t(Ni_to_Li)/colSums(YourCountsDataFilter)*10^6)
write.xlsx(FPKM,file = 'YourFinalFPKM.xls')
