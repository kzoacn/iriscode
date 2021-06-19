from PIL import Image
import numpy as np
import sys
def read(path):
    if path[-3:]!='txt':
        return None
    p=np.loadtxt(path)
    return p


def dis(code1,mask1,code2,mask2):
    ans=0
    al=0
    for i in range(7,64,8):
        for j in range(8,512,16):
            if mask1[i][j]==0 or mask2[i][j]==0:
                continue
            if code1[i][j]!=code2[i][j]:
                ans+=1
            al+=1
    return ans/al


lst=['0000_000',
	'0000_001',
	'0000_002',
	'0000_003',
	'0001_000',
	'0001_001',
	'0001_002',
	'0001_003']


for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        mask1=read(lst[i]+'_mano.txt')
        mask2=read(lst[j]+'_mano.txt')
        code1=read(lst[i]+'_code.txt')
        code2=read(lst[j]+'_code.txt')
        print(lst[i],lst[j],dis(code1,mask1,code2,mask2))
