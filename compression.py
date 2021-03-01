#String Compression

def compress(string):
#compress function which accepts an input string and returns a compressed string.
    #compressed string
    result = ""
    #counter to count continous occurances of character
    count = 1

    #Adding the first character
    result = result + string[0]

    #Iterate through loop, except the last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count = count + 1
        else:
            if(count > 1):
                #Ignore if no repeats
                result = result + str(count)
            result = result + string[i+1]
            #reset the counter
            count = 1
    #print last one
    if(count > 1):
        result = result + str(count)
    return result

assert compress('bbcceeee') == 'b2c2e4'
assert compress('aaabbbcccaaa') == 'a3b3c3a3'
assert compress('a') == 'a'


#time complexity of the compress function
#O(N^2)
