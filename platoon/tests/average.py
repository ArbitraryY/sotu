#!/usr/bin/python

def measureAvg(avgType):
        """Arguements:
        avgType - Which average algorithm to use (aMean|median|iquart)
        """
        #Number of measurements to take.  Use a multiple of 4 if using the
        #interquartile mean
        numMeasures = 3;
        dataPoints = []
        for num in range(1,numMeasures):
                distance=measure()
                time.sleep(0.15)
                dataPoints[i] = distance
        if avgType == 'aMean':
        elif avgType == 'median':
        elif avgType == 'iquart':
        else
                print "not a valid Averaging option"
        return distance


