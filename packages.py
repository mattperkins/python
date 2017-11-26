# create a folder in project directory (i.e myPackage)
# identify folder as a Package by:
# adding an empty file named: __init__.py 

# create module files inside folder i.e bible.py, jesus.py

# bible.py contains a Class
class Lemon:
    ...
# jesus.py contains Two Functions
def lime:
    ...
def peach:
    ...

# outside of package/folder import into working files
# newFile.py
from myPackage.bible import Lemon
from myPackage.jesus import lime, peach

foo = Lemon('bar', 'baz')
bish = lime(args)
bosh = peach(args)
