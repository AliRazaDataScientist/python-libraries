import matplotlib.pyplot as plt
import matplotlib.dates as plt_dates
import pandas as pd
from datetime import datetime, timedelta
plt.style.use('seaborn-v0_8-talk')
# dates = [
#     datetime(2025,1,6),
#     datetime(2025,1,7),
#     datetime(2025,1,8),
#     datetime(2025,1,9),
#     datetime(2025,1,10),
#     datetime(2025,1,11)
#     ]
# y = [11,3,5,7,9,12]
# plt.plot_date(dates,y,linestyle='dashdot')
# plt.gcf().autofmt_xdate()
# date_formate = plt_dates.DateFormatter('%b, %d %Y')
# plt.gca().xaxis.set_major_formatter(date_formate)
#Now Try Another Example
rec = pd.read_csv('data3.csv')
rec['Date'] = pd.to_datetime(rec['Date'])
rec.sort_values('Date',inplace=True)
price_date = rec['Date']
price_close = rec['Close']
plt.plot_date(price_date,price_close,linestyle='dotted')
plt.gcf().autofmt_xdate()
plt.title('Bitcoin Prices')
plt.xlabel('Closing Dates')
plt.ylabel('Closing Price')
plt.tight_layout()
# plt.legend()
plt.show()







