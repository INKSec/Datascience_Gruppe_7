import pandas as pd
import pathlib


# Get current path of main file
mainPath = pathlib.Path(__file__).parent.resolve()
# Path of data files
weatherPath = '\\Daten\\wetter.csv'
kiwoPath = '\\Daten\\kiwo.csv'
umsatzdatenPath = '\\Daten\\umsatzdaten_gekuerzt.csv'

# read weather data in dataframe
myFrameWetter = pd.DataFrame()
myFrameWetter = pd.read_csv(str(mainPath) + weatherPath)

# read kiwo data in dataframe
myFrameKiwo = pd.DataFrame()
myFrameKiwo = pd.read_csv(str(mainPath) + kiwoPath)

# read umsatz data in dataframe
myFrameUmsatz = pd.DataFrame()
myFrameUmsatz = pd.read_csv(str(mainPath) + umsatzdatenPath)

# concat all three dataframes
combinedDataframe = pd.concat([myFrameKiwo, myFrameUmsatz, myFrameWetter], axis=1)

print(combinedDataframe)

# make descriptive stattistics
statistics = combinedDataframe.describe()

print(statistics)


