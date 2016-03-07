import sys
sentencearr = (sys.argv[1]).split(',')
n = sentencearr[3]
w = sentencearr[5]
print str(float(n[:2]) + (float(n[2:])/60)) + " N " + str(float(w[:3]) + (float(w[3:])/60)) + " W"
