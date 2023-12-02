import re
print(sum(map(int,(re.findall("\d",i)[0]+re.findall("\d",i[::-1])[0]for i in open(0)))))