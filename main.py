# The goal of our analysis is to determine a few indicators of heavy traffic on I-94. These indicators can be weather type, time of the day, time of the week, etc. For instance, we may find out that the traffic is usually heavier in the summer or when it snows.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the file with pandas
i94_df = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')
# Examining the first and the last five rows
print(i94_df.head(5))
print(i94_df.tail(5))
# Finding info about the dataframe
i94_df.info()
plt.hist(i94_df['traffic_volume'])
plt.ylabel('Distribution')
plt.xlabel('Traffic Volume')
plt.show()
print('*****')
print(i94_df['traffic_volume'].describe())
#
