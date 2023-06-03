使用本脚本，你需要注意一下几点：\n
1.你需要有Java17及以上版本，Python3任意版本，Python2任意版本，R-4.3版本\n
2.该脚本的使用顺序是：\n
	2-1.将当前工作目录切换到EasyWGCNA/Script/目录下（务必注意此点）\n
	2-2.使用Python3执行main.py脚本，根据提示内容的引导，完成转录组原始数据到获得基因的FPKM值的所有步骤。这这个过程中你需要提供一个GTF格式的基因注释文件，一般有的是GFF3格式的注释文件，你可以使用Script目录下的GFF_TO_GTF.py脚本进行格式转换。（python3 GFF_TO_GTF.py YourGFF3Annotation.gff3 > YourGTFAnnotation.gtf）\n
	2-3.需要你自己手动将EasyWGCNA/WorkFile/TPM_FPKM_calculate_7/目录下的YourFinalFPKM.xlsx文件移动到EasyWGCNA/RWorkFile目录下\n
	2-4.后续的WGNCA分析都将使用R进行，因此你可将RWorkFile目录及其文件移动到任何目录下，开启R（建议使用Rstudio）,将当前工作目录设置到RWorkFile目录下。\n
	2-5.将你的基因注释文件和性状数据文件也放到RWorkFile目录下。（在EasyWGCNA目录下有一份基因注释文件和性状数据文件的样例，你可以按照样例的整理好你的文件）\n
	2-5.使用R（最好是Rstudio）打开RWorkFile目录下WGCNA.R脚本，这个脚本是完成分析的所有脚本，可以帮助你从实现FPKM和性状数据关联分析，最终得到关键基因ID。脚本里面有些代码是读取样本数据和性状ID的，你需要根据你的文件名进行更改。\n
		不过你不需要太担心，R脚本中有大量注释，可以帮助你理解每行代码的作用，你只需要根据注释说明进行微调即可（我在写代码时是分段写的，每段之间有两个空行，非常建议你一段接一段的执行，因为有些参数要根据你上一段的执行结果进行调整）\n