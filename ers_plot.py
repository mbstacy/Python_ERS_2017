import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import sys

def myplot(x,y,style,title,xlabel,ylabel,figsize=(20,5),filename="test.png"):
    fig, axes = plt.subplots()
    ax=y.plot(ax=axes,figsize=figsize,title=title,style=style)
    plt.xticks(rotation=90)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # set xaxis major Dateformater
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # set grid lines
    ax = plt.gca().grid(True)
    fig.savefig(filename,dpi=300, bbox_inches='tight')



if __name__ == '__main__':
    filetype = sys.argv[1]
    image_format = sys.argv[2]
    for filename in sys.argv[3:]:
        data = pd.read_csv(filename)
        if filetype.lower() == "flux":
            data['date']=pd.to_datetime(data['time'],format='%Y%j')
            data.index = data['date']
            myplot(data.index, data[['Ta_min (Deg C)','Ta_mean (Deg C)','Ta_max (Deg C)']],'',
                        "Temperature","Date","Degree Celcius",
                        filename="{0}_temperature.{1}".format(filename.split('.')[0],image_format))
        elif filetype.lower() == "modis":
            # convert to date time data type and set index
            try:
                data['date']=pd.to_datetime(data['Date'],format='%m/%d/%Y')
            except:
                data['date']=pd.to_datetime(data['Date'],format='%m/%d/%y')
            data.index = data['date']
            myplot(data.index,data.ix[:,'GF_NDVI':'GF_EVI'] ,'',"Vegitation Index","Date","Vegitation Index",
                    figsize=(20,10),
                    filename="{0}_veg_index.{1}".format(filename.split('.')[0],image_format))
        else:
            print("Error: first argument must be 'flux' or 'modis'")




    




