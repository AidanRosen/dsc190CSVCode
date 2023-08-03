import pandas as pd 
import sys
import numpy as np
pd.options.plotting.backend = "plotly"


def makeDF(csvPath):
    df = pd.read_csv(csvPath, usecols=["Humidity (%)", "Temperature (F)", "Motion", "Time"])
    return df


dateLower = sys.argv[2] + " " + sys.argv[3]
dateUpper = sys.argv[4] + " " + sys.argv[5]

print(sys.argv[1])
df = makeDF(sys.argv[1])

df[df.Time.between(dateLower, dateUpper)]
print(df) 
print(df.describe())
fig = df.plot(x="Time", y="Humidity (%)")
figTemp = df.plot(x="Time", y="Temperature (F)")
figMotion = df.plot(x="Time", y="Motion")
 
fig.show()
figTemp.show()
figMotion.show()

#2023-08-01 20:03:27 <-- shoot the space is gonna make it a little difficult 
#2023-08-02 12:05:27
