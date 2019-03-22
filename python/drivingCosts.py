# This program compares the effect of driving at different speeds 
# on your fuel consumption.  The user will enter the distance of 
# their drive in kilometers and the cost of gas per liter.  The 
# program will report back the cost of doing that drive at
# different speeds.
distance = float( input( "How long is your daily drive in Kilometers? " ) )
cost = float( input( "How much does gas cost per liter? " ) )
miles_per_gallon = float( input( "What is your car's miles per gallon rating? " ) )

# 0.6 mile = 1 Kilometer, 1 US gallon = 3.78 L, approximately
# convert miles per gallon to kilometers per liter
milesPerGallonPg2kpl = miles_per_gallon / 0.6 / 3.78

# milage tables start at 55mph, need to convert to kph
perDay = cost * ( distance / milesPerGallonPg2kpl )

# calculations for diving at 100 km/h
at100 = round( perDay * 1.03, 2 )
print( "\nIf you drive at " + str( 60 * 1.6 ) + " km/h it will cost $" + \
str( at100 ) + " per day" )
print( "That's $" + str( round( at100 * 365.4, 2 ) ) + " per year.\n" )

# calculations for diving at 120 km/h
at120 = round( perDay * 1.23, 2 )
print( "If you drive at " + str( 75 * 1.6 ) + " km/h it will cost $" + \
str( at120 ) + " per day" )
print( "That's $ " + str( round( at120 * 365.4, 2 ) ) + " per year.\n" )

# show the difference in cost
print( "That's a difference of " + \
str( round( ( at120 - at100 ) * 365.4, 2 ) ) + \
" per year to drive 20 km/h faster." )

# calculate the time for the trip
# how many minutes to drive dist at 100 kph?
timeToDriveAt100 = distance * ( 60 / 100 )
# how many minutes to drive dist at 120 kph?
timeToDriveAt120 = distance * ( 60 / 120 )

# calculate and show the difference in time
timeDiffirence = timeToDriveAt100 - timeToDriveAt120
print( "You save " + str( timeDiffirence ) + " minutes per day." )

#I, Petros Youkhanna, student number 000751379, certify that all code submitted is my own work; that I have not copied it from amy other source. I also certify I have not allowed my work to be copied by others.
