# GPRMCConvert
GPRMC/NMEA Sentence to Long/Lat converter. Useful for inputting raw GPS data into Google Maps.

##Syntax:
`gprmcconvert.py $GPRMC,225446,A,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68`

Replace _$GPRMC,225446,A,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68_ with your GPRMC sentence.

It's really that simple.

##Sample Output:
>gprmcconvert.py $GPRMC,023057.94,A,3038.8964,N,09751.8063,W,0.000,0.000,070316,0,W,A*2A

Results in:

>30.6482733333 N 97.8634383333 W
