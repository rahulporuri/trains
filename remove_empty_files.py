import os

list_of_files = os.listdir('del/')

for filename in list_of_files:
    if os.stat('del/'+filename).st_size == 0:
        print filename
        os.remove('del/'+filename)
