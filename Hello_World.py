#Noah Sherman
#Jan 17 2017
#This is me trying to pull NBA box score data from another text file

import csv #imports csv functionality

with open("/Users/noahsherman/Desktop/Python_NBA_Test.txt") as my_file:
    reader = csv.reader(my_file)
    for line in reader: #For each line in my_file
        if int(line[2]) >= 10 and int(line[3]) >= 10 and int(line[6]) >= 10:
            name = str(line[0]) #Turns first list item in to string, need this to remove useless info, see txt file.
            print "On Jan 17, %s had a triple double, with %s points, %s rebounds, and %s assists." %(name[0:-10], line[6], line[2], line[3])
            #name[0:-10] removes name id that is pulled when copies from bref
        elif int(line[2]) >= 10 and int(line[3]) < 10 and int(line[6]) >= 10:
            name = str(line[0])
            print "On Jan 17, %s had a double double, with %s points and %s rebounds." %(name[0:-10], line[6], line[2])
        elif int(line[2]) < 10 and int(line[3]) >= 10 and int(line[6]) >= 10:
            name = str(line[0])
            print "On Jan 17, %s had a double double, with %s points and %s assists." %(name[0:-10], line[6], line[3])
        else:
            pass
            



my_file.close()

