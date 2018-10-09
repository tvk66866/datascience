import csv

import datetime as dt
import pandas as pd

#from matplotlib import pyplot as plt
#with open('output.csv', 'w') as f1:
    #writer = csv.writer(f1)

filename='NetflixViewingHistory.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row=next(reader)
    print(header_row)


    #writer = csv.writer(f1)

    moviename = []
    watchdate = []
    movie_list = []
    movie_stat = []
    i = 0
    for row in reader:
        moviename.append(row[0])
        watchdate.append(row[1])
        print(moviename[i] + " --> ")
        print(watchdate[i] + "\n")
        i += 1
    print(moviename)
    print(type(watchdate[0]))
    date_ts = dt.datetime.strptime(watchdate[-1],"%m/%d/%y")
    ts_now = dt.datetime.now()
    ts_diff = ts_now - date_ts
    print(date_ts)
    print(ts_diff)
    print(date_ts.year)

n = len(watchdate)



while True:
    #print("Enter the date:")
    m_year = input("Year")
    #print(m_year)
    if m_year == 'q':
        break
    m1_year = dt.datetime.strptime(m_year, "%Y")
    #print(m1_year)


    print(m1_year)
    j = 0
    movie_count = 0
    while j < n:
        year_ts = dt.datetime.strptime(watchdate[j],"%m/%d/%y")


        if m1_year.year == year_ts.year:
            #print(year_ts.year)

            print("You Watched " + moviename[j] + " on "+ watchdate[j] + "\n")


            movie_count += 1

        j += 1
    movie_list.append(str(m1_year.year))
    movie_list.append(str(movie_count))

    #movie_stat.append(movie_list)
    #movie_list.append('\n')
    #f1.write(str(m1_year.year))

    #movie_list[m1_year.year] = movie_count
    print("total movie watched in year " + str(m1_year.year) + " is " + str(movie_count))
#writer.writerows(movie_list)
my_df = pd.DataFrame(movie_list)
my_df.to_csv('my_csv.csv', index = False, header = False)
print(movie_list)
print("Thanks for using this program")

