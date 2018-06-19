import random
import plotly.plotly as py
import plotly.graph_objs as go
counter = 1
stickcounter = 0
switchcounter = 0
doornumber = 3
switchwon= 0
doorcount =0
n= 1000001 #n number of doors you want to try up to
while doorcount < n:
    # loop lots of times...
    while counter < 100000:
        contdoor = random.randint(1, doornumber)
        prizedoor = random.randint(1, doornumber)
        opendoor = 1

        # find the first door which doesn't have the prize and isn't the one the contestant chose
        while opendoor == prizedoor or opendoor == contdoor:
            opendoor += 1
    
        # find out whether the contestant would be better off switching or sticking
        if contdoor == prizedoor:
            stickcounter += 1
        else:
            switchcounter += 1
        counter += 1
    percentwon = (switchcounter/100000) 
    
    doorcount +=10000
trace = go.Scatter(
        x = doornumber,
        y = percentwon,
        mode = "markers"
    )
data = [trace]
py.iplot(data, filename= 'monty hall')
