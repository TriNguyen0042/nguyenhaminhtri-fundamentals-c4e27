from mlab import rv
ramerica = list(rv.find({"continent":"S. America"}))
for rivers in ramerica:
    if rivers["length"]<1000:
        print(ramerica)
