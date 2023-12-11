import re
print(sum(map(int,((x:=re.findall("\d",i))[0]+x[-1]for i in open(0)))))