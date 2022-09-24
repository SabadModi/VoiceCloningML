import glob
import shutil
#import os
dst_dir = "comvoi/wav/"
print ('Named explicitly:')
for name in glob.glob('comvoi/wavs/*/*'):
        shutil.move(name, dst_dir)
        # print ('\t', name)