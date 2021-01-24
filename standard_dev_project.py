import pandas as pd
import math

df = pd.read_csv('./standard_deviation_project_data.csv',header=0)
data = list(df)
for i in range(0,len(data)):
    data[i] = int(data[i])
sum = 0
for i in range(0,len(data)):
    sum = sum + data[i]
    i+=1
mean=sum/len(data)
diff = []
for i in range(0,len(data)):
    differ = data[i]-mean
    diff.append(differ)
sqr = []
for i in range(0,len(diff)):
    square = diff[i]*diff[i]
    sqr.append(square)
sum_sqr = 0
for i in range(0,len(sqr)):
    sum_sqr = sum_sqr + sqr[i]
div = sum_sqr/(len(data)-1)
stndrd_dev = math.sqrt(div)
print(stndrd_dev)
