# 编写人：赵子权
# 编写时间：2022/9/18 10:51
# 邮箱:2939818719@qq.com
# 编写人：赵子权
# 编写时间：2022/9/13 19:20
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('14_LD_view_filter'):
    print('已经存在14_LD_view_filter目录，无需创建了')
else:
    os.mkdir('14_LD_view_filter')

PopLDdecay_software_path = input('请输入PopLDdecay软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/PopLDdecay-3.42/bin/PopLDdecay：')
Plot_OnePop_pl_path = input('请输入Plot_OnePop.pl的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/PopLDdecay-3.42/bin/Plot_OnePop.pl：')
plink_mmh_filtering_path = input('请输入已经完成缺失率，最小等位基因频率，哈温平衡后的plink的二进制文件所在目录，例如：/mnt/storage/zhaoziquan/GWAS/13_Missing_rate_filtering/：')
plink_mmh_filtering_bfilename = os.listdir(plink_mmh_filtering_path)

with open('14_LD_view.sh', 'a') as LD:
    LD.write('#!/bin/bash\n')
    for filename in plink_mmh_filtering_bfilename:
        if '.vcf' in filename:
            filename = re.sub('_plink_filtering.vcf', '', filename)
            LD.write(f'{PopLDdecay_software_path} -InVCF {plink_mmh_filtering_path}{filename}_plink_filtering.vcf -MaxDist 500 -OutStat {filename}_LD\n')
            LD.write(f'perl {Plot_OnePop_pl_path} -inFile {filename}_LD.stat.gz -output {filename}_LD_plot\n')

os.system('mv ./14_LD_view.sh ./14_LD_view_filter/')
print('\033[1;36m在当前目录下，有一个叫14_LD_view_filter的文件夹，里面有一个shell脚本，执行它即可\033[m')

'''
问题1: 为什么LD decay曲线 波动大？
答： LD decay 波动太大的话，有可能是如下两个原因造成的
原因1 ： Ref组装质量太差了（ poor assembly ref）
由于ld decay的r2和物理距离之间的关系，若ref组装scaffold连成LG时，scaffold的顺序出错or中间插入的N的长度严重不对的话，这个极有可能影响到结果。
解决： 这种情况可以对回原来scaffold的坐标上，取长的scaffold来分析
原因2： 可能是SNP 密度太少，即RAD or GBS测序 or芯片数据，这种情况可以用
解决： Perl plot_XXX.pl -bin1 -break -bin2 把参数调大

问题2: 为什么LD decay曲线 密度很密:
答： 只须把 –bin1 –bin2 –break 参数取大点,bin取大些。
Perl plot_XXX.pl -bin1 -break -bin2 把参数调大

问题3: 为什么和PLINK 同样都是默认参数，它的ld很高，decay到0.2的距离相当相当远，你的PopLDdecay则很短？
答： 均是默认，然默认的值不同，Plink的 这一参数特别要注意 ：--ld-window-r2 ，其默认为0.2的，即默认低于0.2的pair-wise是不输出的，所以0.2 decay对应的距离会相当远。
建议为：
【 --ld-window-r2 0 -ld-window 99999 --ld-window-kb 300 --maf 0.005 ] 重跑新一下
Special parameters [ --ld-window-r2 0] , default is 0.2 . so the r2 low 0.2 will be Throw away, you must forget this.

问题4: 为什么最后一个点异常高or低
这个当是maxdis和bin非整倍数的关系 并且最后一个点的pair-wise snp太少存存在异常，如【maxdis 为501k -bin2 10k 最后一bin存在异常】 。 这种情况是极小概率发生的，直接把 xx.bin那个文件最后一个点删除掉就可
'''

'''
绘图的R脚本
data <- read.table("chr5_plot.bin")
pdf("chr5_plot.pdf")
plot(data[,1]/1000,data[,2],type="l",col="blue",main="LD decay",xlab="Distance(Kb)",xlim=c(0,500),ylab=expression(r^{2}),bty="n",lwd=2)
dev.off()
'''