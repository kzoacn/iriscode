from PIL import Image
import numpy as np
import sys
def totxt(path):
    if path[-3:]!='bmp':
        return
    im=Image.open(path)
    p=np.array(im)
    p=p[0:64]
    np.savetxt(path[0:-3]+'txt',p,'%.0f')


if len(sys.argv)>1:
    for x in sys.argv[1:]:
        totxt(x)
