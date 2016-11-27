import glob


header = "<html><body>"
tail = "</body></html>"
body = ""

list_of_trains = []
with open('all_train_numbers.csv', 'rb') as f:
    list_of_train_numbers = sorted([int(line.strip('\n')) for line in f])


for train_number in list_of_train_numbers:
    if glob.glob('train/{}.html'.format(train_number)):
        body += "<a href='train/{}.html'>{} \n</a>".format(train_number, train_number)


with open('summary.html', 'w') as f:
    f.write(header+body+tail)
