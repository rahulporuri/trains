import pandas
import matplotlib.pyplot as plt

from os.path import splitext
import glob

train_numbers = ['11015', '11057', '11071', '12137', '12308', '12322',
                 '12404', '12424', '12502', '12506', '12534', '12542',
                 '12616', '12617', '12622', '12627', '12704', '12802',
                 '14056', '12988', '14056', '15017', '18646', '12809',
                 '15910', '18029']

def _make_plot(df, train_number):
    
    ax = df.plot(figsize=(25,7))
    ax.yaxis.grid()
    ax.xaxis.grid()
    ax.set_xticks([i for i in range(len(df.index.values))])
    ax.set_xticklabels([station for station in df.index.values])
    ax.set_title('train number {}'.format(train_number))
    ax.set_xlabel('stations along the route')
    ax.set_ylabel('delay in minutes')
    plt.xticks(rotation=90)
    plt.savefig('train/{}.png'.format(train_number))
    plt.close()

    return None


def _generate_html(df, train_number):
    with open('train/{}.html'.format(train_number), 'w') as f:
        header = "<head><body>"
        image = "<img src='{}.png'>".format(train_number)
        tail = "</body></html>"
        f.write(header+df.to_html()+image+tail)


with open('all_train_numbers.csv', 'rb') as f:
    temp_list = f.readlines()
    list_of_train_numbers = [number.strip('\n') for number in temp_list]


for train_number in list_of_train_numbers:
    i = 0

    files = glob.glob('del/{}_*.del'.format(train_number))
    for file in files:
        column_name = splitext(file.split('_')[1])[0]
        temp_df = pandas.read_table(file,
                                    delimiter=',',
                                    names=[column_name],
                                    index_col=0
        )

        if not temp_df.empty:
            temp_df[column_name] = pandas.to_numeric(temp_df[column_name].str.split().str[0])
        
            if i > 0:
                df = df.join(temp_df)
            else:
                i += 1
                df = temp_df

    if df is not None:
        #from IPython.core.debugger import Tracer; Tracer()()
        #df['train_number'] = pandas.Series([train_number for i in range(len(df))], index=df.index)
        #df.to_csv('{}_all_days.csv'.format(train_number))

        _make_plot(df, train_number)
        _generate_html(df, train_number)
        df = None
