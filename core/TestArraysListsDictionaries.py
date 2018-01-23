from random import randint

some_array = [[randint(0,9) for i in range(10)] for i in range(10)]

for i in some_array[i]:
    print some_array[i]
    
some_dict = {}
some_dict[1] = "eins"
some_dict[2] = "zwei"
some_dict[3] = "drei"
some_dict[4] = "vier"
some_dict[5] = "fuenf"
some_dict[6] = "sechs"
some_dict[7] = "sieben"
some_dict[8] = "acht"
some_dict[9] = "neun"
some_dict[0] = "null"

another_dict = {}

for i in some_array[i]:    
    another_dict[some_dict.get(some_array[i][0])] = some_array[i]

for key,value in another_dict.iteritems(): 
    print key,value
 

    
    


    