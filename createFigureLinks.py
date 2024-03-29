import glob
import os

FigDir = 'Figures'

if not os.path.exists(FigDir):
    os.makedirs(FigDir)

    
print('\n ***** Find all figures ending with png ****** :') 
for name in glob.glob('*/*/*png'): 
    print(name)
    src = '../'+name
    dst = name[name.rfind('/'):]
#    print(dst)
    dst = FigDir+dst
    try:
        os.symlink(src, dst)
    except:
        pass

print('\n ***** Find all figures ending with jpeg ****** :') 
for name in glob.glob('*/*/*jpeg'): 
    print(name)
    src = '../'+name
    dst = name[name.rfind('/'):]
#    print(dst)
    dst = FigDir+dst
    try:
        os.symlink(src, dst)
    except:
        pass

print('\n ***** Find all figures ending with jpg ****** :') 
for name in glob.glob('*/*/*jpg'): 
    print(name)
    src = '../'+name
    dst = name[name.rfind('/'):]
#    print(dst)
    dst = FigDir+dst
    try:
        os.symlink(src, dst)
    except:
        pass


    
