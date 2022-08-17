# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import urllib
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
# 这个是你放网址的文件名，改过来就可以了
file = open('test.txt')
lines = file.readlines()
aa = []
for line in lines:
    temp = line.replace('\n', '')
    aa.append(temp)
print(aa)

print('开始检查：')
for a in aa:
    tempUrl = a
    try:
        opener.open(tempUrl)
        print(tempUrl + '没问题')
    except urllib.error.HTTPError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    except urllib.error.URLError:
        print(tempUrl + '=访问页面出错')
        time.sleep(2)
    time.sleep(0.1)