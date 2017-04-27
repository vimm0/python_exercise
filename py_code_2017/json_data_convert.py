import json
import numpy as np
# json embedded here, but could be read in from text file
json_string = """{
        "instrument" : "EUR_USD",
        "granularity" : "D",
        "candles" : [
                {
                        "time" : "2014-02-17T22:00:00Z",
                        "openMid" : 1.259445,
                        "highMid" : 1.259955,
                        "lowMid" : 1.251825,
                        "closeMid" : 1.257955,
                        "volume" : 61184,
                        "complete" : true
                },
                {
                        "time" : "2014-02-18T22:00:00Z",
                        "openMid" : 1.257975,
                        "highMid" : 1.259955,
                        "lowMid" : 1.251825,
                        "closeMid" : 1.252945,
                        "volume" : 67528,
                        "complete" : false
                }
        ]
       }"""

candles = json.loads(json_string)['candles']
col_heads = ['time', 'openMid', 'highMid', 'lowMid', 'closeMid', 'volume']
f = lambda c: [c[col] for col in col_heads]
row_wise = [col_heads[:]]
row_wise.extend([f(candle) for candle in candles])
for row in row_wise: print (row)
print
col_wise = zip(*row_wise)
for col in col_wise: print (col)