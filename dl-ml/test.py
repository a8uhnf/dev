import os

path = os.getcwd()
print "Curretn path:-"
print path

bezdekIris_data = open(os.path.join(path, "./dl-ml/data/bezdekIris.data") , "r")

lines = bezdekIris_data.readlines()

print(lines)
for j in lines:
    print j