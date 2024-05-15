import csv
from pyfinviz.screener import Screener

page = 475

screener = Screener(pages=[x for x in range(1, page)])

list_ticker = []
for i in range(0, page):
    if i == 1 or i not in screener.data_frames:
        pass
    else:
        for j in range(len(screener.data_frames[i])):
            list_ticker.append(screener.data_frames[i].Ticker[j])
        list(list_ticker)

# Write the list of tickers to a CSV file
with open('tickers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker"])
    for ticker in list_ticker:
        writer.writerow([ticker])