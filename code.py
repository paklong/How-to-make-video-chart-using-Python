%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#Data can be found here: https://ourworldindata.org/grapher/international-tourist-arrivals-by-world-region
data = pd.read_csv('international-tourist-arrivals-by-world-region.csv', header = 0)
data = data.rename(columns = {' (arrivals)': 'Arrivals'})
Year = np.sort(data.Year.unique())

for yr in Year:
    Entity = data[data.Year == yr].sort_values('Arrivals', ascending = False).Entity
    Arrivals = data[data.Year == yr].sort_values('Arrivals', ascending = False).Arrivals

    plt.rcdefaults()
    fig, ax = plt.subplots()
    Entity_pos = np.arange(len(Entity))

    ax.barh(Entity_pos, Arrivals, align='center', color="blue")
    ax.set_yticks(Entity_pos)
    ax.set_yticklabels(Entity)
    ax.invert_yaxis() 
    ax.set_xlabel('Arrivals')
    ax.set_title('International tourist arrivals by world region')


    for i, v in enumerate(Arrivals):
        ax.text(v, i, " "+str(v), va='center')
        if i == 0:
            ax.text(v , 4, " "+str(yr), weight="bold")


    ax.set(frame_on=False)
    plt.savefig(str(yr) + '.png', bbox_inches='tight')
    
