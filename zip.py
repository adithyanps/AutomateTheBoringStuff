import os
import zipfile
b=zipfile.ZipFile('c.zip')
b.extractall()
print contents
b.close() 
