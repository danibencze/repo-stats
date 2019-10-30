import os
from collections import Counter
path = input("Path to github repo (no need to escape): ")

os.chdir(path)
commitlist = os.system('git log --pretty=format:"%an" --reverse --all > tmp')
print(dict(Counter(open('tmp', 'r').read().split("\n"))))
os.remove('tmp')
input("Press any key to exit...")